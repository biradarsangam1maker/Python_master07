# Exploratory data analysis and basic cleaning of a customer churn dataset
# Keep customer_churn.csv in the same folder.
# Install: pip install pandas matplotlib

import pandas as pd
import matplotlib.pyplot as plt

input_file = "customer_churn.csv"
cleaned_file = "customer_churn_cleaned.csv"

try:
    df = pd.read_csv(input_file)

    print("\n--- FIRST FIVE ROWS ---")
    print(df.head())
    print("\n--- DATASET SHAPE ---")
    print(df.shape)
    print("\n--- COLUMN INFORMATION ---")
    df.info()
    print("\n--- SUMMARY STATISTICS ---")
    print(df.describe(include="all"))
    print("\n--- MISSING VALUES ---")
    print(df.isnull().sum())
    print("\n--- DUPLICATE ROWS ---")
    print(df.duplicated().sum())

    df = df.drop_duplicates()

    numeric_columns = df.select_dtypes(include="number").columns
    for column in numeric_columns:
        df[column] = df[column].fillna(df[column].median())

    categorical_columns = df.select_dtypes(include=["object", "category"]).columns
    for column in categorical_columns:
        if df[column].isnull().any():
            mode = df[column].mode()
            if not mode.empty:
                df[column] = df[column].fillna(mode[0])

    print("\n--- CHURN DISTRIBUTION ---")
    if "Churn" in df.columns:
        print(df["Churn"].value_counts(dropna=False))
        df["Churn"].value_counts().plot(kind="bar", title="Customer Churn")
        plt.xlabel("Churn")
        plt.ylabel("Number of customers")
        plt.tight_layout()
        plt.savefig("churn_distribution.png")
        plt.close()
    else:
        print("A 'Churn' column was not found in this dataset.")

    if len(numeric_columns) > 0:
        df[numeric_columns].hist(figsize=(12, 8), bins=20)
        plt.suptitle("Numeric Feature Distributions")
        plt.tight_layout()
        plt.savefig("numeric_distributions.png")
        plt.close()

    if len(numeric_columns) > 1:
        correlation = df[numeric_columns].corr()
        print("\n--- NUMERIC CORRELATIONS ---")
        print(correlation)
        plt.figure(figsize=(10, 8))
        plt.imshow(correlation, cmap="coolwarm", interpolation="nearest")
        plt.colorbar(label="Correlation")
        plt.xticks(range(len(correlation.columns)), correlation.columns, rotation=90)
        plt.yticks(range(len(correlation.columns)), correlation.columns)
        plt.title("Correlation Matrix")
        plt.tight_layout()
        plt.savefig("correlation_matrix.png")
        plt.close()

    df.to_csv(cleaned_file, index=False)
    print(f"\nCleaned data saved to {cleaned_file}")

except FileNotFoundError:
    print(f"Error: {input_file} was not found. Place it in this folder.")
