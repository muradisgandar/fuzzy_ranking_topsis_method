import pandas as pd
import numpy as np
import xlsxwriter
data = pd.read_excel (r'epldata_final.xlsx')
age = data['age'].values.tolist()
market_value = data['market_value'].values.tolist()
page_views = data['page_views'].values.tolist()
fpl_points = data['fpl_points'].values.tolist()
name = data['name']
club = data['club']
name = np.array(name)
n = len(age)
age = np.array(age)
market_value = np.array(market_value)
page_views = np.array(page_views)
fpl_points = np.array(fpl_points)
weights = [0.2, 0.3, 0.1, 0.4]
age = (np.max(age)-age)/(np.max(age)-np.min(age))
market_value = (np.max(market_value)-market_value)/(np.max(market_value)-np.min(market_value))
page_views = (page_views - np.min(page_views))/(np.max(page_views)-np.min(page_views))
fpl_points = (fpl_points - np.min(fpl_points))/(np.max(fpl_points)-np.min(fpl_points))
age = age*weights[0]
market_value = market_value*weights[1]
page_views = page_views*weights[2]
fpl_points = fpl_points*weights[3]
a_plus = np.zeros(4)
a_minus = np.zeros(4)
a_plus[0] = np.min(age)
a_plus[1] = np.min(market_value)
a_plus[2] = np.max(page_views)
a_plus[3] = np.max(fpl_points)
a_minus[0] = np.max(age)
a_minus[1] = np.max(market_value)
a_minus[2] = np.min(page_views)
a_minus[3] = np.min(fpl_points)
d_plus = np.sqrt((age - a_plus[0])**2+(market_value - a_plus[1])**2+(page_views-a_plus[2])**2+(fpl_points - a_plus[3])**2)
d_minus = np.sqrt((age - a_minus[0])**2+(market_value - a_minus[1])**2+(page_views-a_minus[2])**2+(fpl_points - a_minus[3])**2)
ranking = d_minus/(d_plus+d_minus)

workbook = xlsxwriter.Workbook('results1.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write('B1', 'Footballer_club')
worksheet.write('A1', 'Footballer_name')
for i in range(n):
    worksheet.write(i+1, 0, name[i])
    worksheet.write(i+1, 1, ranking[i])
workbook.close()
