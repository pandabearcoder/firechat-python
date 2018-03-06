from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(
    name='firechat',
    version='0.1',
    description='Port of the javascript firechat sdk to python with the help of firebase-admin',
    long_description=readme,
    url='https://github.com/pandabearcoder/firechat-python',
    author='pandabearcoder',
    author_email='vlouie00@gmail.com',
    license='MIT',
    keywords='firechat firebase chat',
    packages=['firechat'],
    zip_safe=False,
)
