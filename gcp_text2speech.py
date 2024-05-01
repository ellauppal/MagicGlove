import os
from google.cloud import texttospeech # outdated or incomplete comparing to v1
from google.cloud import texttospeech_v1
from speaker_connect import *
from moviepy.editor import concatenate_audioclips, AudioFileClip

def speech_to_text(phrase, audio_file_path):
    print("Running GCP...")
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"/home/magicglove/MagicGlove/api-key.json"

    # instantiates a client
    client = texttospeech_v1.TextToSpeechClient()

    # set the text input to be synthesized
    synthesis_input = texttospeech_v1.SynthesisInput(text=phrase)

    voice = texttospeech_v1.VoiceSelectionParams(
        language_code="en-ca",
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL,
    )

    # select the type of audio file you want returned
    audio_config = texttospeech_v1.AudioConfig(
        audio_encoding=texttospeech_v1.AudioEncoding.MP3
    )

    # perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(
        input=synthesis_input,
        voice=voice,
        audio_config=audio_config
    )

    with open(audio_file_path, "wb") as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        print('Audio content written to file "audiofile.mp3"')
    
    # concating audio files for delay
    audio_clip_paths = ["/home/magicglove/MagicGlove/test/waitnew.m4a", audio_file_path]
    output_path = audio_file_path
    concatenate_audio_moviepy(audio_clip_paths, output_path)
    
    call_speaker()
    
def concatenate_audio_moviepy(audio_clip_paths, output_path):
    clips = [AudioFileClip(c) for c in audio_clip_paths]
    final_clip = concatenate_audioclips(clips)
    final_clip.write_audiofile(output_path)

