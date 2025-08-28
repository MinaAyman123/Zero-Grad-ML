# 📊 Data Analysis Projects

This repository contains **Exploratory Data Analysis (EDA)** projects using Python, Pandas, Seaborn, and Matplotlib.
Each project explores datasets, cleans data, and visualizes insights.

---

## 📂 Projects

### 🔹 1. Titanic Survival Analysis (`Titanic/`)

* Dataset: `train.csv`
* Cleaned missing values (`Age`, `Embarked`, `Cabin`).
* Feature engineering: **Family Size**, **Alone** feature.
* Explored survival patterns by:

  * Passenger Class
  * Sex
  * Embarked Port
  * Family Size / Alone
* Visualizations: Histograms, Count plots, Box plots, Bar plots.

**Key Insights:**

* Women and children had higher survival rates.
* Higher-class passengers survived more often.
* Being alone decreased survival probability.

---

### 🔹 2. Superstore Sales Analysis (`Superstore Sales/`)

* Dataset: `superstore_cleaned.csv`
* Cleaned duplicates and dropped unnecessary columns.
* Feature engineering: **Delivery\_Days = Ship Date - Order Date**.
* Explored profitability and losses:

  * Categories, Segments, Ship Modes
  * Products with negative profits
  * Orders with delivery anomalies
* Visualizations: Histograms, Count plots, Bar plots, Box plots, Pair plots, Heatmaps.

**Key Insights:**

* Discounts often caused negative profits.
* Standard Class is the most common shipping mode but not always profitable.
* Delivery time varies significantly by ship mode.

---

## 🔧 Tools & Libraries

* Python 3
* Pandas
* NumPy
* Seaborn
* Matplotlib


