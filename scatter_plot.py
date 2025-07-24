import pandas as pd
import matplotlib.pyplot as plt
import Utils
import numpy as np

def main():
    df = pd.read_csv("datasets/dataset_train.csv")
    df_numeric = df.select_dtypes(include='number').dropna()

    corr_matrix = Utils.CorrMatrix(df_numeric)
    corr_matrix = corr_matrix.abs()
    # Mask the diagonal (self-correlation)
    mask = corr_matrix.where(~np.eye(corr_matrix.shape[0], dtype=bool))
    print(corr_matrix)
    # Find the two most correlated features
    most_corr_pair = mask.stack().idxmax()
    feature1, feature2 = most_corr_pair
    # map colors by house
    house_colors = {
        "Gryffindor": "lightcoral",
        "Hufflepuff": "lightyellow",
        "Ravenclaw": "cornflowerblue",
        "Slytherin": "mediumseagreen"
    }
    colors = df["Hogwarts House"].map(house_colors)

    # Plot the scatter plot
    plt.figure(figsize=(8, 6))
    for house, color in house_colors.items():
        house_data = df[df["Hogwarts House"] == house]
        plt.scatter(
            house_data[feature1],
            house_data[feature2],
            color=color,
            alpha=0.5,
            label=house
        )
    plt.legend(title="Maisons")
    plt.title(f"Most Similar Features: {feature1} vs {feature2}")
    plt.xlabel(feature1)
    plt.ylabel(feature2)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    print(corr_matrix)

if __name__ == "__main__":
    main()