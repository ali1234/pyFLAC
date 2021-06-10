import numpy as np
import pyflac


class ExampleFLACEncoder(pyflac.StreamEncoder):
    def __init__(self, filename):
        self._filename = filename
        self._output_file = None
        super().__init__(
            write_callback=self.write_callback,
            seek_callback=self.seek_callback,
            tell_callback=self.tell_callback,
            metadata_callback=self.metadata_callback,
            sample_rate=48000,
            blocksize=65535,
            streamable_subset=False,
            verify=True,
        )

    def write_callback(self, buffer: bytes, num_bytes: int, num_samples: int, current_frame: int):
        self._output_file.write(buffer)

    def seek_callback(self, offset):
        print('seek', offset)
        self._output_file.seek(offset)

    def tell_callback(self):
        offset = self._output_file.tell()
        print('tell', offset)
        return offset

    def metadata_callback(self, metadata):
        # Currently this is just a big blob of cdata.
        print('Metadata:', metadata)

    def __enter__(self):
        self._output_file = open(self._filename, 'wb')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.finish()
        self._output_file.close()

    def write(self, b):
        self.process(np.frombuffer(b, dtype=np.int16))


def main():
    with ExampleFLACEncoder('test.flac') as enc:
        for n in range(100):
            enc.write(b'\x00\xff'*1024)


if __name__ == '__main__':
    main()
