# sistema_frames.py

class PerfilUsuario:
    def __init__(self, nombre, edad, patron_gasto, ubicacion, historial_transacciones=None):
        if historial_transacciones is None:
            historial_transacciones = []
        self.nombre = nombre
        self.edad = edad
        self.patron_gasto = patron_gasto
        self.ubicacion = ubicacion
        self.historial_transacciones = historial_transacciones  # lista de montos o frecuencias de gasto

    def agregar_transaccion(self, monto):
        self.historial_transacciones.append(monto)


class SistemaFraudeFrames:
    def __init__(self):
        self.perfiles = []

    def agregar_perfil(self, perfil):
        self.perfiles.append(perfil)

    def verificar_perfil_fraude(self, perfil):
        # Regla 1: Usuario joven con gasto alto
        if perfil.edad < 25 and perfil.patron_gasto == "alto":
            return f"Sospechoso: {perfil.nombre} es joven con un gasto alto."

        # Regla 2: Usuario con patrón de gasto irregular en zona de alto riesgo
        if perfil.patron_gasto == "irregular" and perfil.ubicacion == "zona de alto riesgo":
            return f"Sospechoso: {perfil.nombre} tiene un patrón de gasto irregular en una zona de alto riesgo."

        # Regla 3: Usuario con historial de transacciones altas
        if any(monto > 10000 for monto in perfil.historial_transacciones):
            return f"Sospechoso: {perfil.nombre} tiene transacciones previas de alto monto."

        return f"Perfil de {perfil.nombre} es normal."

# # Ejemplo de uso
# if __name__ == "__main__":
#     # Crear perfiles de usuario (frames)
#     usuario1 = PerfilUsuario(nombre="Usuario1", edad=24, patron_gasto="alto", ubicacion="zona segura")
#     usuario2 = PerfilUsuario(nombre="Usuario2", edad=45, patron_gasto="irregular", ubicacion="zona de alto riesgo")

#     # Agregar transacciones a los usuarios
#     usuario1.agregar_transaccion(5000)
#     usuario2.agregar_transaccion(12000)

#     # Crear sistema de fraude basado en frames y agregar perfiles
#     sistema_frames = SistemaFraudeFrames()
#     sistema_frames.agregar_perfil(usuario1)
#     sistema_frames.agregar_perfil(usuario2)

#     # Verificar cada perfil para determinar si es sospechoso
#     for perfil in sistema_frames.perfiles:
#         print(sistema_frames.verificar_perfil_fraude(perfil))
