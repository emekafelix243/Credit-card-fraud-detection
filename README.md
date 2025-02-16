# Credit Card Default Prediction
## Overview
Credit card fraud is a significant challenge in the financial industry, impacting both financial institutions and customers. As fraudsters develop more sophisticated techniques, it becomes crucial to implement advanced fraud detection models.
This project aims to predict credit card payment defaults using machine learning models. By leveraging customer transaction history and financial attributes, the model assesses the likelihood of default.
________________________________________
## Objectives
The primary goal of this project is to develop a robust fraud detection model that accurately identifies transactions at risk of default. Using machine learning techniques, the model analyzes historical transaction patterns and payment behaviors to predict future defaults.
________________________________________
## Features
•	**Data Preprocessing:** Handling missing values, feature scaling, and encoding categorical variables.
•	**Exploratory Data Analysis (EDA):** Understanding data distribution and feature correlations.
•	**Model Training:** Implementing Logistic Regression, Random Forest, and XGBoost.
•	**Model Evaluation:** Assessing performance using precision, recall, confusion matrix, and AUC-ROC score.
•	**Model Deployment:** Saving the best-performing model for future inference.
________________________________________
## Dataset Overview
The dataset used for this project is the UCI Credit Card dataset, obtained from the UCI Machine Learning Repository. It consists of customer credit card transaction history and financial attributes from Taiwan between April 2005 and September 2005.
### Dataset Information:
•	**Number of Entries:** 30,000
•	**Number of Features:** 25
•	**Target Variable:** default.payment.next.month (1 for default, 0 for non-default)
### Key Features:
•	**Demographics:** AGE, SEX, MARRIAGE, EDUCATION
•	**Credit History:** LIMIT_BAL, PAY_0 to PAY_6 (payment history for six months)
•	**Transaction Details:** BILL_AMT1 to BILL_AMT6 (bill amounts), PAY_AMT1 to PAY_AMT6 (payment amounts)
________________________________________
## Installation
To set up and run this project on your local machine, follow these steps:
1.	Clone the repository:
	  git clone https://github.com/emekafelix243/Credit-card-fraud-detection.git
2.	Navigate to the project directory:
    cd credit-card-default
3.	Create a virtual environment and activate it:
    python -m venv venv 
      # On Windows: venv\Scripts\activate
      # On macOS/Linux: source venv/bin/activate 
4.	Install dependencies:
      pip install -r requirements.txt
5.	Place the dataset in the data/ directory.
________________________________________
## Model Training
  Run the following script to preprocess data, train models, and evaluate performance:
    python train.py
    ________________________________________
## Benchmark Models
    To establish a baseline for fraud detection, three machine learning models were implemented:
1.	Logistic Regression
2.	Random Forest
3.	XGBoost

## Model Training Pipeline:
•	Data Preprocessing: Handling missing values, feature scaling, and encoding categorical features.
•	Feature Engineering: Selecting the most relevant features for training.
•	Model Training: Applying cross-validation for improved generalization.
•	Model Evaluation: Assessing accuracy, precision, recall, F1-score, and ROC-AUC.
________________________________________

## Model Evaluation
Performance metrics of the trained models:
Model	Recall (Non-Defaults)	Recall (Defaults)	AUC-ROC Score
Logistic Regression	0.97	0.24	0.7103
Random Forest	-	0.35	0.7750
XGBoost	-	0.37	0.7795

## Key Insights:
•	All models effectively identify non-defaulting customers but struggle with recall for defaults, which is critical for mitigating credit 
  risk.
•	XGBoost achieved the highest AUC-ROC score (0.7795) but still requires optimization.
________________________________________

## Recommendations
    To improve the fraud detection model, we suggest:
  1.	Enhancing Feature Engineering – Extract meaningful features from transaction patterns.
  2.	Balancing the Dataset – Use oversampling/undersampling techniques (SMOTE) to address class imbalance.
  3.	Adjusting Classification Thresholds – Tune the decision threshold to improve recall for defaults while maintaining accuracy.
  ________________________________________
## Importance of Fraud Detection
Credit card fraud detection is vital for financial institutions to: ? Mitigate financial losses
* Prevent unauthorized transactions
* Maintain trust and confidence in the financial system
  ________________________________________
## Deployment
To use the trained model for predictions:
python predict.py
________________________________________

## Conclusion
The objective of predicting credit card payment defaults was analyzed using Logistic Regression, Random Forest, and XGBoost models. Below are the key takeaways:
Model	Strengths	Weaknesses
Logistic Regression	? High recall for non-defaults (0.97) ? AUC-ROC score: 0.7103	? Poor recall for defaults (0.24) ? Misses many defaulting customers
Random Forest	? Improved recall for defaults (0.35) ? Better AUC-ROC score (0.7750)	? Still struggles with default recall ? Slightly more false positives
XGBoost	? Best AUC-ROC score (0.7795) ? Improved precision for defaults (0.61)	? Recall for defaults remains low (0.37), though slightly better than Random Forest
?? Key Insight:
All models effectively identify non-defaulting customers but struggle with recall for defaults, which is critical for mitigating credit risk. XGBoost performs the best overall but requires further optimization to improve default classification.
? Next Steps:
?? Explore hyperparameter tuning, deep learning models, and real-time fraud detection pipelines!



