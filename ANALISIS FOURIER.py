import numpy as np
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt


# 1. CONFIGURACIÓN DE PARÁMETROS GENERALES

Fs = 1000          # Frecuencia de muestreo (1000 Hz)
T = 1.0 / Fs       # Período de muestreo
N = 2048           # Número de puntos (potencia de 2 para optimizar la FFT)
t = np.linspace(-1, 1, N) # Vector de tiempo


# 2. SEÑAL EN EL DOMINIO DEL TIEMPO (Pulso Rectangular)

# Pulso de ancho 0.4 segundos, centrado en cero
senal_tiempo = np.where(np.abs(t) <= 0.2, 1.0, 0.0)


# 3. CÁLCULO DE LA TRANSFORMADA DE FOURIER (FFT)

# Calculamos la FFT y la normalizamos dividiendo entre N
X_fourier = np.fft.fft(senal_tiempo) / N
# Centramos las frecuencias en 0 Hz
X_fourier_shiftheado = np.fft.fftshift(X_fourier)

# Creamos el vector de frecuencias correspondiente
frecuencias = np.fft.fftfreq(N, T)
frecuencias_shiftheadas = np.fft.fftshift(frecuencias)

# Obtenemos la Magnitud y la Fase
magnitud = np.abs(X_fourier_shiftheado)
fase = np.angle(X_fourier_shiftheado)


# 4. VISUALIZACIÓN DE LOS RESULTADOS

plt.figure(figsize=(10, 10))

# Gráfica 1: Dominio del Tiempo
plt.subplot(3, 1, 1)
plt.plot(t, senal_tiempo, 'b-', linewidth=2)
plt.title('1. Pulso Rectangular (Dominio del Tiempo)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.grid(True)
plt.xlim(-0.8, 0.8)

# Gráfica 2: Espectro de Magnitud (Dominio de la Frecuencia)
plt.subplot(3, 1, 2)
plt.plot(frecuencias_shiftheadas, magnitud, 'r-', linewidth=2)
plt.title('2. Espectro de Magnitud (Dominio de la Frecuencia)')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('|X(f)|')
plt.grid(True)
plt.xlim(-20, 20) # Hacemos zoom en las frecuencias bajas para ver el diseño

# Gráfica 3: Espectro de Fase
plt.subplot(3, 1, 3)
# Filtramos valores de magnitud muy pequeños para evitar ruido visual en la fase
fase_limpia = np.where(magnitud > 0.005, fase, 0.0)
plt.plot(frecuencias_shiftheadas, fase_limpia, 'g-', linewidth=2)
plt.title('3. Espectro de Fase')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Fase (radianes)')
plt.grid(True)
plt.xlim(-20, 20)

plt.tight_layout()

# Guardar la imagen final
plt.savefig('analisis_fourier_pulso.png', dpi=300)
print("¡Análisis completado! Se ha generado el archivo 'analisis_fourier_pulso.png'.")