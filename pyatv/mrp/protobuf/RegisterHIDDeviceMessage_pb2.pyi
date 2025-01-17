"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FieldDescriptor as google___protobuf___descriptor___FieldDescriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from pyatv.mrp.protobuf.VirtualTouchDeviceDescriptorMessage_pb2 import (
    VirtualTouchDeviceDescriptor as pyatv___mrp___protobuf___VirtualTouchDeviceDescriptorMessage_pb2___VirtualTouchDeviceDescriptor,
)

from typing import (
    Optional as typing___Optional,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int


DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class RegisterHIDDeviceMessage(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def deviceDescriptor(self) -> pyatv___mrp___protobuf___VirtualTouchDeviceDescriptorMessage_pb2___VirtualTouchDeviceDescriptor: ...

    def __init__(self,
        *,
        deviceDescriptor : typing___Optional[pyatv___mrp___protobuf___VirtualTouchDeviceDescriptorMessage_pb2___VirtualTouchDeviceDescriptor] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"deviceDescriptor",b"deviceDescriptor"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"deviceDescriptor",b"deviceDescriptor"]) -> None: ...
type___RegisterHIDDeviceMessage = RegisterHIDDeviceMessage

registerHIDDeviceMessage: google___protobuf___descriptor___FieldDescriptor = ...
