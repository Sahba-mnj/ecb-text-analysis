import os
import re
import requests
from bs4 import BeautifulSoup

print("Starting ECB scraping...")

# Create folders
os.makedirs("data", exist_ok=True)
os.makedirs("outputs", exist_ok=True)

# ECB page URL
url = "https://www.ecb.europa.eu/press/press_conference/monetary-policy-statement/2026/html/ecb.is260430~f99cb123a8.en.html"

# Request page
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers, timeout=30)

# Check request
if response.status_code != 200:
    print("Error downloading page")
    exit()

print("Page downloaded successfully")

# Parse HTML
soup = BeautifulSoup(response.text, "lxml")

# Find article section
content = soup.select_one("main div.section")

if content is None:
    print("Could not find article section")
    exit()

print("Article section found")

# Extract paragraphs
elements = content.find_all(["h2", "p"])

text_list = []

for el in elements:

    classes = el.get("class", [])

    # Skip subtitle
    if "ecb-pressContentSubtitle" in classes:
        continue

    text = el.get_text(" ", strip=True)

    # Clean spaces
    text = re.sub(r"\s+", " ", text)

    if text:
        text_list.append(text)

print(f"Total paragraphs found: {len(text_list)}")

# Combine text
full_text = "\n\n".join(text_list)

# Save text file
with open("data/ecb_press_conference.txt", "w", encoding="utf-8") as f:
    f.write(full_text)

print("Text saved successfully")

# =========================
# SENTIMENT ANALYSIS
# =========================

from textblob import TextBlob
import pandas as pd

results = []

for i, paragraph in enumerate(text_list):

    blob = TextBlob(paragraph)

    polarity = blob.sentiment.polarity

    # label
    if polarity > 0.1:
        label = "positive"
    elif polarity < -0.1:
        label = "negative"
    else:
        label = "neutral"

    results.append([
        i + 1,
        paragraph,
        polarity,
        label
    ])

# Create dataframe
df = pd.DataFrame(results, columns=[
    "paragraph_number",
    "paragraph_text",
    "polarity",
    "sentiment_label"
])

# Save CSV
df.to_csv(
    "outputs/ecb_paragraph_sentiment.csv",
    index=False
)

print("Sentiment CSV saved successfully")

# =========================
# AVERAGE SENTIMENT
# =========================

average_polarity = df["polarity"].mean()

print()
print("Average polarity:", round(average_polarity, 3))

if average_polarity > 0.1:
    print("Overall tone: positive")
elif average_polarity < -0.1:
    print("Overall tone: negative")
else:
    print("Overall tone: neutral")


# =========================
# WORD FREQUENCY
# =========================

from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Combine all text
all_text = " ".join(text_list).lower()

# Find words
words = re.findall(r"\b[a-zA-Z]+\b", all_text)

# Custom stopwords
custom_stopwords = {
    "the", "and", "to", "of", "in", "for",
    "on", "is", "with", "that", "we", "are",
    "this", "will", "from", "have", "has",
    "ecb", "euro", "policy", "inflation",
    "interest", "rates", "rate", "percent", "said", "bank",
"banks",
"european",
"central"
}

# Remove stopwords
filtered_words = [
    w for w in words
    if w not in custom_stopwords and len(w) > 3
]

# Count words
word_counts = Counter(filtered_words)

# Top 20 words
top_words = word_counts.most_common(20)

# Create dataframe
df_words = pd.DataFrame(
    top_words,
    columns=["word", "count"]
)

# Save CSV
df_words.to_csv(
    "outputs/ecb_top_words.csv",
    index=False
)

print("Top words CSV saved successfully")

# =========================
# WORDCLOUD
# =========================

wordcloud = WordCloud(
    width=1200,
    height=700,
    background_color="white"
).generate(" ".join(filtered_words))

# Show image
plt.figure(figsize=(12, 7))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")

# Save image
plt.savefig("outputs/ecb_wordcloud.png")

plt.close()

print("Wordcloud saved successfully")

# =========================
# EXTRA ANALYSIS
# =========================

# Average polarity
average_polarity = df["polarity"].mean()

print()
print("Average polarity:", round(average_polarity, 3))

# Overall tone
if average_polarity > 0.1:
    overall_tone = "positive"
elif average_polarity < -0.1:
    overall_tone = "negative"
else:
    overall_tone = "neutral"

print("Overall tone:", overall_tone)

# Most positive paragraphs
top_positive = df.sort_values(
    by="polarity",
    ascending=False
).head(3)

# Most negative paragraphs
top_negative = df.sort_values(
    by="polarity",
    ascending=True
).head(3)

# Save CSVs
top_positive.to_csv(
    "outputs/top_positive_paragraphs.csv",
    index=False
)

top_negative.to_csv(
    "outputs/top_negative_paragraphs.csv",
    index=False
)

print("Top positive paragraphs saved")
print("Top negative paragraphs saved")

# =========================
# SENTIMENT PLOT
# =========================

plt.figure(figsize=(12, 6))

plt.plot(
    df["paragraph_number"],
    df["polarity"]
)

plt.axhline(
    y=0,
    linestyle="--"
)

plt.xlabel("Paragraph Number")
plt.ylabel("Polarity")
plt.title("ECB Paragraph Sentiment")

plt.savefig(
    "outputs/ecb_sentiment_plot.png"
)

plt.close()

print("Sentiment plot saved successfully")