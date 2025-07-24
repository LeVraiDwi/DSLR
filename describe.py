import pandas as pd
import sys
from typing import Any
import math
import Utils

def is_number(val: Any) -> bool:
    try:
        float(val)
        return True
    except (ValueError, TypeError):
        return False

def compute_statistics(values: list[float]) -> dict[str, float]:
    n = len(values)
    notNanValue = [x for x in values if not math.isnan(x)]
    n = len(notNanValue)
    sorted_vals = sorted(notNanValue)

    # Count
    count = int(n)

    # Mean
    mean = Utils.Mean(notNanValue)

    # Std
    std = Utils.Std(notNanValue)

    # Min and Max
    min_val = Utils.Min(notNanValue)
    max_val = Utils.Max(notNanValue)

    q25 = Utils.Percentile(notNanValue, 0.25)
    q50 = Utils.Percentile(notNanValue, 0.50)
    q75 = Utils.Percentile(notNanValue, 0.75)

    return {
        "count": count,
        "mean": mean,
        "std": std,
        "min": min_val,
        "25%": q25,
        "50%": q50,
        "75%": q75,
        "max": max_val
    }

def build_statistics_table(df: pd.DataFrame) -> pd.DataFrame:
    stats_rows = ["count", "mean", "std", "min", "25%", "50%", "75%", "max"]
    stats_dict = {row: [] for row in stats_rows}
    index_tab = []
    for col in df.columns:
        values = [float(val) for val in df[col] if is_number(val)]
        if values:
            stats = compute_statistics(values)
        else:
            continue
        for row in stats_rows:
            stats_dict[row].append(stats[row])
        index_tab.append(col)

    result_df = pd.DataFrame(stats_dict, index=index_tab).T
    return result_df

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <csv_file>")
        return

    csv_file = sys.argv[1]
    try:
        df = pd.read_csv(csv_file)
        stats_table = build_statistics_table(df)
        pd.set_option('display.float_format', '{:,.6f}'.format)
        print(df.describe())
        df = pd.DataFrame(stats_table)
        print(df)
    except FileNotFoundError:
        print(f"File not found: {csv_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()