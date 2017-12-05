import json

def abrir_csv(link):
    	file_in = open(link)
    	archivo = file_in.readlines()
    	file_in.close()

	return archivo

def insert(cur, list, value):
    if len(list) == 1:
        cur[list[0]] = value
        return
    if not cur.has_key(list[0]):
        cur[list[0]] = {}
    insert(cur[list[0]], list[1:], value)

csvfile = abrir_csv('poblaciones.csv')
jsonfile = open('poblacionesauto.json', 'w')

provincia = ''
poblacion = ''
cp = ''

data = {}

contador = 0
contador_p = 1
miClave = ''

for l in csvfile:
	linea = l.split(';')
	
	if ( linea[0] != 'PROVINCIA' ):
		if ( data.get(linea[0]) == None ):
			contador_p = 1

		keyList1 = [linea[0], str(contador_p), 'poblacion']
		keyList2 = [linea[0], str(contador_p), 'cp']

		insert(data, keyList1, linea[1])
		insert(data, keyList2, linea[2].replace("\n", " "))

	contador += 1
	contador_p += 1

data_string = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))

jsonfile.write(data_string)