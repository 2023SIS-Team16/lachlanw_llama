from transformers import AutoProcessor, BarkModel
import scipy

processor = AutoProcessor.from_pretrained("suno/bark")
model = BarkModel.from_pretrained("suno/bark")
voice_preset = "v2/en_speaker_6"
sampling_rate = model.config.sample_rate

def generate_text_to_speech(text_to_generate):
    inputs = processor(
        text = text_to_generate,
        voice_preset = voice_preset
    )

    audio_array = model.generate(**inputs)
    audio_array = audio_array.cpu().numpy().squeeze()

    scipy.io.wavfile.write(f"{text_to_generate}.wav", rate=sampling_rate, data=audio_array)