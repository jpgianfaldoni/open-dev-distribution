from setuptools import setup

setup(name='dev_aberto_joaopga1',
      author='Joao Andrade',
      version='0.1',
      packages=['dev_aberto'],
      python_requires='>=3.6',
      platforms='any',
      install_requires=[
        'requests', 
    ],
    scripts=['scripts/hello.py'],
      )