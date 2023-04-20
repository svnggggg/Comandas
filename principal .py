from comanda import Comanda
listaComandas = []

####


def cargar_pedido():
  #print("chorizo!!!")
  monto = 0
  descripcion = input('Ingrese la descripción de la comanda: \n')
  apellido = input('Pone el apellido: \n')

  while True:
    try:
      monto = abs(float(input('Ingrese el monto del pedido: \n')))
      break
    except:
      print('Pone un numero crack!')

  while True:
    envio = str(input('El pedido es para envío? (si o no): \n'))
    if envio.lower() == 'si' or envio.lower() == 'no':
      envio = True if envio.lower() == 'si' else False
      break
    else:
      print('Pone si o no y no me compliques la vida!')

  comanda = Comanda(descripcion, apellido, monto, envio)
  comanda.aplicarDescuento()
  listaComandas.append(comanda)


def modificar_pedido():
  apellido = input('Ingrese el apellido de la comanda que desea modificar: \n')
  monto = 0
  for comanda in listaComandas:
    if comanda.ApCliente == apellido:
      descripcion = input('Ingrese la nueva descripción de la comanda: \n')
      apellido = input('Pone el nuevo apellido: \n')

      while True:
        try:
          monto = abs(float(input('Ingrese el nuevo monto del pedido: \n')))
          break
        except:
          print('Pone un numero crack!')

      while True:
        envio = str(input('El pedido es para envío? (si o no): \n'))
        if envio.lower() == 'si' or envio.lower() == 'no':
          envio = 'si' if envio.lower() == 'si' else 'no'
          break
        else:
          print('Pone si o no y no me compliques la vida!')

      comanda.descripcion = descripcion
      comanda.envio = envio
      comanda.monto = monto
      comanda.ApCliente = apellido
      comanda.aplicarDescuento()

      print('-------------------------')
      print('Comanda modificada con éxito.')
      print('-------------------------')
      return
  print('No se encontró ningún pedido con ese apellido.')


def eliminar():
  apellido = input('Ingrese el apellido del pedido que desea eliminar: ')

  for i, value in enumerate(listaComandas):
    if (value.ApCliente == apellido):
      listaComandas.pop(i)
      print('-------------------------')
      print('Comanda eliminada con éxito.')
      print('-------------------------')
      break
  else:
    print('No se encontró ninguna comanda con ese apellido.')


def mostrar():
  for i, value in enumerate(listaComandas):
    print('-------------------------')
    print(f'Tu pedido es: {value.descripcion}')
    print(f'El apellido del pedido es: {value.ApCliente}')
    print(f'El monto del pedido es: ${value.monto}')
    print(f'Es con envio: {value.envio}')
    print('-------------------------')


def listar_pedidos_envio():
  noEnvio = False
  for value in listaComandas:
    if value.envio:
      print('-------------------------')
      print(f'Tu pedido es: {value.descripcion}')
      print('Tu pedido es con envio')
      print('-------------------------')
      noEnvio = True
  if not noEnvio:
    print('-------------------------')
    print('Ninguna comanda tiene envio.')
    print('-------------------------')


def ingresos():
  total = 0
  for comanda in listaComandas:
    total += comanda.monto
  print('-------------------------')
  print("El ingreso total es de: $", total)
  print('-------------------------')


while True:
  print('-------------------------')
  print('Seleccione una opción:')
  print('1. Carga de pedidos')
  print('2. Modificar un pedido')
  print('3. Eliminar un pedido')
  print('4. Listar pedidos')
  print('5. Listar pedidos por envío')
  print('6. Ingresos totales')
  print('7. Salir')
  print('-------------------------')

  opcion = (input('Ingrese una opción (1-7): '))

  if opcion == '1':
    cargar_pedido()
  elif opcion == '2':
    modificar_pedido()
  elif opcion == '3':
    eliminar()
  elif opcion == '4':
    mostrar()
  elif opcion == '5':
    listar_pedidos_envio()
  elif opcion == '6':
    ingresos()
  elif opcion == '7':
    print('Hasta el infinito y mas allá!')
    break
