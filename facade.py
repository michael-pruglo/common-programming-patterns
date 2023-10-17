#!/usr/bin/env python3


class VideoFile: pass
class OggCompressionCodec: pass
class CodecFactory:
    def extract(self, file): pass
class MPEG4CompressionCodec: pass
class BitrateReader:
    def read(filename, source_codec): pass
    def convert(buffer, dest_codec): pass
class AudioMixer:
    def fix(self, file): pass


class VideoConverter:
    def convert(self, filename, format):
        print("facade is using complicated hidden logic...")
        file = VideoFile()
        source_codec = CodecFactory().extract(file)
        dest_codec = MPEG4CompressionCodec() if format == "mp4" else OggCompressionCodec()
        buffer = BitrateReader.read(filename, source_codec)
        result = BitrateReader.convert(buffer, dest_codec)
        result = AudioMixer().fix(result)
        print("aaand it's done")
        return result


if __name__ == "__main__":
    convertor = VideoConverter()
    file = convertor.convert("silly_birds.ogg", "mp4")
