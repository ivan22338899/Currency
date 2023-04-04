#import csv
import pandas as pd
df = pd.read_csv(r'Currencies.csv')
# with open('Currencies.csv') as df:
    #reader = csv.DictReader(df)
    #for row in reader:
        #print(row)
Total = df['Price'].sum()    
n = len(df)
Total2 = Total/n
print(df.nsmallest(1, ['Price']))
print(df.nlargest(1, ['Price']))
print (Total2)
print (n)


print(n)