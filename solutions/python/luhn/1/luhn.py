class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        # limpiamos la cadena de espacios
        num = self.card_num.replace(" ","")

        # comprobaciones
        # Tienen que tener al menos 2 digitos 
        if len(num) <= 1:
            return False
        # Solo deben de tener digitos
        if not num.isdigit():
            return False 

        # convertimos en una lista para poder iterar
        num = list(num)
        for i in range(len(num)):
            # convertimos cada elemento en int
            num[i] = int(num[i])

        # tomamos cada 2 elementos iniciando en el penultimo
        for i in range(-2,-len(num)-1,-2):
            # multiplicamos cada elemento por 2
            apoyo = num[i] * 2
            # si es mayor a 9 restamos 9 al resultado
            if apoyo > 9:
                apoyo -= 9
            # agregamos apoyo en el mismo indice
            num[i] = apoyo

        return sum(num) % 10 == 0
