from setuptools import setup, find_packages

setup(
    name="autonomous-sim",
    version="0.1.0",
    author="priya-sharma-ai",
    description="Autonomous Driving Perception Simulator",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/priya-sharma-ai/autonomous-sim",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=[
        "torch>=2.0",
        "numpy>=1.24",
        "pyyaml>=6.0",
        "tqdm>=4.65",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
    ],
)
