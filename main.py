import argparse
import sys
from typing import List, Tuple


class FractionGenerator:
    """Fraction Generator.

    Attributes
    ==========
    state: List[int]
        ``self.state`` can only be in 5 different states.

        - When ``self.state == 0`, generator is at its initial state.
          Calling generator at inital state will yield ``(0, 1)``.
        - When ``self.state == 1`, generator will find all co-primes of
          ``self.nominator`` and stores them in ``self.memory``.
          Each time a co-prime ``p`` is found, generator will yield
          ``(self.nominator, p)``.
          When all co-primes are exhausted, set ``self.state = 2``.
        - When ``self.state == 2`, generator will enumerate all co-primes
          ``(n, m)`` in ``self.memory`` and yield ``(m, n)``.
          When all co-primes are exhausted, set ``self.state = 3``.
        - When ``self.state == 3`, generator will enumerate all co-primes
          ``(n, m)`` in ``self.memory`` and yield ``(-n, m)``.
          When all co-primes are exhausted, set ``self.state = 4``.
        - When ``self.state == 4`, generator will enumerate all co-primes
          ``(n, m)`` in ``self.memory`` and yield ``(-m, n)``.
          When all co-primes are exhausted, reset ``self.state = 1`` and
          ``self.memory`` and increase ``self.nominator``.

    denominator: int
        Incrementally record co-primes of ``self.nominator``.
    nominator: int
        Incrementally enumerate natural numbers.
    memory: List[Tuple[int, int]]
        Record all co-primes of ``self.nominator``.
    memory_idx: int
        Index of co-primes being yield.
    """

    def __init__(self):
        self.denominator = 1
        self.nominator = 0
        self.state = 0
        self.memory = []
        self.memory_idx = 0

    def gcd(self, a: int, b: int) -> int:
        if a == 0:
            if b != 0:
                return b
            else:
                return None
        if b == 0:
            return a

        while a != 1:
            r = a % b
            if r == 0:
                return b
            a, b = b, r
        return 1

    def __next__(self) -> Tuple[int, int]:
        """Yield rationals.

        Returns
        =======
        Tuple[int, int]
            Rationals where the first element is nominator and the second is
            denominator.
        """
        # Generating (0, 1).
        if self.nominator == 0:
            res = (0, 1)
            self.nominator = 1
            self.state = 1

        # Generating (1, 1) and (-1, 1).
        elif self.nominator == 1:
            if self.state == 1:
                res = (1, 1)
                self.state = 3
            else:
                res = (-1, 1)
                self.nominator = 2
                self.state = 1

        # Generating (2, 1), (1, 2), (-2, 1), (-1, 2).
        elif self.nominator == 2:
            if self.state == 1:
                res = (2, 1)
                self.state = 2
            elif self.state == 2:
                res = (1, 2)
                self.state = 3
            elif self.state == 3:
                res = (-2, 1)
                self.state = 4
            else:
                res = (-1, 2)
                self.nominator = 3
                self.state = 1

        # Generating the rest.
        else:
            # State 1.
            if self.state == 1:
                # Enumerate all number p to construct fraction (n, p) where
                # n and p have no common divisor (gcd(n, p) == 1).
                for denominator in range(self.denominator, self.nominator):
                    if self.gcd(self.nominator, denominator) == 1:
                        break

                res = (self.nominator, denominator)
                self.denominator = denominator + 1
                self.memory.append(res)

                # Advance to state 2 when exhausting all known co-primes.
                # Reset denominator to 1.
                if denominator == self.nominator - 1:
                    self.state = 2
                    self.denominator = 1
            # State 2.
            elif self.state == 2:
                res = self.memory[self.memory_idx]
                res = (res[1], res[0])
                self.memory_idx += 1

                # Advance to state 3 when exhausting all fractions in memory.
                # Reset memory index to 0.
                if self.memory_idx == len(self.memory):
                    self.memory_idx = 0
                    self.state = 3
            # State 3.
            elif self.state == 3:
                res = self.memory[self.memory_idx]
                res = (-res[0], res[1])
                self.memory_idx += 1

                # Advance to state 4 when exhausting all fractions in memory.
                # Reset memory index to 0.
                if self.memory_idx == len(self.memory):
                    self.memory_idx = 0
                    self.state = 4
            # State 4.
            else:
                res = self.memory[self.memory_idx]
                res = (-res[1], res[0])
                self.memory_idx += 1

                # Reset to state 1 when exhausting all fractions in memory.
                # Cleanup memory and increment nominator.
                if self.memory_idx == len(self.memory):
                    self.memory = []
                    self.memory_idx = 0
                    self.state = 1
                    self.nominator += 1

        return res


def bijection(n: int) -> List[Tuple[int, int]]:
    """Bijective which maps natural numbers to rationals.

    Parameters
    ==========
    n: int
        Maximum natural number being mapped to rationals.

    Returns
    =======
    List[Tuple[int, int]]
        List of rationals being mapped.
    """
    res = []
    gen = FractionGenerator()
    for i in range(n + 1):
        res.append(next(gen))

    return res


def parse_args(argv: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--n',
        help='The n-th rational number.',
        required=True,
        type=int
    )
    parser.add_argument(
        '--all',
        help='List all rational numbers in `range(0, n)`.',
        action='store_true',
    )

    args = parser.parse_args(argv)

    return args


def main(argv: List[str]):
    args = parse_args(argv)

    res = bijection(n=args.n)

    if args.all:
        for nominator, denominator in res:
            print(f'{nominator}/{denominator}')

    else:
        nominator, denominator = res[-1]
        print(f'{nominator}/{denominator}')


if __name__ == '__main__':
    main(sys.argv[1:])
