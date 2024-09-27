from setuptools import setup, find_packages

setup(
    name='pyColorPrint',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'termcolor',
    ],
    description='Utility for colored  print and input statements',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/roamingsaint/pyColorPrint.git',
    author='Kanad Rishiraj',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
)
