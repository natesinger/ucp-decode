from setuptools import setup
setup(
    name = 'ucp-decode',
    version = '1.0.0',
    description = 'Python parser for interpreting keyboard captures, under USB device class definition HID 1.11.',
    url = 'https://github.com/nmsinger/ucp-decode.git',
    author = 'Nate Singer',
    author_email = 'nathaniel@singer.cloud',
    license = 'Apache 2.0',
    packages = ['ucp-decode'],
    python_requires='>=3.5',
    entry_points = {
        'console_scripts': [
            'ucp_decode = ucp_decode.__main__:main'
        ]
    })
