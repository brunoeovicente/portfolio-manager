
from enum import Enum
from dataclasses import dataclass


class InstrumentType(Enum):
    OPTION = 'option'
    FUTURE = 'future'


@dataclass
class Instrument:
    id : str
    jurisdiction_id : str
    type: InstrumentType

