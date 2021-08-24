# Limit time and memory usage of a Python function

## Installation

```
pip install flimit
```

## Usage

```python
from flimit.memory import limit_memory
from flimit.time import limit_time

@limit_memory(10**9)
@limit_time(60)
def f(...):  # f will have a limit of 1 Go allocation memory and 60 seconds computation time
    ...
```

## Tests

```
python -m pytest tests
```