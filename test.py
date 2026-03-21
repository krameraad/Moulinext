from enum import Enum
from dataclasses import dataclass


class Result(Enum):
    SUCCESS = 'O'
    FAILURE = 'X'
    TIMEOUT = 'T'
    MEMLEAK = 'M'
    NULLCHK = 'N'


@dataclass
class Test:
    input: str
    description: str
    result: Result | None = Result.SUCCESS
