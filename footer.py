from test import Test, Result
from formatting import X, H, HU, HI, D, R, G


def print_footer(test_collection: dict[str, list[Test]]) -> None:
    print(f"{HU}\nError details{X}")
    print(f"{H}Key: '●': Success")
    ok_count, count = 0, 0

    for group in test_collection.keys():
        print(f"\n{HI}{group}{X}")
        print(f"{D}{'─' * 80}{X}")
        for test in test_collection[group]:
            count += 1
            match test.result:
                case Result.SUCCESS:
                    check = G + "●" + X
                    ok_count += 1
                case Result.FAILURE:
                    check = R + "◯" + X
                case Result.TIMEOUT:
                    check = R + "◷" + X
                case Result.MEMLEAK:
                    check = R + "▭" + X
                case Result.NULLCHK:
                    check = R + "◎" + X
            print(f"{test.name:>20} {check} {test.description}")

    color = R if ok_count == count else G
    print(
        f"{HU}\nTests passed:{X} "
        f"{color}{ok_count:>6} / {count}{X}")
