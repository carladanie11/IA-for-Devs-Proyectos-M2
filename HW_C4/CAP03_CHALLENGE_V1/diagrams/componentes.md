classDiagram
    class WebApp {
        +buscarHabitaciones()
        +reservarHabitacion()
    }

    class MobileApp {
        +buscarHabitaciones()
        +reservarHabitacion()
    }

    class LoadBalancer {
        +redireccionarSolicitudes()
    }

    class BookingService {
        +gestionarReservas()
    }

    class AuthenticationService {
        +autenticarUsuario()
    }

    class InventoryService {
        +consultarDisponibilidad()
        +actualizarInventario()
    }

    class PaymentService {
        +procesarPagos()
    }

    class NotificationService {
        +enviarNotificaciones()
    }

    class ExternalAPIIntegrator {
        +sincronizarReservas()
    }

    WebApp --> LoadBalancer
    MobileApp --> LoadBalancer
    LoadBalancer --> BookingService
    LoadBalancer --> AuthenticationService
    LoadBalancer --> InventoryService
    BookingService --> PaymentService
    BookingService --> NotificationService
    BookingService --> ExternalAPIIntegrator
    AuthenticationService --> UserDatabase
    InventoryService --> InventoryDatabase
    PaymentService --> PaymentDatabase
    ExternalAPIIntegrator --> ExternalBookingPlatforms