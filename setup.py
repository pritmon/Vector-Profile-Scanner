from setuptools import setup, find_packages

setup(
    name="vector-profile-scanner",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "tensorflow==2.20.0",
        "pytest==8.2.2",
        "notebook==7.2.1",
        "pandas==2.2.2",
        "matplotlib==3.9.0"
    ],
)
