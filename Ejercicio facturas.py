facturas = {}
op = '' #A P T
while op != 'T':
    if op == 'A':
        serie = input('Ingrese número de serie de la factura: ')
        importe = input('Ingrese el importe de la factura: ')
        facturas[serie] = importe
    if op == 'P':
        serie = input('¿Cuál es el número de serie de la factura a pagar? ')
        facturas.pop(serie,0)
    op = input('¿Deseas añadir una factura (A), pagarla (P) o terminarlo (T)? ')

print('Facturas pendientes de pago.')
for k,v in facturas.items():
    print(k,v)
