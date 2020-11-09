from setuptools import setup

readme = open('README.md', 'r')
long_description = readme.read()
readme.close()

setup(
    name='snapy',
    version='1.0.3',
    author='Justin Boylan-Toomey',
    author_email='justin.boylan-toomey@outlook.com',
    description='SnaPy is a Python library for detecting near duplicate texts'
                ' using Minhash and Locality Sensitive Hashing.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/justinnbt/SnaPy',
    packages=['snapy'],
    install_requires=['mmh3', 'numpy'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ]
)
