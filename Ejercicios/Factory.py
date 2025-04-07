# Ejercicio1:Estamos trabajando en una aplicación de administración de vehículos de una concesionaria multinacional. 
# Tienes diferentes tipos de vehículos: automóviles, camiones y motocicletas, y necesitas crear instancias de estos objetos en diferentes partes de tu código.

class Vehiculo:

    def __init__(self, tipo):

        self.tipo = tipo


    def arrancar(self):

        print(f"Arrancando el vehículo de tipo {self.tipo}")


    def detener(self):

        print(f"Deteniendo el vehículo de tipo {self.tipo}")


class Automovil(Vehiculo):

    def __init__(self):

        super().__init__('Automóvil')


class Camion(Vehiculo):

    def __init__(self):

        super().__init__('Camión')


class Motocicleta(Vehiculo):

    def __init__(self):

        super().__init__('Motocicleta')
        
# Ahora, creamos la clase Factory que se encargará de crear instancias de los diferentes tipos de vehículos:

class FabricaVehiculos:

    @staticmethod

    def crear_vehiculo(tipo):

        if tipo == 'automovil':

            return Automovil()

        elif tipo == 'camion':

            return Camion()

        elif tipo == 'motocicleta':

            return Motocicleta()

        else:

            raise ValueError('Tipo de vehículo no válido')
        
# utilizar la fábrica para crear instancias de vehículos:

mi_vehiculo = FabricaVehiculos.crear_vehiculo('automovil')

mi_vehiculo.arrancar()  # Output: Arrancando el vehículo de tipo Automóvil


otro_vehiculo = FabricaVehiculos.crear_vehiculo('camion')

otro_vehiculo.detener()  # Output: Deteniendo el vehículo de tipo Camión