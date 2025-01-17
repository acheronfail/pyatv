"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.internal.containers import (
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.internal.enum_type_wrapper import (
    _EnumTypeWrapper as google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from pyatv.mrp.protobuf.Common_pb2 import (
    RepeatMode as pyatv___mrp___protobuf___Common_pb2___RepeatMode,
    ShuffleMode as pyatv___mrp___protobuf___Common_pb2___ShuffleMode,
)

from typing import (
    Iterable as typing___Iterable,
    NewType as typing___NewType,
    Optional as typing___Optional,
    Text as typing___Text,
    cast as typing___cast,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int


DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

CommandValue = typing___NewType('CommandValue', builtin___int)
type___CommandValue = CommandValue
Command: _Command
class _Command(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[CommandValue]):
    DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
    Unknown = typing___cast(CommandValue, 0)
    Play = typing___cast(CommandValue, 1)
    Pause = typing___cast(CommandValue, 2)
    TogglePlayPause = typing___cast(CommandValue, 3)
    Stop = typing___cast(CommandValue, 4)
    NextTrack = typing___cast(CommandValue, 5)
    PreviousTrack = typing___cast(CommandValue, 6)
    AdvanceShuffleMode = typing___cast(CommandValue, 7)
    AdvanceRepeatMode = typing___cast(CommandValue, 8)
    BeginFastForward = typing___cast(CommandValue, 9)
    EndFastForward = typing___cast(CommandValue, 10)
    BeginRewind = typing___cast(CommandValue, 11)
    EndRewind = typing___cast(CommandValue, 12)
    Rewind15Seconds = typing___cast(CommandValue, 13)
    FastForward15Seconds = typing___cast(CommandValue, 14)
    Rewind30Seconds = typing___cast(CommandValue, 15)
    FastForward30Seconds = typing___cast(CommandValue, 16)
    SkipForward = typing___cast(CommandValue, 18)
    SkipBackward = typing___cast(CommandValue, 19)
    ChangePlaybackRate = typing___cast(CommandValue, 20)
    RateTrack = typing___cast(CommandValue, 21)
    LikeTrack = typing___cast(CommandValue, 22)
    DislikeTrack = typing___cast(CommandValue, 23)
    BookmarkTrack = typing___cast(CommandValue, 24)
    SeekToPlaybackPosition = typing___cast(CommandValue, 45)
    ChangeRepeatMode = typing___cast(CommandValue, 46)
    ChangeShuffleMode = typing___cast(CommandValue, 47)
    EnableLanguageOption = typing___cast(CommandValue, 53)
    DisableLanguageOption = typing___cast(CommandValue, 54)
    NextChapter = typing___cast(CommandValue, 25)
    PreviousChapter = typing___cast(CommandValue, 26)
    NextAlbum = typing___cast(CommandValue, 27)
    PreviousAlbum = typing___cast(CommandValue, 28)
    NextPlaylist = typing___cast(CommandValue, 29)
    PreviousPlaylist = typing___cast(CommandValue, 30)
    BanTrack = typing___cast(CommandValue, 31)
    AddTrackToWishList = typing___cast(CommandValue, 32)
    RemoveTrackFromWishList = typing___cast(CommandValue, 33)
    NextInContext = typing___cast(CommandValue, 34)
    PreviousInContext = typing___cast(CommandValue, 35)
    ResetPlaybackTimeout = typing___cast(CommandValue, 41)
    SetPlaybackQueue = typing___cast(CommandValue, 48)
    AddNowPlayingItemToLibrary = typing___cast(CommandValue, 49)
    CreateRadioStation = typing___cast(CommandValue, 50)
    AddItemToLibrary = typing___cast(CommandValue, 51)
    InsertIntoPlaybackQueue = typing___cast(CommandValue, 52)
    ReorderPlaybackQueue = typing___cast(CommandValue, 55)
    RemoveFromPlaybackQueue = typing___cast(CommandValue, 56)
    PlayItemInPlaybackQueue = typing___cast(CommandValue, 57)
    PrepareForSetQueue = typing___cast(CommandValue, 58)
    SetPlaybackSession = typing___cast(CommandValue, 59)
Unknown = typing___cast(CommandValue, 0)
Play = typing___cast(CommandValue, 1)
Pause = typing___cast(CommandValue, 2)
TogglePlayPause = typing___cast(CommandValue, 3)
Stop = typing___cast(CommandValue, 4)
NextTrack = typing___cast(CommandValue, 5)
PreviousTrack = typing___cast(CommandValue, 6)
AdvanceShuffleMode = typing___cast(CommandValue, 7)
AdvanceRepeatMode = typing___cast(CommandValue, 8)
BeginFastForward = typing___cast(CommandValue, 9)
EndFastForward = typing___cast(CommandValue, 10)
BeginRewind = typing___cast(CommandValue, 11)
EndRewind = typing___cast(CommandValue, 12)
Rewind15Seconds = typing___cast(CommandValue, 13)
FastForward15Seconds = typing___cast(CommandValue, 14)
Rewind30Seconds = typing___cast(CommandValue, 15)
FastForward30Seconds = typing___cast(CommandValue, 16)
SkipForward = typing___cast(CommandValue, 18)
SkipBackward = typing___cast(CommandValue, 19)
ChangePlaybackRate = typing___cast(CommandValue, 20)
RateTrack = typing___cast(CommandValue, 21)
LikeTrack = typing___cast(CommandValue, 22)
DislikeTrack = typing___cast(CommandValue, 23)
BookmarkTrack = typing___cast(CommandValue, 24)
SeekToPlaybackPosition = typing___cast(CommandValue, 45)
ChangeRepeatMode = typing___cast(CommandValue, 46)
ChangeShuffleMode = typing___cast(CommandValue, 47)
EnableLanguageOption = typing___cast(CommandValue, 53)
DisableLanguageOption = typing___cast(CommandValue, 54)
NextChapter = typing___cast(CommandValue, 25)
PreviousChapter = typing___cast(CommandValue, 26)
NextAlbum = typing___cast(CommandValue, 27)
PreviousAlbum = typing___cast(CommandValue, 28)
NextPlaylist = typing___cast(CommandValue, 29)
PreviousPlaylist = typing___cast(CommandValue, 30)
BanTrack = typing___cast(CommandValue, 31)
AddTrackToWishList = typing___cast(CommandValue, 32)
RemoveTrackFromWishList = typing___cast(CommandValue, 33)
NextInContext = typing___cast(CommandValue, 34)
PreviousInContext = typing___cast(CommandValue, 35)
ResetPlaybackTimeout = typing___cast(CommandValue, 41)
SetPlaybackQueue = typing___cast(CommandValue, 48)
AddNowPlayingItemToLibrary = typing___cast(CommandValue, 49)
CreateRadioStation = typing___cast(CommandValue, 50)
AddItemToLibrary = typing___cast(CommandValue, 51)
InsertIntoPlaybackQueue = typing___cast(CommandValue, 52)
ReorderPlaybackQueue = typing___cast(CommandValue, 55)
RemoveFromPlaybackQueue = typing___cast(CommandValue, 56)
PlayItemInPlaybackQueue = typing___cast(CommandValue, 57)
PrepareForSetQueue = typing___cast(CommandValue, 58)
SetPlaybackSession = typing___cast(CommandValue, 59)

class CommandInfo(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    command: type___CommandValue = ...
    enabled: builtin___bool = ...
    active: builtin___bool = ...
    preferredIntervals: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___float] = ...
    localizedTitle: typing___Text = ...
    minimumRating: builtin___float = ...
    maximumRating: builtin___float = ...
    supportedRates: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___float] = ...
    localizedShortTitle: typing___Text = ...
    repeatMode: pyatv___mrp___protobuf___Common_pb2___RepeatMode.EnumValue = ...
    shuffleMode: pyatv___mrp___protobuf___Common_pb2___ShuffleMode.EnumValue = ...
    presentationStyle: builtin___int = ...
    skipInterval: builtin___int = ...
    numAvailableSkips: builtin___int = ...
    skipFrequency: builtin___int = ...
    canScrub: builtin___int = ...
    supportedPlaybackQueueTypes: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___int] = ...
    supportedCustomQueueIdentifiers: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text] = ...
    supportedInsertionPositions: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___int] = ...
    supportsSharedQueue: builtin___bool = ...
    upNextItemCount: builtin___int = ...
    preferredPlaybackRate: builtin___float = ...
    supportedPlaybackSessionTypes: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text] = ...
    currentPlaybackSessionTypes: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text] = ...
    playbackSessionIdentifier: typing___Text = ...

    def __init__(self,
        *,
        command : typing___Optional[type___CommandValue] = None,
        enabled : typing___Optional[builtin___bool] = None,
        active : typing___Optional[builtin___bool] = None,
        preferredIntervals : typing___Optional[typing___Iterable[builtin___float]] = None,
        localizedTitle : typing___Optional[typing___Text] = None,
        minimumRating : typing___Optional[builtin___float] = None,
        maximumRating : typing___Optional[builtin___float] = None,
        supportedRates : typing___Optional[typing___Iterable[builtin___float]] = None,
        localizedShortTitle : typing___Optional[typing___Text] = None,
        repeatMode : typing___Optional[pyatv___mrp___protobuf___Common_pb2___RepeatMode.EnumValue] = None,
        shuffleMode : typing___Optional[pyatv___mrp___protobuf___Common_pb2___ShuffleMode.EnumValue] = None,
        presentationStyle : typing___Optional[builtin___int] = None,
        skipInterval : typing___Optional[builtin___int] = None,
        numAvailableSkips : typing___Optional[builtin___int] = None,
        skipFrequency : typing___Optional[builtin___int] = None,
        canScrub : typing___Optional[builtin___int] = None,
        supportedPlaybackQueueTypes : typing___Optional[typing___Iterable[builtin___int]] = None,
        supportedCustomQueueIdentifiers : typing___Optional[typing___Iterable[typing___Text]] = None,
        supportedInsertionPositions : typing___Optional[typing___Iterable[builtin___int]] = None,
        supportsSharedQueue : typing___Optional[builtin___bool] = None,
        upNextItemCount : typing___Optional[builtin___int] = None,
        preferredPlaybackRate : typing___Optional[builtin___float] = None,
        supportedPlaybackSessionTypes : typing___Optional[typing___Iterable[typing___Text]] = None,
        currentPlaybackSessionTypes : typing___Optional[typing___Iterable[typing___Text]] = None,
        playbackSessionIdentifier : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"active",b"active",u"canScrub",b"canScrub",u"command",b"command",u"enabled",b"enabled",u"localizedShortTitle",b"localizedShortTitle",u"localizedTitle",b"localizedTitle",u"maximumRating",b"maximumRating",u"minimumRating",b"minimumRating",u"numAvailableSkips",b"numAvailableSkips",u"playbackSessionIdentifier",b"playbackSessionIdentifier",u"preferredPlaybackRate",b"preferredPlaybackRate",u"presentationStyle",b"presentationStyle",u"repeatMode",b"repeatMode",u"shuffleMode",b"shuffleMode",u"skipFrequency",b"skipFrequency",u"skipInterval",b"skipInterval",u"supportsSharedQueue",b"supportsSharedQueue",u"upNextItemCount",b"upNextItemCount"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"active",b"active",u"canScrub",b"canScrub",u"command",b"command",u"currentPlaybackSessionTypes",b"currentPlaybackSessionTypes",u"enabled",b"enabled",u"localizedShortTitle",b"localizedShortTitle",u"localizedTitle",b"localizedTitle",u"maximumRating",b"maximumRating",u"minimumRating",b"minimumRating",u"numAvailableSkips",b"numAvailableSkips",u"playbackSessionIdentifier",b"playbackSessionIdentifier",u"preferredIntervals",b"preferredIntervals",u"preferredPlaybackRate",b"preferredPlaybackRate",u"presentationStyle",b"presentationStyle",u"repeatMode",b"repeatMode",u"shuffleMode",b"shuffleMode",u"skipFrequency",b"skipFrequency",u"skipInterval",b"skipInterval",u"supportedCustomQueueIdentifiers",b"supportedCustomQueueIdentifiers",u"supportedInsertionPositions",b"supportedInsertionPositions",u"supportedPlaybackQueueTypes",b"supportedPlaybackQueueTypes",u"supportedPlaybackSessionTypes",b"supportedPlaybackSessionTypes",u"supportedRates",b"supportedRates",u"supportsSharedQueue",b"supportsSharedQueue",u"upNextItemCount",b"upNextItemCount"]) -> None: ...
type___CommandInfo = CommandInfo
