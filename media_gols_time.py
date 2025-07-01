#encoding: utf-8
file = open('c:/Users/Julia Julia Julia/Documents/Brasileiro 2024 (Srie A) - Dataset - Final.txt','r', encoding='utf-8')
gols_feitos = dict()
media = dict()
for i in file:
    lista = i.split(',')
    gols = lista[3].split('-')
    gols_feitos[lista[2]] = gols_feitos.get(lista[2],0) + int(gols[0])
    gols_feitos[lista[4]] = gols_feitos.get(lista[4],0) + int(gols[1])
for time, gols in gols_feitos.items():
    media[time] = gols/38
print(media)