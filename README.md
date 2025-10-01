### py-robot-template

[![Codecov](https://codecov.io/gh/MarcinMaciaszek/py-robot-template/branch/main/graph/badge.svg)](https://codecov.io/gh/MarcinMaciaszek/py-robot-template) [![CI](https://github.com/MarcinMaciaszek/py-robot-template/actions/workflows/ci.yml/badge.svg)](https://github.com/MarcinMaciaszek/py-robot-template/actions/workflows/ci.yml)

py-robot-template is a template project demonstrating how to create a Python package for use with RobotFramework.

## Features
- Example of building a custom RobotFramework library in Python
- Simple test versioning approach
- Instructions for building and using as a command-line tool
- Uses [uv](https://github.com/astral-sh/uv) for environment management

## Getting Started
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/py-robot-template.git
   ```
2. Create a virtual environment using uv (Python 3.11+ required):
   ```bash
   uv venv
   ```
3. (Optional) Install development dependencies:
   ```bash
   uv pip install -e ".[dev]"
   ```

## Running Tests with uv
To run unit tests with coverage and generate a coverage report:
```bash
uv run coverage run --source=src/py_robot_template -m unittest discover tests/unit
uv run coverage xml
```
To view the coverage report in the terminal:
```bash
uv run coverage report
```

To run RobotFramework tests:
```bash
uv run robot tests/robot
```

## Project Structure
- `src/py_robot_template` - Python library code
- `tests/robot` - RobotFramework test suites
- `tests/unit` - Unit tests for Python code

## Contributing

Contributions are welcome! Before starting development:

1. Install `uv`:
   ```bash
   pip install uv
   ```
2. Create a virtual environment using uv:
   ```bash
   uv venv
   ```
3. Activate the virtual environment:
   - On Unix/macOS:
     ```bash
     source .venv/bin/activate
     ```
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
5. Install pre-commit hooks:
   ```bash
   pre-commit install
   ```
6. (Optional) Run all hooks manually on all files:
   ```bash
   pre-commit run --all-files
   ```

Pre-commit will automatically check your code before every commit.

To contribute:
1. Fork this repository.
2. Create a new branch for your feature or fix:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Make your changes and add tests if needed.
4. Commit your changes:
   ```bash
   git commit -am "Add your feature description"
   ```
5. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```
6. Open a pull request describing your changes.

Please ensure your code follows the existing style and passes all tests before submitting a pull request.

### Code Style & Checks

- To run ruff linter:
  ```bash
  ruff check .
  ```
- To format code with ruff:
  ```bash
  ruff format .
  ```
- To run mypy type checks:
  ```bash
  mypy .
  ```

## License
This project is licensed under the MIT License.

This project supports Python 3.11 and newer. All checks are run for Python 3.11, 3.12, and 3.13 in CI.
