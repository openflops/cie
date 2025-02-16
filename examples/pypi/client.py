#!/usr/bin/env python3

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

import flame.client as flame

import argparse

parser = argparse.ArgumentParser(description='Flame Pi Python Example.')
parser.add_argument('-n', '--task_num', type=int, help="The total number of tasks in the session.")
parser.add_argument('-i', '--task_input', type=int, help="The input of each task to calculate Pi.")
args = parser.parse_args()

area = 0.0


def get_circle_area(task):
    global area
    area += float(task.output)

conn = flame.connect("127.0.0.1:8080")
ssn = conn.create_session(application="pi", slots=1)

# Convert args.task_input into bytes type.
task_input = str(args.task_input).encode()
task_inputs = [task_input] * args.task_num

# Submit all task inputs to Flame, and wait for the result.
ssn.run_all_tasks(task_inputs=task_inputs, on_completed=get_circle_area)

# Calculate the Pi.
pi = 4 * area / (args.task_input * args.task_num)

print("pi = 4*({}/{}) = {}".format(area, args.task_input * args.task_num, pi))

ssn.close()