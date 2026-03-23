from test import Test, Result, RESULT_TO_GLYPH
from formatting import X, H, HU, HI, D, R, G, M


def print_footer(tests_performed: dict[str, list[Test]]) -> None:
    print(f"{HU}\nError details{X}")
    print(
        f"{H}Key:     {G}● Success    {R}◯ Failure    "
        f"… Time-out    {M}& Memory leak    * Malloc guard{X}")
    ok_count, count = 0, 0

    for group in tests_performed.keys():
        report = f"\n{HI}{group}{X} {D}{'─' * (79 - len(group))}{X}\n"
        for test in tests_performed[group]:
            count += 1
            if test.result == Result.SUCCESS:
                ok_count += 1
            check = RESULT_TO_GLYPH[test.result]
            if test.result:
                report += f"{test.name:>20} {check} {test.description}\n"
        if [x for x in tests_performed[group] if x.result != Result.SUCCESS]:
            print(report)

    color = R if ok_count != count else G
    print(
        f"{HU}\nTests passed:{X}\n"
        f"{color}{ok_count:>3} / {count}{X}")
