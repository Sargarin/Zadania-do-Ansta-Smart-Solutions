from decimal import *


# Funkcja tworząca liste pośrednich kodów pocztowych pomiędzy podanymi przez nas kodami pocztowymi
def zad1_generator_kodów_pocztowych(startowy_kod, końcowy_kod):
    lista_kodów = []
    # Rozbicie string-ów(kodów) na poszczególne int-y w celui wykonywania operacji na nich
    x1 = int(startowy_kod.split("-")[0])
    x2 = int(startowy_kod.split("-")[1])
    y1 = int(końcowy_kod.split("-")[0])
    y2 = int(końcowy_kod.split("-")[1])
    # Start pętli dodające pośrednie kody pcoztowe do listy
    while (x1 <= y1 and x2 != y2):
        if (x1 != y1):
            for i in range(x2, 1000):
                lista_kodów.append(str(x1) + '-' + str(i))
        else:
            for i in range(x2, y2 + 1):
                lista_kodów.append(str(x1) + '-' + str(i))

        x2 = 0
        x1 += 1
    return lista_kodów


# Funkcja znajdująca brakujące elementy listy o długości n, zwracająca liste złożoną z tych elementów
def zad2_brakujące_elementy_listy(lista_wejsciowa, n_element):
    lista_testowa = []
    lista_wejsciowa.sort()
    # utworzenie pełnej listy
    for i in range(1, n_element + 1):
        lista_testowa.append(i)
    # Usunięcie elementów znajdujacych się w otrzymanej liście
    for i in range(0, len(lista_wejsciowa)):
        lista_testowa.remove(lista_wejsciowa[i])
    return lista_testowa


#Funckja wypełniająca liste podanymi wartościami typu decimal, ze skokiem 0.5
def zad3_generator_licz_ze_skokiem(x_poczatkowe, y_koncowe):
    lista_koncowa = []
    while (x_poczatkowe <= y_koncowe):
        d = Decimal(x_poczatkowe)
        lista_koncowa.append(d)
        x_poczatkowe += 0.5
    return lista_koncowa
