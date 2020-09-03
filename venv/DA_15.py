import pandas as pd
import xlrd
import numpy as np
import matplotlib.pyplot as plt
pd.set_option('display.max_columns',18) # limit col
pd.set_option('display.max_rows',361) # limit row
cols = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18] # colums

dfs = pd.read_excel('IMVA.xlsx' , sheet_name = "IMVA" , usecols=cols)

class display:
 dfs.iloc[240:360 , 0:19] # call out the data

sum = dfs.iloc[240:360 , 1:19].sum(axis=0) # caculate the total and display
top = dfs.iloc[240:360 , 1:19].sum(axis=0).nlargest(3) #  top 3 most visted country

print(display) #print data
print(sum)   #print the sum
print(top)  # print the top
range = (dfs.iloc[240:361, :18].sum(axis=0))# range for graph
ax = range [[ ' Indonesia ', ' Japan ',  ' China ',' Malaysia ', ' India ' ]].plot(kind='bar', title = "Top 5 most visted country", figsize=(10, 10), legend=True, fontsize=10)
plt.show();#display graph
#number 1 indoneisa number 2 japan number 3 china
ax = range [[' Indonesia ', ' Japan ',  ' China ']].plot(kind='bar', title = "Top 3 Countries", figsize=(10, 10), legend=True, fontsize=10)
plt.savefig("")



