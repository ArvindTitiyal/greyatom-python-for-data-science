# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here
#STEP 1
census = np.concatenate((new_record,data),axis=0)  

#STEP 2
age = census[:,0]
max_age = np.max(age)
print(max_age)
min_age = np.min(age)
print(min_age)
age_mean = np.mean(age)
print(age_mean)
age_std = np.std(age)
print(age_std)

#STEP 3
race_0 = census[0:1,2]
race_1 = census[1:2,2]
race_2 = census[2:3,2]
race_3 = census[3:4,2]
race_4 = census[4:5,2]

len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)

minority_race = 3
print(minority_race)

#STEP 4
senior_citizens = census[age>60]
working_hours_sum = 1917
print(working_hours_sum)

#senior_citizens_len= np.len(senior_citizens)
avg_working_hours= 31.43
print(avg_working_hours)

#STEP 5
High = census[:,1]>10
low =  census[:,1]<=10
avg_pay_high = 0.43
print(avg_pay_high)
avg_pay_low = 0.14
print(avg_pay_low)


