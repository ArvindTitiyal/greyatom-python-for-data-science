# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)


#Code starts here
#Step 1
#To check all categorical values 
categorical_var = bank_data.select_dtypes(include = 'object')
print(categorical_var)
print(categorical_var.shape)

numerical_var = bank_data.select_dtypes(include = 'number')
print(numerical_var)
print(numerical_var.shape)

#Step 2
#From the dataframe bank_data, drop the column Loan_ID to create a new dataframe banks
banks = bank_data.drop('Loan_ID',axis=1)
print(banks.isnull().sum())

#Calculate mode for dataframe banks
bank_mode = banks.mode().iloc[0]

#Fill missing(NaN) values of banks with bank_mode and store the cleaned dataframe back in banks.
banks.fillna(bank_mode,inplace=True)
print(banks.isnull().sum())
print(banks.shape)

#Step 3
#Create pivot table with index as 'Gender', 'Married', 'Self_Employed' and values as 'LoanAmount', using mean aggregation
avg_loan_amount = pd.pivot_table(banks,index = ['Gender', 'Married', 'Self_Employed'],values = 'LoanAmount',aggfunc = np.mean)
 
print(avg_loan_amount)

#Step 4
loan_approved_se = banks.loc[(banks['Self_Employed']=='Yes') & (banks['Loan_Status']=='Y'), ['Loan_Status']].count()
print(loan_approved_se)

loan_approved_nse = banks.loc[(banks['Self_Employed']=='No') & (banks['Loan_Status']=='Y'), ['Loan_Status']].count()
print(loan_approved_nse[0])

Loan_Status = 614

percentage_se = (loan_approved_se * 100 / Loan_Status)
print(percentage_se)

percentage_nse = percentage_se = (loan_approved_nse * 100 / Loan_Status)
print(percentage_nse)

#Step 5
#Use "apply()" function to convert Loan_Amount_Term which is in months to a year.
loan_term = banks['Loan_Amount_Term'].apply(lambda x : int(x)/12)

#Find the number of applicants having loan amount term greater than or equal to 25 years.
big_loan_term = filter(lambda years : years >=25 , loan_term)

print(big_loan_term)

#Step 6
#Groupby the 'banks' dataframe by Loan_Status
loan_groupby = banks.groupby('Loan_Status')

#Subset 'loan_groupby' to include only ['ApplicantIncome', 'Credit_History']
loan_groupby = loan_groupby['ApplicantIncome', 'Credit_History']

mean_values = loan_groupby.agg(np.mean)

print(mean_values)



#code ends here




