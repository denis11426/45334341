import pandas as pd


def reshape_fuel_file(input_file, output_file):
    print(f"\nReshaping file: {input_file}")

    df = pd.read_csv(input_file)

    long_df = df.melt(id_vars="Date", var_name="full_name", value_name="price_per_1000l")

    split_cols = long_df["full_name"].str.split("_", expand=True)

    long_df["country"] = split_cols[0]
    long_df["fuel_type"] = split_cols[4]
    long_df["price_type"] = split_cols[2] + "_" + split_cols[3]

    long_df = long_df[["Date", "country", "fuel_type", "price_type", "price_per_1000l"]]

    print(long_df.head(10))
    print(long_df.shape)

    long_df.to_csv(output_file, index=False)
    print(f"Long file saved as {output_file}")


def main():
    reshape_fuel_file(
        input_file="prices_with_taxes_fuels_only.csv",
        output_file="prices_with_taxes_long.csv"
    )

    reshape_fuel_file(
        input_file="prices_wo_taxes_fuels_only.csv",
        output_file="prices_wo_taxes_long.csv"
    )


if __name__ == "__main__":
    main()