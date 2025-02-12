# An introduction to Marimo – a modern replacement for Jupyter notebooks

William Henney, DAWGI Meeting, 2025-02-11, IRyA-UNAM

## Abstract

Jupyter notebooks make it fun and easy to do science with Python, especially for exploratory work. However, they are not without problems. For example, the result depends on the order in which the cells are executed, which means it is easy for a notebook to end up in a broken or non-reproducible state. Marimo is a new type of notebook that aims to solve this problem and many others. It takes a "reactive" approach to execution, which guarantees consistency. I give a short demonstration of Marimo's features, while discussing its advantages/disadvantages and what changes in mindset are necessary in order to use it effectively. 

## Resumen

Los cuadernos de Jupyter hacen que sea divertido y fácil hacer ciencia con Python, especialmente para el trabajo exploratorio. Sin embargo, no están exentos de problemas. Por ejemplo, el resultado depende del orden en el que se ejecutan las celdas, lo que significa que es fácil que un cuaderno termine en un estado roto o no reproducible. Marimo es un nuevo tipo de cuaderno que busca resolver este problema y muchos otros. Adopta un enfoque “reactivo” para la ejecución, lo que garantiza la consistencia. Presento una breve demostración de las características de Marimo, mientras discuto sus ventajas y desventajas, así como los cambios de mentalidad necesarios para utilizarlo de manera efectiva.

## Outline of presentation



<a id="orgfda4382"></a>

### What is Marimo?

-   A more modern take on interactive notebooks for python
-   <https://marimo.io>
-   <https://docs.marimo.io/getting_started/>


<a id="org4f91112"></a>

### Live demo of Marimo

-   Install marimo ([instructions](INSTALL_LOG.md))
    -   I recommend using uv, but you can also use pip, conda, etc
-   Open a new marimo notebook in a sandbox
    
        marimo edit --sandbox dawgi-marimo-demo.py
-   Show how it deals with missing imports
-   Set up a blackbody spectrum for 10,000 K and plot it
-   Show how the plot is automatically updated if you change the temperature parameter
-   Demonstrate other features
    -   Inline docs, UI elements, markdown cells, app view, dependency graph, python file
    -   [Detailed plan](demo_plan.md)
-   The notebook that I wrote during the talk is [dawgi-marimo-demo02.py](live-demo/dawgi-marimo-demo02.py)
-   A slightly more elaborate version that I wrote while practicing is [here](first-try-uv-project/dawgi-marimo.py)
-   Show more complicated notebook
    -   [Canceled due to lack of time]


<a id="org8216171"></a>

## Reasons to try Marimo

-   Reactive notebooks guarantee consistency
-   Notebooks are saved as pure python files
-   Wide range of interactive UI elements
-   Sandbox mode for easy reproducibility and dependency management


<a id="orge1e3a0e"></a>

## Making the most out of Marimo

-   There are some "lazy practices" that are easy to fall into with Jupyter, but won't work so well with Marimo
    -   For instance, cut-and-paste style of programming
-   Keep global variables to a minimum
-   Use a declarative style rather than imperative style
-   Make extensive use functions and classes to organize your code


<a id="org1c179f2"></a>

### Reasons for caution

-   Marimo is very new
    -   Pace of change is rapid
    -   Still relatively few integrations with other tools compared with jupyter (Google Colab, Github diffs, Quarto, Jupyterbook, etc)
    -   Maybe it will never gain traction and be forgotten in a few years (unlikely, I think)
-   Python only (unlike jupyter which also supports Julia, R, Fortran, C++, etc)
-   Many of Marimo's advantages can be obtained in other ways, e.g.
    -   Jupytext for pure python representation
    -   Ipywidgets for interactive elements
    -   Streamlit or Dash for interactive dashboards and web apps
-   But Marimo has a unique set of features and is easier to use than most of these


## More details

- Description installation/configuration steps in [INSTALL_LOG.org](./INSTALL_LOG.org).
- Notes on things to say during the live demo in [demo_plan.org](./demo_plan.org). 
