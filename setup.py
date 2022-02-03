from setuptools import setup

setup(
   name='Tasmota',
   version='0.1',
   description='Easy HTTP interface to Tasmota powered devices',
   author='Felix Weichselgartner',
   author_email='info@felix-weichselgartner.de',
   packages=['Tasmota'],
   install_requires=['requests', 'lxml'],
)
