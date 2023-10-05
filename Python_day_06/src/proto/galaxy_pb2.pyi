from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TaskState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    TASK_OPEN: _ClassVar[TaskState]
    TASK_IN_PROGRESS: _ClassVar[TaskState]
    TASK_POST_PONED: _ClassVar[TaskState]
    TASK_CLOSED: _ClassVar[TaskState]
    TASK_DONE: _ClassVar[TaskState]
TASK_OPEN: TaskState
TASK_IN_PROGRESS: TaskState
TASK_POST_PONED: TaskState
TASK_CLOSED: TaskState
TASK_DONE: TaskState

class GalacticPossition(_message.Message):
    __slots__ = ["pos"]
    POS_FIELD_NUMBER: _ClassVar[int]
    pos: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, pos: _Optional[_Iterable[float]] = ...) -> None: ...

class Ship(_message.Message):
    __slots__ = ["alignment", "name", "ship_class", "length", "crew_size", "armed", "officers"]
    class AlignmentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        Ally: _ClassVar[Ship.AlignmentType]
        Enemy: _ClassVar[Ship.AlignmentType]
    Ally: Ship.AlignmentType
    Enemy: Ship.AlignmentType
    class ClassType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        Corvette: _ClassVar[Ship.ClassType]
        Frigate: _ClassVar[Ship.ClassType]
        Cruiser: _ClassVar[Ship.ClassType]
        Destroyer: _ClassVar[Ship.ClassType]
        Carrier: _ClassVar[Ship.ClassType]
        Dreadnought: _ClassVar[Ship.ClassType]
    Corvette: Ship.ClassType
    Frigate: Ship.ClassType
    Cruiser: Ship.ClassType
    Destroyer: Ship.ClassType
    Carrier: Ship.ClassType
    Dreadnought: Ship.ClassType
    class Officer(_message.Message):
        __slots__ = ["first_name", "second_name", "rank"]
        FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
        SECOND_NAME_FIELD_NUMBER: _ClassVar[int]
        RANK_FIELD_NUMBER: _ClassVar[int]
        first_name: str
        second_name: str
        rank: str
        def __init__(self, first_name: _Optional[str] = ..., second_name: _Optional[str] = ..., rank: _Optional[str] = ...) -> None: ...
    ALIGNMENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SHIP_CLASS_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    CREW_SIZE_FIELD_NUMBER: _ClassVar[int]
    ARMED_FIELD_NUMBER: _ClassVar[int]
    OFFICERS_FIELD_NUMBER: _ClassVar[int]
    alignment: Ship.AlignmentType
    name: str
    ship_class: Ship.ClassType
    length: float
    crew_size: int
    armed: bool
    officers: _containers.RepeatedCompositeFieldContainer[Ship.Officer]
    def __init__(self, alignment: _Optional[_Union[Ship.AlignmentType, str]] = ..., name: _Optional[str] = ..., ship_class: _Optional[_Union[Ship.ClassType, str]] = ..., length: _Optional[float] = ..., crew_size: _Optional[int] = ..., armed: bool = ..., officers: _Optional[_Iterable[_Union[Ship.Officer, _Mapping]]] = ...) -> None: ...
