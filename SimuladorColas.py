import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import queue
import random
import time
import tkinter as tk
from tkinter import scrolledtext


datos_ingresos = pd.DataFrame({
    'Tipo de Residente': ['Residente', 'Visitante'] * 48,
    'Hora de Ingreso': ['12:00 AM', '12:00 AM', '01:00 AM', '01:00 AM', '02:00 AM', '02:00 AM', '03:00 AM', '03:00 AM', '04:00 AM', '04:00 AM',
                        '05:00 AM', '05:00 AM', '06:00 AM', '06:00 AM', '07:00 AM', '07:00 AM', '08:00 AM', '08:00 AM', '09:00 AM', '09:00 AM',
                        '10:00 AM', '10:00 AM', '11:00 AM', '11:00 AM', '12:00 PM', '12:00 PM', '01:00 PM', '01:00 PM', '02:00 PM', '02:00 PM',
                        '03:00 PM', '03:00 PM', '04:00 PM', '04:00 PM', '05:00 PM', '05:00 PM', '06:00 PM', '06:00 PM', '07:00 PM', '07:00 PM',
                        '08:00 PM', '08:00 PM', '09:00 PM', '09:00 PM', '10:00 PM', '10:00 PM', '11:00 PM', '11:00 PM','12:00 AM', '12:00 AM', '01:00 AM', '01:00 AM', '02:00 AM', '02:00 AM', '03:00 AM', '03:00 AM', '04:00 AM', '04:00 AM',
                        '05:00 AM', '05:00 AM', '06:00 AM', '06:00 AM', '07:00 AM', '07:00 AM', '08:00 AM', '08:00 AM', '09:00 AM', '09:00 AM',
                        '10:00 AM', '10:00 AM', '11:00 AM', '11:00 AM', '12:00 PM', '12:00 PM', '01:00 PM', '01:00 PM', '02:00 PM', '02:00 PM',
                        '03:00 PM', '03:00 PM', '04:00 PM', '04:00 PM', '05:00 PM', '05:00 PM', '06:00 PM', '06:00 PM', '07:00 PM', '07:00 PM',
                        '08:00 PM', '08:00 PM', '09:00 PM', '09:00 PM', '10:00 PM', '10:00 PM', '11:00 PM', '11:00 PM'],
    'Cantidad': [
        8, 2, 35, 0, 28, 1, 35, 3, 27, 4, 11, 1, 5, 4, 18, 0, 32, 0, 28, 0, 24, 3, 13, 1, 32, 4, 13, 0, 17, 0, 15, 3, 34, 4, 33, 2, 3, 1, 9, 4, 27, 0, 30, 1, 29, 4, 8, 4, 2, 4, 5, 1, 31, 2, 10, 3, 14, 0, 34, 3, 26, 8, 28, 0, 0, 4, 35, 3, 10, 1, 16, 4, 5, 1, 31, 0, 1, 1, 9, 2, 13, 4, 3, 0, 4, 3, 31, 3, 26, 1, 8, 0, 8, 1, 0, 2
        ]
})

tamaño_muestra = 100

