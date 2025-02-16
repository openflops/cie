# TODO(k82cn): It's better to re-org the python sdk with rpc subdir.

import os
import sys
script_dir = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(script_dir, "."))

__all__ = [
    "client",
    "service"
]
