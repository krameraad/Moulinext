import subprocess
import os
import shutil

from test import (
    Test,
    Result,
    add_test,
    test_cmd_simple,
    list_tests,
)
from norm import test_norminette
from formatting import (  # noqa
    X,
    H,
    HU,
    HI,
    D,
    R,
    G,
    DG,
)

tests: dict[str, list[Test]] = {}


program_dir = os.path.dirname(os.path.abspath(__file__))
test_dir = program_dir + "/tests"
tmp_dir = program_dir + "/.tmp"
lib_path = tmp_dir + "/libft.a"
project_dir = os.getcwd()
print(lib_path, test_dir + "/test_strlen.c")

if os.path.exists(tmp_dir):
    shutil.rmtree(tmp_dir)
shutil.copytree(project_dir, tmp_dir)
os.chdir(tmp_dir)

with open(program_dir + "/header.txt") as f:
    print(f.read())


def check_bad_files(dir: str) -> bool:
    "Returns `True` if there are any extra files in the project folder."
    with open(dir + "/expected_files.txt") as f:
        requirements = {line.strip() for line in f}
        if requirements == set(os.listdir()):
            return False
    return True


result = Result(int(check_bad_files(program_dir)))
add_test(
    tests, "Project",
    Test("Extra files", "No unauthorized files are present.", result)
)

test_norminette(tests)

test_cmd_simple(
    ["make", "-s", "-j"], tests, "Makefile",
    Test("make", "Library compiles normally using `make`.")
)

result = Result(int(not os.path.exists("./libft.a")))
add_test(
    tests, "Makefile",
    Test("libft.a", "Library is found at `./libft.a`.", result))


if list_tests(tests, "Makefile"):
    print(f"{R}\nFailed to run tests: library compilation failure.{X}")
else:
    out = subprocess.run(["gcc", test_dir + "/test_strlen.c", lib_path])
    if not out.returncode:
        out = subprocess.run(["a.out"])
    print(f"{out.returncode:032b}")


print(f"{HU}\nError details{X}")
ok_count, ko_count = 0, 0

for group in tests.keys():
    print(f"\n{HI}{group}{X}")
    print(f"{D}{'─' * 80}{X}")
    for test in tests[group]:
        if test.result == Result.SUCCESS:
            check = G + "●" + X
            ok_count += 1
        else:
            check = R + "◯" + X
            ko_count += 1
        print(f"{test.input:>20} {check} {test.description}")

color = R if ko_count else G
print(
    f"{HU}\nTests passed:{X} "
    f"{color}{ok_count:>6} / {ok_count + ko_count}{X}")
