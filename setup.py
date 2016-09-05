from setuptools import setup,find_packages
setup(
    name='ztresizer',
    version='0.0.1',
    keywords=('image','resizer'),
    description='just a simple image resizer',
    license='GPL License',
    install_requires=['Image'],
    author='Xiaozhe Yaoi@zhitan',
    author_email='xiaozhe.yaoi@gmail.com',
    packages=find_packages(),
    platforms='any',
)