import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la distribución normal
promedio = 2.020
desviacion_estandar = 1.76
tamaño_muestra = 1000

# Generar números aleatorios con distribución normal
numeros_aleatorios = np.random.normal(promedio, desviacion_estandar, tamaño_muestra)

# Tomar el valor absoluto de los números generados
numeros_aleatorios = np.abs(numeros_aleatorios)

# Generar datos de tiempo (hora)
horas_dia = np.linspace(0, 48, tamaño_muestra)

# Crear subgráficos
fig, axs = plt.subplots(2, 2, figsize=(20, 15), gridspec_kw={'height_ratios': [2, 3]})

# Gráfico 1: Histograma de los datos generados respecto a la hora del día
im = axs[0, 0].hist2d(horas_dia, numeros_aleatorios, bins=(20, 20), cmap=plt.cm.Greens)
axs[0, 0].set_title('Distribución de Ingresos por Hora del Día')
axs[0, 0].set_xlabel('Hora del Día')
axs[0, 0].set_ylabel('Número de Personas')
fig.colorbar(im[3], ax=axs[0, 0], label='Frecuencia')

# Gráfico 2: Curva de distribución normal teórica respecto a la hora del día
x = np.linspace(0, 48, 100)
p = (1 / (desviacion_estandar * np.sqrt(2 * np.pi))) * np.exp(-(x - promedio)**2 / (2 * desviacion_estandar**2))
# Escalar la curva teórica para que se ajuste a la escala del histograma
escala_curva = tamaño_muestra / np.sum(p)
axs[0, 1].plot(x, p * escala_curva, 'k', linewidth=2)
axs[0, 1].set_title('Distribución Normal Teórica')
axs[0, 1].set_xlabel('Hora del Día')
axs[0, 1].set_ylabel('Número de Ingresos')

# Añadir información adicional a la distribución normal teórica
axs[0, 1].axvline(promedio, color='r', linestyle='--', label='Media')
axs[0, 1].axvline(promedio + desviacion_estandar, color='b', linestyle='--', label='+1 Desviación Estándar')
axs[0, 1].axvline(promedio - desviacion_estandar, color='b', linestyle='--', label='-1 Desviación Estándar')
axs[0, 1].fill_between(x, 0, p * escala_curva, where=((x >= (promedio - desviacion_estandar)) & (x <= (promedio + desviacion_estandar))), color='gray', alpha=0.3, label='68% dentro de 1 Desviación Estándar')

# Mostrar la leyenda
axs[0, 1].legend()

# Calcular el promedio de ingresos para cada hora
promedio_por_hora = []
for hora in np.unique(horas_dia):
    promedio_por_hora.append(np.mean(numeros_aleatorios[horas_dia == hora]))

# Gráfico 3: Curva de distribución de ingresos promedios por hora
axs[1, 0].plot(np.unique(horas_dia), promedio_por_hora, color='orange', linewidth=2)
axs[1, 0].set_title('Distribución de Ingresos Promedios por Hora del Día')
axs[1, 0].set_xlabel('Hora del Día')
axs[1, 0].set_ylabel('Ingreso Promedio')
axs[1, 0].grid(True)

# Detalles adicionales para la última gráfica
axs[1, 0].set_xticks(np.arange(0, 50, 4))
axs[1, 0].set_ylim(0, max(promedio_por_hora) + 1)  # Ajustar límite superior del eje y
axs[1, 0].grid(axis='y', linestyle='--', alpha=0.7)

# Ocultar la última gráfica en la segunda fila
axs[1, 1].axis('off')

# Ajustar el diseño para evitar solapamientos y abrir en pantalla completa
plt.tight_layout(h_pad=2)

# Agregar más detalles
axs[0, 0].set_xticks(np.arange(0, 50, 4))
axs[0, 1].legend(loc='upper right')

# Mostrar los subgráficos
plt.subplots_adjust(left=0.05, right=0.99, top=0.95, bottom=0.05, wspace=0.2, hspace=0.4)
plt.show()
