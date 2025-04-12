CREATE TABLE IF NOT EXISTS reservas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER NOT NULL,
    habitacion_id INTEGER NOT NULL,
    fecha_inicio TEXT NOT NULL,
    fecha_fin TEXT NOT NULL,
    estado TEXT NOT NULL
);