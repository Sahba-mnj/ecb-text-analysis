# ECB Text Analysis Project

## Overview

This project performs textual analysis on a European Central Bank (ECB) monetary policy press conference page.

The script scrapes the press conference text directly from the ECB website, cleans the extracted text, performs paragraph-level sentiment analysis using TextBlob, and generates word frequency statistics and visualizations.

---

## Selected ECB Page

ECB Monetary Policy Press Conference

Date:
30 April 2026

Source:
https://www.ecb.europa.eu/press/press_conference/monetary-policy-statement/2026/html/ecb.is260430~f99cb123a8.en.html

---

## Project Features

- Web scraping with Requests and BeautifulSoup
- HTML parsing using CSS selectors
- Clean text extraction
- Paragraph-by-paragraph sentiment analysis
- Sentiment polarity scoring with TextBlob
- CSV export of sentiment results
- Word frequency analysis
- Custom stopword filtering
- Word cloud generation
- Sentiment trend visualization
- Extraction of top positive and negative paragraphs

---

## Technologies Used

- Python
- Requests
- BeautifulSoup
- Pandas
- TextBlob
- Matplotlib
- WordCloud

---

## Folder Structure

```text
ecb-text-analysis/
│
├── scripts/
│   └── ecb_text_analysis.py
│
├── data/
│   └── ecb_press_conference.txt
│
├── outputs/
│   ├── sentiment.csv
│   ├── word_freq.csv
│   ├── wordcloud.png
│   ├── sentiment_trend.png
│   ├── top_positive.csv
│   └── top_negative.csv
│
└── README.md
```

---

## Main Findings


Most paragraphs showed neutral to mildly positive sentiment, reflecting the formal and technical communication style of ECB monetary policy communication.

The analysis highlighted recurring themes related to inflation, markets, growth, and financial conditions.