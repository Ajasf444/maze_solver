from enum import StrEnum, auto


class SolutionStrategy(StrEnum):
    A_STAR = auto()
    DEPTH_FIRST_SEARCH = auto()
    GREEDY = auto()
