# ADRIANA_VALENCIA_ACT2_FOURIER.IDS
Actividad Formativa 2 - SIMULACIÓN Y ANÁLISIS DE SEÑALES CON LA TRANSFORMADA DE FOURIER
Este repositorio contiene las simulaciones en Python para analizar señales elementales en los dominios del tiempo y de la frecuencia utilizando la Transformada Rápida de Fourier (FFT).

 Estructura del Proyecto

El repositorio está conformado por los siguientes archivos:
* main.py: Código base para la generación de señales en el dominio del tiempo.
* fourier_analysis.p`: Script para calcular y graficar el espectro de magnitud y fase.
* `propiedades_fourier.py: Código para validar la propiedad de desplazamiento temporal.
*Analisis fourier senoidal.py
* ANALISIS DE FOURIER.jpg: Espectro de magnitud y fase del pulso rectangular.
* PULSO ESCALON.jpg`: Espectro de magnitud y fase de la función escalón unitario.
* propiedades desplazamiento.jpg: Espectro de magnitud y fase de la función senoidal.

---

 Hallazgos y Análisis de Resultados

 1. Pulso Rectangular 
* **Tiempo:** Un pulso de amplitud 1.0 distribuido simétricamente alrededor de cero.
* **Frecuencia:** Su transformada da como resultado una función tipo **Sinc** ($\frac{\sin(x)}{x}$). El pico central de magnitud se ubica en 0Hz, representando el valor promedio de la señal. Las discontinuidades abruptas en el tiempo provocan que el espectro de magnitud se extienda de forma amortiguada hacia frecuencias más altas.

 2. Función Escalón Unitario
* **Tiempo:** Un salto brusco de 0 a 1 exactamente en t = 0.
* **Frecuencia:** Presenta una concentración masiva de energía en $0\text{ Hz}$ ($|X(f)| = 0.5$) debido a su componente continua. La magnitud decae de forma suave y continua conforme aumenta la frecuencia, reflejando las componentes necesarias para reconstruir la transición abrupta del escalón.
 3. Función Senoidal (5 Hz) 
* **Tiempo:** Una oscilación periódica pura que completa exactamente 5 ciclos por segundo.
* **Frecuencia:** Al ser una frecuencia pura, toda su energía se concentra en dos picos simétricos localizados exactamente en -5Hz y +5Hz. La fase muestra valores exactos de  radianes en dichas frecuencias, validando de forma precisa la teoría matemática de Fourier.

 Conclusión General

El análisis demuestra que los eventos rápidos o discontinuidades en el dominio del tiempo (como en el pulso y el escalón) requieren un espectro amplio y continuo de frecuencias para poder ser representados. En contraste, las señales suaves y periódicas (como la senoide) se representan mediante espectros discretos y localizados. Esto evidencia la utilidad práctica de la Transformada de Fourier para identificar la distribución de energía de una señal y diseñar filtros en aplicaciones de ingeniería.
