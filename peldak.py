from random import randint

randomszamok:list[int] = []
for x in range(10):
    randomszamok.append(randint(10, 99))

print(randomszamok)

# sorozatszámítás tétele (összegzés)
s:int = 0
for szam in randomszamok:
    s += szam
print(f'számok összege: {s}')

# szélsőérték meghatározás
maxi:int = 0
for i in range(1, len(randomszamok)):
    if randomszamok[i] > randomszamok[maxi]:
        maxi = i
print(f'legnagyobb elem indexe: {maxi}')
print(f'legnagyobb elem értéke: {randomszamok[maxi]}')

# lineáris keresés
keresett_elem:int = int(input('írj be egy számot: '))
for szam in randomszamok:
    if szam == keresett_elem:
        print('benne van a szám a listában')
        print(f'indexe: {randomszamok.index(szam)}')
        break
else: print(f'nincs benne a keresett szám a listában')

# megszámlálás tétele
c:int = 0
for szam in randomszamok:
    if szam % 2 == 0: c += 1
print(f'páros számok száma: {c}')

# linker "break" nélkül (ez volna a hivatalos):
keresett_elem:int = int(input('írj be egy számot: '))
i:int = 0
while i < len(randomszamok) and keresett_elem != randomszamok[i]:
    i += 1
if i < len(randomszamok):
    print('a keresett elem benne van a listában')
    print(f'indexe: {i}')
else: print('nincs benne a keresett elem')