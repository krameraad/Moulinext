import subprocess
from subprocess import CalledProcessError

from test_info import TestInfo

X = "\033[0m"
H = "\033[1m"
D = "\033[2m"
R = "\033[91m"

errors: dict[str, list[str]] = {}


def add_error(errors: dict, error: dict[str, list[str]]) -> None:
    if not errors.get(error.keys[0])
    

try:
    subprocess.run(["norminette"], check=True)
except CalledProcessError:
    add_error(
        {"norme": ["Failed norminette check."]}
    )

# try:
#     subprocess.run(["make"], check=True)
# except CalledProcessError as e:
#     print("Compilation failed.")

# try:
#     subprocess.run(["make", "fclean"], check=True)
# except CalledProcessError as e:
#     print(e)

for error in errors:
    print(error)
print(f"{R}")
