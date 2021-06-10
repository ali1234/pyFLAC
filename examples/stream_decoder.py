import os

import numpy as np
import pyflac


class ExampleFLACDecoder(pyflac.StreamDecoder):
    def __init__(self, input_filename, output_filename):
        self._input_filename = input_filename
        self._output_filename = output_filename
        self._input_file = None
        self._output_file = None
        self._fake_pos = 0

        super().__init__(
            read_callback=self.read_callback,
            write_callback=self.write_callback,
            seek_callback=self.seek_callback,
            tell_callback=self.tell_callback,
            length_callback=self.length_callback,
            eof_callback=self.eof_callback,
        )

    def read_callback(self, num_bytes: int):
        return self._input_file.read(num_bytes)

    def write_callback(self, buffer: np.ndarray, num_bytes: int, num_samples: int, current_frame: int):
        self._output_file.write(buffer.tobytes())

    def seek_callback(self, offset):
        print('seek', offset)
        self._input_file.seek(offset)

    def tell_callback(self):
        offset = self._input_file.tell()
        print('tell', offset)
        return offset

    def length_callback(self):
        return os.fstat(self._input_file.fileno()).st_size

    def eof_callback(self):
        return self.tell_callback() == self.length_callback()

    def __enter__(self):
        self._input_file = open(self._input_filename, 'rb')
        self._output_file = open(self._output_filename, 'wb')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._input_file.close()
        self._output_file.close()


def main():
    with ExampleFLACDecoder('test.flac', 'test.raw') as enc:
        enc.process()


if __name__ == '__main__':
    main()
