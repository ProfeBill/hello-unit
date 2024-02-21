# Interfaz de Usuario tipo consola para la funcionalidad de calcular la cuota de tarjeta de credito
import PaymentLogic

#  Obtener los datos de entrada
purchase_amount = float( input( "Ingrese el valor la compra: ") )
num_payments = int( input( "Ingrese el numero de cuotas: ") )
interest_rate = float( input( "Ingrese la tasa de interés: ") ) / 100

#  Realizar el proceso
payment = PaymentLogic.calcPayment( purchase_amount, interest_rate, num_payments )

# Mostrar los datos de salida
print( f"El valor de la cuota es: {payment}" )