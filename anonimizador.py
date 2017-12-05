# -*- coding: utf-8 -*-
import model, random
import nombres
import apellidos
import calles
import empresas

nombres_generados   = []
contactos_generados = []
razones_sociales    = []
nif_generados       = []
tipos_cliente       = [u'empresa', u'individual', u'individual', u'individual']

def get_tipo_cliente():
    tipo_cliente = random.choice(tipos_cliente)
        
    return tipo_cliente

def get_nuevo_nombre():
    global nombres_generados
    nnombre = ''
    while ( nnombre=='' or nnombre in nombres_generados):
        nnombre = random.choice(apellidos.apellidos) + " " + random.choice(apellidos.apellidos) + ", " + random.choice(nombres.nombres)
        
    nombres_generados.append(nnombre)
    return nnombre

def get_nuevo_contacto():
    global contactos_generados
    ncontacto = ''
    while ( ncontacto=='' or ncontacto in contactos_generados):
        ncontacto = random.choice(nombres.nombres) + " " + random.choice(apellidos.apellidos)
        
    contactos_generados.append(ncontacto)
    return ncontacto

def get_razon_social():
    global razones_sociales
    nrazon = ''
    while ( nrazon=='' or nrazon in razones_sociales):
        nrazon = random.choice(empresas.tipo_grupo) + " " + random.choice(apellidos.apellidos) + ", " + random.choice(empresas.tipo_sociedad)
        
    razones_sociales.append(nrazon)
    return nrazon

def get_nuevo_nif(tipo_cliente):
    global nif_generados
    nnif = ''
    while ( nnif=='' or nnif in nif_generados):
        if ( tipo_cliente == 'empresa'):
            nnif = u'B%08d' % random.randint(0,100000000)
        elif  ( tipo_cliente == 'individual'):
            nnif = u'%08dZ' % random.randint(0,100000000)
        
    nif_generados.append(nnif)
    return nnif

#model.setup_all()

contador = 1
max_clientes = 100
clientes = {}

while contador < max_clientes:
    
    print ""
    print "Cliente %d / %d " % (contador, max_clientes)
    
    tipo_cliente   = get_tipo_cliente()
    nuevo_nombre   = get_nuevo_nombre()
    nuevo_contacto = get_nuevo_contacto()
    nueva_razon    = get_razon_social()
    nuevo_nif      = get_nuevo_nif(tipo_cliente)
    
    cliente = {}

    if ( tipo_cliente == 'empresa' ):
        cliente['razon_social'] = nueva_razon
    elif ( tipo_cliente == 'individual' ):
        cliente['razon_social'] = nuevo_nombre

    cliente['nif']          = nuevo_nif

    cliente['direccion']    = u'' + random.choice(calles.calles)+ u", %d " % random.randint(1,99)
    cliente['poblacion']    = u"Miciudad %d" % contador
    cliente['provincia']    = u'Miprovincia %d' % contador
    cliente['cp']           = u'990%02d' % random.randint(0,99) 
    cliente['email']        = u''
    cliente['telefono']     = u''
    cliente['contacto']     = nuevo_contacto

    cliente['id_externo']   = u'%d' % contador
      
    if contador not in clientes.keys():
        clientes[contador]=[]
    clientes[contador].append(cliente)

    print u"Razón social:   %s     " % cliente['razon_social']
    print "Nif:             %s     " % cliente['nif']
    print u"Dirección:      %s     " % cliente['direccion']
    print u"Población:      %s     " % cliente['poblacion']
    print u"Provincia:      %s     " % cliente['provincia']
    print u"Código Postal:  %s     " % cliente['direccion']
    print u"Email:          %s     " % cliente['email']
    print u"Teléfono:       %s     " % cliente['telefono']
    print "Nombre contacto: %s     " % cliente['contacto']
    
    contador += 1