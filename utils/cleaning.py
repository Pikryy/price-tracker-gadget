import pandas as pd

KURS_INR_KE_IDR = 195  # sesuaikan, tulis di README

def clean_data(path):
    df = pd.read_csv(path)

    # rename
    df = df.rename(columns={
        "Price": "price_inr",
        "is_fast_chargig": "is_fast_charging",
        "charging_type": "charging_watt",
        "storage_capacity": "storage",
    })

    # buang HP jadul / outlier
    df = df[(df["ram"] >= 1) & (df["storage"].fillna(32) >= 8)]
    df = df[df["battery_capacity"] <= 10000]

    # nilai tidak valid -> NaN
    df["antutu_score"] = df["antutu_score"].replace(0, pd.NA)

    # isi kosong
    df["processor_brand"] = df["processor_brand"].fillna("Unknown")
    df["processor"] = df["processor"].fillna("Unknown")
    df["display_type"] = df["display_type"].fillna("Unknown")
    df["storage"] = df["storage"].fillna(df["storage"].median())
    df["front_camera"] = df["front_camera"].fillna(df["front_camera"].median())
    df["charging_watt"] = df["charging_watt"].fillna(0)

    # harga rupiah + nama tampilan
    df["price_idr"] = df["price_inr"] * KURS_INR_KE_IDR
    df["nama"] = df["brand"].str.title() + " " + df["model"]

    return df.reset_index(drop=True)

if __name__ == "__main__":
    df = clean_data("data/raw/mobile.csv")
    df.to_csv("data/clean_gadget.csv", index=False)
    print(df.shape)