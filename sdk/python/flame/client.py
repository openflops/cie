# Copyright 2023 The Flame Authors.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from enum import Enum
import grpc

import frontend_pb2_grpc
import frontend_pb2
import types_pb2

def connect(addr):
    channel = grpc.insecure_channel(addr)
    return Connection(channel)

class Connection:
    def __init__(self, channel):
        self.channel = channel

    def create_session(self, *, application, slots):
        stub = frontend_pb2_grpc.FrontendStub(self.channel)
        spec = types_pb2.SessionSpec(application=application, slots=slots)
        req = frontend_pb2.CreateSessionRequest(session=spec)
        ssn = stub.CreateSession(req)
        return Session(stub, ssn)


class SessionState(Enum):
    Open = 0
    Closed = 1


class Session:
    def __init__(self, stub, ssn):
        self.stub = stub
        self.id = ssn.metadata.id

    def create_task(self, task_input):
        spec = types_pb2.TaskSpec(input=task_input, session_id=self.id)
        task = self.stub.CreateTask(frontend_pb2.CreateTaskRequest(task=spec))
        return Task(task)

    def get_task(self, task_id):
        req = frontend_pb2.GetTaskRequest(task_id=task_id, session_id=self.id)
        task = self.stub.GetTask(req)
        return Task(task)

    def watch_task(self, *, task_id, on_completed=None, on_error=None):
        req = frontend_pb2.WatchTaskRequest(task_id=task_id, session_id=self.id)
        tasks = self.stub.WatchTask(req)
        for task in tasks:
            state = TaskState(task.status.state)
            if state == TaskState.Succeed and on_completed != None:
                on_completed(Task(task))

    def run_all_tasks(self, *, task_inputs, on_completed=None, on_error=None):
        tasks = []
        for task_input in task_inputs:
            tasks.append(self.create_task(task_input))
        for task in tasks:
            self.watch_task(task_id=task.id, on_completed=on_completed, on_error=on_error)

    def close(self):
        self.stub.CloseSession(frontend_pb2.CloseSessionRequest(session_id=self.id))


class TaskState(Enum):
    Pending = 0
    Running = 1
    Succeed = 2
    Failed = 3


class Task:
    def __init__(self, task):
        self.id = task.metadata.id
        self.session_id = task.spec.session_id
        self.input = task.spec.input
        self.output = task.spec.output
        self.state = TaskState(task.status.state)
