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
<img width="1917" height="1010" alt="Screenshot 2025-12-19 143200" src="https://github.com/user-attachments/assets/f2c643fc-d7da-41a0-bd9e-4dcd7c03a3f7" />


---

## 🗄 Database Schema (SQL Server)
A relational table was designed to store cleaned data.

📷 **Table Preview in SSMS**  
<img width="1914" height="988" alt="Screenshot 2025-12-19 144233" src="https://github.com/user-attachments/assets/3c88cb12-ff6d-4c95-8e3e-faefee080b36" />


---

## 📊 Analytics Queries
- Total revenue analysis
- Brand-wise average selling price
- Top-performing states
- Vehicle depreciation trend

📷 **SQL Query Output**  
<img width="1902" height="950" alt="Screenshot 2025-12-19 143513" src="https://github.com/user-attachments/assets/b2d44ada-4ef9-47f3-8804-c6930acfc31b" />
<img width="1919" height="990" alt="Screenshot 2025-12-19 143724" src="https://github.com/user-attachments/assets/6290ff5f-bd26-4f50-b507-877180b3ac9b" />
<img width="1911" height="981" alt="Screenshot 2025-12-19 143743" src="https://github.com/user-attachments/assets/eaf2664a-0021-4cb0-84e5-15b3b89e4462" />


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
