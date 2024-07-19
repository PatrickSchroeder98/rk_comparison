from setuptools import setup, find_packages
"""Setup for this project."""

setup(
    name='rk_comparison',
    version='1.0.0',
    description='A project for comparing numerical methods.',
    author='Patrick Schröder',
    author_email='patrickschroder479@gmail.com',
    url='https://github.com/PatrickSchroeder98/rk_comparison',
    packages=find_packages(),
    install_requires=[
        'matplotlib',
        'PyQt6',
    ],
    extras_require={
        'dev': [
            'pytestqt',
            'black',
            'sphinx',
        ],
    },
    entry_points={
        'console_scripts': [
            'rk_comparison=rk_comparison.main:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Windows',
    ],
    python_requires='>=3.10',
)