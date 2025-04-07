```mermaid
classDiagram
    class Vehiculo {
        - tipo: str
        + __init__(tipo: str)
        + arrancar()
        + detener()
    }

    class Automovil {
        + __init__()
    }

    class Camion {
        + __init__()
    }

    class Motocicleta {
        + __init__()
    }

    class FabricaVehiculos {
        + crear_vehiculo(tipo: str) static
    }

    Vehiculo <|-- Automovil
    Vehiculo <|-- Camion
    Vehiculo <|-- Motocicleta
    FabricaVehiculos ..> Vehiculo : crea