'''
CARGAR FILAS Y COLUMNAS DE LA MATRIZ ESPARSA BIPARTIRA
'''

entrada = open('bipartite.csv')

lines = []

for line in entrada:
    lines.append(line.split(','))
    
for line in lines:
    for i in range(1,len(line)):
        line[i] = int(line[i])

fila = lines[0][1:]
col = lines[1][1:]

del line
del lines
del entrada
del i

#%%

'''
CARGAR FILAS Y COLUMNAS DE LA MATRIZ ESPARSA DE PESOS 
'''

entrada = open('weights-repo.csv')

lines = []

for line in entrada:
    lines.append(line.split(','))

for i in range(1,len(lines[0])):
    lines[0][i] = float(lines[0][i])
    
for line in lines[1:]:
    for i in range(1,len(line)):
        line[i] = int(line[i])

peso = lines[0][1:]
ufila = lines[1][1:]
ucol = lines[2][1:]

del line
del lines
del entrada
del i
