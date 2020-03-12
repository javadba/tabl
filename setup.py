import setuptools

exec(open("tabl/_version.py").read())

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tabl",
    keywords='data table',
    version=__version__,
    author="Stephen Boesch",
    author_email="javadba@gmail.com",
    description="Lightweight, intuitive and fast data-tables. Forked from github.com/BastiaanBergman/tabel",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/javadba/tabl",
    packages=setuptools.find_packages(),
    license='MIT',
    python_requires='>=3.8',
    install_requires=['numpy', 'tabulate'],
    classifiers=[
#        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
#        "Programming Language :: Python :: 3.7",
#        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    project_urls={
        "Documentation": "https://tabl.readthedocs.io/en/stable/",
        "Source Code": "https://github.com/javadba/tabl",
    }
)
