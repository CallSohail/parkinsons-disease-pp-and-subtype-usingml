# Parkinson's Disease Progression Prediction 
## Table of Contents
- [Overview](#overview)
- [Objectives](#objectives)
- [Project Structure](#project-structure)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [Model Architecture](#model-architecture)
- [Results](#results)
- [Contributors](#contributors)
- [License](#license)

---

## Overview
This project, *Parkinson's Disease Progression Prediction*, leverages machine learning models to identify subtypes of Parkinson's disease (PD) and predict disease progression. Using comprehensive clinical and genetic data, we aim to support personalized treatment approaches, optimized clinical trials, and patient management.

## Objectives
- **Identify PD Subtypes**: Classify patients into progression rates (slow, moderate, and fast progressors).
- **Develop Predictive Models**: Train models to forecast disease course, using baseline clinical factors, biomarkers, and genetic data.
- **Utilize Machine Learning Techniques**: Employ supervised and unsupervised learning models to analyze PD data effectively.

## Project Structure
```plaintext
📦 Parkinsons-Disease-Progression-Prediction
├── README.md                     # Project documentation
├── data                           # Data directory
├── notebooks                      # Jupyter notebooks for data analysis and modeling
├── src                            # Source code for the models and processing
│   ├── preprocessing.py           # Data preprocessing scripts
│   ├── modeling.py                # Machine learning models
│   └── visualization.py           # Visualization functions
├── app.py                         # Streamlit app for interactive exploration
├── requirements.txt               # Python package dependencies
└── LICENSE                        # Project license

```
# Parkinson's Disease Progression Prediction

This project, *Parkinson's Disease Progression Prediction*, leverages machine learning models to identify subtypes of Parkinson's disease (PD) and predict disease progression. Using comprehensive clinical and genetic data, we aim to support personalized treatment approaches, optimized clinical trials, and patient management.

## Technologies
Programming Language: Python (3.10+)
Libraries and Frameworks:
- Data Processing: Pandas, NumPy, Scikit-learn
- Modeling: XGBoost, LightGBM, Random Forest
- Visualization: Matplotlib, Seaborn, Plotly, SHAP
- Web Application: Streamlit

## Installation
To run this project locally, follow these steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Parkinsons-Disease-Progression-Prediction.git
   cd Parkinsons-Disease-Progression-Prediction
   ```
2. Create a Virtual Environment (Optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
3. Install Dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Streamlit App:
   ```bash
   streamlit run app.py
   ```

## Usage
- Data Input: Use either provided sample datasets or upload new patient data.
- Subtype Prediction: Explore PD subtypes and view patient progression predictions with probability distributions.
- Feature Importance: Visualize feature impact using SHAP values for insights into model predictions.

## Model Architecture
The project uses both supervised and unsupervised learning models:
- Unsupervised Learning: Non-negative Matrix Factorization (NMF) to represent progression space, and Gaussian Mixture Model (GMM) for clustering subtypes.
- Supervised Learning: Ensemble XGBoost, LightGBM, and Random Forest models to predict disease progression and subtype classification.

## Results
The predictive models demonstrate high accuracy:
- Subtype Classification: The models can accurately distinguish PD progression rates, achieving an AUC of 0.92 on baseline factors.
- Cross-validation: Validation on independent datasets such as the PDBP cohort shows consistent predictive accuracy.

| Model         | AUC Score |
|---------------|-----------|
| XGBoost       | 0.92      |
| LightGBM      | 0.91      |
| Random Forest  | 0.89      |

## Contributors
- Ahmad Nabi Sultan
- Muhammad Sohail
- Supervisor: Dr. Anwar ul Haq

