import subprocess

from test import Test, Result, add_tests, test_cmd_simple
from formatting import X, HU, R, DG


def test_norminette(tests_performed: dict[str, list[Test]]) -> None:
    test = Test("norminette", "All files pass norminette.")
    out = subprocess.run(["norminette"], capture_output=True)
    if out.returncode:
        test.result = Result.FAILURE
    out = out.stdout.decode("ascii").splitlines()
    out = "\n".join([x for x in out if "Error" in x])
    if out:
        print(f"{HU}\nNorminette{X}")
        print(R + out + X)
    else:
        print(DG + "\nNorminette: no problems found." + X)
    add_tests(tests_performed, "The Norm", [test])
