# from commanduino._version import __version__

from setuptools import find_packages, setup

requirements = ['pyserial']

setup(name="commanduino",
      version='0.1',
      description="A library to interact with an arduino board running Arduino-CommandHandler and derivatives",
      author="Jonathan Grizou",
      author_email='jonathan.grizou@gmail.com',
      platforms=["any"],
      url="https://github.com/croningp/commanduino",
      install_requires=requirements,
      packages=find_packages(),
      )
