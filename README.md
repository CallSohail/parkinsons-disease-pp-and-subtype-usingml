Parkinson's Disease Progression Prediction


Table of Contents
Overview
Objectives
Project
Structure
Technologies
Installation
Usage
Model
Architecture
Results
Contributors
License
Overview
This project, Parkinson's Disease Progression Prediction, leverages machine learning models to identify subtypes of Parkinson's disease (PD) and predict disease progression. Using comprehensive clinical and genetic data, we aim to support personalized treatment approaches, optimized clinical trials, and patient management.

Objectives
Identify PD Subtypes: Classify patients into progression rates (slow, moderate, and fast progressors).
Develop Predictive Models: Train models to forecast disease course, using baseline clinical factors, biomarkers, and genetic data.
Utilize Machine Learning Techniques: Employ supervised and unsupervised learning models to analyze PD data effectively.
Project Structure
bash
Copy code
📦 Parkinsons-Disease-Progression-Prediction
├── README.md                     
# Project documentation

├── data                           
# Data directory

├── notebooks                      
# Jupyter notebooks for data analysis and modeling

├── src                            
# Source code for the models and processing

│   ├── preprocessing.py           
# Data preprocessing scripts

│   ├── modeling.py                
# Machine learning models

│   └── visualization.py           
# Visualization functions

├── app.py                         
# Streamlit app for interactive exploration

├── requirements.txt               
# Python package dependencies

└── LICENSE                        
# Project license

Technologies
Programming Language: Python (3.10+)
Libraries and Frameworks:
Data Processing: Pandas, NumPy, Scikit-learn
Modeling: XGBoost, LightGBM, Random Forest
Visualization: Matplotlib, Seaborn, Plotly, SHAP
Web Application: Streamlit
Installation
Clone the Repository:

bash
Copy code
git 
clone
 https://github.com/yourusername/Parkinsons-Disease-Progression-Prediction.git
cd
 Parkinsons-Disease-Progression-Prediction
Create a Virtual Environment (Optional but recommended):

bash
Copy code
python -m venv venv
source
 venv/bin/activate  
# On Windows, use `venv\Scripts\activate`

Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Run the Streamlit App:

bash
Copy code
streamlit run app.py
Usage
Data Input: Use either provided sample datasets or upload new patient data.
Subtype Prediction: Explore PD subtypes and view patient progression predictions with probability distributions.
Feature Importance: Visualize feature impact using SHAP values for insights into model predictions.
Model Architecture
The project uses both supervised and unsupervised learning models:

Unsupervised Learning: Non-negative Matrix Factorization (NMF) to represent progression space, and Gaussian Mixture Model (GMM) for clustering subtypes.
Supervised Learning: Ensemble models using XGBoost, LightGBM, and Random Forest to predict disease progression and subtype classification.
Results
The predictive models demonstrate high accuracy:

Subtype Classification: The models can accurately distinguish PD progression rates, achieving an AUC of 0.92 on baseline factors.
Cross-validation: Validation on independent datasets such as the PDBP cohort shows consistent predictive accuracy.
Contributors
Ahmad Nabi Sultan
Muhammad Sohail
Supervisor: Dr. Anwar ul Haq
License
This project is licensed under the MIT License. See the
LICENSE
file for details.
