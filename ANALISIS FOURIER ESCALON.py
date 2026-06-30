import numpy as np
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt

# 1. CONFIGURACIÓN DE PARÁMETROS GENERALES

Fs = 1000          # Frecuencia de muestreo (1000 Hz)
T = 1.0 / Fs       # Período de muestreo
N = 2048           # Número de puntos
t = np.linspace(-1, 1, N) # Vector de tiempo


# 2. SEÑAL EN EL DOMINIO DEL TIEMPO (Función Escalón Unitario)

# El escalón vale 1 para t >= 0, y 0 en cualquier otro caso
senal_escalon = np.where(t >= 0, 1.0, 0.0)

# 3. CÁLCULO DE LA TRANSFORMADA DE FOURIER (FFT)

X_fourier = np.fft.fft(senal_escalon) / N
X_fourier_shiftheado = np.fft.fftshift(X_fourier)

frecuencias = np.fft.fftfreq(N, T)
frecuencias_shiftheadas = np.fft.fftshift(frecuencias)

magnitud = np.abs(X_fourier_shiftheado)
fase = np.angle(X_fourier_shiftheado)

=
# 4. VISUALIZACIÓN DE LOS RESULTADOS

plt.figure(figsize=(10, 10))

# Gráfica 1: Dominio del Tiempo
plt.subplot(3, 1, 1)
plt.plot(t, senal_escalon, 'r-', linewidth=2)
plt.title('1. Función Escalón Unitario (Dominio del Tiempo)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.grid(True)

# Gráfica 2: Espectro de Magnitud
plt.subplot(3, 1, 2)
plt.plot(frecuencias_shiftheadas, magnitud, 'b-', linewidth=2)
plt.title('2. Espectro de Magnitud del Escalón')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('|X(f)|')
plt.grid(True)
plt.xlim(-10, 10) # Hacemos zoom cerca de 0 Hz

# Gráfica 3: Espectro de Fase
plt.subplot(3, 1, 3)
fase_limpia = np.where(magnitud > 0.005, fase, 0.0)
plt.plot(frecuencias_shiftheadas, fase_limpia, 'g-', linewidth=2)
plt.title('3. Espectro de Fase del Escalón')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Fase (radianes)')
plt.grid(True)
plt.xlim(-10, 10)

plt.tight_layout()

# Guardar la imagen del análisis del escalón
plt.savefig('analisis_fourier_escalon.png', dpi=300)
print("¡Análisis del escalón completado! Archivo 'analisis_fourier_escalon.png' generado.")
