import subprocess
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


def add_test(
        tests: dict[str, list[Test]],
        category: str,
        test: Test
        ) -> None:
    "Add test result `test` to `tests`, in `category`."
    if category not in tests:
        tests.update({category: [test]})
    else:
        tests[category].append(test)


def test_cmd_simple(
        cmd: list[str],
        tests: dict[str, list[Test]],
        group: str,
        test: Test,
        ) -> None:
    "Run a simple command and see if it returns an error code."
    if subprocess.run(cmd).returncode:
        test.result = Result.FAILURE
    add_test(tests, group, test)
