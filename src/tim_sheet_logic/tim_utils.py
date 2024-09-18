import pandas as pd
import numpy as np
from scipy import stats

def get_neighborhood_ppsf(neighborhood: pd.DataFrame) -> float:
    neighborhood["PPSF"] = neighborhood["PRICE"] / neighborhood["SQUARE FEET"]
    neighborhood = neighborhood.sort_values("PPSF", ascending=False).head(n=5)
    # drop outliers
    neighborhood = neighborhood[(np.abs(stats.zscore(neighborhood["PPSF"])) < 1)]
    value = neighborhood["PPSF"].mean()
    return round(value, 2)