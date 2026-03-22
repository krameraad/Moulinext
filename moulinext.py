import subprocess
import os
import shutil

from test import Test, Result, add_test, test_cmd_simple


X = "\033[0m"     # Clear formatting
H = "\033[1m"     # Bold (Header)
HU = "\033[1;4m"  # Header Underlined
HI = "\033[1;3m"  # Header Italics
D = "\033[2m"     # Dim
R = "\033[91m"    # Red
G = "\033[92m"    # Green

tests: dict[str, list[Test]] = {}


prog_dir = os.path.dirname(os.path.abspath(__file__))
test_dir = prog_dir + "/tests"
tmp_dir = prog_dir + "/.tmp"

# shutil.copy(os.curdir, tmp_dir + "/test")


def check_bad_files() -> bool:
    "Returns `True` if there are any extra files in the project folder."
    with open(prog_dir + "/expected_files.txt") as f:
        requirements = {line.strip() for line in f}
        if requirements == set(os.listdir()):
            return False
    return True


subprocess.run(["make", "fclean"])
result = Result.FAILURE \
    if check_bad_files() else Result.SUCCESS
add_test(
    tests, "Project",
    Test("Extra files", "No unauthorized files are present.", result))

test_cmd_simple(
    ["norminette"], tests, "The Norm",
    Test("norminette", "All files pass norminette.")
)
test_cmd_simple(
    ["make"], tests, "Makefile",
    Test("make", "Library compiles normally using `make`.")
)

result = Result.SUCCESS \
    if os.path.exists("./libft.a") else Result.FAILURE
add_test(
    tests, "Makefile",
    Test("libft.a", "Library is found at `./libft.a`.", result))


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

if ko_count:
    color = R
else:
    color = G
print(
    f"{HU}\nTests passed:{X} "
    f"{color}{ok_count:>6} / {ok_count + ko_count}{X}")
