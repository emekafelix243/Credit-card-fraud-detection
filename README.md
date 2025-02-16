# 💳 Credit Card Default Prediction  

## 📌 Overview  

Credit card fraud is a significant challenge in the financial industry, impacting both **financial institutions** and **customers**. As fraudsters develop more sophisticated techniques, it becomes crucial to implement **advanced fraud detection models**.  

This project aims to **predict credit card payment defaults** using **machine learning models**. By leveraging **customer transaction history** and **financial attributes**, the model assesses the likelihood of default.  

---

## 🎯 Objectives  

The primary goal of this project is to develop a **robust fraud detection model** that accurately identifies transactions at risk of default.  

✅ **Analyze historical transaction patterns**  
✅ **Predict future defaults using machine learning**  
✅ **Optimize recall for defaulted transactions**  

---

## 🚀 Features  

✔ **Data Preprocessing:** Handling missing values, feature scaling, and encoding categorical variables.  
✔ **Exploratory Data Analysis (EDA):** Understanding data distribution and feature correlations.  
✔ **Model Training:** Implementing **Logistic Regression, Random Forest, and XGBoost**.  
✔ **Model Evaluation:** Assessing performance using **precision, recall, confusion matrix, and AUC-ROC score**.  
✔ **Model Deployment:** Saving the **best-performing model** for future inference.  

---

## 📊 Dataset Overview  

The dataset used for this project is the **UCI Credit Card dataset**, obtained from the **UCI Machine Learning Repository**. It consists of **customer credit card transaction history** and **financial attributes** from Taiwan between **April 2005 and September 2005**.  

 ## 🔍 Dataset Information:  

- **📌 Number of Entries:** 30,000  
- **📌 Number of Features:** 25  
- **🎯 Target Variable:** `default.payment.next.month`  
  - **1** → Default  
  - **0** → Non-default  

## 🔑 Key Features  

✔ **Demographics:** `AGE`, `SEX`, `MARRIAGE`, `EDUCATION`  
✔ **Credit History:** `LIMIT_BAL`, `PAY_0` to `PAY_6` (payment history for six months)  
✔ **Transaction Details:** `BILL_AMT1` to `BILL_AMT6` (bill amounts), `PAY_AMT1` to `PAY_AMT6` (payment amounts)  

---

## ⚙️ Installation  

To set up and run this project on your local machine, follow these steps:  

## 1️⃣ Clone the repository:  
git clone https://github.com/emekafelix243/Credit-card-fraud-detection.git

## 📌 Conclusion
The objective of predicting credit card payment defaults was analyzed using Logistic Regression, Random Forest, and XGBoost models. Below are the key takeaways:

## 📊 Model Performance Summary  

| **Model**              | **✅ Strengths**                                | **❌ Weaknesses**                              |
|------------------------|-----------------------------------------------|-----------------------------------------------|
| **Logistic Regression** | ✅ High recall for non-defaults **(0.97)**    | ❌ Poor recall for defaults **(0.24)**        |
|                        | ✅ AUC-ROC score: **0.7103**                   | ❌ Misses many defaulting customers           |
| **Random Forest**      | ✅ Improved recall for defaults **(0.35)**     | ❌ Still struggles with default recall        |
|                        | ✅ Better AUC-ROC score **(0.7750)**           | ❌ Slightly more false positives              |
| **XGBoost**           | ✅ Best AUC-ROC score **(0.7795)**             | ❌ Recall for defaults remains low **(0.37)** |
|                        | ✅ Improved precision for defaults **(0.61)**  | ❌ Slightly better than Random Forest         |

## 🔑 Key Insights
1️⃣ All models effectively identify non-defaulting customers but struggle with recall for defaults, which is critical for mitigating credit risk.

2️⃣ XGBoost performs the best overall, but further optimization is required to improve default

## 🚀 Next Steps  
🔹 **Explore hyperparameter tuning** to optimize model performance.  
🔹 **Experiment with deep learning models** (e.g., Neural Networks).  
🔹 **Develop real-time fraud detection pipelines** for better responsiveness.  
