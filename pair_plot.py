import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def main():
    # Charger le dataset
    df = pd.read_csv("datasets/dataset_train.csv")
    
    # Sélectionner uniquement les colonnes numériques + maison
    df_numeric = df.select_dtypes(include='number')
    df_numeric["House"] = df["Hogwarts House"]
    
    # Supprimer les lignes avec des NaN
    df_numeric = df_numeric.dropna()
    
    # Afficher une pair plot colorée par maison
    sns.pairplot(df_numeric, hue="House", diag_kind="hist", plot_kws={"alpha": 0.6, "s": 40})
    
    plt.suptitle("Pair Plot des Cours (par Maison)", y=1.02)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()