-- Create banks table
CREATE TABLE IF NOT EXISTS banks (
    bank_id SERIAL PRIMARY KEY,
    bank_name VARCHAR(255) UNIQUE NOT NULL,
    app_name VARCHAR(255)
);

-- Create reviews table
CREATE TABLE IF NOT EXISTS reviews (
    review_id SERIAL PRIMARY KEY,
    bank_id INT REFERENCES banks(bank_id),
    review_text TEXT NOT NULL,
    rating INT,
    review_date DATE,
    sentiment_label VARCHAR(10),
    sentiment_score FLOAT,
    theme_name VARCHAR(100),
    source VARCHAR(50)
);

-- Optional: Indexes for faster queries
CREATE INDEX IF NOT EXISTS idx_reviews_bank_id ON reviews(bank_id);
CREATE INDEX IF NOT EXISTS idx_reviews_theme_name ON reviews(theme_name);
