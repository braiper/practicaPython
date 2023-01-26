class automovil:
    def __init__ (self,modelo,marca,puertas):
        self.modelo=modelo
        self.marca=marca
        self.puertas=puertas
        print ('Mi auto es ', self.marca,', modelo ',self.modelo, ' y tiene ',self.puertas,' puertas')

    def camino (self,distancia):
        print('Tiene',distancia,' km recorridos')
    
    def material(self, tela):
        print ('La funda de mis asientos son de:', tela)
    def color(self, tonalidad):
        print('Mi auto es de color ',tonalidad, 'es el unico color de la marca ',self.marca)
peugeot = automovil(2012,'Peugeot',4)
peugeot.camino(350)
peugeot.material('cuerina')
peugeot.color('dorado')

audi = automovil(2020,'Audi',3)
audi.camino(750)
audi.material('tela')
audi.color('turquesa')