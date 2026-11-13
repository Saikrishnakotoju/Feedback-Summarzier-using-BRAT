from transformers import pipeline

def abstractive_summary(file_path, max_len=60, min_len=25):
    with open(file_path, 'r') as file:
        text = file.read()

    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summary = summarizer(text, max_length=max_len, min_length=min_len, do_sample=False)
    
    return summary[0]['summary_text']

file_path = "C:/Users/User/Desktop/majorpp/sample_feedback_25.txt"
abs_summary = abstractive_summary(file_path)
print("🔹 Abstractive Summary:\n", abs_summary)
