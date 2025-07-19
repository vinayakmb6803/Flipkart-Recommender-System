from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()
    setup(
        name="Flipkart LLM Project",
        version="0.1",
        author="Vinayak",
        packages=find_packages(),
        install_requires=requirements)
    