import types_pb2 as _types_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RegisterApplicationRequest(_message.Message):
    __slots__ = ("name", "application")
    NAME_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_FIELD_NUMBER: _ClassVar[int]
    name: str
    application: _types_pb2.ApplicationSpec
    def __init__(self, name: _Optional[str] = ..., application: _Optional[_Union[_types_pb2.ApplicationSpec, _Mapping]] = ...) -> None: ...

class UnregisterApplicationRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UpdateApplicationRequest(_message.Message):
    __slots__ = ("name", "application")
    NAME_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_FIELD_NUMBER: _ClassVar[int]
    name: str
    application: _types_pb2.ApplicationSpec
    def __init__(self, name: _Optional[str] = ..., application: _Optional[_Union[_types_pb2.ApplicationSpec, _Mapping]] = ...) -> None: ...

class GetApplicationRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListApplicationRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateSessionRequest(_message.Message):
    __slots__ = ("session",)
    SESSION_FIELD_NUMBER: _ClassVar[int]
    session: _types_pb2.SessionSpec
    def __init__(self, session: _Optional[_Union[_types_pb2.SessionSpec, _Mapping]] = ...) -> None: ...

class DeleteSessionRequest(_message.Message):
    __slots__ = ("session_id",)
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    def __init__(self, session_id: _Optional[str] = ...) -> None: ...

class OpenSessionRequest(_message.Message):
    __slots__ = ("session_id",)
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    def __init__(self, session_id: _Optional[str] = ...) -> None: ...

class CloseSessionRequest(_message.Message):
    __slots__ = ("session_id",)
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    def __init__(self, session_id: _Optional[str] = ...) -> None: ...

class GetSessionRequest(_message.Message):
    __slots__ = ("session_id",)
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    def __init__(self, session_id: _Optional[str] = ...) -> None: ...

class ListSessionRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateTaskRequest(_message.Message):
    __slots__ = ("task",)
    TASK_FIELD_NUMBER: _ClassVar[int]
    task: _types_pb2.TaskSpec
    def __init__(self, task: _Optional[_Union[_types_pb2.TaskSpec, _Mapping]] = ...) -> None: ...

class DeleteTaskRequest(_message.Message):
    __slots__ = ("task_id", "session_id")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    session_id: str
    def __init__(self, task_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class GetTaskRequest(_message.Message):
    __slots__ = ("task_id", "session_id")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    session_id: str
    def __init__(self, task_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class WatchTaskRequest(_message.Message):
    __slots__ = ("task_id", "session_id")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    session_id: str
    def __init__(self, task_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...
