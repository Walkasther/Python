import speech_recognition as sr
import moviepy.editor as mp

# Caminho do arquivo de vídeo
video_path = "/mnt/data/I.A. Protestante vs I. A. Católica PT2. MARIA Idolatria ou Hiperdulia (1).mp4"

# Extrair áudio do vídeo
video = mp.VideoFileClip(video_path)
audio_path = "/mnt/data/audio.wav"
video.audio.write_audiofile(audio_path)

# Inicializar o reconhecedor de fala
recognizer = sr.Recognizer()

# Carregar o áudio
audio = sr.AudioFile(audio_path)

# Transcrever o áudio
with audio as source:
    recognizer.adjust_for_ambient_noise(source)
    audio_text = recognizer.recognize_google(source, language="pt-BR")

audio_text[:500]  # Mostrando os primeiros 500 caracteres da transcrição para conferir qualidade
