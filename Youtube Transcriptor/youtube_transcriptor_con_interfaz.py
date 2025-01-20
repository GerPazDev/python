import tkinter as tk
from tkinter import messagebox
from youtube_transcript_api import YouTubeTranscriptApi

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

def fetch_transcript():
    """
    Obtiene la transcripción y la guarda en un archivo.
    """
    video_url = url_entry.get()
    output_filename = filename_entry.get()

    if not video_url or not output_filename:
        messagebox.showerror("Error", "Por favor, completa todos los campos.")
        return

    try:
        # Extraer el ID del video
        video_id = get_youtube_video_id(video_url)

        # Obtener la transcripción
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['es'])

        # Guardar la transcripción en un archivo
        with open(output_filename, "w", encoding="utf-8") as file:
            for entry in transcript:
                text = entry['text']
                file.write(f"{text}\n")
        
        messagebox.showinfo("Éxito", f"Transcripción guardada en {output_filename}.")

    except Exception as e:
        messagebox.showerror("Error", f"No se pudo obtener la transcripción: {e}")

# Crear la ventana principal
root = tk.Tk()
root.title("Transcriptor de YouTube")
root.geometry("400x200")

# Etiqueta y campo de entrada para la URL
tk.Label(root, text="URL del video de YouTube:").pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# Etiqueta y campo de entrada para el nombre del archivo
tk.Label(root, text="Nombre del archivo de salida (.txt):").pack(pady=5)
filename_entry = tk.Entry(root, width=50)
filename_entry.pack(pady=5)

# Botón para generar la transcripción
tk.Button(root, text="Generar Transcripción", command=fetch_transcript).pack(pady=20)

# Ejecutar la aplicación
root.mainloop()
