import subprocess
from pathlib import Path

from test import Test, Result
from test_registry import REGISTRY


def test_func(
        path_tests: Path,
        funcname: str,
        nullcheck: bool = False,
        ) -> list[Test]:
    path = path_tests / funcname
    out = subprocess.run(["gcc", path / "tester.c", "libft.a"], check=True)

    test_list = []
    for test in REGISTRY[funcname]:
        path = Path(path_tests / funcname / test[0]).with_suffix(".txt")
        try:
            out = subprocess.run(["./a.out", path], timeout=1)
            test_list.append(Test(*test, Result(out.returncode)))
        except subprocess.TimeoutExpired:
            test_list.append(Test(*test, Result.TIMEOUT))

    if nullcheck:
        out = subprocess.run(["./a.out"])
        test_list.append(Test("NULL", "NULL argument causes segfault.",
                         Result(not out.returncode)))

    return test_list
