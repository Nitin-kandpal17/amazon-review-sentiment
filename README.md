# Amazon Review Sentiment Analysis 🛒

A sentiment analysis project to classify Amazon product reviews as Positive, Neutral, or Negative. Built with traditional ML models and deployed using FastAPI.

## 🔍 Project Overview
- **Goal**: Predict sentiment of Amazon reviews (text).
- **Models Used**: Multinomial Naive Bayes, Logistic Regression, LSTM
- **Vectorization**: TF-IDF
- **Pipeline**: Data cleaning ➝ Vectorization ➝ Model training ➝ API deployment

## 🗂️ Project Structure
├── api/ # FastAPI code                                                   
│ └── app.py                                                             
├── data/ # Raw and cleaned datasets                                                  
│ ├── raw_reviews.csv                                                       
│ └── cleaned_reviews.json                                                         
├── models/ # Trained models (pkl files)                                                          
│ ├── naive_bayes.pkl                                                  
│ ├── lstm_model.h5                                                               
│ └── tfidf_vectorizer.pkl                                                                     
├── notebooks/ # Jupyter notebooks                                                                          
│ ├── 1_data_exploration.ipynb                                                                                      
│ ├── 2_preprocessing.ipynb                                                                                       
│ ├── 3_model_training.ipynb                                                                        
│ ├── 4_class_imbalance.ipynb                                                                        
│ └── 5_deployment.ipynb                                                                        
├── report/ # Report images                                                                               
├── results/ # Predictions/output                                                                           
├── .gitignore                                                                         
├── README.md                                                                                            
├── LICENSE                                                                           
└── requirements.txt                                                                     

## 🚀 Deployment
- Run API locally using:
```bash
uvicorn api.app:app --reload
```
+ Test endpoint at: http://127.0.0.1:8000/docs


## 📦 Installation
```bash
git clone https://github.com/Nitin-kandpal17/amazon-review-sentiment.git
cd sentiment-analysis
pip install -r requirements.txt
```

## 📋 Features
+ Cleaned and lemmatized corpus using spaCy

+ Addressed class imbalance with SMOTE

+ API endpoint for real-time sentiment prediction

## 📌 Usage
```bash
curl -X POST "http://127.0.0.1:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{"text": "This product is amazing!"}'
```
## 🧠 Sample Output
```json
  {"text": "This product is amazing!",
  "predicted_class": 2,
  "sentiment": "Positive"}
```

## 📄 License
This project is licensed under the MIT License.

---

## 👨‍💻 About the Author

**Nitin Kandpal**  
Creating intelligent solutions with Python, Machine Learning, Deep Learning, and APIs.

- 🔗 [GitHub](https://github.com/Nitin-kandpal17)
- 🧠 Passionate about building real-world AI tools and sharing knowledge.
- 🎥 I also create educational YouTube videos on Python and Data Science.

---
