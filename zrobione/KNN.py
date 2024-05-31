import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from collections import Counter

# Załadowanie zbioru danych iris
dane_iris = load_iris()
X = dane_iris.data
y = dane_iris.target

# Przekształcenie danych na DataFrame dla wygody
df = pd.DataFrame(data=np.c_[X, y], columns=dane_iris.feature_names + ['target'])

# Podział danych na zbiór treningowy i testowy (70% treningowy, 30% testowy)
X_trening, X_test, y_trening, y_test = train_test_split(df[dane_iris.feature_names], df['target'], test_size=0.3, random_state=42)

def dystans_euklidesowy(a, b):
    return np.sqrt(np.sum((a - b) ** 2))

def dystans_manhattan(a, b):
    return np.sum(np.abs(a - b))

def dystans_cosinusowy(a, b):
    return 1 - (np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))

def knn(liczba_sasiadow, X_trening, y_trening, X_test, metryka):
    przewidziane_klasy = []
    for _, punkt_testowy in X_test.iterrows():
        dystanse = []
        for _, punkt_treningowy in X_trening.iterrows():
            if metryka == 'euklidesowy':
                dystanse.append(dystans_euklidesowy(punkt_testowy.values, punkt_treningowy.values))
            elif metryka == 'manhattan':
                dystanse.append(dystans_manhattan(punkt_testowy.values, punkt_treningowy.values))
            elif metryka == 'cosinusowy':
                dystanse.append(dystans_cosinusowy(punkt_testowy.values, punkt_treningowy.values))
        indeksy_najblizszych = np.argsort(dystanse)[:liczba_sasiadow]
        najblizsze_klasy = y_trening.iloc[indeksy_najblizszych].values
        najczestsza_klasa = Counter(najblizsze_klasy).most_common(1)[0][0]
        przewidziane_klasy.append(najczestsza_klasa)
    return przewidziane_klasy

# Parametr liczba_sasiadow = 3, różne metryki
liczba_sasiadow = 3
metryki = ['euklidesowy', 'manhattan', 'cosinusowy']
wyniki = {}

for metryka in metryki:
    y_przewidziane = knn(liczba_sasiadow, X_trening, y_trening, X_test, metryka)
    dokladnosc = np.mean(y_przewidziane == y_test) * 100
    wyniki[metryka] = dokladnosc
    print(f'Metryka: {metryka}, Dokładność: {dokladnosc:.2f}%')

# Wyświetlenie wyników
print("Wyniki:", wyniki)
