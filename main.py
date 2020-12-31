import argparse
import math
import sys
from typing import Generator, List, Tuple


def q_generator() -> Generator[Tuple[int, int], None, None]:
    """Rationals generator.

    Yields
    ======
    Generator[Tuple[int, int], None, None]
        Rationals represented by tuple of two integers.
    """
    yield (0, 1)
    yield (1, 1)
    yield (-1, 1)
    n = 2
    while True:
        for i in range(1, n):
            # Only yields co-primes, which avoid duplicated enumeration.
            if math.gcd(n, i) == 1:
                yield (n, i)
                yield (i, n)
                yield (-n, i)
                yield (-i, n)
        n += 1


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
    gen = q_generator()
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
