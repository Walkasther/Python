from flask import Flask, request, jsonify
import numpy as np
import sounddevice as sd

app = Flask(__name__)

# Parâmetros do sinal
sample_rate = 44100
duration = 0.1
freq_0 = 20000
freq_1 = 21000

def generate_tone(frequency, duration, sample_rate):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    return 0.5 * np.sin(2 * np.pi * frequency * t)

@app.route('/encode', methods=['POST'])
def encode():
    data = request.json
    message = data.get('message', '')

    if not message:
        return jsonify({'error': 'Message is required'}), 400

    audio_sequence = []
    for bit in message:
        frequency = freq_1 if bit == '1' else freq_0
        tone = generate_tone(frequency, duration, sample_rate)
        audio_sequence.append(tone)

    audio_data = np.concatenate(audio_sequence)
    sd.play(audio_data, sample_rate)
    sd.wait()

    return jsonify({'status': 'Message encoded and played'}), 200

@app.route('/decode', methods=['POST'])
def decode():
    record_duration = 2  # Ajuste conforme necessário
    recorded_audio = sd.rec(int(record_duration * sample_rate), samplerate=sample_rate, channels=1)
    sd.wait()

    # Aqui, seria implementada a decodificação semelhante ao exemplo anterior.
    # Vou usar um retorno de exemplo, substitua pelo seu processo de decodificação.
    decoded_message = "101010"  # Substitua pelo processo de decodificação real

    return jsonify({'message': decoded_message}), 200

if __name__ == '__main__':
    app.run(debug=True)
