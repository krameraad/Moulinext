from dataclasses import dataclass


@dataclass
class TestInfo:
    test: str
    info: str

    def __str__(self):
        return (
            f"- {self.test}\n"
            f"\t{self.info}"
        )
