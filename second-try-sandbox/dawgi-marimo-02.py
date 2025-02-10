# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "astropy==7.0.1",
#     "marimo",
#     "matplotlib==3.10.0",
#     "numpy==2.2.2",
#     "seaborn==0.13.2",
# ]
# ///

import marimo

__generated_with = "0.11.0"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(r"""# Demo of Marimo Notebook for DAWGI""")
    return


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import astropy.units as u
    from astropy.modeling import models
    from matplotlib import pyplot as plt
    import seaborn as sns
    return mo, models, np, plt, sns, u


@app.cell
def _(sns):
    sns.set_context("talk")
    return


@app.cell
def _(models, u):
    temperature = 10_000
    bb = models.BlackBody(
        temperature=temperature * u.K
    )
    bb
    return bb, temperature


@app.cell
def _(np, u):
    waves = np.linspace(
        1000 * u.AA, 1 * u.micron
    )
    waves
    return (waves,)


@app.cell
def _(mo, temperature):
    mo.md(rf"""## Graph of Black Body spectrum ($T = {temperature:,}$ K)""".replace(',', r'\,'))
    return


@app.cell
def _(bb, plt, waves):
    fig, ax = plt.subplots()
    ax.plot(waves, bb(waves))
    ax.set(xlabel="Wavelength, micron")
    fig
    return ax, fig


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
