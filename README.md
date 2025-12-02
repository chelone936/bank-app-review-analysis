# Bank App Review Analysis

## Overview

This project analyzes customer reviews of Ethiopian bank mobile apps to uncover key drivers, pain points, and actionable recommendations for improving user experience. It scrapes, cleans, and analyzes reviews from Google Play, applies sentiment and thematic analysis, and visualizes insights for stakeholders.

## Features

- **Scraping Reviews:** Collects reviews for major Ethiopian banks using Google Play Scraper.
- **Data Cleaning:** Removes duplicates, non-English/mixed reviews, and normalizes dates/ratings.
- **Sentiment Analysis:** Uses VADER to classify reviews as positive, negative, or neutral.
- **Thematic Analysis:** Applies LDA topic modeling to identify major themes in user feedback.
- **Visualization:** Jupyter notebook provides charts, word clouds, and actionable recommendations.
- **SQL Schema:** Database schema and queries for storing and analyzing reviews.

## Project Structure

```
├── data/                # CSV files: raw, cleaned, and analyzed reviews
├── notebooks/           # Jupyter notebook for insights and recommendations
├── scripts/             # Python scripts for scraping, cleaning, and analysis
├── sql/                 # SQL schema and verification queries
├── src/                 # (Reserved for future code)
├── tests/               # (Reserved for future tests)
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
```

## Workflow

1. **Scrape Reviews:**
	- Run `scripts/scrape_reviews.py` to collect reviews from Google Play for CBE, BOA, and Dashen Bank.
	- Output: `data/raw_reviews_combined.csv`

2. **Clean Reviews:**
	- Run `scripts/clean_reviews.py` to filter, deduplicate, and normalize reviews.
	- Output: `data/clean_reviews.csv`

3. **Sentiment & Thematic Analysis:**
	- Run `scripts/sentiment_and_thematic_analysis.py` to assign sentiment labels/scores and extract themes using LDA.
	- Output: `data/sentiment_themes_lda.csv`

4. **Explore Insights:**
	- Open `notebooks/insights.ipynb` for visualizations, comparisons, and recommendations.

5. **Database Schema & Queries:**
	- Use `sql/schema.sql` to set up tables for banks and reviews.
	- Use `sql/verify_data.sql` for sample queries and data validation.

## Setup

1. **Install Python dependencies:**
	```powershell
	pip install -r requirements.txt
	```

2. **(Optional) Download NLTK Data:**
	- The sentiment analysis script uses VADER from NLTK. If running for the first time, uncomment the line in `sentiment_and_thematic_analysis.py`:
	  ```python
	  nltk.download('vader_lexicon')
	  ```

## Key Files

- `scripts/scrape_reviews.py`: Scrapes reviews from Google Play.
- `scripts/clean_reviews.py`: Cleans and filters reviews.
- `scripts/sentiment_and_thematic_analysis.py`: Sentiment and topic modeling.
- `notebooks/insights.ipynb`: Visualizes findings and provides recommendations.
- `sql/schema.sql`: Database schema for banks and reviews.
- `sql/verify_data.sql`: SQL queries for data validation and exploration.

## Example Insights

- **Drivers:** App reliability and updates are the strongest positive themes.
- **Pain Points:** Usability and performance issues are common negative themes.
- **Recommendations:** Improve navigation, optimize speed, and communicate updates clearly.

See the notebook for detailed charts and recommendations per bank.

## License

This project is for educational and research purposes.
