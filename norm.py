from test import Test, test_cmd_simple
from formatting import (
    X,
    HU,
    R,
    DG,
)


def test_norminette(tests: dict) -> None:
    out = test_cmd_simple(
        ["norminette"], tests, "The Norm",
        Test("norminette", "All files pass norminette.")
    )
    out = out.decode("ascii").splitlines()
    out = "\n".join([x for x in out if "Error" in x])
    if out:
        print(f"{HU}\nNorminette{X}")
        print(R + out + X)
    else:
        print(DG + "\nNorminette: no problems found." + X)
