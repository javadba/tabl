import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tabel",
    version="1.0.0",
    author="Bastiaan Bergman",
    author_email="Bastiaan.Bergman@gmail.com",
    description="Lightweight, intuitive and fast data-tables.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/tabel",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)