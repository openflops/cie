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

import flame
import unittest


class FlameTestCase(unittest.TestCase):
    def test_session_creation(self):
        conn = flame.connect("127.0.0.1:8080")
        ssn = conn.create_session(application="flmexec", slots=1)
        self.assertIsNotNone(ssn)
        ssn.close()

    def test_multi_session_creation(self):
        conn = flame.connect("127.0.0.1:8080")
        for i in range(5):
            ssn = conn.create_session(application="flmexec", slots=1)
            self.assertIsNotNone(ssn)
            ssn.close()

    def test_session_creation_with_tasks(self):
        conn = flame.connect("127.0.0.1:8080")
        ssn = conn.create_session(application="flmexec", slots=1)
        self.assertIsNotNone(ssn)
        task = ssn.create_task(None)
        ssn.watch_task(task_id = task.id)
        ssn.close()


if __name__ == '__main__':
    unittest.main()
