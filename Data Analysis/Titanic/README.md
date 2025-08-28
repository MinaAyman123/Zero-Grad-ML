
````markdown
# 🚢 Titanic Survival Analysis (EDA)

This repository contains an exploratory data analysis (EDA) of the **Titanic dataset** (`train.csv`).  
The goal is to clean the dataset, explore relationships between features, and analyze which factors influenced survival.

---

## 📂 Dataset
The dataset comes from the famous **Kaggle Titanic Competition**.  
It includes passenger information such as:
- Pclass (Ticket Class)
- Name, Sex, Age
- SibSp (Siblings/Spouses aboard)
- Parch (Parents/Children aboard)
- Fare
- Cabin
- Embarked (Port of Embarkation)
- Survival status (0 = Did not survive, 1 = Survived)

---

## 🔧 Steps Performed
1. **Data Cleaning**
   - Removed missing values in `Embarked`.
   - Dropped irrelevant features: `PassengerId`, `Name`, `Ticket`, and `Cabin`.
   - Filled missing `Age` values with the **median age per (Pclass, Sex, Embarked)** group.

2. **Exploratory Data Analysis (EDA)**
   - Distribution plots for numeric features (`Age`, `Fare`, etc.).
   - Count plots for categorical features (`Sex`, `Embarked`).
   - Survival rate analysis across features using group means and barplots.

3. **Outlier Detection & Removal**
   - Applied the IQR method on `Age` and `Fare`.
   - Filtered extreme fares (`Fare < 52`) for better visualization.

4. **Feature Engineering**
   - Created `Family Size = SibSp + Parch`.
   - Created `Alone = True` if passenger had no family aboard.

5. **Visualization**
   - Histograms and countplots for distributions.
   - Boxplots to check outliers.
   - Barplots showing **average survival rate per feature**.

---

## 📊 Example Insights
- **Women survived more often** than men.
- **1st class passengers** had a higher chance of survival.
- People traveling **alone** had lower survival rates.
- Large families also had lower survival rates compared to small families.

---

## 🛠️ Technologies Used
- **Python**  
- **Pandas** (data manipulation)  
- **Seaborn** & **Matplotlib** (visualizations)  
- **NumPy**  

---

## 🚀 How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/titanic-eda.git
````

2. Navigate to the project folder:

   ```bash
   cd titanic-eda
   ```
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
4. Run the script:

   ```bash
   python analysis.py
   ```

