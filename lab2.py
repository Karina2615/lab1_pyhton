# -*- coding: utf-8 -*-
import csv

file_path = "C:/Users/karin/OneDrive/Desktop/studying/python/Lab2/netflix_list.csv"

name = []
list = []
with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
    csv_reader = csv.reader(f, delimiter=',')
    name = next(csv_reader)  
    for row in csv_reader:
        list.append(row)
'''
rating = name.index("rating")
above_7_5_list = [x for x in list if x[rating] != "" and float(x[rating]) > 7.5]

for i in above_7_5_list:  
    print(f"{i[1]}, {i[rating]}")
'''

'''
first_5_column = [x[:5] for x in list]

for i in first_5_column:
    print(i)

'''

'''
def eng(lst):
    lang_index = name.index('language')
    for i in lst:
        if i[lang_index] == 'English':
            yield i

for row in eng(list):
    print(f"{row[1]} - {row[10]}")

'''

'''
def ended_2015(lst):
    end_index = name.index('endYear')
    for i in lst:
        if i[end_index] != '' and int(i[end_index]) >= 2015:
            yield i

for row in ended_2015(list):
    print(f"{row[1]} - {row[5]}")

'''
