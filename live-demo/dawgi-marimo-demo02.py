# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "astropy==7.0.1",
#     "marimo",
#     "matplotlib==3.10.0",
#     "numpy==2.2.2",
# ]
# ///

import marimo

__generated_with = "0.11.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    from astropy import units as u
    from astropy.modeling import models
    from matplotlib import pyplot as plt
    return mo, models, np, plt, u


@app.cell
def _(np, u):
    waves = np.linspace(
        1000 * u.AA, 2 * u.micron
    )
    waves
    return (waves,)


@app.cell
def _(TEMPERATURE, models, u):
    bb = models.BlackBody(
        temperature=TEMPERATURE.value * u.K
    )
    return (bb,)


@app.cell
def _(bb, plt, waves):
    fig, ax = plt.subplots()
    ax.plot(waves, bb(waves))
    fig
    return ax, fig


@app.cell
def _():
    return


@app.cell
def _(mo):
    TEMPERATURE = mo.ui.slider(
        start=5000, stop=50000, step=1000
    )
    TEMPERATURE
    return (TEMPERATURE,)


if __name__ == "__main__":
    app.run()
