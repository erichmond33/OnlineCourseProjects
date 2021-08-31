# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 22:50:00 2021

@author: eeric
"""


import csv

strs = []
strs2 = []
strs3 = []
strs4 = []
strs5 = []
strs6 = []
strs7 = []
strs8 = []
strs9 = []
strs10 = []


with open('data.csv', 'r') as csvFile:
        reader = csv.reader(csvFile, delimiter=',', quotechar='"')

        for row in reader:
            str = row[20]
            strs.append(str[0:2])
            
            str2 = row[21]
            strs2.append(str[0:2])
            
            str3 = row[22]
            strs3.append(str[0:2])
            
            str4 = row[23]
            strs4.append(str[0:2])
            
            str5 = row[24]
            strs5.append(str[0:2])
            
            str6 = row[25]
            strs6.append(str[0:2])
            
            str7 = row[26]
            strs7.append(str[0:2])
            
            str8 = row[27]
            strs8.append(str[0:2])
            
            str9 = row[28]
            strs9.append(str[0:2])
            
            str10 = row[29]
            strs10.append(str[0:2])
            
            
            
            #print(str)
            
        print(strs)
        
# Writing all the data into a csv
with open('data.csv', 'a', newline='') as csvfile:
    fieldnames = ["Website", "lat", "lng", "VS_code", "Spyder", "soffice", "jnotebook", "Ip", "Time", "Date",
    "Previous Website 1", "Previous Website 2", "Previous Website 3", "Previous Website 4", "Previous Website 5", "Previous Website 6", "Previous Website 7", "Previous Website 8", "Previous Website 9", "Previous Website 10", 
    "PW1 Time", "PW2 Time", "PW3 Time", "PW4 Time", "PW5 Time", "PW6 Time", "PW7 Time", "PW8 Time", "PW9 Time", "PW10 Time", "Full Url", "Hours (y)", "Date (y)", "PH1", "PH2", "PH3", "PH4", "PH5", "PH6", "PH7", "PH8", "PH9", "PH10"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    for i in range(1, 886):
        writer.writerow({'PH1' : strs[i], 'PH2' : strs2[i], 'PH3' : strs3[i], 'PH4' : strs4[i], 'PH5' : strs5[i], 'PH6' : strs6[i], 'PH7' : strs7[i], 'PH8' : strs8[i], 'PH9' : strs9[i], 'PH10' : strs10[i]})
