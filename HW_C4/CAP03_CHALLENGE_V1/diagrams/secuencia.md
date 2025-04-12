sequenceDiagram
    participant Usuario
    participant WebApp
    participant LoadBalancer
    participant BookingService
    participant AuthenticationService
    participant InventoryService
    participant PaymentService
    participant NotificationService

    Usuario ->> WebApp: Inicia búsqueda de habitaciones
    WebApp ->> LoadBalancer: Enviar solicitud de búsqueda
    LoadBalancer ->> BookingService: Redirigir solicitud de búsqueda
    BookingService ->> InventoryService: Consultar disponibilidad
    InventoryService -->> BookingService: Retornar disponibilidad
    BookingService -->> WebApp: Mostrar resultados al usuario

    Usuario ->> WebApp: Seleccionar habitación y proceder a reservar
    WebApp ->> LoadBalancer: Enviar solicitud de reserva
    LoadBalancer ->> BookingService: Redirigir solicitud de reserva
    BookingService ->> AuthenticationService: Validar usuario
    AuthenticationService -->> BookingService: Usuario autenticado
    BookingService ->> InventoryService: Bloquear habitación
    InventoryService -->> BookingService: Confirmación de bloqueo
    BookingService ->> PaymentService: Procesar pago
    PaymentService -->> BookingService: Confirmación de pago
    BookingService ->> NotificationService: Enviar notificación
    NotificationService -->> Usuario: Confirmación de reserva