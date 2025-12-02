-- Count reviews per bank
SELECT 
    b.bank_name, 
    COUNT(r.review_id) AS review_count
FROM banks b
LEFT JOIN reviews r ON b.bank_id = r.bank_id
GROUP BY b.bank_name
ORDER BY review_count DESC;

-- Average rating per bank
SELECT 
    b.bank_name, 
    AVG(r.rating) AS avg_rating
FROM banks b
LEFT JOIN reviews r ON b.bank_id = r.bank_id
GROUP BY b.bank_name
ORDER BY avg_rating DESC;

-- Count reviews per sentiment label
SELECT 
    sentiment_label, 
    COUNT(*) AS review_count
FROM reviews
GROUP BY sentiment_label
ORDER BY review_count DESC;

-- 4️⃣ Count reviews per theme
SELECT 
    theme_name, 
    COUNT(*) AS review_count
FROM reviews
GROUP BY theme_name
ORDER BY review_count DESC;

-- Check for reviews with missing critical fields
SELECT *
FROM reviews
WHERE review_text IS NULL
   OR bank_id IS NULL
   OR rating IS NULL
   OR review_date IS NULL;

-- Sample 10 reviews per bank
SELECT b.bank_name, r.review_text, r.rating, r.sentiment_label, r.theme_name
FROM banks b
JOIN reviews r ON b.bank_id = r.bank_id
ORDER BY b.bank_name
LIMIT 10;
