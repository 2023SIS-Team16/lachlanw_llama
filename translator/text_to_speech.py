from flask import Flask, request, Response
from transformers import AutoProcessor, BarkModel
import io
import scipy.io.wavfile

app = Flask(__name__)

processor = AutoProcessor.from_pretrained("suno/bark")
model = BarkModel.from_pretrained("suno/bark")
voice_preset = "v2/en_speaker_6"
sampling_rate = model.config.sample_rate

@app.route("/generate_tts", methods=['POST'])
def generate_text_to_speech():
    data = request.get_json()
    
    text_to_generate = data.get('text', None)
    if not text_to_generate:
        return Response("Invalid text data", status=400)

    inputs = processor(text=text_to_generate, voice_preset=voice_preset)

    audio_array = model.generate(**inputs)
    audio_array = audio_array.cpu().numpy().squeeze()
    
    buf = io.BytesIO()
    scipy.io.wavfile.write(buf, rate=sampling_rate, data=audio_array)
    
    buf.seek(0)

    return Response(buf, content_type="audio/wav")
