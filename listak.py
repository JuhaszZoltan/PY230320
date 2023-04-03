nevek:list[str] = [
    # 0        1        2
    'Éva', 'Bianka', 'Rita', 
    #  3          4        5
    'Renáta', 'Zsuzsa', 'Emese', 
    'Zsófi', 'Zsuzsa', 'Veronika', 
    'Margó', 'Szilvia', ]

ures_lista = []

szamok:list[int] = [36, 11, 42, 26, 121]

# list elemeinek liírása:
print(nevek)

# lista elemeinek bejárása:
for nev in nevek:
    print(f'a(z) {nev} egy női név')

# lista adott indexedik elemének elérése:
print(nevek[3])

# lista edott indexű helyen lévő elemének módosítása:
nevek[3] = 'Bernadett'
print(nevek)

# ún. out of range exception (aka. "hibaüzenet"), jelentése:
# olyan dologra hivatkozol, ami nem létezik
# nagyon gyakori hiba kezdőknél
# print(nevek[99])

lista_hossza:int = len(nevek)
print(f'lista hossza: {lista_hossza}')

print(nevek[len(nevek) - 1])

# listához elem hozzáadása:
uj_nev:str = 'Kata'
nevek.append(uj_nev)

nevek.append('Flóra')

print(nevek)

for i in range(len(nevek)):
    print(f'a lista {i + 1}. eleme: {nevek[i]}')

# NEM "ABC rendbe" teszi, hanem karakterkód szerint növekvőbe (ami csak "majdnem" ABC-rend)
# nevek.sort()
# print(nevek)

szamok.sort()
print(szamok)

# vár egy értéket ami olyan típusú, mint amilyen elemeket tartalmaz a lista, 
# ennek az ELSŐ előfordulását törli 
nevek.remove('Zsuzsa')
print(nevek)

# 'beszúr' elemet a listáva (<hová>, <mit>)
nevek.insert(0, 'Angelina')
print(nevek)

# megfordítja az elemek sorrendjét
nevek.reverse()
print(nevek)

# visszaadja a keresett elem indexét
margo_index:int = nevek.index('Margó')
print(margo_index)

# ha olyan elem indexét keresem, ami nincs is, exceptiont kapok:
# exc:int = nevek.index('Balázs')

