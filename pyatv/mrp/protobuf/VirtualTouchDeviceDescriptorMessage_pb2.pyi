"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
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

class VirtualTouchDeviceDescriptor(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    absolute: builtin___bool = ...
    integratedDisplay: builtin___bool = ...
    screenSizeWidth: builtin___float = ...
    screenSizeHeight: builtin___float = ...

    def __init__(self,
        *,
        absolute : typing___Optional[builtin___bool] = None,
        integratedDisplay : typing___Optional[builtin___bool] = None,
        screenSizeWidth : typing___Optional[builtin___float] = None,
        screenSizeHeight : typing___Optional[builtin___float] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"absolute",b"absolute",u"integratedDisplay",b"integratedDisplay",u"screenSizeHeight",b"screenSizeHeight",u"screenSizeWidth",b"screenSizeWidth"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"absolute",b"absolute",u"integratedDisplay",b"integratedDisplay",u"screenSizeHeight",b"screenSizeHeight",u"screenSizeWidth",b"screenSizeWidth"]) -> None: ...
type___VirtualTouchDeviceDescriptor = VirtualTouchDeviceDescriptor
