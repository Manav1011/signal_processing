import librosa
import soundfile as sf
import os

def make_audio_11_seconds(input_path, output_path, target_duration=11.0):
    # Load audio
    y, sr = librosa.load(input_path, sr=None)  # Keep original sample rate
    current_duration = librosa.get_duration(y=y, sr=sr)
    target_length = int(target_duration * sr)

    if current_duration > target_duration:
        # Trim
        y = y[:target_length]
    else:
        # Pad with zeros (silence)
        padding = target_length - len(y)
        y = librosa.util.fix_length(y, size=target_length)

    # Save the result
    sf.write(output_path, y, sr)
    print(f"Processed {input_path} -> {output_path} [{target_duration} sec]")

# Example usage for 3 files
input_files = ["audio4.wav", "audio5.wav", "audio6.wav"]
output_folder = "output_audios"

os.makedirs(output_folder, exist_ok=True)

for file in input_files:
    input_path = file
    output_path = os.path.join(output_folder, os.path.basename(file))
    make_audio_11_seconds(input_path, output_path)
