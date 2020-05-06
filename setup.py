from setuptools import setup
setup(
    name = 'upc-decode',
    version = '1.0.0',
    packages = ['upc-decode'],
    entry_points = {
        'console_scripts': [
            'upc_decode = upc_decode.__main__:main'
        ]
    })