class FilaIngresoConjunto:
    def __init__(self, residentes, visitantes, ventana):
        self.residentes = residentes
        self.visitantes = visitantes
        self.cola = queue.Queue()
        self.ventana = ventana
        self.text_area = None

    def entrada_residente(self, hora):
        tiempo_entrada = random.uniform(1, 2)
        time.sleep(tiempo_entrada)
        mensaje = f"Residente ingresó entre las {hora} y las {hora + 1}. Tiempo de espera: {tiempo_entrada:.2f} minutos"
        self.mostrar_mensaje(mensaje)

    def entrada_visitante(self, hora):
        tiempo_entrada = random.uniform(1, 5)
        time.sleep(tiempo_entrada)
        mensaje = f"Visitante ingresó entre las {hora} y las {hora + 1}. Tiempo de espera: {tiempo_entrada:.2f} minutos"
        self.mostrar_mensaje(mensaje)

    def tiempo_de_descanso(self):
        tiempo_descanso = random.uniform(1, 30)
        time.sleep(tiempo_descanso)
        mensaje = f"Tiempo de descanso: {tiempo_descanso:.2f} minutos"
        self.mostrar_mensaje(mensaje)

    def tiempo_de_espera_aleatorio(self):
        if random.uniform(0, 1) < 0.5:
            tiempo_espera = random.uniform(0, 10)  # Ajusta los límites según sea necesario
            time.sleep(tiempo_espera)
            mensaje = f"Esperando {tiempo_espera:.2f} minutos antes de ingresar."
            self.mostrar_mensaje(mensaje)
            return tiempo_espera
        return 0

    def mostrar_mensaje(self, mensaje):
        self.text_area.insert(tk.END, mensaje + '\n')
        self.text_area.see(tk.END)
        self.ventana.update()

    def simular_ingresos_en_hora(self, hora):
        mensaje = f"\n--- Hora {hora} ---"
        self.mostrar_mensaje(mensaje)

        # Convert residentes_en_hora and visitantes_en_hora to integers
        residentes_en_hora = int(self.residentes[hora - 1])
        visitantes_en_hora = int(self.visitantes[hora - 1])

        personas_en_hora = [('residente', hora)] * residentes_en_hora + [('visitante', hora)] * visitantes_en_hora
        random.shuffle(personas_en_hora)

        for tipo, hora in personas_en_hora:
            tiempo_espera = self.tiempo_de_espera_aleatorio()
            time.sleep(tiempo_espera)
            
            self.mostrar_mensaje(mensaje)
            if tipo == 'residente':
                self.entrada_residente(hora)
            elif tipo == 'visitante':
                self.entrada_visitante(hora)

        # Descomenta la siguiente línea si deseas agregar un tiempo de descanso entre horas
        # self.tiempo_de_descanso()

    def simular_ingresos(self):
        self.ventana.title("Simulación de Ingresos")
        self.text_area = scrolledtext.ScrolledText(self.ventana, wrap=tk.WORD, width=50, height=20)
        self.text_area.pack(expand=True, fill='both')

        horas = list(range(1, len(self.residentes) + 1))

        for hora in horas:
            self.simular_ingresos_en_hora(hora)


# Datos proporcionados



def visualizar_distribucion_ingresos(promedio, desviacion_estandar, tamaño_muestra,nombre):
    
    # plt.figure(num=nombre)
    # plt.figure(figsize=(20, 15))

    # Generar números aleatorios con distribución normal
    numeros_aleatorios = np.random.normal(promedio, desviacion_estandar, tamaño_muestra)

    # Tomar el valor absoluto de los números generados
    numeros_aleatorios = np.abs(numeros_aleatorios)

    # Generar datos de tiempo (hora)
    horas_dia = np.linspace(0, 48, tamaño_muestra)

    
    # plt.title(nombre)
    # Crear subgráficos
    fig, axs = plt.subplots(2, 2,num=nombre, figsize=(20, 15), gridspec_kw={'height_ratios': [2, 3]})
    

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
    axs[0, 1].set_xlabel('Numero de Ingresos')
    axs[0, 1].set_ylabel('Cantidad por dia')

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
    return numeros_aleatorios


def calcular_estadisticas_transformacion_z(datos):
    # Calcular la media y la desviación estándar
    media_residente = datos[datos['Tipo de Residente'] == 'Residente']['Cantidad'].mean()
    std_residente = datos[datos['Tipo de Residente'] == 'Residente']['Cantidad'].std()

    media_visitante = datos[datos['Tipo de Residente'] == 'Visitante']['Cantidad'].mean()
    std_visitante = datos[datos['Tipo de Residente'] == 'Visitante']['Cantidad'].std()

    # Aplicar la transformación Z
    datos['Z_Residente'] = (datos[datos['Tipo de Residente'] == 'Residente']['Cantidad'] - media_residente) / std_residente
    datos['Z_Visitante'] = (datos[datos['Tipo de Residente'] == 'Visitante']['Cantidad'] - media_visitante) / std_visitante

    return datos,media_residente,std_residente,media_visitante,std_visitante



# Aplicar el método
datos_ingresos_transformados, media_residente,std_residente,media_visitante,std_visitante = calcular_estadisticas_transformacion_z(datos_ingresos)

# Mostrar el resultado
print(datos_ingresos_transformados[['Tipo de Residente', 'Hora de Ingreso', 'Cantidad', 'Z_Residente', 'Z_Visitante']])

numeros_aleatorios_residente = visualizar_distribucion_ingresos(media_residente,std_residente,tamaño_muestra,"Gráfica Residente")
numeros_aleatorios_visitante =visualizar_distribucion_ingresos(media_visitante,std_visitante,tamaño_muestra,"Gráfica Visitante")

ventana = tk.Tk()
fila_ingreso = FilaIngresoConjunto(numeros_aleatorios_residente, numeros_aleatorios_visitante, ventana)
fila_ingreso.simular_ingresos()
ventana.mainloop()
