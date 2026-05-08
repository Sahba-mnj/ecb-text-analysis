# ECB Text Analysis Project

## Project Summary

The project analyses text from a European Central Bank (ECB) monetary policy press conference page.

The script scrapes the press conference text directly from the ECB website, cleans the scraped text, performs paragraph-level sentiment analysis with TextBlob, and generates word frequency statistics and visualizations.

## Selected ECB Page

ECB Monetary Policy Press Conference

Date:
30 April 2026

Source:
https://www.ecb.europa.eu/press/press_conference/monetary-policy-statement/2026/html/ecb.is260430~f99cb123a8.en.html

---

## Project Features

- Web scraping with Requests and BeautifulSoup
- HTML parsing with CSS selectors
- Clean text extraction
- Paragraph-by-paragraph sentiment analysis
- Sentiment polarity scoring using TextBlob
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

## Why TextBlob?

TextBlob was chosen because the assignment required a sentiment analysis tool other than VADER. The tool offers a straightforward sentiment analysis technique based on polarity which suits paragraph-level textual analysis well.

---

## Folder Structure

```text
ecb-text-analysis/
│
├── scripts/
│   └── ecb_text_analysis.py
│
├── data/
│   └── ecb_press_conference_2026-04-30.txt
│
├── outputs/
│   ├── ecb_paragraph_sentiment.csv
│   ├── ecb_top_words.csv
│   ├── ecb_wordcloud.png
│   ├── ecb_sentiment_plot.png
│   ├── top_positive_paragraphs.csv
│   └── top_negative_paragraphs.csv
│
├── environment.yml
│
└── README.md
```



## Main Findings

The sentiment analysis indicated that most ECB press conference paragraphs scored relatively neutral to slightly positive sentiments. This reflects the ECB’s cautious and data-driven communication style in monetary policy discussions.

Paragraphs discussing war-related uncertainty, energy price concerns, inflation threats, and unfavorable growth conditions had relatively neutral to negative sentiment scores. On the other hand, paragraphs regarding the ECB’s policy continuity, stability of the financial sector, and controlling inflation in the medium term had relatively positive sentiment scores.

The word frequency analysis and word cloud highlighted recurring themes such as energy, growth, financial conditions, markets, inflation outlook, and monetary policy transmission.

Because ECB communication is highly technical and formal, the sentiment analysis results should be interpreted as general indicators rather than exact measurements of economic optimism or pessimism.