from setuptools import setup
setup(
    name = 'ucp-decode',
    version = '1.0.0',
    packages = ['ucp-decode'],
    python_requires='>=3.5',
    entry_points = {
        'console_scripts': [
            'ucp_decode = ucp_decode.__main__:main'
        ]
    })
