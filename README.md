# UEBA Anomaly Detection

## 📌 Project Overview
This project is a **User and Entity Behavior Analytics (UEBA)** system built in Python.  
It uses **machine learning (scikit-learn)** to learn patterns of normal user activity and then detect deviations (anomalies) that may indicate **insider threats or suspicious behavior**.  

The goal is to simulate a lightweight security analytics tool that helps reduce risks by automatically flagging abnormal activity.

---

## ⚙️ Tech Stack
- Python 3.8+
- scikit-learn
- pandas
- numpy
- matplotlib

---

## 📂 Project Structure
```
ueba-anomaly-detection/
 ├── src/               # Python scripts
 │    ├── anomaly_detector.py
 │    ├── train_model.py
 │    └── utils.py
 ├── data/              # Sample datasets for testing
 │    ├── user_logs.csv
 │    └── sample_events.csv
 ├── README.md
 ├── requirements.txt
 └── LICENSE
```

---

## 🚀 How to Run

1. **Clone this repository**
   ```bash
   git clone https://github.com/your-username/ueba-anomaly-detection.git
   cd ueba-anomaly-detection
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run anomaly detection**
   ```bash
   python src/anomaly_detector.py
   ```

---

## 📊 Expected Output
- Trains on normal user activity logs.  
- Identifies unusual behavior (anomalies) and flags them.  
- Provides basic accuracy metrics and false-positive reduction techniques.  

Sample Output:
```
Training completed...
Detection Accuracy: 94.2%
False Positive Rate: 3.1%
Flagged anomalies saved in anomalies.csv
```

---

## 🎯 Learning Outcomes
By completing this project, you will:
- Gain hands-on experience with **UEBA concepts**.  
- Apply **machine learning for anomaly detection**.  
- Work with **realistic security data simulation**.  
- Showcase a professional security project on GitHub, LinkedIn, and your resume.  

---

## 👩‍💻 Author
Maimoona – Security Enthusiast | Exploring UEBA, AI, and Automation  

---

## 📌 Next Steps
- Extend detection with deep learning models.  
- Add real-time log monitoring using Kafka or AWS Kinesis.  
