from google_play_scraper import reviews, Sort
import pandas as pd

# Dictionary of banks: bank_name -> app_package_name
banks = {
    "CBE": "com.combanketh.mobilebanking",
    "BOA": "com.boa.boaMobileBanking",
    "Dashen": "com.dashen.dashensuperapp"
}

all_reviews = []
max_reviews_per_bank = 2000  # Limit reviews per bank

# Loop through each bank app
for bank_name, app_package in banks.items():
    print(f"Scraping reviews for {bank_name}...")
    
    batch_size = 100
    cursor = None
    review_count = 0
    
    while review_count < max_reviews_per_bank:
        result, cursor = reviews(
            app_package,
            lang='en',
            country='us',
            sort=Sort.NEWEST,
            count=batch_size,
            continuation_token=cursor
        )
        
        if not result:
            break
        
        # Extract relevant fields
        for r in result:
            if review_count >= max_reviews_per_bank:
                break  # Stop if we reached the limit
                
            all_reviews.append({
                "bank_name": bank_name,
                "review": r['content'],
                "rating": r['score'],
                "date": r['at']
            })
            review_count += 1
            
            # Print every 100 reviews
            if review_count % 100 == 0:
                print(f"{bank_name}: Scraped {review_count} reviews so far...")
        
        if cursor is None:
            break

    print(f"Finished scraping {review_count} reviews for {bank_name}.\n")

# Convert to DataFrame
df = pd.DataFrame(all_reviews)

# Save to CSV
df.to_csv('data/raw_reviews_combined.csv', index=False)
print(f"Saved {len(df)} reviews to data/raw_reviews_combined.csv")
