#This code can be used as a template to plot CCL data vs Depth from any given raw data file
import pandas as pd 
import matplotlib.pyplot as plt 
df= pd.read_csv('15_9-F-5_Run1_10B.csv', low_memory = False) #'title of the file' 
a = df["TDEP"] #TDEP: Depth column in excel file 
b = df["CCLC"] #CCLC: CCL measurements in excel file 
c= [float(i) for i in a[3:-4]] 
d = [float(i) for i in b[3:-4]] 
plt.figure(figsize=(4,20)) 
plt.plot(d, c) #plot of CCL vs Depth 
plt.xlabel('CCL') 
plt.ylabel('Depth') 
plt.title('CCL') 
plt.xlim(min(d),max(d)) 
plt.ylim(max(c),min(c)) 
plt.show()
