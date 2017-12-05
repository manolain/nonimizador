import json
import csv
import random

jsonfile = open('file.json', 'w')

with open('poblaciones.json') as data_file:    
    data = json.load(data_file)

provincia = random.choice(data.keys())

#print "Provincia: %s" % data[provincia]

poblacion = random.choice(data[provincia].keys())

print "Poblacion: %s" % data[provincia][poblacion]

