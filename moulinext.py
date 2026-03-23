# import subprocess
import os
import shutil
from pathlib import Path

from test import (
    Test,
    Result,
    add_tests,
    test_cmd_simple,
    test_func,
    test_ctype,
)
from norm import test_norminette
from footer import print_footer
from formatting import X, R

tests_performed: dict[str, list[Test]] = {}

# Path setup
# -----------------------------------------------------------------------------
path_script = Path(__file__).absolute().parent
path_tests = path_script / "tests"
path_tmp = path_script / ".tmp"
path_libft = path_tmp / "libft.a"
path_project = Path().resolve()

if path_tmp.exists():
    shutil.rmtree(path_tmp)
shutil.copytree(path_project, path_tmp)
os.chdir(path_tmp)

# -----------------------------------------------------------------------------
print(Path(path_script / "header.txt").read_text())


def check_bad_files(dir: str) -> bool:
    "Returns `True` if there's a file mismatch in the project folder."
    with open(dir / "expected_files.txt") as f:
        requirements = {line.strip() for line in f}
        if requirements == set(os.listdir()):
            return False
    return True


test_norminette(tests_performed)

result = Result(int(check_bad_files(path_script)))
add_tests(
    tests_performed, "Project",
    [Test("Extra/missing files",
          "Repository contents match requirements.", result)]
)

test_cmd_simple(
    ["make", "-s", "-j"], tests_performed, "Makefile",
    Test("make", "Library compiles normally using `make`.")
)

result = Result(int(not os.path.exists("./libft.a")))
add_tests(
    tests_performed, "Makefile",
    [Test("libft.a", "Library is found at `./libft.a`.", result)]
)


if [x for x in tests_performed["Makefile"] if x.result != Result.SUCCESS]:
    print(f"{R}\n\nFailed to run tests: library compilation failure.{X}")
else:
    test_ctype(tests_performed, path_tests, "isalpha")
    test_ctype(tests_performed, path_tests, "isdigit")
    test_ctype(tests_performed, path_tests, "isalnum")
    test_ctype(tests_performed, path_tests, "isascii")
    test_ctype(tests_performed, path_tests, "isprint")
    test_func(tests_performed, path_tests, "strlen", True)
    test_func(tests_performed, path_tests, "atoi", True)
    print()

print_footer(tests_performed)
