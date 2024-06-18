import wave
import numpy as np
import struct

# Definición de parámetros globales
duracion = 1.0  # Duración de cada nota en segundos
amplitud = 16000  # Amplitud de la señal

# Frecuencias de las notas
Fre_notas = {
    'Do' : 261.63,
    'Re' : 293.66,
    'Mi' : 329.63,
    'Fa' : 349.23,
    'Sol': 392.00,
    'La' : 440.00,
    'Si' : 523.25
}

# Listas de notas y configuraciones
notas1 = ["Do", "Re", "Mi", "Fa", "Sol", "La", "Si"]
notas2 = ["Si", "La", "Sol", "Fa", "Mi", "Re", "Do"]
notas3 = ["Do", "Re", "Mi", "Fa", "Sol", "La", "Si"]

configuraciones = [
    (notas1, 44100, 1, 'tonos1.wav'),
    (notas2, 22050, 2, 'tonos2.wav'),
    (notas3, 8000,  1, 'tonos3.wav')
]




#--------------------------------------------------------------------------------------------------
# Funciones
#--------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------
# Funcion 1
#--------------------------------------------------------------------------------------------------

def generar_nota(frecuencia, duracion, sample_rate, amplitud):
    # Crear un array de puntos de tiempo, de 0 a 'duracion', con 'sample_rate * duracion' muestras
    t = np.linspace(0, duracion, int(sample_rate * duracion), endpoint=False)
    
    # Generar una onda sinusoidal con la frecuencia y amplitud especificadas
    onda = amplitud * np.sin(2 * np.pi * frecuencia * t)
    
    # Retornar la onda generada
    return onda
    
#--------------------------------------------------------------------------------------------------
# Funcion 2
#--------------------------------------------------------------------------------------------------

def empaquetar_datos(audio_data):
    datos_empaquetados = []  # Lista para almacenar las muestras empaquetadas
    
    # Iterar sobre cada muestra en los datos de audio
    for muestra in audio_data:
        # Empaquetar la muestra en un formato de 2 bytes (short) en orden little-endian
        packed_sample = struct.pack('<h', int(muestra))  # '<h' para short en little-endian
        # Añadir la muestra empaquetada a la lista
        datos_empaquetados.append(packed_sample)
    
    # Unir todas las muestras empaquetadas en una sola secuencia de bytes
    return b''.join(datos_empaquetados)

#--------------------------------------------------------------------------------------------------
# Funcion 3
#--------------------------------------------------------------------------------------------------

def crear_archivo(nombre, sample_rate, canales, audio_data):
    with wave.open(nombre, 'w') as archivo:
        nchannels = canales
        sampwidth = 2  # 2 bytes por muestra
        nframes = len(audio_data) // sampwidth
        archivo.setparams((nchannels, sampwidth, sample_rate, nframes, 'NONE', 'not compressed'))
        archivo.writeframes(audio_data)

#--------------------------------------------------------------------------------------------------
# Funcion 4
#--------------------------------------------------------------------------------------------------

def generar_audio(notas, sample_rate, canales):
    audio_data = []  # Lista para almacenar los datos de audio generados
    
    # Iterar sobre cada nota en la lista de notas
    for nota in notas:
        # Obtener la frecuencia correspondiente a la nota actual
        frecuencia = Fre_notas[nota]
        
        # Generar la onda de la nota con la frecuencia obtenida
        # 'duracion' y 'amplitud' deberían estar definidas en el contexto global o como parámetros de la función
        onda = generar_nota(frecuencia, duracion, sample_rate, amplitud)
        
        # Si el audio es estéreo (2 canales), duplicar la onda para ambos canales
        if canales == 2:
            # Repetir la onda para crear dos canales (estéreo)
            onda = np.repeat(onda[:, np.newaxis], 2, axis=1)  # Duplicar para estéreo
            onda = onda.flatten()  # Aplanar la matriz resultante en un solo vector
        
        # Agregar la onda generada a la lista de datos de audio
        audio_data.extend(onda)
    
    # Convertir la lista de datos de audio a un array de numpy con tipo de dato int16
    # estó pára mayor eficiencia de memoria, ya que este limita los datos a 16 bits 
    audio_data = np.array(audio_data, dtype=np.int16)
    
    # Empaquetar los datos de audio en el formato adecuado (esto podría ser, por ejemplo, convertir a formato WAV)
    audio_data_empaquetados = empaquetar_datos(audio_data)
    
    # Retornar los datos de audio empaquetados
    return audio_data_empaquetados

#--------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------


# Generar y guardar los archivos de sonido
for notas, sample_rate, canales, archivo in configuraciones:
    audio_data = generar_audio(notas, sample_rate, canales)
    crear_archivo(archivo, sample_rate, canales, audio_data)
    print(f"Archivo {archivo} creado con éxito.")
