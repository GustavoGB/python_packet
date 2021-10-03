from setuptools import setup

setup(
    name='dev_aberto_gustavogb',
    version='0.1.0',    
    description='A example Python package',
    url='https://github.com/GustavoGB/python_packet',
    author='Gustavo Gobetti',
    author_email='gustavogb@al.insper.edu.br',
    license='MIT LICENSE',
    packages=['dev_aberto'],
    install_requires=[
                      'requests'                     
                      ],
    scripts=['scripts/hello.py'],

    classifiers=[
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',         
        'Programming Language :: Python :: 3.9',
    ],
)