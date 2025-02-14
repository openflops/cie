import types_pb2 as _types_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CloseSessionRequest(_message.Message):
    __slots__ = ["session_id"]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    def __init__(self, session_id: _Optional[str] = ...) -> None: ...

class CreateSessionRequest(_message.Message):
    __slots__ = ["session"]
    SESSION_FIELD_NUMBER: _ClassVar[int]
    session: _types_pb2.SessionSpec
    def __init__(self, session: _Optional[_Union[_types_pb2.SessionSpec, _Mapping]] = ...) -> None: ...

class CreateTaskRequest(_message.Message):
    __slots__ = ["task"]
    TASK_FIELD_NUMBER: _ClassVar[int]
    task: _types_pb2.TaskSpec
    def __init__(self, task: _Optional[_Union[_types_pb2.TaskSpec, _Mapping]] = ...) -> None: ...

class DeleteSessionRequest(_message.Message):
    __slots__ = ["session_id"]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    def __init__(self, session_id: _Optional[str] = ...) -> None: ...

class DeleteTaskRequest(_message.Message):
    __slots__ = ["session_id", "task_id"]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    task_id: str
    def __init__(self, task_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class GetSessionRequest(_message.Message):
    __slots__ = ["session_id"]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    def __init__(self, session_id: _Optional[str] = ...) -> None: ...

class GetTaskRequest(_message.Message):
    __slots__ = ["session_id", "task_id"]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    task_id: str
    def __init__(self, task_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class ListSessionRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class OpenSessionRequest(_message.Message):
    __slots__ = ["session_id"]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    def __init__(self, session_id: _Optional[str] = ...) -> None: ...

class WatchTaskRequest(_message.Message):
    __slots__ = ["session_id", "task_id"]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    task_id: str
    def __init__(self, task_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...
