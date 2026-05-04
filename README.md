# 🌍 Language Translation Model

This project is a multilingual language translation system built using a transformer-based **Seq2Seq (Sequence-to-Sequence)** model. It allows users to translate English text into multiple languages through a simple and interactive web interface.

---

## 🚀 Features

* Translate English text to:

  * Hindi 🇮🇳
  * French 🇫🇷
  * Japanese 🇯🇵
* Built using a **pretrained mBART transformer model**
* Simple and user-friendly UI using **Streamlit**
* Fast performance with **model caching**
* Handles both simple and complex sentences

---

## 🧠 Technology Used

* Python
* Hugging Face Transformers
* mBART (Multilingual Seq2Seq Model)
* Streamlit

---

## 🔄 How It Works

This project uses a **Seq2Seq (Sequence-to-Sequence)** architecture:

* The **encoder** processes the input sentence
* The **decoder** generates the translated output
* The model is pretrained on large multilingual datasets

---

## ▶️ How to Run the Project

1. Install dependencies:

```
pip install transformers torch sentencepiece streamlit
```

2. Run the application:

```
streamlit run app.py
```

3. Open in browser and start translating 🎉

---

## 📌 Example

**Input:**

```
Artificial Intelligence is transforming industries.
```

**Output (Japanese):**

```
人工知能は産業を変革しています。
```

---

## 🎯 Conclusion

This project demonstrates the practical implementation of a **transformer-based Seq2Seq model** for real-time language translation, combining machine learning with an interactive user interface.

---

## 👩‍💻 Author

Gowthami R
