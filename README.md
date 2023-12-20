# Usage
We use poetry to handle dependencies.
If you do not have poetry, see the [installtion instructions](https://python-poetry.org/docs/#installing-with-the-official-installer).

Once installed:

ALlow for easy use with your IDE (e.g VSCODE) by running:

```bash
poetry config virtualenvs.in-project true

```
And then run:

```bash
poetry install
```

Now you can open or reload your VSCODE window, and activate the environment.

# Adding dependencies:

```bash
poetry add <DEPENDENCY_NAME>

```

Reload vscode window and dependencies should be there.

