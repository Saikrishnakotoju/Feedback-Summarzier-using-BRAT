# Feedback-Summarzier-using-BRAT
# Abstractive Text Summarizer (BART)

Summarizes customer feedback into a short, natural-sounding summary using the pretrained BART model from Hugging Face (`facebook/bart-large-cnn`).

## What It Does
Reads a feedback text file and generates a new summary in its own words (abstractive summarization), rather than copying existing sentences.

## Tech Stack
Python, Hugging Face Transformers

## Installation
```bash
pip install transformers torch
```

## Usage
1. Put your feedback in a text file, for example `sample_feedback.txt`
2. Set `file_path` in the script to that file
3. Run:
```bash
python your_script_name.py
```

## Parameters
- `max_len` (default 60): maximum summary length in tokens
- `min_len` (default 25): minimum summary length in tokens

## Sample Output
```
Abstractive Summary:
<paste your real output here>
```

## Limitations
- BART accepts about 1024 tokens, so long text gets truncated
- Uses the pretrained model without fine-tuning
- Abstractive models can occasionally produce details not in the original text

## Future Improvements
- Split long feedback into chunks, summarize each, then combine
- Add sentiment classification
- Build a simple Streamlit interface

## Author
Sai Krishna Kotoju | [LinkedIn](https://www.linkedin.com/in/saikrishna-kotoju)
