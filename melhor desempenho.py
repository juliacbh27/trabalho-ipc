#encoding: utf-8
file = open('c:/Users/Julia Julia Julia/Documents/Brasileiro 2024 (Srie A) - Dataset - Final.txt','r', encoding='utf-8')
manadante_vitoria = dict()
visitante_vitoria = dict()
gols_feitos = dict()
for i in file:
    lista = i.split(',')
    gols = lista[3].split('-')
    gols_feitos[lista[2]] = gols_feitos.get(lista[2],0) + int(gols[0])
    gols_feitos[lista[4]] = gols_feitos.get(lista[4],0) + int(gols[1])
    if int(gols[0]) > int(gols[1]):
        manadante_vitoria[lista[2]] = manadante_vitoria.get(lista[2],0)+1
    elif int(gols[0]) < int(gols[1]):
        visitante_vitoria[lista[4]] = visitante_vitoria.get(lista[4],0)+1 
melhor_visitante_qtd= max(visitante_vitoria.values())
melhor_visitante  = max(visitante_vitoria, key=visitante_vitoria.get)
melhor_mandante_qtd= max(manadante_vitoria.values())
melhor_mandante  = max(manadante_vitoria, key=manadante_vitoria.get)
time_mais_gols = max(gols_feitos,key=gols_feitos.get)
time_mais_gols_qtd = max(gols_feitos.values())
print('O time com mais vitórias em casa é  ',melhor_mandante, 'com ',melhor_mandante_qtd, 'vitórias ')
print('O time com mais vitórias fora de  casa é ',melhor_visitante, 'com ',melhor_visitante_qtd, 'vitórias')
print('O time que mais fez gols é ',time_mais_gols,'tendo feito ',time_mais_gols_qtd,'gols')