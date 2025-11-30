import pandas as pd
import re
import langdetect
from langdetect import DetectorFactory
import logging

# --------------------
# Setup
# --------------------
DetectorFactory.seed = 0

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Input/output
input_csv = "data/raw_reviews_combined.csv" 
output_csv = "data/clean_reviews.csv"


# Helper Functions

amharic_pattern = re.compile(r'[\u1200-\u137F]')

def contains_amharic(text):

    return bool(amharic_pattern.search(str(text)))

def is_english(text):
    
    if contains_amharic(text):
        return False
    try:
        return langdetect.detect(text) == 'en'
    except:
        return False


# Load Raw Data

logging.info(f"Loading raw data from {input_csv}")
df = pd.read_csv(input_csv)
logging.info(f"Total reviews before cleaning: {len(df)}")


# Cleaning Steps

df = df.dropna(subset=["review", "rating"])
logging.info(f"After dropping missing review/rating: {len(df)}")

df = df.drop_duplicates(subset=["review"])
logging.info(f"After removing duplicates: {len(df)}")

df = df[df["review"].apply(is_english)]
logging.info(f"After removing non-English/mixed reviews: {len(df)}")

df["date"] = pd.to_datetime(df["date"], errors="coerce").dt.strftime("%Y-%m-%d")
df = df.dropna(subset=["date"])
logging.info(f"After normalizing dates: {len(df)}")

df["rating"] = df["rating"].astype(int)
df["review"] = df["review"].str.strip()

if "source" not in df.columns:
    df["source"] = "Google Play"


# Save Clean Data

df.to_csv(output_csv, index=False)
logging.info(f"Saved cleaned dataset to {output_csv}")
logging.info(f"Total clean reviews: {len(df)}")
