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
