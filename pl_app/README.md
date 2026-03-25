\# Placement Eligibility Streamlit Application



\## Project Overview

This project is an end-to-end data-driven application designed to evaluate and filter students based on placement eligibility criteria. It integrates data generation, database management, SQL-based analytics, and an interactive Streamlit dashboard.



\## Objectives

\- Build a structured data pipeline from data generation to visualization

\- Store and manage data using a relational database

\- Implement SQL queries for analysis and insights

\- Develop an interactive UI for filtering and exploration



\## Project Workflow



\### Step 1: Data Generation

\- Synthetic data is generated using the Faker library

\- Four datasets are created:

&nbsp; - students

&nbsp; - programming

&nbsp; - soft\_skills

&nbsp; - placements

\- Data is stored in CSV format for validation and reuse



\### Step 2: Database Setup

\- SQLite database is used for storage

\- Tables are created using SQL schema definitions

\- Relationships are maintained using foreign keys (student\_id)



\### Step 3: Data Insertion

\- CSV files are loaded into the database using Pandas

\- Bulk insertion is handled using the to\_sql() function



\### Step 4: SQL Queries and Insights

\- Multiple SQL queries are implemented to extract insights:

&nbsp; - Top students based on performance

&nbsp; - Average programming performance per batch

&nbsp; - Soft skills distribution

&nbsp; - Placement status analysis

&nbsp; - High package students

\- Queries use JOIN, WHERE, GROUP BY, ORDER BY, and aggregation functions



\### Step 5: Streamlit Application

\- Interactive dashboard built using Streamlit

\- Features include:

&nbsp; - Sidebar filters for eligibility criteria

&nbsp; - Dynamic SQL query execution

&nbsp; - Display of filtered student data

&nbsp; - Buttons to view analytical insights



\## Database Schema



Tables:

\- students

\- programming

\- soft\_skills

\- placements



All tables are connected using student\_id as a foreign key.



\## Technologies Used

\- Python

\- Pandas

\- SQLite

\- Streamlit

\- Faker

\- SQL



\## How to Run the Project



1\. Navigate to the project directory

2\. Generate data:

&nbsp;  python src/data\_generator.py



3\. Create database tables:

&nbsp;  python database/create\_tables.py



4\. Insert data:

&nbsp;  python database/insert\_data.py



5\. Run the application:

&nbsp;  python -m streamlit run app/app.py



6\. Run the queries:

&nbsp;  python -m src/queries.py



\## Key Learnings

\- Designing relational databases

\- Writing and optimizing SQL queries

\- Building interactive dashboards using Streamlit

\- Implementing modular and reusable code using OOP

\- Managing end-to-end data workflows



\## Conclusion

This project demonstrates how to build a complete data application, starting from data generation to user-facing analytics. It highlights practical skills in data engineering, SQL, and frontend visualization.







