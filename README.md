# demo-broken-repo

Intentionally broken Python project used to demonstrate the **Test-Failure Healer** agent.

## Bugs hidden in `src/calculator.py`

Three bugs are intentionally introduced. The agent must find and fix them.

| Test | Expected behaviour | Bug |
|---|---|---|
| `test_divide_by_zero_raises_value_error` | `divide(5,0)` raises `ValueError` | raises `ZeroDivisionError` instead |
| `test_average_empty_list` | `average([])` returns `0.0` | raises `ZeroDivisionError` |
| `test_is_prime_one_is_not_prime` | `is_prime(1)` returns `False` | returns `True` |

## Running tests

```bash
pip install -r requirements.txt
pytest -v
# 3 tests fail out of 10
```

## Demo usage

Published as its own public repository: https://github.com/Sacha1710/demo-broken-repo

Point the agent at it:

```bash
curl -X POST http://localhost:8080/repair \
  -H 'Content-Type: application/json' \
  -d '{"repo_url": "https://github.com/Sacha1710/demo-broken-repo", "branch": "main"}'
```
