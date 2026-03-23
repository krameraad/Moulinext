import subprocess
from pathlib import Path
from enum import IntEnum, auto
from dataclasses import dataclass

from test_registry import REGISTRY
from formatting import X, D, R, G, M


class Result(IntEnum):
    "Types of test results. Success is `0`, failure is `1`."
    SUCCESS = 0
    FAILURE = auto()
    TIMEOUT = auto()
    MEMLEAK = auto()
    NULLCHK = auto()


RESULT_TO_GLYPH = {
    Result.SUCCESS: G + "●" + X,
    Result.FAILURE: R + "◯" + X,
    Result.TIMEOUT: R + "…" + X,
    Result.MEMLEAK: M + "&" + X,
    Result.NULLCHK: M + "*" + X,
}


@dataclass
class Test:
    name: str
    description: str
    result: Result | None = Result.SUCCESS


def add_tests(
        tests_performed: dict[str, list[Test]],
        category: str,
        to_add: list[Test]
        ) -> None:
    "Add test results `to_add` to `tests`, in `category`."
    if category not in tests_performed:
        tests_performed.update({category: to_add})
        print(f"\n{f'{category} {D}-{X} ':>31}", end="")
    else:
        tests_performed[category] += to_add
    for test in to_add:
        print(RESULT_TO_GLYPH[test.result], end="")


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
    add_tests(tests, group, [test])
    return proc.stdout


def test_func(
        tests_performed: dict[str, list[Test]],
        path_tests: Path,
        funcname: str,
        nullcheck: bool = False,
        ) -> None:
    path = path_tests / funcname / "tester.c"
    out = subprocess.run(["gcc", path, "libft.a"], check=True)

    test_list = []
    for test in REGISTRY[funcname]:
        path = Path(path_tests / funcname / test[0]).with_suffix(".txt")
        try:
            out = subprocess.run(["./a.out", path], timeout=0.5)
            test_list.append(Test(*test, Result(out.returncode)))
        except subprocess.TimeoutExpired:
            test_list.append(Test(*test, Result.TIMEOUT))

    if nullcheck:
        out = subprocess.run(["./a.out"])
        test_list.append(Test("NULL", "NULL argument should segfault.",
                         Result(not out.returncode)))

    add_tests(tests_performed, funcname, test_list)


def test_ctype(
        tests_performed: dict[str, list[Test]],
        path_tests: Path,
        funcname: str,
        ) -> None:
    path = (path_tests / "ctype" / funcname).with_suffix(".c")
    out = subprocess.run(["gcc", path, "libft.a"], check=True)

    test_list = []
    for test in REGISTRY["ctype"]:
        path = Path(path_tests / "ctype" / test[0]).with_suffix(".txt")
        try:
            out = subprocess.run(["./a.out", path], timeout=1)
            test_list.append(Test(*test, Result(out.returncode)))
        except subprocess.TimeoutExpired:
            test_list.append(Test(*test, Result.TIMEOUT))

    add_tests(tests_performed, funcname, test_list)
