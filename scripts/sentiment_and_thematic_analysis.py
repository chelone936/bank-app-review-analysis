import nltk
import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import string

# nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()


# Load cleaned reviews

df = pd.read_csv(r'data/clean_reviews.csv')


# VADER Sentiment Analysis

def get_vader_sentiment(text):
    scores = sia.polarity_scores(text)
    compound = scores['compound']

    if compound >= 0.05:
        label = "positive"
    elif compound <= -0.05:
        label = "negative"
    else:
        label = "neutral"

    return pd.Series([label, compound])

df[['sentiment_label', 'sentiment_score']] = df['review'].apply(get_vader_sentiment)


# Preprocessing function

def clean_text(text):
    return text.lower().translate(str.maketrans('', '', string.punctuation))

df['clean_review'] = df['review'].astype(str).apply(clean_text)


# LDA Topic Modeling

# Vectorize reviews
vectorizer = CountVectorizer(stop_words='english', max_features=3000)
X = vectorizer.fit_transform(df['clean_review'])

# Fit LDA model
n_topics = 5  # number of themes
lda = LatentDirichletAllocation(n_components=n_topics, random_state=42)
lda.fit(X)

# Display top words per topic and define human-readable theme names
n_top_words = 20
feature_names = vectorizer.get_feature_names_out()

# Define mapping based on observed themes
theme_mapping = {
    0: "App Updates & Reliability",
    1: "Transactions & Account Functionality",
    2: "User Experience / Usability",
    3: "Bank Brand & Features",
    4: "Performance Issues / Pain Points"
}

# Print top words for reference
for idx, topic in enumerate(lda.components_):
    top_features_indices = topic.argsort()[-n_top_words:][::-1]
    top_features = [feature_names[i] for i in top_features_indices]
    print(f"\n=== Theme {idx} ({theme_mapping[idx]}) ===")
    print(top_features)

# Assign each review to the most probable topic
topic_values = lda.transform(X)
df['lda_topic'] = topic_values.argmax(axis=1)
df['theme_name'] = df['lda_topic'].map(theme_mapping)


# Save the results

df.to_csv(r"data/sentiment_themes_lda.csv", index=False)
print("Saved sentiment + theme analysis to 'sentiment_themes_lda.csv'")
