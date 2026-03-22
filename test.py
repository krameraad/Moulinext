import subprocess
from enum import IntEnum, auto
from dataclasses import dataclass


class Result(IntEnum):
    "Types of test results. Success is `0`, failure is `1`."
    SUCCESS = 0
    FAILURE = auto()
    TIMEOUT = auto()
    MEMLEAK = auto()
    NULLCHK = auto()


@dataclass
class Test:
    name: str
    description: str
    result: Result | None = Result.SUCCESS


def list_tests(
        tests: dict[str, list[Test]],
        category: str,
        result: Result = Result.SUCCESS,
        inverse: bool = True
        ) -> list[Test]:
    """List all tests of a specified group.
    By default, looks for tests with an unsuccessful result.

    Args:
        tests: Test result collection to check.
        category: Category to look for tests in.
        result: Which result to find.
        inverse: Whether to return everything BUT the specified `result`.

    Returns:
        Filtered list of tests.
    """
    check = (lambda x, y: x != y) if inverse else (lambda x, y: x == y)
    ret = []
    for test in tests[category]:
        if check(test.result, result):
            ret.append(test)
    return ret


def add_test(
        tests: dict[str, list[Test]],
        category: str,
        to_add: list[Test]
        ) -> None:
    "Add test results `to_add` to `tests`, in `category`."
    if category not in tests:
        tests.update({category: to_add})
    else:
        tests[category] += to_add


def test_cmd_simple(
        cmd: list[str],
        tests: dict[str, list[Test]],
        group: str,
        test: Test,
        ) -> bytes:
    "Run a simple command and see if it returns an error code."
    proc = subprocess.run(cmd, capture_output=True)
    if proc.returncode:
        test.result = Result.FAILURE
    add_test(tests, group, [test])
    return proc.stdout
