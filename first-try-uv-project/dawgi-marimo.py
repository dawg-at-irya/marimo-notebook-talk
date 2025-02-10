import marimo

__generated_with = "0.11.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import astropy.units as u
    import astropy.modeling.models as models
    from matplotlib import pyplot as plt
    import seaborn as sns
    import numpy as np
    return mo, models, np, plt, sns, u


@app.cell
def _(sns):
    sns.set_context("talk")
    return


@app.cell
def _(TEMPERATURE, models, u):
    bb = models.BlackBody(
        # temperature=10_000 * u.K
        temperature=TEMPERATURE.value * u.K
    )
    bb
    return (bb,)


@app.cell
def _(np, u):
    wavs = np.linspace(
        1000 * u.AA, 1 * u.micron, 200
    )
    wavs
    return (wavs,)


@app.cell
def _(mo):
    TEMPERATURE = mo.ui.slider(1000, 50_000, step=500, value=10_000)
    TEMPERATURE
    return (TEMPERATURE,)


@app.cell
def _(bb, plt, wavs):
    fig, ax = plt.subplots()
    ax.plot(wavs, bb(wavs))
    ax.set(
        xscale="linear",
        yscale="linear",
        xlabel="Wavelength, micron",
        ylim=[0, None],
    )
    fig
    return ax, fig


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
