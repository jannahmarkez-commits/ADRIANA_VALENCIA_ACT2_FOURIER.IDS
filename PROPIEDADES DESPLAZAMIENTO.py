import numpy as np
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt


# 1. CONFIGURACIÓN DE PARÁMETROS GENERALES

Fs = 1000          
T = 1.0 / Fs       
N = 2048           
t = np.linspace(-1, 1, N) 


# 2. DEFINICIÓN DE SEÑALES (Original vs Desplazada)

# Pulso original centrado en 0
pulso_original = np.where(np.abs(t) <= 0.2, 1.0, 0.0)

# Pulso desplazado (retrasado t0 = 0.3 segundos hacia la derecha)
t0 = 0.3
pulso_desplazado = np.where(np.abs(t - t0) <= 0.2, 1.0, 0.0)

#
# 3. CÁLCULO DE LA FFT

# FFT de la señal original
X_orig = np.fft.fftshift(np.fft.fft(pulso_original) / N)
# FFT de la señal desplazada
X_desp = np.fft.fftshift(np.fft.fft(pulso_desplazado) / N)

frecuencias = np.fft.fftshift(np.fft.fftfreq(N, T))

# Magnitud y Fase de ambas
mag_orig, fase_orig = np.abs(X_orig), np.angle(X_orig)
mag_desp, fase_desp = np.abs(X_desp), np.angle(X_desp)

# Limpieza de fase para evitar ruido visual
fase_orig = np.where(mag_orig > 0.005, fase_orig, 0.0)
fase_desp = np.where(mag_desp > 0.005, fase_desp, 0.0)


# 4. GRAFICACIÓN COMPARATIVA

plt.figure(figsize=(12, 10))

# Dominio del Tiempo
plt.subplot(3, 1, 1)
plt.plot(t, pulso_original, 'b-', label='Original (Centrado)', linewidth=2)
plt.plot(t, pulso_desplazado, 'r--', label=f'Desplazado (t0 = {t0}s)', linewidth=2)
plt.title('Propiedad de Desplazamiento: Dominio del Tiempo')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.grid(True)
plt.legend()

# Espectro de Magnitud
plt.subplot(3, 1, 2)
plt.plot(frecuencias, mag_orig, 'b-', label='Magnitud Original', linewidth=2)
plt.plot(frecuencias, mag_desp, 'r--', label='Magnitud Desplazada', linewidth=2)
plt.title('Espectro de Magnitud (¡Son idénticos!)')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('|X(f)|')
plt.grid(True)
plt.xlim(-15, 15)
plt.legend()

# Espectro de Fase
plt.subplot(3, 1, 3)
plt.plot(frecuencias, fase_orig, 'b-', label='Fase Original', linewidth=2)
plt.plot(frecuencias, fase_desp, 'r-', label='Fase Desplazada', linewidth=1.5)
plt.title('Espectro de Fase (El desplazamiento añade una pendiente lineal)')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Fase (radianes)')
plt.grid(True)
plt.xlim(-15, 15)
plt.legend()

plt.tight_layout()
plt.savefig('propiedad_desplazamiento.png', dpi=300)
print("¡Simulación de propiedad completada! Archivo 'propiedad_desplazamiento.png' generado.")