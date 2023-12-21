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


# Goal of the project

To succesfully complete the project, we define a clear set of goals:

- Create the best forecast possible on the dataset.
- We are free to use whataver model(s) we want, we can be creative. We can decide to go deep or go wide if we want.
- The RSME is the main evaluation method. Yet, deeper analysis is highly recommended.
- 20% code / 80% report, but good code is necessary for a good report.


# TODO
Let's consider the following todo's, unless you have better idea's (feel free to change / add / remove todo's)

- [x] Extract data preprocessing methods from AFCS.ipynb

- [x] Extract prophet model declaration from AFCS.ipynb
- [x] Evaluate prophet model in dedicated notebook (extract evaluation logic from AFCS.ipynb)

- [ ] Extract arima model declaration from AFCS.ipynb
- [ ] Evaluate arima model in dedicated notebook (extract evaluation logic from AFCS.ipynb)

- [ ]  Extract TBATS model declaration from AFCS.ipynb
- [ ] Evaluate TBATS model in dedicated notebook (extract evaluation logic from AFCS.ipynb)

- [ ] Extract Exploratoray Data Analysis from AFCS.ipynb and make plots in separate notebook.
- [ ] Try out more models (with dedicated .py and .ipynb files for model declarations and perfomance evaluationr respectively)


# TODO: report

- [ ] Write a max 12 pages, ACM (association for Computing Machinery) style report about all of the above, and submit to canvas.
- [ ] Add section on the dataset
- [ ] State in report the we use RMSE to comapare models.
- [ ] Finish results, conclusion, discussion.
- [ ] Write abstract.
- [ ] deeper analysis.


## Results section:
ARIMA
- [ ] RMSE
- [x] Parameter TABLE

TBATS
- [x] RMSE
- [x] Parameter TABLE

PROPHET
- [ ] RMSE
- [ ] Parameter TABLE