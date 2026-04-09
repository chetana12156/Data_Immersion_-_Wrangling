import pandas as pd


df = pd.read_csv("data\\raw\\marketing_campaign.csv", sep='\t')

df['Income'].fillna(df['Income'].median(), inplace=True)

df.drop_duplicates(inplace=True)


df['Marital_Status'] = df['Marital_Status'].replace({
    'Together': 'Married',
    'Absurd': 'Single',
    'YOLO': 'Single',
    'Divorced': 'Single',
    'Widow': 'Single'
})


df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'], dayfirst=True)


df['Age'] = 2026 - df['Year_Birth']

df['Total_Spending'] = df[['MntWines','MntFruits','MntMeatProducts',
                          'MntFishProducts','MntSweetProducts','MntGoldProds']].sum(axis=1)

df['Children'] = df['Kidhome'] + df['Teenhome']


df.drop(['ID'], axis=1, inplace=True)


df.to_csv("data\\cleaned\\cleaned_data.csv", index=False)
print("Data cleaning completed successfully!")

#Insights


# 1. Average spending by category (to see top products)
avg_spending = df[['MntWines','MntFruits','MntMeatProducts',
                   'MntFishProducts','MntSweetProducts','MntGoldProds']].mean()

print("\nTop Spending Categories:\n", avg_spending.sort_values(ascending=False))


# 2. Income vs Total Spending correlation
# Helps understand if higher income → higher spending
corr = df[['Income','Total_Spending']].corr()

print("\nIncome vs Spending Correlation:\n", corr)


# 3. Campaign response rate (% of customers who responded)
response_rate = df['Response'].value_counts(normalize=True) * 100

print("\nCampaign Response (%):\n", response_rate)


# 4. Web activity (engagement level)
web_activity = df[['NumWebPurchases','NumWebVisitsMonth']].mean()

print("\nAverage Web Activity:\n", web_activity)


# 5. Complaint rate
complaints = df['Complain'].value_counts(normalize=True) * 100

print("\nComplaint Rate (%):\n", complaints)