# Ejemplo de sistema mejorado basado en reglas para detectar transacciones sospechosas

class SistemaDeReglasFraude:
    def __init__(self, monto_umbral=10000, paises_alto_riesgo=None, limite_destinatarios=3):
        if paises_alto_riesgo is None:
            paises_alto_riesgo = ["PaisA", "PaisB"]
        self.monto_umbral = monto_umbral
        self.paises_alto_riesgo = paises_alto_riesgo
        self.limite_destinatarios = limite_destinatarios

    def verificar_transaccion(self, transaccion):
        # Regla 1: Monto excede el umbral
        if transaccion["monto"] > self.monto_umbral:
            return "Sospechosa: El monto excede el umbral."
        
        # Regla 2: Transacción desde país de alto riesgo
        if transaccion["pais"] in self.paises_alto_riesgo:
            return "Sospechosa: Transacción desde país de alto riesgo."
        
        # Regla 3: Frecuencia de transacciones inusualmente alta
        if transaccion["frecuencia"] > 5:
            return "Sospechosa: Frecuencia de transacciones inusualmente alta."
        
        # Regla 4: Transacción en horario nocturno (ej. 12 AM a 5 AM)
        if 0 <= transaccion["hora"] <= 5:
            return "Sospechosa: Transacción realizada en horario nocturno."
        
        # Regla 5: Transacciones a múltiples destinatarios en corto tiempo
        if transaccion["num_destinatarios"] > self.limite_destinatarios:
            return "Sospechosa: Transacción realizada a múltiples destinatarios en corto tiempo."
        
        return "Transacción normal."

# # Ejemplo de transacción
# transaccion = {
#     "monto": 8500,
#     "pais": "PaisA",
#     "frecuencia": 1,
#     "hora": 2,
#     "num_destinatarios": 4
# }

# sistema_fraude = SistemaDeReglasFraude()
# resultado = sistema_fraude.verificar_transaccion(transaccion)
# print(resultado)  # Resultado: Sospechosa: Transacción realizada en horario nocturno.
