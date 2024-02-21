

def calcPayment(purchase_amount,interest_rate,num_payments):
    """
    Calcula la cuota a pagar por una compra con una tarjeta de crédito
    compra : Valor de la compra con la tarjeta
    tasa : Debe ser un porcentaje entre 1 y 100
    plazo : numero de cuotas a diferir la compra

    El resultado no esta redondeado
    """

    # Verificamos que la tasa de interes no se a mayor que 3.8% mensual
    if interest_rate > ( 3.8/100 ) :
       raise Exception( "ERROR: La tasa de interes supera el máximo" )

    i = interest_rate
    return (purchase_amount * i) / (1 - (1 + i) ** (-num_payments))

