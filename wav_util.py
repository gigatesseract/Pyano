import math
import wave
import struct


def create_sound(freq, datasize, fname, frate):
    amp = 8000.0
    sine_list = []
    for x in range(datasize):
        sine_list.append(math.sin(2 * math.pi * freq * (x / frate)))

    wav_file = wave.open(fname, "w")

    nchannels = 1
    sampwidth = 2
    framerate = int(frate)
    nframes = datasize
    comptype = "NONE"
    compname = "not compressed"
    wav_file.setparams((nchannels, sampwidth, framerate, nframes, comptype, compname))

    for s in sine_list:
        wav_file.writeframes(struct.pack("h", int(s * amp / 2)))
    wav_file.close()


# def play_sound(fname, flag):
#     chunk = 2048
#     f = wave.open(fname, "rb")
#     # instantiate PyAudio
#     p = pyaudio.PyAudio()
#     # open stream
#     stream = p.open(
#         format=p.get_format_from_width(f.getsampwidth()),
#         channels=f.getnchannels(),
#         rate=f.getframerate(),
#         output=True,
#     )
#     # read data
#     data = f.readframes(chunk)

#     # play stream
#     while data and flag:

#         stream.write(data)
#         data = f.readframes(chunk)

#     # stop stream  stream.stop_stream()
#     stream.close()

#     p.terminate()


if __name__ == "__main__":
    frate = 44100.00  # that's the framerate
    freq = 440.0  # that's the frequency, in hertz
    seconds = 3  # seconds of file
    data_length = int(frate * seconds)  # number of frames
    fname = "sample.wav"  # name of file
    make_sine(440.0, data_length, fname, 44100.0)

