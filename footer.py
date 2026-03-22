from test import Test, Result
from formatting import X, H, HU, HI, D, R, G, M


def print_footer(test_collection: dict[str, list[Test]]) -> None:
    print(f"{HU}\nError details{X}")
    print(
        f"{H}Key:     {G}● Success    {R}◯ Failure    "
        f"… Time-out    {M}& Memory leak    * Malloc guard{X}")
    ok_count, count = 0, 0

    for group in test_collection.keys():
        print(f"\n{HI}{group}{X} {D}{'─' * (79 - len(group))}{X}")
        for test in test_collection[group]:
            count += 1
            match test.result:
                case Result.SUCCESS:
                    check = G + "●" + X
                    ok_count += 1
                case Result.FAILURE:
                    check = R + "◯" + X
                case Result.TIMEOUT:
                    check = R + "…" + X
                case Result.MEMLEAK:
                    check = M + "&" + X
                case Result.NULLCHK:
                    check = M + "*" + X
            print(f"{test.name:>20} {check} {test.description}")

    color = R if ok_count != count else G
    print(
        f"{HU}\nTests passed:{X}\n"
        f"{color}{ok_count:>3} / {count}{X}")
