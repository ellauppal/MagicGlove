from pydub import AudioSegment
from pydub.playback import play

def call_speaker():
    audio_file = "/home/magicglove/MagicGlove/test/audiofile.mp3"
    song = AudioSegment.from_mp3(audio_file)
    play(song)
