from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
ExecutorBound: ExecutorState
ExecutorIdle: ExecutorState
ExecutorRunning: ExecutorState
ExecutorUnknown: ExecutorState
LogShim: Shim
RestShim: Shim
RpcShim: Shim
SessionClosed: SessionState
SessionOpen: SessionState
StdioShim: Shim
TaskFailed: TaskState
TaskPending: TaskState
TaskRunning: TaskState
TaskSucceed: TaskState

class Application(_message.Message):
    __slots__ = ["arguments", "command", "environments", "name", "shim", "working_directory"]
    ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENTS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SHIM_FIELD_NUMBER: _ClassVar[int]
    WORKING_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    arguments: _containers.RepeatedScalarFieldContainer[str]
    command: str
    environments: _containers.RepeatedScalarFieldContainer[str]
    name: str
    shim: Shim
    working_directory: str
    def __init__(self, name: _Optional[str] = ..., shim: _Optional[_Union[Shim, str]] = ..., command: _Optional[str] = ..., arguments: _Optional[_Iterable[str]] = ..., environments: _Optional[_Iterable[str]] = ..., working_directory: _Optional[str] = ...) -> None: ...

class Executor(_message.Message):
    __slots__ = ["metadata", "spec", "status"]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    metadata: Metadata
    spec: ExecutorSpec
    status: ExecutorStatus
    def __init__(self, metadata: _Optional[_Union[Metadata, _Mapping]] = ..., spec: _Optional[_Union[ExecutorSpec, _Mapping]] = ..., status: _Optional[_Union[ExecutorStatus, _Mapping]] = ...) -> None: ...

class ExecutorSpec(_message.Message):
    __slots__ = ["applications", "slots"]
    APPLICATIONS_FIELD_NUMBER: _ClassVar[int]
    SLOTS_FIELD_NUMBER: _ClassVar[int]
    applications: _containers.RepeatedCompositeFieldContainer[Application]
    slots: int
    def __init__(self, slots: _Optional[int] = ..., applications: _Optional[_Iterable[_Union[Application, _Mapping]]] = ...) -> None: ...

class ExecutorStatus(_message.Message):
    __slots__ = ["state"]
    STATE_FIELD_NUMBER: _ClassVar[int]
    state: ExecutorState
    def __init__(self, state: _Optional[_Union[ExecutorState, str]] = ...) -> None: ...

class Metadata(_message.Message):
    __slots__ = ["id", "owner"]
    ID_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    id: str
    owner: str
    def __init__(self, id: _Optional[str] = ..., owner: _Optional[str] = ...) -> None: ...

class Result(_message.Message):
    __slots__ = ["message", "return_code"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RETURN_CODE_FIELD_NUMBER: _ClassVar[int]
    message: str
    return_code: int
    def __init__(self, return_code: _Optional[int] = ..., message: _Optional[str] = ...) -> None: ...

class Session(_message.Message):
    __slots__ = ["metadata", "spec", "status"]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    metadata: Metadata
    spec: SessionSpec
    status: SessionStatus
    def __init__(self, metadata: _Optional[_Union[Metadata, _Mapping]] = ..., spec: _Optional[_Union[SessionSpec, _Mapping]] = ..., status: _Optional[_Union[SessionStatus, _Mapping]] = ...) -> None: ...

class SessionList(_message.Message):
    __slots__ = ["sessions"]
    SESSIONS_FIELD_NUMBER: _ClassVar[int]
    sessions: _containers.RepeatedCompositeFieldContainer[Session]
    def __init__(self, sessions: _Optional[_Iterable[_Union[Session, _Mapping]]] = ...) -> None: ...

class SessionSpec(_message.Message):
    __slots__ = ["application", "slots"]
    APPLICATION_FIELD_NUMBER: _ClassVar[int]
    SLOTS_FIELD_NUMBER: _ClassVar[int]
    application: str
    slots: int
    def __init__(self, application: _Optional[str] = ..., slots: _Optional[int] = ...) -> None: ...

class SessionStatus(_message.Message):
    __slots__ = ["completion_time", "creation_time", "failed", "pending", "running", "state", "succeed"]
    COMPLETION_TIME_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIME_FIELD_NUMBER: _ClassVar[int]
    FAILED_FIELD_NUMBER: _ClassVar[int]
    PENDING_FIELD_NUMBER: _ClassVar[int]
    RUNNING_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    SUCCEED_FIELD_NUMBER: _ClassVar[int]
    completion_time: int
    creation_time: int
    failed: int
    pending: int
    running: int
    state: SessionState
    succeed: int
    def __init__(self, state: _Optional[_Union[SessionState, str]] = ..., creation_time: _Optional[int] = ..., completion_time: _Optional[int] = ..., pending: _Optional[int] = ..., running: _Optional[int] = ..., succeed: _Optional[int] = ..., failed: _Optional[int] = ...) -> None: ...

class Task(_message.Message):
    __slots__ = ["metadata", "spec", "status"]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    metadata: Metadata
    spec: TaskSpec
    status: TaskStatus
    def __init__(self, metadata: _Optional[_Union[Metadata, _Mapping]] = ..., spec: _Optional[_Union[TaskSpec, _Mapping]] = ..., status: _Optional[_Union[TaskStatus, _Mapping]] = ...) -> None: ...

class TaskSpec(_message.Message):
    __slots__ = ["input", "output", "session_id"]
    INPUT_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    input: bytes
    output: bytes
    session_id: str
    def __init__(self, session_id: _Optional[str] = ..., input: _Optional[bytes] = ..., output: _Optional[bytes] = ...) -> None: ...

class TaskStatus(_message.Message):
    __slots__ = ["completion_time", "creation_time", "state"]
    COMPLETION_TIME_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    completion_time: int
    creation_time: int
    state: TaskState
    def __init__(self, state: _Optional[_Union[TaskState, str]] = ..., creation_time: _Optional[int] = ..., completion_time: _Optional[int] = ...) -> None: ...

class SessionState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class TaskState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class Shim(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ExecutorState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
