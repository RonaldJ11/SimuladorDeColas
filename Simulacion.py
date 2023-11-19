import queue
import random
import time
import tkinter as tk
from tkinter import scrolledtext

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

        residentes_en_hora = self.residentes[hora - 1]
        visitantes_en_hora = self.visitantes[hora - 1]

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

# Ejemplo de uso
residentes_por_hora = [5, 10, 8, 6, 12]  # Ejemplo: residentes que llegan cada hora
visitantes_por_hora = [8, 15, 10, 5, 20]  # Ejemplo: visitantes que llegan cada hora

ventana = tk.Tk()
fila_ingreso = FilaIngresoConjunto(residentes_por_hora, visitantes_por_hora, ventana)
fila_ingreso.simular_ingresos()
ventana.mainloop()
