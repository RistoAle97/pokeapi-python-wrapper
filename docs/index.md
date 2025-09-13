<div align="center">
    <h1>PyPokéClient</h1>
    <img src="logo.png" width=35% /><br>
    <strong>Synchronous and asynchronous clients to fetch data from PokéAPI</strong><br><br>
    <a href="https://github.com/python/cpython">
        <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
    </a>
    <a href="https://github.com/pydantic/pydantic">
        <img src="https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white" />
    </a><br>
    <a href="https://pypi.org/project/pypokeclient/">
        <img src="https://img.shields.io/pypi/v/pypokeclient.svg?style=for-the-badge&logo=pypi&logoColor=white" />
    </a>
    <a href="https://pypi.org/project/pypokeclient/">
        <img src="https://img.shields.io/pypi/pyversions/pypokeclient.svg?style=for-the-badge&logo=python&logoColor=white" />
    </a>
</div>


---

## :material-notebook: Features
**PyPokéClient** is a Python wrapper for fetching data from PokéAPI, its main features are:

- **Coverage:** all PokéAPI endpoints are covered.
- **Data validation:** uses Pydantic dataclasses for the API implementation.
- **Flexibility:** can choose between synchronous and asynchronous clients.
- **Caching:** can employ a local cache system for faster responses and to respect PokéAPI Fair Use policy.

---

## :material-package: Installation
!!! warning "Requirements"
    This package requires :simple-python: >= 3.12.

It is highly advised to create a new virtual environment.
=== ":simple-uv: uv"
    ```console
    $ uv venv
    ```
=== ":simple-python: pip"
    ```console
    $ python -m venv .venv
    ```

!!! note
    When using the default virtual environment name (i.e.: _.venv_), uv will automatically find and use the virtual environment during subsequent invocations.

Then, activate the virtual environment
=== ":material-linux: Linux"
    ```console
    $ source .venv/bin/activate
    ```
=== ":material-microsoft-windows: cmd"
    ```console
    > .\.venv\Scripts\activate.bat
    ```
=== ":material-powershell: PowerShell"
    ```console
    > .\.venv\Scripts\Activate.ps1
    ```

You can now install the package by simply
=== ":simple-uv: uv"
    ```console
    $ uv pip pypokeclient
    ```
=== ":simple-python: pip"
    ```console
    $ pip install pypokeclient
    ```
