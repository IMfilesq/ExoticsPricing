import numpy as np
import pandas as pd

from src.option.area_spread.area_spread import AreaSpreadOption as ASO
from src.option.area_spread.var_red_area_spread import AreaSpreadOption as RVASO

def validate_var_red() -> None:
    KO = pd.read_csv("data/KO_stock.csv")
    PEP = pd.read_csv("data/PEP_stock.csv")

    red = RVASO(KO["Open"][::-1], PEP["Open"][::-1], 30, 0.1)
    base = ASO(KO["Open"][::-1], PEP["Open"][::-1], 30, 0.1)

    n_sims = 10000
    amer_red_prices = np.empty(n_sims)
    amer_base_prices = np.empty(n_sims)
    eu_red_prices = np.empty(n_sims)
    eu_base_prices = np.empty(n_sims)

    for i in range(n_sims):
        amer_red_prices[i] = red.american_price(1, 100, 10)
        amer_base_prices[i] = base.american_price(1, 100, 10)
        eu_red_prices[i] = red.european_price(1, 100, 10)
        eu_base_prices[i] = base.european_price(1, 100, 10)
        print(f"Iteration {i + 1}")

    KO = pd.read_csv("data/KO_stock.csv")
    PEP = pd.read_csv("data/PEP_stock.csv")

    red = RVASO(KO["Open"][::-1], PEP["Open"][::-1], 30, 0.1)
    base = ASO(KO["Open"][::-1], PEP["Open"][::-1], 30, 0.1)

    n_sims = 10000
    amer_red_prices = np.empty(n_sims)
    amer_base_prices = np.empty(n_sims)
    eu_red_prices = np.empty(n_sims)
    eu_base_prices = np.empty(n_sims)

    for i in range(n_sims):
      amer_red_prices[i] = red.american_price(1, 100, 10)
      amer_base_prices[i] = base.american_price(1, 100, 10)
      eu_red_prices[i] = red.european_price(1, 100, 10)
      eu_base_prices[i] = base.european_price(1, 100, 10)
      print(f"Iteration {i + 1}")


    n_boot = 1000
    boot_amer_reductions = np.empty(n_boot)
    boot_eu_reductions = np.empty(n_boot)

    for i in range(n_boot):
      indices = np.random.choice(n_sims, size=n_sims, replace=True)
      b_amer_red = amer_red_prices[indices]
      b_amer_base = amer_base_prices[indices]
      b_eu_red = eu_red_prices[indices]
      b_eu_base = eu_base_prices[indices]

      boot_amer_reductions[i] = (1 - np.var(b_amer_red, ddof=1) / np.var(b_amer_base, ddof=1)) * 100
      boot_eu_reductions[i] = (1 - np.var(b_eu_red, ddof=1) / np.var(b_eu_base, ddof=1)) * 100

    alfa = 0.05
    amer_ci = np.percentile(boot_amer_reductions, [100 * (alfa / 2), 100 * (1 - alfa / 2)])
    eu_ci = np.percentile(boot_eu_reductions, [100 * (alfa / 2), 100 * (1 - alfa / 2)])

    amer_point = (1 - np.var(amer_red_prices, ddof=1) / np.var(amer_base_prices, ddof=1)) * 100
    eu_point = (1 - np.var(eu_red_prices, ddof=1) / np.var(eu_base_prices, ddof=1)) * 100

    print(f"\nAmerican variance reduced by: {amer_point:.2f} % " f"(95% CI: [{amer_ci[0]:.2f}%, {amer_ci[1]:.2f}%])")
    print(f"European variance reduced by: {eu_point:.2f} % " f"(95% CI: [{eu_ci[0]:.2f}%, {eu_ci[1]:.2f}%])"
    )

if __name__ == "__main__":
    validate_var_red()