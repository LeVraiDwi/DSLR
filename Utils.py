import math
import pandas as pd
import numpy as np
# Mean
def Mean(values: list[float]) -> float:
    values = GetNotNan(values)
    total = 0.0
    n = len(values)
    for v in values:
        total += v
    mean = total / n if n else float('nan')
    return mean

# Std
def Std(values: list[float]) -> float:
    squared_diff = 0.0
    n = len(values)
    for v in values:
        squared_diff += (v - Mean(values)) ** 2
    std = (squared_diff / n) ** 0.5 if n else float('nan')
    return std

# Min
def Min(values: list[float]) -> float:
    n = len(values)
    sorted_vals = sorted(values)
    min_val = sorted_vals[0] if n else float('nan')
    return min_val

# Max    
def Max(values: list[float]) -> float:
    n = len(values)
    sorted_vals = sorted(values)
    max_val = sorted_vals[-1] if n else float('nan')
    return max_val

# Percentiles
def Percentile(values: list[float], p: float) -> float:
    n = len(values)
    sorted_vals = sorted(values)
    if n == 0:
        return float('nan')
    k = (n - 1) * p
    f = int(k)
    c = min(f + 1, n - 1)
    if f == c:
        return sorted_vals[f]
    return sorted_vals[f] + (sorted_vals[c] - sorted_vals[f]) * (k - f)

# remove nan valuex
def GetNotNan(values: list[float]) -> list[float]:
    return [x for x in values if not math.isnan(x)]

def Cov(v1: list[float], v2: list[float]) -> list[float]:
    valueX = np.array(v1)
    valueY = np.array(v2)

    if (len(valueX) != len(valueY)):
        raise ValueError("list don't have the same size")

    meanX = Mean(v1)
    meanY = Mean(v2)
    
    cov = np.sum((valueX - meanX) * (valueY - meanY))

    return cov

# Correlation between two set
def Corr(dataFrame: pd.DataFrame) -> list[float]:
    features = dataFrame.columns

    if (len(features) != 2):
        raise ValueError("must have 2 feature")
    
    if (features[0] == features[1]):
        return 1
    v1 = dataFrame[features[0]]
    v2 = dataFrame[features[1]]
    n = len(v1)
    cov = Cov(v1.values, v2.values)
    std1 = Std(v1)
    std2 = Std(v2)

    if std1 == 0 or std2 == 0:
        return 0
    return (cov / (std1 * std2)) / n # normalize with n

# return correlation matrix
def CorrMatrix(dataFrame: pd.DataFrame) -> pd.DataFrame:
    
    features = dataFrame.columns
    n = len(features)
    corr_matrix = np.zeros((n, n))

    for i in range(1, n):
        for j in range(1, n):
            new_df = dataFrame[[features[i], features[j]]].dropna()
            if (j >= i):
                corr_matrix[i, j] = Corr(new_df)
            else:
                corr_matrix[i, j] = corr_matrix[j, i]
    
    corr_df = pd.DataFrame(corr_matrix, index=features, columns=features)
    return corr_df