# import subprocess
import os
import shutil
from pathlib import Path

from functests import test_func
from test import (
    Test,
    Result,
    add_test,
    test_cmd_simple,
    list_tests,
)
from norm import test_norminette
from footer import print_footer
from formatting import X, R

test_collection: dict[str, list[Test]] = {}

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
    "Returns `True` if there are any extra files in the project folder."
    with open(dir / "expected_files.txt") as f:
        requirements = {line.strip() for line in f}
        if requirements == set(os.listdir()):
            return False
    return True


result = Result(int(check_bad_files(path_script)))
add_test(
    test_collection, "Project",
    [Test("Extra/missing files", "Repo contents match requirements.", result)]
)

test_norminette(test_collection)

test_cmd_simple(
    ["make", "-s", "-j"], test_collection, "Makefile",
    Test("make", "Library compiles normally using `make`.")
)

result = Result(int(not os.path.exists("./libft.a")))
add_test(
    test_collection, "Makefile",
    [Test("libft.a", "Library is found at `./libft.a`.", result)]
)


if list_tests(test_collection, "Makefile"):
    print(f"{R}\nFailed to run tests: library compilation failure.{X}")
else:
    add_test(
        test_collection, "strlen", test_func(path_tests, "strlen", True))

print_footer(test_collection)
