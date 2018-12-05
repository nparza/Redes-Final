
'''
CARGAR FILAS Y COLUMNAS DE LA MATRIZ ESPARSA BIPARTIRA
OBS: en el csv, la primera línea corresponde a los ínidices de los usuarios
y la segunda a los índices de los repos, dependiendo la representación que 
quiero hacer, se puede elegir cuáles representan filas y cuáles columnas
'''

entrada = open('bipartite.csv')

lines = []

for line in entrada:
    lines.append(line.split(','))
    
for line in lines:
    for i in range(1,len(line)):
        line[i] = int(line[i])

fila = lines[1][1:]
col = lines[0][1:]

del line
del lines
del entrada
del i

#%%

'''
CARGAR FILAS Y COLUMNAS DE LA MATRIZ ESPARSA DE PESOS 
'''

entrada = open('weights-user.csv')

lines = []

for line in entrada:
    lines.append(line.split(','))

for i in range(1,len(lines[0])):
    lines[0][i] = float(lines[0][i])
    
for line in lines[1:]:
    for i in range(1,len(line)):
        line[i] = int(line[i])

upeso = lines[0][1:]
ufila = lines[1][1:]
ucol = lines[2][1:]

del line
del lines
del entrada
del i

#%%

'''
CARGAR MEMBERSHIP DEL CLUSTERING
'''

entrada = open('cluster-infomap-repos-directed.csv')

for line in entrada:
    line = line.split(',')
for i in range(len(line)):
    line[i] = int(line[i])
    
membership = line   

del i, entrada, line


