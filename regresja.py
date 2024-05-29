import numpy as np
import pandas as pd

#  DATAFRAME

df = pd.DataFrame()
df['X'] = [1, 2, 3, 4, 5]
df['Y'] = [4, 6, 9, 11, 18]

#  ŚREDNIA I ODCHYLENIE

def srednia(tab):
    return sum(tab) / len(tab)

def odchylenie(tab, srednia):
    return np.sqrt(sum((x - srednia) ** 2 for x in tab) / (len(tab) - 1))


#  KORELACJA PEARSONA


pear = pd.DataFrame(df[:])
pear['y2'] = df['Y'] * df['Y']
pear['xy'] = df['X'] * df['Y']
pear['x2'] = df['X'] * df['X']



def wspPerarsona(x,y,y2,xy,x2):
    return (len(x) * sum(xy) - sum(x) * sum(y) ) / (np.sqrt((len(x) * sum(x2) - sum(x) ** 2) * (len(x) * sum(y2) - sum(y) ** 2)))


#  ZMIENNE

Mx = srednia(pear['X'])
My = srednia(pear['Y'])
Sx = odchylenie(pear['X'], srednia(pear['X']))
Sy = odchylenie(pear['Y'], srednia(pear['Y']))
r = wspPerarsona(pear['X'], pear['Y'], pear['y2'], pear['xy'], pear['x2'])
b = r * Sy /Sx
a = My - b * Mx



def predict(x, a, b):
    return b * x + a



df.loc[len(df)] = [7, np.NaN] 
df.loc[len(df)] = [8, np.NaN]
df.at[5, 'Y'] = predict(df['X'][5], a, b)
df.at[6, 'Y'] = predict(df['X'][6], a, b)

print('PODSUMOWANIE')
print(f'Mx = {Mx}\n My = {My}\n Sx = {Sx}\n Sy = {Sy}\n Współczynnik Pearsona = {r}\n Przewidywana wartość y dla x = 7: {df["Y"][5]}\n Przewidywana wartość y dla x = 8: {df["Y"][6]}')

print('\nKońcowy zbiór danych')
print(df)



