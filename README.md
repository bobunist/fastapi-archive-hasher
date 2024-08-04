# Example archive downloader.

## How it works:

It is three times in async mode, downloads and writes the archive locally
in a temporary directory, extracts the files,
asserts and returns their hashes if they are correct.

## Quickstart:

First, create <code>.env</code> file with archive url:

Example:

```dotenv
REPO_URL=https://gitea.radium.group/radium/project-configuration/archive/master.zip
```

Then run the following commands to bootstrap your environment with <code>poetry</code>:

```shell
poetry install
poetry shell
```

To run the web application in debug mode, ensure you are in the root
directory and use the following command:

```shell
make
```

## Web routes:

All routes are accessible via the <code>/docs</code> or <code>/redoc</code> paths with Swagger or ReDoc.

## Tests:

Tests for this project can be found in the <code>tests/</code> folder.

The test environment variables are set up in the <code>project.toml</code>
file at the <code>[tool.pytest.ini_options]</code> section.

```toml
[tool.pytest.ini_options]
env = [
  "REPO_URL=https://github.com/nsidnev/fastapi-realworld-example-app/archive/refs/heads/master.zip",
]
pythonpath = ["."]
testpaths = ["tests"]
python_files = "test*.py"
addopts = "-rsxX -l --tb=short --strict-markers --doctest-modules"
xfail_strict = "true"
```

For run tests use:

```shell
make test
```

For tests coverage report use:

```shell
make report
```

## Project structure:

Files related to application are in the <code>app/</code>
or <code>tests/</code> directories. Application parts are:

```
├── api                           - web related stuff.
│     └── v1                      - version of router.
│         ├── dependencies.py     - dependencies with controllers realizations.
│         └── router.py           - router definition.
│
├── controllers                   - business-logic combining use-cases.
│         └── v1                  - version of controllers.
│             └── dependencies.py - dependencies with repos realizations.
│
├── domain                        - models and schemas stuff.
│
├── interfaces                    - asbtract repos and other interfaces.
│
├── repository                    - all crud stuff.
│
├── use_cases                     - business logic decomposed for reuse.
│
├── utils                         - utils for any layers.
│
│
├── config.py                     - env and const configurator.
└── main.py                       - fastAPI application creation and configuration.
```
