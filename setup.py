from distutils.core import setup

setup(
    name='pyjos',
    version='0.1.0',
    description='A Jingdong SDK for Python which imitates official PHP SDK.',
    long_description=open('DESCRIPTION.rst').read(),
    license='BSD License',
    requires=['requests', 'six'],
    packages=['pyjos', 'pyjos.request'],
    author='Ziya Tang',
    author_email='tcztzy@gmail.com',
    url='https://github.com/tcztzy/pyjos',
    platforms='any',
)
