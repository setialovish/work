import pandas as pd
import time
address_to_Check = pd.read_csv(r'addresses_for_task.csv')
splitted_Address = address_to_Check['Address'].str.split(',')
df  = pd.read_csv(r'Townlands__OSi_National_Placenames_Gazetteer.csv', usecols=(0,1,3,12))
df = df.drop_duplicates(subset=['County','English_Name'])
time_start = time.time()
for i in range(0,len(splitted_Address)):
    #print (splitted_Address[i])
    for j in range(0,len(splitted_Address[i])-1):
        #print (splitted_Address[i][j].upper(),str(splitted_Address[i][-1]).upper())
        x = df[(df.English_Name == str(splitted_Address[i][j]).upper().strip()) & (df.County == str(splitted_Address[i][-1]).upper().strip())]
        #print (x)
        if len(x):
            splitted_Address[i].append(x.iloc[0]['X'])
            splitted_Address[i].append(x.iloc[0]['Y'])
            break
time_end = time.time()
print("Time taken:",time_end - time_start)
splitted_Address.to_csv(r'output1.csv',)
