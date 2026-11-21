# Practical Laboratory Activities

**Author:** Mayank Mishra  
**Date:** 21 November 2026  
**Environment:** Python 3.12, Jupyter Notebook

This repository contains five practical laboratory exercises covering exploratory
data analysis, OpenCV image blending, generative-AI prompt engineering,
e-commerce review analytics, and an interactive Gradio chatbot.

---

## Quick start

```powershell
# From the project root
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m jupyter notebook
```

Open the five notebooks from the project root so that all relative paths in the
notebooks resolve correctly.

---

## Notebooks and deliverables

| Exercise | Notebook | Main outputs |
| --- | --- | --- |
| 1 — Exploratory Data Analysis | `Exercise1_MayankMishra.ipynb` | `outputs/Exercise1/scatter_plot.png`, `outputs/Exercise1/Exercise1_output.xlsx` |
| 2 — Image Blending with OpenCV | `Exercise2_MayankMishra.ipynb` | `outputs/Exercise2/image1.jpg`, `image2.jpg`, `blended_image.jpg`, `comparison.png` |
| 3 — Generative AI Prompt Engineering | `Exercise3_MayankMishra.ipynb` | `outputs/Exercise3/video_screenshot.png`, `reference_collage.jpg`, local `exercise3_animatic.mp4` |
| 4 — E-Commerce Text & Quantitative Analytics | `Exercise4_MayankMishra.ipynb` | `outputs/Exercise4/cleaned_reviews.csv`, `product_summary.csv`, `wordcloud.png`, two supporting charts |
| 5 — Interactive AI Prototyping with Gradio | `Exercise5_MayankMishra.ipynb` | `outputs/Exercise5/gradio_screenshot.png`, `gradio_screenshot_initial.png` |

Exercise 3 intentionally uses **one Markdown cell only**, as required by the
exercise instructions. It contains the full write-up, prompt, storyboard, and
result status.

---

## Project structure

```text
Practical_Laboratory_Project/
│
├── Exercise1_MayankMishra.ipynb
├── Exercise2_MayankMishra.ipynb
├── Exercise3_MayankMishra.ipynb
├── Exercise4_MayankMishra.ipynb
├── Exercise5_MayankMishra.ipynb
├── Exercise5_app.py
├── requirements.txt
├── README.md
│
├── dataset/
│   └── flipkart_reviews.csv
│
└── outputs/
    ├── Exercise1/
    │   ├── scatter_plot.png
    │   └── Exercise1_output.xlsx
    │
    ├── Exercise2/
    │   ├── image1.jpg
    │   ├── image2.jpg
    │   ├── blended_image.jpg
    │   └── comparison.png
    │
    ├── Exercise3/
    │   ├── video_screenshot.png
    │   ├── reference_collage.jpg
    │   ├── exercise3_animatic.mp4
    │   └── exercise3_animatic.gif
    │
    ├── Exercise4/
    │   ├── cleaned_reviews.csv
    │   ├── product_summary.csv
    │   ├── wordcloud.png
    │   ├── rating_distribution.png
    │   └── top_products.png
    │
    └── Exercise5/
        ├── gradio_screenshot.png
        └── gradio_screenshot_initial.png
```

---

## Exercise notes

### Exercise 1 — Exploratory Data Analysis & Automated Reporting

- Generated a reproducible 100-row DataFrame with `f1`–`f4` using
  `numpy.random.seed(42)`.
- Plotted `f2` against `f3`. The Pearson correlation is **0.02**, so there is no
  meaningful linear relationship in this random sample.
- Calculated `f5` as the row-wise mean of `f1`–`f4`.
- Exported all five columns to an Excel workbook with `Data` and `Summary`
  sheets.

### Exercise 2 — Image Blending Using OpenCV

- Inputs: a mountain landscape and a Santorini cityscape, both 1600 × 900.
- Resized both to 800 × 450 and blended with:

  ```python
  cv2.addWeighted(image1, 0.5, image2, 0.5, 0)
  ```

- Saved the blended image and a three-panel comparison figure.
- OpenCV reads images in BGR order, so images were converted to RGB before
  Matplotlib display.

**Image attribution:** Lorem Picsum photo IDs 29 (Alexander Shustov) and 49
(Margaret Barley), retrieved from <https://picsum.photos/>. Lorem Picsum serves
freely usable Unsplash photographs.

