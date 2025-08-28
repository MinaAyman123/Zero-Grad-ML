# 📊 Superstore Data Analysis

This project performs **exploratory data analysis (EDA)** on the **Superstore dataset** using **Python, Pandas, Seaborn, Matplotlib, and NumPy**.
The goal is to extract insights about sales, profits, delivery times, and customer behavior.

---

## 🔧 Tools & Libraries

* **Python 3**
* **Pandas** → Data manipulation
* **NumPy** → Numerical operations
* **Seaborn & Matplotlib** → Data visualization

---

## 📂 Dataset

The dataset used is `superstore_cleaned.csv`.
It contains information about:

* Orders (Order ID, Order Date, Ship Date, Ship Mode)
* Customers (Customer ID, Segment, Region)
* Products (Category, Sub-Category, Product Name)
* Sales, Quantity, Discount, Profit

---

## 🚀 Steps in Analysis

### 1. Data Loading & Cleaning

* Read dataset with Pandas.
* Checked data info, shape, duplicates, and descriptive statistics.
* Dropped unnecessary columns (`Order ID`, `Customer Name`, `Sub-Category`).

### 2. Filtering & Exploration

* Extracted records for **specific categories** (e.g., Furniture).
* Analyzed orders from **specific customers**.
* Checked **highest order frequency dates**.
* Investigated **products with losses** (negative profit).

### 3. Feature Engineering

* Converted `Order Date` and `Ship Date` into datetime format.
* Created a new feature: **Delivery\_Days = Ship Date - Order Date**.

### 4. Visualizations

* **Histograms**: Distribution of `Quantity`, `Discount`, and `Delivery_Days`.
* **Count plots**: Frequency of categories and customer segments.
* **Bar plots**: Average profit by `Category`, `Segment`, and `Ship Mode`.
* **Box plot**: Distribution of `Sales`.
* **Pair plot**: Relationship between numerical features.
* **Correlation heatmap**: Insights into relationships between numerical columns.

---

## 📈 Key Insights

* Some products and orders generate **negative profit**, especially with high discounts.
* **Standard Class shipping** is the most common but not always profitable.
* Delivery times vary significantly depending on shipping mode.
* Certain categories contribute more consistently to profit.

---

## 📌 Future Work

* Build predictive models (e.g., forecast sales/profits).
* Optimize discount strategies.
* Analyze customer lifetime value (CLV).
* Implement dashboards for business users.


