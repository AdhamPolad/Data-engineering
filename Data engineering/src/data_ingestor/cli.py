import argparse
import os
import pandas as pd


def main():
    # Create command-line arguments
    parser = argparse.ArgumentParser(
        description="Clean and process a CSV dataset"
    )

    parser.add_argument(
        "--input",
        required=True,
        help="Path to the input CSV file"
    )

    parser.add_argument(
        "--output",
        required=True,
        help="Path to the output CSV file"
    )

    args = parser.parse_args()

    # Read the CSV dataset
    df = pd.read_csv(args.input)

    print("\n========== ORIGINAL DATASET ==========")

    # Number of rows and columns
    print(f"Number of rows: {df.shape[0]}")
    print(f"Number of columns: {df.shape[1]}")

    # Column names
    print("\nColumn names:")
    print(df.columns.tolist())

    # First 5 rows
    print("\nFirst 5 rows:")
    print(df.head())

    # Data types
    print("\nData types:")
    print(df.dtypes)

    # Missing values
    print("\nMissing values:")
    print(df.isna().sum())

    # ---------------------------------------
    # A. Clean column names
    # ---------------------------------------

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    print("\n========== CLEANED COLUMN NAMES ==========")
    print(df.columns.tolist())

    # ---------------------------------------
    # B. Remove completely empty rows
    # ---------------------------------------

    empty_rows = df.isna().all(axis=1).sum()

    print(f"\nCompletely empty rows found: {empty_rows}")

    df = df.dropna(how="all")

    # ---------------------------------------
    # C. Remove duplicate rows
    # ---------------------------------------

    duplicate_count = df.duplicated().sum()

    print(f"Duplicate rows found: {duplicate_count}")

    df = df.drop_duplicates()

    # ---------------------------------------
    # D. Handle missing values
    # ---------------------------------------

    # The certificate column contains missing values.
    # We replace missing values with "Unknown" because
    # a missing certificate does not mean the movie is invalid.

    if "certificate" in df.columns:
        df["certificate"] = df["certificate"].fillna("Unknown")

    # ---------------------------------------
    # 7. Filter the dataset
    # ---------------------------------------

    print("\n========== FILTERING DATASET ==========")

    print(f"Rows before filtering: {len(df)}")

    # Select movies with an IMDb rating of 8.0 or higher
    filtered_df = df[df["imdb_rating"] >= 8.0]

    print(f"Rows after filtering: {len(filtered_df)}")

    print("\nMovies with IMDb rating 8.0 or higher:")
    print(filtered_df[["series_title", "imdb_rating"]].to_string(index=False))

    # ---------------------------------------
    # Save processed dataset
    # ---------------------------------------

    output_directory = os.path.dirname(args.output)

    if output_directory:
        os.makedirs(output_directory, exist_ok=True)

    df.to_csv(args.output, index=False)

    print("\n========== PROCESSED DATASET ==========")

    print(f"Number of rows: {df.shape[0]}")
    print(f"Number of columns: {df.shape[1]}")

    print("\nRemaining missing values:")
    print(df.isna().sum())

    print(f"\nCleaned dataset saved to: {args.output}")


if __name__ == "__main__":
    main()

