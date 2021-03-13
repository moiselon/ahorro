print('*************')
print('bienvenido')
print('*************\n')

class cliente ():
    cedula = '001-12851662'
    tarjeta_de_credito = '400 134 567 9010'
    codigo_de_cliente = '2001'
    nombre = 'roberto luciano alcantara'
    direccion = 'calle 8 570 los alcarrizos americanos'
    fecha_de_nacimiento = '26/3/2001'
    estado_de_cuenta = 'aprobada'
    clientes_suspendido = ['ramon caceres', 'julior perez', 'guillermo matrinez' , 'ramona luciana perez' , 'moises nicolas mendez mejias']

cliente1 = cliente()

print('su cedula es: ', cliente1.cedula)
print('su tarjeta es: ',cliente1.tarjeta_de_credito)
print('su codigo de cliente es : ', cliente1.codigo_de_cliente)
print('su nombre es: ', cliente1.nombre)
print('su direccion es: ', cliente1.direccion)
print('su fecha de nacimiento es: ', cliente1.fecha_de_nacimiento)
print('su estado de cuenta esta ', cliente1.estado_de_cuenta)
print('los clientes que tienen sus cuentas bloqueda son:\n')

print(cliente1.clientes_suspendido)

print('fin, espero que le halla gustado.')
