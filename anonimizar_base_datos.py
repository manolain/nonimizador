# -*- coding: utf-8 -*-
#pylint: skip-file
import model, random
import nombres #@UnresolvedImport
import apellidos #@UnresolvedImport
import calles #@UnresolvedImport

nombres_generados = []
nif_generados      = []

def get_nuevo_nombre():
    global nombres_generados
    nnombre = ''
    while ( nnombre=='' or nnombre in nombres_generados):
        nnombre = random.choice(apellidos.apellidos) + " " + random.choice(apellidos.apellidos) + ", " + random.choice(nombres.nombres)
        
    nombres_generados.append(nnombre)
    return nnombre

def get_nuevo_nif():
    global nif_generados
    nnif = ''
    while ( nnif=='' or nnif in nif_generados):
        nnif = u'B%08d' % random.randint(0,100000000)
        
    nif_generados.append(nnif)
    return nnif

model.setup_all()

instalaciones = model.Instalacion.query.all()#@UndefinedVariable

for instalacion in instalaciones:
    instalacion.razon_social = u'Instalacion de testing' 
    instalacion.nif          = u'B12345678'    
    instalacion.direccion                = u'Calle Gasolineras s/n'
    instalacion.poblacion                = u'Miciudad'
    instalacion.provincia                = u'Miprovincia'
    instalacion.cp                       = u'99999'
    instalacion.cim                      = u'12345678'
    
    instalacion.email_interno            = u'payway@localhost'
    instalacion.email_usuario            = u'payway@localhost'
    instalacion.email_password           = u'password'
    instalacion.email_notificacion       = u'payway@localhost'
    instalacion.smtp_server        #@UndefinedVariable      = u'localhost'
    instalacion.email_auxiliar1          = u''
    instalacion.email_auxiliar2          = u''
    instalacion.email_auxiliar3          = u''
    instalacion.email_auxiliar4          = u''
    
    
usuarios = model.UsuarioWeb.query.all()#@UndefinedVariable

for usuario in usuarios:
    usuario.password=u'5ebf9b249658a46a5d3ccf8f2c9c95bb'
    
distribuidores = model.Distribuidor.query.all()#@UndefinedVariable

for distribuidor in distribuidores:
    distribuidor.nombre = u'Distribuidor %d' % distribuidor.id# -*- coding: utf-8 -*-d
    distribuidor.razon_social = u'Distribuidor %d SL' % distribuidor.id
    distribuidor.nif = u'B1234%04d' % distribuidor.id    
    distribuidor.cae = u'ES000%04d' % distribuidor.id
    distribuidor.direccion                = u'Calle Distribuidor %d s/n' % distribuidor.id
    distribuidor.poblacion                = u'Miciudad'
    distribuidor.provincia                = u'Miprovincia'
    distribuidor.cp                       = u'99999'
    distribuidor.email                    = u''
    distribuidor.telefono                 = u''
    distribuidor.contacto                 = u''
    

clientes = model.Cliente.query.all()#@UndefinedVariable

contador = 1
max_clientes = len(clientes)

for cliente in clientes:
    print "Cliente %d / %d " % (contador, max_clientes)
    nuevo_nombre = get_nuevo_nombre()
    nuevo_nif    = get_nuevo_nif()
    viejo_nif    = cliente.nif
    
    
    cliente.razon_social = nuevo_nombre
    cliente.nif          = nuevo_nif
    
    cliente.direccion    = u'' + random.choice(calles.calles)+ u", %d " % random.randint(1,99)
    cliente.poblacion    = u"Miciudad %d" % cliente.id
    cliente.provincia    = u'Miprovincia %d' % cliente.id
    cliente.cp           = u'990%02d' % random.randint(0,99) 
    cliente.email        = u''
    
    cliente.telefono     = u''
    cliente.contacto     = u''
                 
    cliente.id_externo   = u'%d' % contador
    
    contador += 1
    
    model.session.commit()#@UndefinedVariable
    
    identificaciones = model.Identificacion.query.filter(model.Identificacion.cliente == cliente).all()#@UndefinedVariable
    
    for identificacion in identificaciones:
        identificacion.descripcion = u'Tarjeta %d de Cliente %d' %(identificacion.id, cliente.id)
        
    model.session.commit()#@UndefinedVariable
        
        
    facturas = model.Factura.query.filter(model.Factura.nif==viejo_nif).all()#@UndefinedVariable
    
    for factura in facturas:
              
        factura.razon_social = cliente.razon_social
        factura.nif          = cliente.nif
        factura.direccion    = cliente.direccion 
        factura.poblacion    = cliente.poblacion
        factura.provincia    = cliente.provincia
        factura.cp           = cliente.cp   
        factura.id_externo   = cliente.id_externo
        
    model.session.commit()#@UndefinedVariable    

    albaranes = model.Albaran.query.filter(model.Albaran.nif==viejo_nif).all()#@UndefinedVariable
    model.session.commit()#@UndefinedVariable
    for albaran in albaranes:
              
        albaran.razon_social = cliente.razon_social
        albaran.nif          = cliente.nif
        albaran.direccion    = cliente.direccion 
        albaran.poblacion    = cliente.poblacion
        albaran.provincia    = cliente.provincia
        albaran.cp           = cliente.cp    
        albaran.id_externo   = cliente.id_externo
        
    model.session.commit()#@UndefinedVariable   
        
op_bancarias = model.OperacionBancaria.query.all()#@UndefinedVariable

contador = 0
max_op_bank = len(op_bancarias)
for op_bancaria in op_bancarias:
    if contador%1000:
        print "Op bank %d / %d" % (contador, max_op_bank)
    op_bancaria.bn_titular = u''
    op_bancaria.bn_banco   = u'MiBanK'
    contador += 1
    
model.session.commit()#@UndefinedVariable
    
descargas = model.Descarga.query.all()#@UndefinedVariable

for descarga in descargas:
    descarga.documento = ''
    
grupos = model.GrupoCliente.query.all()#@UndefinedVariable

for grupo in grupos:
    grupo.nombre = u"Grupo %d" % grupo.id 

descuentos = model.Descuento.query.all()#@UndefinedVariable

for descuento in descuentos:
    descuento.descripcion = u"Descuento %d de %0.2f" % (descuento.id, descuento.valor)
    
    
tipos = model.TipoFormaPagoEfectivo.query.all()#@UndefinedVariable

for tipo in tipos:
    tipo.nombre = u'Tipo %d' % (tipo.id)
    
mtos = model.MovimientoCaja.query.all()#@UndefinedVariable

for mto in mtos:
    mto.nota = u''
    
drapidos = model.DescuentoRapido.query.all()#@UndefinedVariable

for drapido in drapidos:
    drapido.descripcion = u'Descuento rápido %d ' % (drapido.id)

model.session.commit()#@UndefinedVariable
