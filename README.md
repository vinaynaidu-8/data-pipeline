# Vehicle Sales Data Pipeline (End-to-End)

## 📌 Project Overview
This project demonstrates an end-to-end data engineering pipeline using real-world vehicle sales data. The objective is to clean raw data, store it in a relational database, and perform analytical queries to extract business insights.

---

## 🛠 Tech Stack
- Python (Pandas)
- SQL Server
- SQL Server Management Studio (SSMS)
- Git & GitHub

---

## 📂 Dataset
Source: Vehicle Sales CSV dataset  
Records: ~290,000 rows

---

## 🔄 Project Workflow
1. Raw CSV data ingestion
2. Data cleaning and transformation using Python
3. Feature engineering (car age calculation)
4. Export cleaned data
5. Import data into SQL Server
6. Run analytical SQL queries

---

## 🧹 Data Cleaning (Python)
- Removed duplicates
- Handled missing values
- Converted sale date to datetime
- Created `car_age` feature

📷 **Python Cleaning Output**  
![Python Cleaning](screenshots/python_cleaning_output.png)

---

## 🗄 Database Schema (SQL Server)
A relational table was designed to store cleaned data.

📷 **Table Preview in SSMS**  
![SSMS Table](screenshots/ssms_table_preview.png)

---

## 📊 Analytics Queries
- Total revenue analysis
- Brand-wise average selling price
- Top-performing states
- Vehicle depreciation trend

📷 **SQL Query Output**  
![SQL Output](screenshots/sql_query_output.png)

---

## 📈 Key Insights
- Premium brands command higher average prices
- Certain states contribute significantly to total sales
- Vehicle price decreases with age

---

## 🎯 Learning Outcomes
- Practical experience with data pipelines
- SQL analytics on large datasets
- Data quality and schema design
- Real-world data engineering workflow

---

## 🚀 Future Improvements
- Automate pipeline using scheduled jobs
- Add cloud storage (AWS S3)
- Create dashboards using Power BI
