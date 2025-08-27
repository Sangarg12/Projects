# Customer Churn Analysis - Telecom Company 📊

A comprehensive exploratory data analysis (EDA) project to identify key factors driving customer churn in a telecommunications company and provide actionable business recommendations.

## 📋 Table of Contents
- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Key Findings](#key-findings)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Results & Recommendations](#results--recommendations)
- [Financial Impact](#financial-impact)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Project Overview

This project analyzes customer churn patterns in a telecom company to:
- Identify the primary reasons behind customer churn
- Understand customer behavior patterns
- Provide data-driven recommendations to reduce churn rate
- Quantify the financial impact of churn reduction strategies

**Objective**: To identify the reasons behind customer churn and develop strategies to improve customer retention.

## 📊 Dataset

**Source**: [Kaggle - Telco Customer Churn Dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn/data)

**Dataset Details**:
- **Total Records**: 7,043 customers
- **Features**: 21 columns
- **Target Variable**: Churn (Yes/No)

### Column Descriptions:
| Column | Description |
|--------|-------------|
| customerID | Unique customer identifier |
| gender | Customer gender (Male/Female) |
| SeniorCitizen | Whether customer is senior citizen (0/1) |
| Partner | Whether customer has a partner (Yes/No) |
| Dependents | Whether customer has dependents (Yes/No) |
| tenure | Number of months with company |
| PhoneService | Phone service subscription (Yes/No) |
| MultipleLines | Multiple phone lines (Yes/No/No phone service) |
| InternetService | Internet service type (DSL/Fiber optic/No) |
| OnlineSecurity | Online security service (Yes/No/No internet service) |
| OnlineBackup | Online backup service (Yes/No/No internet service) |
| DeviceProtection | Device protection service (Yes/No/No internet service) |
| TechSupport | Technical support service (Yes/No/No internet service) |
| StreamingTV | TV streaming service (Yes/No/No internet service) |
| StreamingMovies | Movie streaming service (Yes/No/No internet service) |
| Contract | Contract term (Month-to-month/One year/Two year) |
| PaperlessBilling | Paperless billing (Yes/No) |
| PaymentMethod | Payment method used |
| MonthlyCharges | Monthly charges amount |
| TotalCharges | Total charges over tenure |
| Churn | Customer churned (Yes/No) |

## 🔍 Key Findings

### Current Performance Metrics:
- **Total Customers**: 7,043
- **Churn Rate**: 26.5% (1,869 customers)
- **Retention Rate**: 73.5% (5,174 customers)
- **Monthly Revenue Loss**: $139,130.85
- **Projected Annual Loss**: $1,669,570.20

### Top Churn Risk Factors:
1. **Month-to-month contracts**: 42.7% churn rate
2. **New customers (0-12 months)**: 47.4% churn rate
3. **Electronic check payment**: 45.3% churn rate
4. **Fiber optic internet service**: 41.9% churn rate
5. **No Tech Support**: 41.6% churn rate

### Key Insights:
- **Contract Type**: Customers with longer contracts (1-2 years) have significantly lower churn rates
- **Payment Method**: Electronic check users are highest risk, automatic payments reduce churn
- **Tenure Impact**: Most churn occurs within the first 12 months
- **Service Add-ons**: Customers without additional services are more likely to churn
- **Demographics**: Senior citizens show higher churn rates (41.7% vs 23.6%)

## 🛠 Technologies Used

- **Python 3.x**
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computing
- **Matplotlib** - Data visualization
- **Seaborn** - Statistical data visualization
- **Jupyter Notebook** - Development environment

## ⚙️ Installation
1. **Install required packages and python**:
```bash
pip install pandas numpy matplotlib seaborn jupyter
```
2. **Download the dataset**:
- Placed the CSV file in the project directory

## 🚀 Usage

1. **Open Jupyter Notebook**:
```bash
jupyter notebook
```

2. **Run the analysis**:
- Open `Customer-Churn-EDA.ipynb`
- Execute cells sequentially to reproduce the analysis

3. **Key sections in the notebook**:
- Data loading and exploration
- Data cleaning and preprocessing
- Univariate and bivariate analysis
- Churn analysis by different factors
- Visualization of key insights
- Business recommendations

## 📁 Project Structure

```
customer-churn-analysis/
│
├── Customer-Churn-EDA.ipynb    # Main analysis notebook
├── Customer-Churn-EDA.pdf      # PDF report of analysis
├── Customer-Churn.csv          # Dataset (download separately)
├── README.md                   # Project documentation
├── requirements.txt            # Python dependencies
└── visualizations/             # Generated charts and plots
    ├── churn_by_contract.png
    ├── churn_by_payment.png
    └── tenure_analysis.png
```

## 💡 Results & Recommendations

### Immediate Actions Required:

1. **Contract Conversion Program**
   - Target 3,875 month-to-month customers
   - Offer 20-30% discounts for longer contracts
   - **Potential Impact**: 10-15% churn reduction

2. **Payment Method Migration**
   - Convert 2,365 electronic check users to automatic payments
   - Incentivize with autopay discounts
   - **Potential Impact**: 8-12% churn reduction

3. **New Customer Onboarding**
   - Implement 90-day intensive support program
   - Regular check-ins and proactive support
   - **Potential Impact**: 15-20% early churn reduction

4. **Service Upselling Strategy**
   - Promote add-on services (Tech Support, Online Security)
   - Bundle services at attractive pricing
   - Target customers without additional services

## 💰 Financial Impact

### Churn Reduction Scenarios:

| Scenario | Target Churn Rate | Monthly Savings | Annual Savings |
|----------|-------------------|----------------|----------------|
| Conservative | 20% | $34,126 | $409,517 |
| Moderate | 15% | $60,378 | $724,530 |
| Aggressive | 12% | $76,128 | $913,538 |

### Success Metrics to Monitor:
- Monthly churn rate
- Contract conversion rates
- Payment method migration rates
- New customer retention (first 12 months)
- Customer lifetime value
- Revenue per customer



## 📞 Contact

**Your Name** - garg.sandeep1996@gmail.com

---

⭐ **If you found this project helpful, please give it a star!** ⭐
