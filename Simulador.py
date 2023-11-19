import pandas as pd

# Datos proporcionados
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

# Calcular la media y la desviación estándar
media_residente = datos_ingresos[datos_ingresos['Tipo de Residente'] == 'Residente']['Cantidad'].mean()
std_residente = datos_ingresos[datos_ingresos['Tipo de Residente'] == 'Residente']['Cantidad'].std()

media_visitante = datos_ingresos[datos_ingresos['Tipo de Residente'] == 'Visitante']['Cantidad'].mean()
std_visitante = datos_ingresos[datos_ingresos['Tipo de Residente'] == 'Visitante']['Cantidad'].std()

print("Media Residente:", media_residente)
print("Desviación estándar Residente:", std_residente)
print("Media Visitante:", media_visitante)
print("Desviación estándar Visitante:", std_visitante)

# Aplicar la transformación Z
datos_ingresos['Z_Residente'] = (datos_ingresos[datos_ingresos['Tipo de Residente'] == 'Residente']['Cantidad'] - media_residente) / std_residente
datos_ingresos['Z_Visitante'] = (datos_ingresos[datos_ingresos['Tipo de Residente'] == 'Visitante']['Cantidad'] - media_visitante) / std_visitante

print(datos_ingresos[['Tipo de Residente', 'Hora de Ingreso', 'Cantidad', 'Z_Residente', 'Z_Visitante']])

