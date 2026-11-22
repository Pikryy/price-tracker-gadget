import numpy as np
import pandas as pd

KURS_INR_KE_IDR = 197  # asumsi, tulis di README
RAW_PATH = "data/raw/cleaned_df.csv"
CLEAN_PATH = "data/clean_gadget.csv"


def _buat_nama(row):
    brand, model = str(row["brand"]).strip(), str(row["model"]).strip()
    # hindari "Vivo vivo S2 5G"
    dasar = model if model.lower().startswith(brand.lower()) else f"{brand.title()} {model}"
    return f"{dasar} ({row['ram']:g}/{row['storage']:g}GB)"


def clean_data(path=RAW_PATH):
    df = pd.read_csv(path)

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
    df["antutu_score"] = df["antutu_score"].replace(0, np.nan)

    # isi kosong
    for col in ["processor_brand", "processor", "display_type"]:
        df[col] = df[col].fillna("Unknown")
    df["storage"] = df["storage"].fillna(df["storage"].median())
    df["front_camera"] = df["front_camera"].fillna(df["front_camera"].median())
    df["charging_watt"] = df["charging_watt"].fillna(0)

    # harga rupiah + nama tampilan
    df["price_idr"] = (df["price_inr"] * KURS_INR_KE_IDR).round(-3)
    df["nama"] = df.apply(_buat_nama, axis=1)

    return df.reset_index(drop=True)


if __name__ == "__main__":
    df = clean_data()
    df.to_csv(CLEAN_PATH, index=False)
    print("Selesai:", df.shape)