import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Create a sample customer churn dataset
data = {
    'CustomerID': range(1, 11),
    'Age': [25, 30, 45, 35, np.nan, 50, 28, 40, 60, 32],
    'MonthlyCharges': [50, 60, 80, 70, 90, np.nan, 55, 85, 95, 65],
    'Tenure': [2, 12, 24, 6, 1, 36, 8, 18, 48, 10],
    'Churn': ['Yes', 'No', 'No', 'Yes', 'Yes',
              'No', 'No', 'Yes', 'No', 'No']
}

df = pd.DataFrame(data)

# Display original data
print("Original Dataset:")
print(df)

# 1. Clean the data
df.drop_duplicates(inplace=True)

# 2. Handle missing values
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['MonthlyCharges'] = df['MonthlyCharges'].fillna(
    df['MonthlyCharges'].mean()
)

print("\nCleaned Dataset:")
print(df)

# 3. Generate summary statistics
print("\nSummary Statistics:")
print(df.describe())

# 4. Churn count
print("\nCustomer Churn Count:")
print(df['Churn'].value_counts())

# 5. Calculate average monthly charges by churn
print("\nAverage Monthly Charges by Churn:")
print(df.groupby('Churn')['MonthlyCharges'].mean())

# 6. Visualize churn distribution
sns.countplot(data=df, x='Churn')
plt.title("Customer Churn Distribution")
plt.show()

# 7. Visualize monthly charges by churn
sns.boxplot(data=df, x='Churn', y='MonthlyCharges')
plt.title("Monthly Charges vs Customer Churn")
plt.show()

# 8. Visualize correlation
numeric_df = df.select_dtypes(include=np.number)
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()