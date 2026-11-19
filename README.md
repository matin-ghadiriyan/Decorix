# Decorix

**A Python library for managing decorators and function execution hooks.**

Decorix provides a simple way to manage function hooks and create conditional decorators. It allows you to execute custom functions before, after, or regardless of the execution result of another function.

## Features

- **Before Hook:** Execute a registered function before the decorated function.
- **After Hook:** Execute a registered function after the decorated function and receive its return value.
- **Finally Hook:** Execute a registered function regardless of whether the decorated function succeeds or raises an exception.
- **Hook Registration:** Register and manage functions using unique keys.
- **Conditional Decorators:** Validate conditions before executing a decorated function.
- **Custom Exceptions:** Handle invalid values, types, and missing or duplicate keys.

## Project Structure

```text
Decorix/
│
├── src/
│   ├── decorators/
│   │   └── hooks/
│   │       ├── BaseHooks.py
│   │       └── __init__.py
│   │
│   ├── BaseClass.py
│   ├── app.py
│   ├── exceptions.py
│   └── __init__.py
│
├── .gitignore
├── CHANGELOG.md
└── README.md
```

## Hooks

Decorix currently provides three types of hooks.

### Before

Executes a registered function before the decorated function.

```python
@app.before("before_task")
def my_function():
    print("Function is about to execute")
```

### After

Executes a registered function after the decorated function and passes the original function's return value to it.

```python
@app.after("after_task")
def my_function():
    print("Function executed successfully")
```

### Finally

Executes a registered function after the decorated function finishes, whether it returns normally or raises an exception.

```python
@app._finally("finally_task")
def my_function():
    print("Execution finished")
```

## Hook Registration

Functions are registered using unique string keys.

```python
app.register(
    before_task=lambda: print("Before"),
    after_task=lambda result: print(result),
    finally_task=lambda: print("Finally")
)
```

Each hook uses its corresponding registered key.

## Conditional Decorators

The `validate` decorator checks multiple conditions before executing the original function.

```python
@app.validate(
    error_handler,
    condition_one,
    condition_two
)
def my_function():
    print("All conditions passed")
```

If any condition returns `False`, the error handler is executed instead of the original function.

## Exceptions

Decorix defines custom exceptions for different validation and registration errors:

- `ValueIsNotValid`
- `TypeIsNotValid`
- `KeyIsAlreadyExists`
- `KeyIsNotInDictionary`

## Requirements

- Python
- No third-party dependencies are currently required by the source code.

## Development Status

Decorix is currently under development. Its API and internal structure may change in future releases.

## License

See the `LICENSE` file for licensing information.