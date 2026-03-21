import subprocess
import os

from test import Test, Result


X = "\033[0m"     # Clear formatting
H = "\033[1m"     # Bold (Header)
HU = "\033[1;4m"  # Header Underlined
HI = "\033[1;3m"  # Header Italics
D = "\033[2m"     # Dim
R = "\033[91m"    # Red
G = "\033[92m"    # Green

tests: dict[str, list[Test]] = {}


def add_test(tests: dict[str, list[Test]], group: str, test: Test) -> None:
    if group not in tests:
        tests.update({group: [test]})
    else:
        tests[group].append(test)


def test_cmd_simple(
            cmd: list[str],
            tests: dict[str, list[Test]],
            group: str,
            test: Test,
        ) -> None:
    if subprocess.run(cmd).returncode:
        test.result = Result.FAILURE
    add_test(tests, group, test)


def check_bad_files() -> bool:
    "Returns `True` if there are any extra files in the project folder."
    script_dir = os.path.dirname(os.path.abspath(__file__))
    with open(script_dir + "/expected_files.txt") as f:
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
            color, grade = G, "OK"
            ok_count += 1
        else:
            color, grade = R, "KO"
            ko_count += 1
        print(f"{test.input:>20} {D}•{X} "
              f"{color}[{grade}]{X} {test.description}")

if ko_count:
    color = R
else:
    color = G
print(
    f"{HU}\nTests passed:{X} "
    f"{color}{ok_count:>6} / {ok_count + ko_count}{X}")
