import wave
import struct

#Вводим со строки название входного аудио
source = wave.open(input(),mode="rb")
dest = wave.open("out.wav",mode="wb")
dest.setparams(source.getparams())

frames_count = source.getnframes()
data = struct.unpack("<" + str(frames_count) + "h",
                    source.readframes(frames_count))
#'h' означает uint16_t, '<' означает Little Endian ( https://docs.python.org/3/library/struct.html , http://soundfile.sapp.org/doc/WaveFormat/ ).

#Лучше сделать тут функцию process
volume = float(input())
# uint16_t min/max, иначе ошибка, ибо значение может выйти за пределы uint16_t, хоть uint16_t и беззнаковый, но мы должны учесть диапозон с знаками.
newdata = list(map(lambda t: max(-32767,min(32767,int(t*volume))), data))

newframes = struct.pack("<" + str(len(newdata)) + "h", *newdata)
dest.writeframes(newframes)
source.close()
dest.close()