# Decorix

**Decorix** is a Python library focused on function decorators and hook-based execution management.

It provides a structured way to execute custom functions before, after, and finally around the execution of another function. It also includes an exception-handling mechanism that allows developers to capture and process error information.

## Features

- **Before Hooks:** Execute registered functions before the decorated function.
- **After Hooks:** Execute registered functions after successful function execution and receive its return value.
- **Finally Hooks:** Execute registered functions when the decorated function finishes, whether it succeeds or raises an exception.
- **Exception Handler:** Capture exception information and pass it to registered handler functions.
- **Multiple Hooks:** Register different hooks using separate keys.
- **Reusable Decorators:** Apply registered hooks to multiple functions.
- **Function Metadata Preservation:** Preserve the original function metadata using `functools.wraps`.

## Hook Types

| Hook | Description |
|---|---|
| `Before` | Runs before the original function. |
| `After` | Runs after successful execution and receives the return value. |
| `Finally` | Runs when the function finishes, including when an exception occurs. |
| `Handler` | Captures exceptions and provides their information to a registered callback. |

## Usage

The following examples assume that a configured Decorix instance is available as `app`.

### 1. Before Hook

```python
app.b().register(
    start=lambda: print("Before execution")
)

@app.b().before("start")
def worker():
    print("Working...")

worker()
```

### 2. After Hook

After hooks receive the return value of the decorated function.

```python
app.a().register(
    result=lambda value: print("Result:", value)
)

@app.a().after("result")
def worker():
    return "Task completed"

worker()
```

### 3. Finally Hook

Finally hooks execute even when the decorated function raises an exception.

```python
app.f().register(
    finish=lambda: print("Execution finished")
)

@app.f()._finally("finish")
def worker():
    print("Working...")
    return "Done"

worker()
```

### 4. Exception Handling

The Handler mechanism provides access to exception details.

```python
app.h().register(
    error=lambda error, message, traceback, exception:
        print(f"Error: {error}")
)

@app.h().handler("error")
def worker():
    return 12 + "hello"

worker()
```

The handler callback receives:

| Argument | Description |
|---|---|
| `error` | Exception class name. |
| `message` | Exception message. |
| `traceback` | Full traceback as a string. |
| `exception` | Original exception object. |

## Combining Hooks

Different hook types can be applied to the same function.

```python
@app.b().before("start")
@app.a().after("result")
@app.f()._finally("finish")
def worker():
    print("Working...")
    return "Completed"

worker()
```

For a successful execution, the intended lifecycle is:

```text
Before
  |
Original Function
  |
After
  |
Finally
```

If the original function raises an exception, the After hook is skipped, while the Finally hook still executes.

## Testing

Decorix includes tests for hook execution and exception handling.

Run the test suite from the project root:

```bash
python -m test.test_hooks
```

## Project Status

Decorix is under active development.

Features, APIs, and internal implementation may change as the project evolves.

## License

License information will be added when the project license is established.
