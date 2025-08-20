# 📧 23f2001992@ds.study.iitm.ac.in
# Marimo notebook demo
import marimo

__generated_with = "0.8.15"
app = marimo.App()


# --- Cell 1: Define base parameters ----------------------
# Data flow: This cell sets the initial value for `a`
@app.cell
def cell1():
    a = 10
    return a


# --- Cell 2: Define variable depending on `a` ------------
# Data flow: `b` depends on `a`
@app.cell
def cell2(a):
    b = a * 2
    return b


# --- Cell 3: Interactive slider --------------------------
# Data flow: slider output `factor` affects calculations
@app.cell
def cell3(mo):
    factor = mo.ui.slider(1, 10, value=3, label="Multiplier")
    factor
    return factor


# --- Cell 4: Dynamic markdown output ---------------------
# Data flow: Combines variables from previous cells
@app.cell
def cell4(a, b, factor, mo):
    mo.md(f"""
    # Dynamic Report

    - Base `a` = **{a}**
    - Derived `b` = **{b}**
    - Slider `factor` = **{factor.value}**

    ## Computation
    Final result = **{b * factor.value}**
    """)
    return


if __name__ == "__main__":
    app.run()
