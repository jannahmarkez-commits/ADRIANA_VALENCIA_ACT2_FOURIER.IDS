import numpy as np
import matplotlib

# Configurar un backend no interactivo para evitar advertencias en entornos web
matplotlib.use('Agg') 
import matplotlib.pyplot as plt


# 1. CONFIGURACIÓN DE PARÁMETROS GENERALES

Fs = 1000          # Frecuencia de muestreo (1000 muestras por segundo)
T = 1.0 / Fs       # Período de muestreo
t = np.linspace(-1, 1, 2000) # Vector de tiempo de -1 a 1 segundo


# 2. CREACIÓN DE LAS SEÑALES ELEMENTALES

# A. Pulso Rectangular (Ancho de 0.4 segundos, centrado en 0)
pulso_rectangular = np.where(np.abs(t) <= 0.2, 1.0, 0.0)

# B. Función Escalón Unitario (Heaviside) - Activa en t >= 0
funcion_escalon = np.where(t >= 0, 1.0, 0.0)

# C. Función Senoidal (Frecuencia de 5 Hz)
frecuencia_seno = 5 
funcion_senoidal = np.sin(2 * np.pi * frecuencia_seno * t)


# 3. VISUALIZACIÓN DE LAS SEÑALES EN EL DOMINIO DEL TIEMPO

plt.figure(figsize=(10, 8))

# Gráfica del Pulso Rectangular
plt.subplot(3, 1, 1)
plt.plot(t, pulso_rectangular, 'b-', linewidth=2)
plt.title('1. Pulso Rectangular en el Dominio del Tiempo')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.grid(True)
plt.ylim(-0.2, 1.2)

# Gráfica de la Función Escalón
plt.subplot(3, 1, 2)
plt.plot(t, funcion_escalon, 'r-', linewidth=2)
plt.title('2. Función Escalón Unitario en el Dominio del Tiempo')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.grid(True)
plt.ylim(-0.2, 1.2)

# Gráfica de la Función Senoidal
plt.subplot(3, 1, 3)
plt.plot(t, funcion_senoidal, 'g-', linewidth=2)
plt.title(f'3. Función Senoidal en el Dominio del Tiempo ({frecuencia_seno} Hz)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.grid(True)
plt.ylim(-1.2, 1.2)

# Ajustar diseño automáticamente
plt.tight_layout()


# 4. GUARDAR EL RESULTADO

# Guardamos la imagen en el espacio de trabajo en lugar de usar plt.show()
plt.savefig('mis_senales_tiempo.png', dpi=300)
print("¡Código ejecutado con éxito! Revisa tus archivos, se ha generado 'mis_senales_tiempo.png'.")