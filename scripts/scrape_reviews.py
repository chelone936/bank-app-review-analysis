from google_play_scraper import reviews, Sort
import pandas as pd
import time
import sys


apps = {
    "CBE": "com.combanketh.mobilebanking",
    "BOA": "com.boa.boaMobileBanking",
    "Dashen": "com.dashen.dashensuperapp"
}

all_reviews = []

def collect_reviews(app_name, app_id, target=1000):
    """
    Fetches reviews for a given app until the target count is reached.
    Using 450 ensures 400+ survive preprocessing.
    """
    collected = 0
    batch_size = 200

    while collected < target:
        try:
            batch, _ = reviews(
                app_id,
                lang="en",
                country="us",
                sort=Sort.NEWEST,
                count=batch_size
            )

            for r in batch:
                all_reviews.append({
                    "review": r["content"],
                    "rating": r["score"],
                    "date": r["at"],
                    "bank": app_name,
                    "source": "Google Play"
                })

            collected += len(batch)
            print(f"{app_name}: {collected} reviews so far...")

        except Exception as e:
            print(f"Error scraping {app_name}: {str(e)}")
            time.sleep(3)

        time.sleep(1)

# Run scraper
for bank, app_id in apps.items():
    print(f"\n==== Scraping {bank} ====")
    collect_reviews(bank, app_id)

df = pd.DataFrame(all_reviews)
df.to_csv("data/raw_reviews.csv", index=False)
print("\nSaved raw_reviews.csv with:", len(df), "rows")
