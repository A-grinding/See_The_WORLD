# 🌍 World Sentiment Analyzer (Reddit-Based)

## 📌 Overview

This project is a **Sentiment Analysis Web Application** that analyzes public opinion on any keyword by extracting real-time data from Reddit. It allows users to input a word or topic (e.g., *Artificial Intelligence*) and visualize how people feel about it — whether **positive, negative, or neutral**.

The system integrates **Python, R, and Reddit API** to perform data collection, processing, sentiment analysis, and visualization.

---

## 🎯 Features

* 🔎 Search any keyword/topic
* 🌐 Fetch real-time posts from Reddit
* 🧠 Perform sentiment analysis (Positive / Negative / Neutral)
* 📊 Visualize sentiment distribution using graphs
* 🧾 Display actual Reddit posts for context
* ⚡ Interactive and simple UI

---

## 🖼️ Screenshots

### 🔹 1. Sentiment Analysis Graph

<img width="1385" height="695" alt="Screenshot 2026-03-28 at 5 15 08 AM" src="https://github.com/user-attachments/assets/8373d965-6c13-40ad-bb99-26fd3eb65c1b" />


* Displays distribution of sentiments across keywords
* Colors represent:

  * 🔴 Negative
  * 🟢 Neutral
  * 🔵 Positive

---

### 🔹 2. User Input Interface
<img width="1470" height="830" alt="Screenshot 2026-03-28 at 4 50 47 AM" src="https://github.com/user-attachments/assets/f6d48368-7241-4aa3-a972-123a6eb856d5" />


* User enters a keyword (e.g., *Artificial Intelligence*)
* Clean and minimal UI for interaction

---

### 🔹 3. Reddit Posts Output
<img width="1282" height="705" alt="Screenshot 2026-03-28 at 5 29 51 AM" src="https://github.com/user-attachments/assets/c5dba7ca-8e77-46a4-9e4b-f9d1b865178c" />

* Displays real Reddit posts related to the keyword
* Helps understand context behind sentiment

---

## 🏗️ Tech Stack

### 🔹 Frontend

* Streamlit (Python-based UI framework)

### 🔹 Backend

* Python (Data fetching & processing)
* Reddit API (Data source)

### 🔹 Data Analysis & Visualization

* R Programming
* ggplot2 (for graphs)

---

## ⚙️ System Architecture

1. **User Input** → Enter keyword in Streamlit UI
2. **Data Collection** → Python fetches Reddit posts using API
3. **Data Processing** → Clean and prepare text data
4. **Sentiment Analysis** → Classify into Positive, Neutral, Negative
5. **Visualization (R)** → Generate graphs using ggplot2
6. **Display Results** → Show graph + posts in UI

---

## 📁 Project Structure

```
📦 project/
 ┣ 📜 app.py                  
 ┣ 📜 reddit_fetch.py         
 ┣ 📜 sentiment_analysis.py   
 ┣ 📜 generate_insight.R      
 ┣ 📜 analyzed_tweets.csv     
 ┣ 📜 requirements.txt        
 ┗ 📜 README.md               
```

---

## 🚀 Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2️⃣ Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Install R Packages

```R
install.packages("ggplot2")
```

### 4️⃣ Setup Reddit API

* Create Reddit app: https://www.reddit.com/prefs/apps
* Add:

  * client_id
  * client_secret
  * user_agent

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 📈 Example Use Case

Input:

```
artificial intelligence
```

Output:

* Sentiment graph
* Reddit posts
* Insight into public opinion

---

## ⚠️ Challenges Faced

* Integrating **R with Python (Streamlit)**
* Debugging `Rscript` execution errors
* Handling noisy Reddit data
* API rate limits

---

## 🔮 Future Improvements

* Advanced NLP (BERT, Transformers)
* Multi-platform integration
* Real-time analytics
* Word clouds & trend tracking

---

## 🙌 Conclusion

This project demonstrates how **Python + R + APIs** can be combined to build a powerful analytics tool for understanding public sentiment.

---

## 👨‍💻 Author

**[Your Name]**
B.Sc Data Science & AI

---

## ⭐ Acknowledgment

* Reddit API
* Streamlit
* R & ggplot2
* Open-source NLP tools

---
