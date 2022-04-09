import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cairotest",
    version="0.2.2",
    scripts=["cairotest.py"],
    author="Jamie Gabbay",
    author_email="bellissimogiorno@gmail.com",
    description="A smart test framework for cairo-lang and starknet based on pytest and hypothesis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bellissimogiorno/cairotest",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: Hypothesis",
    ],
    install_requires=[
        "hypothesis>=6.41.0",
    ],
)
