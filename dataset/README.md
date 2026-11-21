# Flipkart reviews dataset

`flipkart_reviews.csv` is the dataset used in Exercise 4.

## Source

The copy in this project was downloaded from the public Hugging Face dataset:

<https://huggingface.co/datasets/ml-hub/flipkart-reviews>

File: `review_flipkart.csv` (saved locally as `flipkart_reviews.csv`).

This dataset mirrors the Flipkart product-review data commonly distributed
through Kaggle for educational sentiment-analysis exercises. Refer to the
upstream dataset page for the current license and usage terms.

## Shape and columns

- **Rows:** 205,052
- **Columns:** 6

| Column | Description |
| --- | --- |
| `product_name` | Flipkart product name |
| `product_price` | Listed product price |
| `Rate` | Star rating (1–5) |
| `Review` | Full review text |
| `Summary` | Short review summary |
| `Sentiment` | Positive, neutral, or negative label |

The raw file contains a small number of malformed rows (three product names in
the rating/price fields), 11 missing summaries, 24,664 missing full reviews, and
34,375 exact duplicate rows. Exercise 4 documents and handles these issues.

## Usage

The dataset is included solely for the laboratory exercise. No personal data is
intentionally included in this project copy.