### Exercise 3 — Generative AI Prompt Engineering

- **Selected tool:** Runway (the prompt is also compatible with Google Veo).
- **Target:** 3-second, 16:9 video using the two original images and the blended
  image from Exercise 2.
- **Prompt and camera plan:** documented in the single Markdown cell of
  `Exercise3_MayankMishra.ipynb`.
- **Execution status:** no real Runway/Veo generation was performed because the
  service requires an account, credits, and interactive upload access.
- `outputs/Exercise3/video_screenshot.png` is a **storyboard**, and
  `exercise3_animatic.mp4` is a **locally rendered OpenCV animatic preview**.
  Neither is presented as AI-generated output.
- `reference_collage.jpg` combines the three frames into one image for tools
  that accept only a single reference image.

To complete the exercise with a real tool:

1. Open Runway or Google Veo and start an image-to-video project.
2. Upload `image1.jpg`, `image2.jpg`, and `blended_image.jpg`, or upload
   `reference_collage.jpg` if only one reference is allowed.
3. Paste the exact prompt from the notebook.
4. Set duration to 3 seconds and aspect ratio to 16:9.
5. Replace the “Result and Evidence” section with the real video link or a
   screenshot of the generated result.

### Exercise 4 — E-Commerce Text & Quantitative Analytics

**Dataset:** `dataset/flipkart_reviews.csv` contains **205,052 rows** and six
columns: `product_name`, `product_price`, `Rate`, `Review`, `Summary`,
`Sentiment`. The public copy used here was obtained from the Hugging Face
dataset [`ml-hub/flipkart-reviews`](https://huggingface.co/datasets/ml-hub/flipkart-reviews),
which mirrors the Flipkart review data used in the exercise.

**Cleaning performed:**

- Renamed `product_name` → `Product_name` and `product_price` → `Price`.
- Converted `Rate` and `Price` to numeric values.
- Kept ratings from 1 to 5.
- Removed rows with missing essential fields.
- Removed 34,375 exact duplicate rows.
- Normalised text fields and added `Review_length`.

**Results after cleaning:**

| Metric | Value |
| --- | --- |
| Clean rows | 170,674 |
| Products | 958 |
| Mean rating | 4.06 |
| Median price | ₹849 |
| Mean price | ₹4,488.55 |
| Most-reviewed product | cello 18-piece Opalware dinner set (4,362 reviews) |
| Positive / neutral / negative | 134,699 / 9,503 / 26,472 |

The notebook produces `items`, a product-level DataFrame with `mean_rating`,
`mean_price`, and `review_count`, and saves it as `product_summary.csv`.

### Exercise 5 — Interactive AI Prototyping with Gradio

- Built a rule-based chatbot with `gr.ChatInterface`.
- Added a title, welcome message, and four sample prompts.
- Launched locally on `127.0.0.1:7860`, verified an HTTP 200 response, and closed
  the server cleanly.
- The chatbot requires no API key. It can later be connected to an LLM by
  replacing the `chatbot()` function.
- Run the standalone version with:

  ```powershell
  python Exercise5_app.py
  ```

  Then open <http://127.0.0.1:7860>.

The screenshot `gradio_screenshot.png` shows the working interface with a user
prompt and the bot response. `gradio_screenshot_initial.png` shows the initial
screen with the sample prompts.

---

## Reproducing the executed notebooks

The notebooks are already executed and contain their outputs. To re-run them:

```powershell
python -m nbconvert --to notebook --execute --inplace --ExecutePreprocessor.timeout=1200 Exercise1_MayankMishra.ipynb
python -m nbconvert --to notebook --execute --inplace --ExecutePreprocessor.timeout=1200 Exercise2_MayankMishra.ipynb
python -m nbconvert --to notebook --execute --inplace --ExecutePreprocessor.timeout=1200 Exercise4_MayankMishra.ipynb
python -m nbconvert --to notebook --execute --inplace --ExecutePreprocessor.timeout=1200 Exercise5_MayankMishra.ipynb
```

Exercise 3 is a Markdown-only notebook and does not need execution.


## Libraries used

pandas, NumPy, Matplotlib, openpyxl, OpenCV, WordCloud, Gradio, Pillow,
Jupyter, nbformat, nbconvert, ipykernel, requests, and kagglehub.
