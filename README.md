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

# TODO
Let's consider the following todo's, unless you have better idea's (feel free to change / add / remove todo's)
- [x] Extract data preprocessing methods from AFCS.ipynb
- [x] Extract prophet model declaration froom AFCS.ipynb
- [x] Evaluate prophet model in dedicated notebook (extract evaluation logic from AFCS.ipynb)
- [ ] Extract arima model declaration froom AFCS.ipynb
- [ ] Evaluate arima model in dedicated notebook (extract evaluation logic from AFCS.ipynb)
- [ ] Extract Exploratoray Data Analysis from AFCS.ipynb and make plots in separate notebook.
- [ ] Try out more models (with dedicated .py and .ipynb files for model declarations and perfomance evaluationr respectively)
- [ ] Finish Report.
