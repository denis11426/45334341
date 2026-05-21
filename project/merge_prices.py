import pandas as pd

def merge_price_files():
    with_tax = pd.read_csv("prices_with_taxes_long.csv")
    wo_tax = pd.read_csv("prices_wo_taxes_long.csv")

    with_tax = with_tax.rename(columns={"price_per_1000l": "price_with_tax"})
    wo_tax = wo_tax.rename(columns={"price_per_1000l": "price_wo_tax"})

    merged = pd.merge(
        with_tax[["Date", "country", "fuel_type", "price_with_tax"]],
        wo_tax[["Date", "country", "fuel_type", "price_wo_tax"]],
        on=["Date", "country", "fuel_type"],
        how="inner"
    )

    merged["tax_amount"] = merged["price_with_tax"] - merged["price_wo_tax"]
    merged["tax_share"] = merged["tax_amount"] / merged["price_with_tax"]

    merged.to_csv("prices_merged.csv", index=False)
    print("Merged file saved as prices_merged.csv")
    print(merged.head())
    print(merged.shape)

    return merged

if __name__ == "__main__":
    merge_price_files()