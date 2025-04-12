stateDiagram-v2
    [*] --> Pendiente
    Pendiente --> Confirmada: Pago exitoso
    Confirmada --> Pagada: Procesar pago
    Pagada --> Modificada: Usuario modifica reserva
    Pagada --> Cancelada: Usuario cancela reserva
    Modificada --> Pagada: Confirmar cambios
    Cancelada --> [*]