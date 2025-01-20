from youtube_transcript_api import YouTubeTranscriptApi
import os

def get_youtube_video_id(url):
    """
    Extrae el ID del video de una URL de YouTube.
    """
    import re
    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    raise ValueError("URL de YouTube no válida.")

def fetch_transcript(video_url, output_filename="transcripcion.txt", language='es'):
    """
    Obtiene la transcripción de un video de YouTube en el idioma deseado y la guarda en un archivo .txt.
    
    :param video_url: URL del video de YouTube.
    :param output_filename: Nombre del archivo de salida.
    :param language: Idioma de la transcripción (por ejemplo, 'es' para español).
    """
    try:
        # Extraer el ID del video
        video_id = get_youtube_video_id(video_url)
        
        # Intentar obtener la transcripción en el idioma especificado
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[language])
        
        # Procesar y guardar la transcripción en un archivo .txt
        with open(output_filename, "w", encoding="utf-8") as file:
            for entry in transcript:
                text = entry['text']
                file.write(f"{text}\n")
        
        print(f"Transcripción guardada en {output_filename}.")
    except Exception as e:
        print(f"Error al obtener la transcripción: {e}")

# Uso del script
video_url = input("Ingresa la URL del video de YouTube: ")
output_filename = "transcripcion_espanol.txt"
fetch_transcript(video_url, output_filename, language='es')
