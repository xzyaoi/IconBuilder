from setuptools import setup,find_packages
setup(
    name='iconbuilder',
    version='0.0.1',
    keywords=('image','resizer'),
    description='just a simple image resizer',
    license='GPL License',
    py_modules=['iconbuilder'],
    install_requires=['Image','Click'],
    author='Xiaozhe Yaoi@zhitan',
    author_email='xiaozhe.yaoi@gmail.com',
    packages=find_packages(),
    platforms='any',
    entry_points='''
        [console_scripts]
        iconbuilder=iconbuilder:main
    ''',
)