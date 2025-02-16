import types_pb2 as _types_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ApplicationContext(_message.Message):
    __slots__ = ("name", "shim", "url", "command")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SHIM_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    name: str
    shim: _types_pb2.Shim
    url: str
    command: str
    def __init__(self, name: _Optional[str] = ..., shim: _Optional[_Union[_types_pb2.Shim, str]] = ..., url: _Optional[str] = ..., command: _Optional[str] = ...) -> None: ...

class SessionContext(_message.Message):
    __slots__ = ("session_id", "application", "common_data")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_FIELD_NUMBER: _ClassVar[int]
    COMMON_DATA_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    application: ApplicationContext
    common_data: bytes
    def __init__(self, session_id: _Optional[str] = ..., application: _Optional[_Union[ApplicationContext, _Mapping]] = ..., common_data: _Optional[bytes] = ...) -> None: ...

class TaskContext(_message.Message):
    __slots__ = ("task_id", "session_id", "input")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    INPUT_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    session_id: str
    input: bytes
    def __init__(self, task_id: _Optional[str] = ..., session_id: _Optional[str] = ..., input: _Optional[bytes] = ...) -> None: ...

class TaskOutput(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    def __init__(self, data: _Optional[bytes] = ...) -> None: ...

class RegisterServiceRequest(_message.Message):
    __slots__ = ("address", "service_id")
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
    address: str
    service_id: str
    def __init__(self, address: _Optional[str] = ..., service_id: _Optional[str] = ...) -> None: ...

class RegisterServiceResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
