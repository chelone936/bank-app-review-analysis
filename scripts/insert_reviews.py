import pandas as pd
import psycopg2

# Load CSV
df = pd.read_csv("data/sentiment_themes_lda.csv")

# DB connection
conn = psycopg2.connect(
    dbname="bank_reviews",
    user="postgres",
    password="yourpassword",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Insert banks
banks = df['bank_name'].unique()
for bank in banks:
    app_name = bank + " Mobile"
    cur.execute("""
    INSERT INTO banks (bank_name, app_name)
    VALUES (%s, %s)
    ON CONFLICT (bank_name) DO NOTHING;
    """, (bank, app_name))
conn.commit()

# Get bank IDs
cur.execute("SELECT bank_id, bank_name FROM banks;")
bank_map = {name: id for id, name in cur.fetchall()}

# Insert reviews
for _, row in df.iterrows():
    cur.execute("""
    INSERT INTO reviews (bank_id, review_text, rating, review_date, sentiment_label, sentiment_score, theme_name, source)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        bank_map[row['bank_name']],
        row['review'],
        row.get('rating', None),
        row.get('review_date', None),
        row['sentiment_label'],
        row['sentiment_score'],
        row['theme_name'],
        "Google Play"
    ))

conn.commit()
cur.close()
conn.close()
print("Data inserted successfully!")
