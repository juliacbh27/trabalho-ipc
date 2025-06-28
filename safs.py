#encoding: utf-8
file = open('c:/Users/Julia Julia Julia/Documents/Brasileiro 2024 (Srie A) - Dataset - Final.txt','r', encoding='utf-8')
SAFs = ('Botafogo (RJ)','Cruzeiro','Bahia','Atlético-MG','Cuiabá','Fortaleza','Atl Goianiense','Vasco da Gama')
gols_feitos = dict()
gols_sofridos = dict()
vitorias = dict()
derrotas = dict()
empates = dict()
pontos = dict()
for i in file:
    lista = i.split(',')
    gols = lista[3].split('-')
    gols_feitos[lista[2]] = gols_feitos.get(lista[2],0) + int(gols[0])
    gols_feitos[lista[4]] = gols_feitos.get(lista[4],0) + int(gols[1])
    gols_sofridos[lista[4]] = gols_sofridos.get(lista[4],0) + int(gols[0])
    gols_sofridos[lista[2]] = gols_sofridos.get(lista[2],0) + int(gols[1])
    if gols[0]>gols[1]:
        vitorias[lista[2]] = vitorias.get(lista[2],0)+1  
        derrotas[lista[4]] = derrotas.get(lista[4],0)+1  
    elif gols[0]<gols[1]:
        vitorias[lista[4]] = vitorias.get(lista[4],0)+1  
        derrotas[lista[2]] = derrotas.get(lista[2],0)+1  
    elif gols[0] == gols[1]:
        empates[lista[4]] = empates.get(lista[4],0)+1  
        empates[lista[2]] = empates.get(lista[2],0)+1 

gols_sofridos_saf = 0
gols_sofridos_outros = 0
gols_feitos_saf = 0
gols_feitos_outros = 0
vitorias_saf = 0
vitorias_outros = 0
derrotas_saf = 0
derrotas_outros = 0
for k,v in gols_feitos.items():
    if k in SAFs:
        gols_feitos_saf += int(v)
    else:
        gols_feitos_outros += int(v)
for a,b in gols_sofridos.items():
    if a in SAFs:
        gols_sofridos_saf += int(b)
    else:
        gols_sofridos_outros += int(b)
for c,d in vitorias.items():
    if c in SAFs:
        vitorias_saf += int(d)
    else:
        vitorias_outros += int(d)
for e,f in derrotas.items():
    if e in SAFs:
        derrotas_saf += int(f)
    else:
        derrotas_outros += int(f)
print('Gols feitos por times SAFs: ',gols_feitos_saf)
print('Gols sofridos por times SAF: ',gols_sofridos_saf)
print('Vitórias de times SAF: ', vitorias_saf)
print('Derrotas time SAF: ', derrotas_saf)
print('Gols feitos por times sem SAFs: ',gols_feitos_outros)
print('Gols sofridos por times sem SAF: ',gols_sofridos_outros)
print('Vitórias de times sem SAF: ', vitorias_outros)
print('Derrotas time sem SAF: ', derrotas_outros)