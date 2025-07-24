import pandas as pd
import matplotlib.pyplot as plt
import Utils

def main():
    df = pd.read_csv("datasets/dataset_train.csv")
    # List of all course columns (excluding metadata)
    course_columns = [
        "Arithmancy", "Astronomy", "Herbology", "Defense Against the Dark Arts",
        "Divination", "Muggle Studies", "Ancient Runes", "History of Magic",
        "Transfiguration", "Potions", "Care of Magical Creatures", "Charms", "Flying"
    ]

    # Clean data: remove rows with missing house or course values
    df = df[df["Hogwarts House"].notna()]

    # Plot histogram
    fig, axes = plt.subplots(nrows=3, ncols=5, figsize=(20, 10))
    i: int = 0

    std_devs = {}
    color = ["lightcoral", "lightyellow", "cornflowerblue", "mediumseagreen"]
    for course in course_columns:
        ax = axes[int(i / 5), i % 5]
        groups = df.groupby("Hogwarts House")[course]
        means = groups.apply(Utils.Mean)
        for j, (house, scores) in enumerate(groups):
            # Drop NaN values and convert to list
            scores = scores.dropna()
            ax.hist(scores, bins=15, alpha=0.5, label=house, color=color[j])
        ax.set_title(f"{course}")
        ax.set_xlabel("Score")
        ax.set_ylabel("Nb Student")
        ax.legend(title="House")
        i += 1
        if len(means) == 4:  # Only consider if all four houses are present
            std_devs[course] = Utils.Std(means)
    
    # Find the most homogeneous course (lowest std dev)
    most_homogeneous_course = min(std_devs, key=std_devs.get)
    tabe = df.groupby("Hogwarts House")[most_homogeneous_course]
    for j, (house, scores) in enumerate(tabe):
        # Drop NaN values and convert to list
        scores = scores.dropna()
        axes[2, 3].hist(scores, bins=15, alpha=0.5, label=house, color=color[j])
    axes[2, 3].set_title(f"Most homogeneous: {most_homogeneous_course}")
    axes[2, 3].set_xlabel("Score")
    axes[2, 3].set_ylabel("Nb Student")
    axes[2, 3].set_ylim(auto=True)
    axes[2, 3].legend(title="House")
    

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()