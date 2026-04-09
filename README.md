#  Customer Personality Analysis - Data Cleaning Project

##  Objective
To clean and preprocess a customer dataset and prepare it for analysis by handling missing values, correcting inconsistencies, and creating meaningful features.

---

##  Dataset
Customer Personality Analysis dataset from Kaggle.

---

##  Data Issues (Before Cleaning)
- Missing values present in the Income column  
- Duplicate records in the dataset  
- Inconsistent categorical values in Marital_Status  
- Date column not in proper datetime format  
- Raw data not suitable for direct analysis  

---

##  Data Cleaning Steps
- Handled missing values in the Income column using median  
- Removed duplicate records  
- Standardized categorical values (Marital_Status)  
- Converted date column to proper datetime format  

---

##  Feature Engineering
- Created **Age** from Year_Birth  
- Created **Total_Spending** from product-related columns  
- Created **Children** from Kidhome and Teenhome  

---

##  Key Insights
- Higher income customers tend to spend more  
- Wine and meat products have the highest spending  
- Campaign response rate is low  
- Customers show good online engagement  
- Complaint rate is very low  

---

##  Key Definitions
- **Data Cleaning**: The process of fixing or removing incorrect, incomplete, or inconsistent data  
- **Feature Engineering**: Creating new meaningful variables from existing data  
- **Missing Values**: Data points that are not recorded or unavailable  
- **Categorical Data**: Data that represents categories (e.g., marital status)  
- **Correlation**: A measure of how strongly two variables are related  

---

##  Outcome (After Cleaning)

The dataset was successfully cleaned and transformed into a structured, analysis-ready format. Key data quality issues such as missing values, duplicates, inconsistent categorical entries, and improper date formats were resolved.

For example, missing values in the **Income** column were filled using median imputation to maintain data consistency without skewing results. In the **Marital_Status** column, inconsistent values such as "Together", "Absurd", and "YOLO" were standardized into meaningful categories like "Married" and "Single".

The **Dt_Customer** column was converted into a proper datetime format, enabling time-based analysis. Additionally, new features were created to enhance the dataset:
- **Age** was derived from Year_Birth
- **Total_Spending** was calculated by combining all product-related spending columns
- **Children** was computed from Kidhome and Teenhome

After these transformations, the dataset became clean, consistent, and suitable for further analysis. For instance, it clearly showed that customers with higher income tend to have higher total spending, and that categories like wine and meat contribute the most to overall purchases.

Overall, the cleaned dataset is now reliable and ready for data analysis, visualization, or machine learning tasks.