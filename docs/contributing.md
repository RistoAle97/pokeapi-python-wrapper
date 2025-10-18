# Contributing
!!! tip
    You can use github desktop instead of git if it makes life easier for you.

If you want to contribute to the source code or the docs:

1. Fork the repository on :simple-github:.
1. Create a new branch where to commit your changes.
1. Clone your branch locally.

    ```console
    $ git clone -b <your_branch> https://github.com/{your-account}/pokeapi-python-wrapper
    $ cd pokeapi-python-wrapper
    ```

1. Create a virtual environment and activate it.

You're now ready to apply your desired changes, follow the next two subsections for more details. Feel free to open a pull request after you have committed your changes :heart:.

---

## :material-git: Source code
Install the package in editable mode with `dev` dependencies
=== ":simple-uv: uv"
    ```console
    $ uv pip install -e . --group dev
    ```
=== ":simple-python: pip"
    ```console
    $ pip install -e . --group dev
    ```

Then, install the pre-commit hooks in order to stop your commit if some check does not pass
```console
$ prek install
```

It is advised to run the type checker before committing
!!! warning
    Please note that `ty` is not production ready yet, so this passage is not mandatory
```console
$ ty check pypokeclient
```

---

## :material-archive: Docs
Install the package in editable mode with `docs` dependencies
=== ":simple-uv: uv"
    ```console
    $ uv pip install -e . --group docs
    ```
=== ":simple-python: pip"
    ```console
    $ pip install -e . --group docs
    ```

Start mkdocs to see a preview of the docs
```console
$ mkdocs serve
```
