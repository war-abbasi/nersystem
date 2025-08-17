# 📝 Named Entity Recognition (NER) System

This project demonstrates a **Named Entity Recognition (NER)** system that can automatically detect:
- 👤 **People**
- 🏢 **Organizations**
- 🌍 **Locations**

from raw text like news articles or reports.

---

## ✨ Features
- Uses **spaCy's pre-trained model** (`en_core_web_sm`) for entity extraction.
- Identifies and groups entities into `PERSON`, `ORG`, and `GPE`.
- Interactive console-based input.
- Results displayed in JSON format.
- Optional entity visualization with spaCy’s `displacy`.

---

## 🛠️ Tech Stack
- **Python 3.8+**
- **spaCy**
- (Optional) Hugging Face Transformers for advanced/fine-tuned models.

---

## 📂 Project Structure
```

NER-System/
│── ner\_system.py        # Main NER script
│── requirements.txt     # Dependencies
│── README.md            # Documentation

````

---

## ⚙️ Setup Instructions
1. **Clone the repo**
   ```bash
   git clone https://github.com/war-abbasi/nersystem.git
   cd nersystem
````

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Download spaCy model**

   ```bash
   python -m spacy download en_core_web_sm
   ```

4. **Run the script**

   ```bash
   python ner_system.py
   ```

---

## 🚀 Example Run

```
📌 Named Entity Recognition (NER) System
Type or paste text, and I'll extract People, Orgs, and Locations.
Type 'exit' to quit.

Enter text: Apple was founded by Steve Jobs in California.

Extracted Entities:
{
  "PERSON": ["Steve Jobs"],
  "ORG": ["Apple"],
  "GPE": ["California"]
}
```

---

## 📊 Possible Improvements

* Swap spaCy with a **Hugging Face Transformer model** (e.g., BERT, RoBERTa).
* Fine-tune a model on **CoNLL-2003 dataset** for higher accuracy.
* Evaluate using **Precision, Recall, F1-score**.
* Build a small **web app** with Streamlit or Flask to showcase the results.

---

## 👩‍💻 Author

This project was created as part of my learning in **NLP and Information Extraction**.

```
