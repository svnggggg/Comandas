class Comanda:

  def __init__(self, descripcion, ApCliente, monto, envio):
    self.descripcion = descripcion
    self.ApCliente = ApCliente
    self.monto = monto
    self.envio = envio

  def aplicarDescuento(self):
    if self.monto >= 5000:
      if self.envio == False:
        self.monto = self.monto - self.monto * 0.1
      else:
        self.monto = self.monto - self.monto * 0.05