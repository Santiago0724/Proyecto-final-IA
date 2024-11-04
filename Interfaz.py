# interfaz_fraude.py

import tkinter as tk
from tkinter import messagebox
from Reglas import SistemaDeReglasFraude
from frames import SistemaFraudeFrames, PerfilUsuario

def verificar_fraude():
    try:
        # Recoger datos de la transacción
        monto = float(entry_monto.get())
        pais = entry_pais.get()
        frecuencia = int(entry_frecuencia.get())
        hora = int(entry_hora.get())
        num_destinatarios = int(entry_destinatarios.get())
        
        transaccion = {
            "monto": monto,
            "pais": pais,
            "frecuencia": frecuencia,
            "hora": hora,
            "num_destinatarios": num_destinatarios
        }

        sistema_fraude = SistemaDeReglasFraude()
        resultado = sistema_fraude.verificar_transaccion(transaccion)
        messagebox.showinfo("Resultado Transacción", resultado)
    
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores válidos en todos los campos de la transacción.")

def verificar_perfil():
    try:
        # Recoger datos del perfil de usuario
        nombre = entry_nombre.get()
        edad = int(entry_edad.get())
        patron_gasto = entry_patron_gasto.get()
        ubicacion = entry_ubicacion.get()
        
        perfil = PerfilUsuario(nombre=nombre, edad=edad, patron_gasto=patron_gasto, ubicacion=ubicacion)

        # Sistema de frames para verificar el perfil de usuario
        sistema_frames = SistemaFraudeFrames()
        sistema_frames.agregar_perfil(perfil)
        resultado = sistema_frames.verificar_perfil_fraude(perfil)
        messagebox.showinfo("Resultado Perfil", resultado)
    
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores válidos en todos los campos del perfil de usuario.")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Sistema de Detección de Fraude Financiero")

# Sección para datos de la transacción
tk.Label(ventana, text="--- Datos de la Transacción ---").grid(row=0, column=0, columnspan=2)

tk.Label(ventana, text="Monto de la Transacción:").grid(row=1, column=0, padx=5, pady=5)
entry_monto = tk.Entry(ventana)
entry_monto.grid(row=1, column=1, padx=5, pady=5)

tk.Label(ventana, text="País de la Transacción:").grid(row=2, column=0, padx=5, pady=5)
entry_pais = tk.Entry(ventana)
entry_pais.grid(row=2, column=1, padx=5, pady=5)

tk.Label(ventana, text="Frecuencia de Transacciones:").grid(row=3, column=0, padx=5, pady=5)
entry_frecuencia = tk.Entry(ventana)
entry_frecuencia.grid(row=3, column=1, padx=5, pady=5)

tk.Label(ventana, text="Hora de la Transacción (0-23):").grid(row=4, column=0, padx=5, pady=5)
entry_hora = tk.Entry(ventana)
entry_hora.grid(row=4, column=1, padx=5, pady=5)

tk.Label(ventana, text="Número de Destinatarios:").grid(row=5, column=0, padx=5, pady=5)
entry_destinatarios = tk.Entry(ventana)
entry_destinatarios.grid(row=5, column=1, padx=5, pady=5)

# Botón para verificar la transacción
boton_verificar_transaccion = tk.Button(ventana, text="Verificar Transacción", command=verificar_fraude)
boton_verificar_transaccion.grid(row=6, column=0, columnspan=2, pady=10)

# Sección para datos del perfil de usuario
tk.Label(ventana, text="--- Datos del Perfil de Usuario ---").grid(row=7, column=0, columnspan=2)

tk.Label(ventana, text="Nombre:").grid(row=8, column=0, padx=5, pady=5)
entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=8, column=1, padx=5, pady=5)

tk.Label(ventana, text="Edad:").grid(row=9, column=0, padx=5, pady=5)
entry_edad = tk.Entry(ventana)
entry_edad.grid(row=9, column=1, padx=5, pady=5)

tk.Label(ventana, text="Patrón de Gasto (alto/irregular):").grid(row=10, column=0, padx=5, pady=5)
entry_patron_gasto = tk.Entry(ventana)
entry_patron_gasto.grid(row=10, column=1, padx=5, pady=5)

tk.Label(ventana, text="Ubicación (zona segura/alto riesgo):").grid(row=11, column=0, padx=5, pady=5)
entry_ubicacion = tk.Entry(ventana)
entry_ubicacion.grid(row=11, column=1, padx=5, pady=5)

# Botón para verificar el perfil de usuario
boton_verificar_perfil = tk.Button(ventana, text="Verificar Perfil de Usuario", command=verificar_perfil)
boton_verificar_perfil.grid(row=12, column=0, columnspan=2, pady=10)

# Ejecuta la ventana principal
ventana.mainloop()
