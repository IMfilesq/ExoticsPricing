# Area Spread Option Pricing

**Author:** Igor Misterowicz

## Description

Independent options pricing project focused on a custom **area spread option**.

This option pays off the *area* between the normalized price paths of two assets (normalized so that both start at 1 at \( t_0 \)).

Key characteristics:
- Multi-asset
- Path-dependent

Pricing therefore requires:
- Full path simulation
- Cholesky decomposition
- Longstaff–Schwartz algorithm (for American-style exercise)


### Simplification

Currently the model uses **constant volatility** estimated from the most recent asset movements (instead of Heston stochastic volatility).  
The modular design of the code makes adding stochastic volatility straightforward in the future.

### Validation

The validation scripts can be found in `validation/` folder and their results in `outputs/` folder.

The use of control and antithetic variates results in 30% variance reduction on both european and american Ara Spread Option prices.

The Area Spred Option is original, so direct validation of the results was not possible.  
To validate the simulation engine, a classic **put option** was also implemented. It successfully converges to QuantLib put prices.


### Visualization

The repository includes functionality to plot the simulated paths for both:
- Put options
- Area spread options

Charts are saved in the `outputs/` folder.

---

## Setup

Requires [`uv`](https://github.com/astral-sh/uv) (can be installed via `pip`):

```bash
uv sync
```

## Running the examples

```bash
uv run python -m examples.run_all
```