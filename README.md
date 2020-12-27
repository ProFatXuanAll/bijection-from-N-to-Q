# bijection-from-N-to-Q

Using python to define a bijection from N to Q.

## Installation

```sh
pipenv install
```

## Execution

```sh
# Launch virtual environment.
pipenv shell

# Get n-th rational number from bijection.
python main.py --n 100

# Get rational numbers from bijection in range 0 to n.
python main.py --n 100 --all
```

## Test

```sh
pipenv install --dev
pipenv run test
pipenv run test-coverage
```
