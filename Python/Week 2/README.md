# 🧰 Wuzzuf Job Scraper

This Python script scrapes job listings from [Wuzzuf.net](https://wuzzuf.net) based on a user's search query and exports the results into a `.csv` file.

## 📦 Features

* Automatically searches Wuzzuf jobs by keyword
* Scrapes:

  * Job Titles
  * Company Names
  * Job Description
  * Occupation Type
  * Job Location
  * Reference Link to the job
* Saves results in a structured CSV file using `pandas`

## 🚀 How to Run

1. **Install Requirements**

```bash
pip install requests beautifulsoup4 lxml pandas
```

2. **Run the script**

```bash
python wuzzuf_scraper.py
```

3. **Enter your search keyword**
   When prompted, enter your job search keyword (e.g. `Python developer`, `Data Analyst`, etc.)

4. **Result**
   A CSV file named like `python-developer.csv` will be generated in the same directory.

## 🧠 Example

```bash
Search on Wzzuff: python developer
```

Creates file: `python-developer.csv`

## 📁 Output Format

| Titles           | Company      | References                                    | Descriptions | Occupation | Area  |
| ---------------- | ------------ | --------------------------------------------- | ------------ | ---------- | ----- |
| Python Developer | Tech Company | [https://wuzzuf.net/](https://wuzzuf.net/)... | ...          | Full Time  | Cairo |

## 🛠️ Functions Overview

* `Search_on(name)` → builds the Wuzzuf search URL
* `number_of_Page(url)` → gets number of job pages
* `soup(num, url)` → scrapes all pages
* `Wzzuff(name)` → main function, saves results to CSV

## ✅ Notes

* Make sure you have an active internet connection.
* This script is tailored to Wuzzuf’s current HTML structure — changes to the site may require updates.
