# Copyright 2025 The Flame Authors.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from concurrent import futures
from urllib.parse import urlparse
import logging
import grpc

import shim_pb2_grpc
import shim_pb2

class ApplicationContext:
    def __init__(self, app_context):
        self.name = app_context.name

class SessonContext:
    def __init__(self, ssn_context):
        self.session_id = ssn_context.id,
        self.application = ApplicationContext(ssn_context.application),
        self.common_data = ssn_context.common_data,

class TaskContext:
    def __init__(self, task_context):
        self.task_id = task_context.task_id
        self.session_id = task_context.session_id
        self.input = task_context.input

class FlameService:
    def on_session_enter(self, ssn_context):
        pass

    def on_session_enter(self):
        pass

    def on_task_invoke(self, task_context) -> bytes:
        pass

class GrpcShimService(shim_pb2_grpc.GrpcShimServicer):
    def __init__(self, service):
        self.service = service

    def OnSessionEnter(self, ctx):
        ssn_ctx = SessonContext(ctx)
        self.service.on_session_enter(ssn_ctx)
        
    def OnSessionLeave(self):
        self.service.on_session_leave()
        
    def OnTaskInvoke(self, ctx):
        task_ctx = TaskContext(ctx)
        output = self.service.on_task_invoke(task_ctx)
        return shim_pb2.TaskOutput(output)

def start_service(service):
    log = logging.getLogger(__name__)
    url = os.environ['FLAME_SERVICE_MANAGER']
    o = urlparse(url)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    shim_pb2_grpc.add_GrpcShimServicer_to_server(GrpcShimService(service), server)
    server.add_insecure_port("[::]:" + o.port)
    log.info("The Flame service was started at " + url)

    server.start()
    server.wait_for_termination()
