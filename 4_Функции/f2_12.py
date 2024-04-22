# -*- coding: utf-8 -*-
path = "D:\APK_data/hoz_sub1.csv"
days_file = open(path,'r')
days = days_file.read()
new_path = "D:\APK_data/hoz_sub1.csv"
new_days = open(new_path,'w')
title = 'Days of the Week\n'
new_days.write(title)
print(title)
new_days.write(days)
print(days)
days_file.close()
new_days.close()