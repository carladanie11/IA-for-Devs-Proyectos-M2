import sqlite3

# Conectar a la base de datos de reservas usando una ruta absoluta
conn = sqlite3.connect('/home/carla/Documentos/IAforDevs/IA-for-Devs-Proyectos-M2/IA-for-Devs-Proyectos-M2/reservacion-habitaciones/backend/database/booking_db.sqlite')
cursor = conn.cursor()

# Crear una consulta
cursor.execute("SELECT * FROM reservas")
reservas = cursor.fetchall()

# Cerrar la conexión
conn.close()

print(reservas)