from setuptools import setup

setup(
    name='pyFLAC',
    version='0.1.0',
    description='A Python wrapper for libFLAC',
    long_description=open('README.rst').read(),
    author='Sonos, Inc',
    author_email='joe.todd@sonos.com',
    url='https://github.com/Sonos-Inc/pyFLAC',
    packages=['pyflac'],
    setup_requires=['cffi>=1.4.0'],
    cffi_modules=[
        'pyflac/builder/encoder.py:ffibuilder',
        'pyflac/builder/decoder.py:ffibuilder'
    ],
    install_requires=['cffi>=1.4.0'],
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Multimedia :: Sound/Audio',
        'Topic :: System :: Archiving :: Compression',
    ],
)