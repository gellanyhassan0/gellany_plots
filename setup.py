import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gellany_plots",
    version=__version__,
    author="Elgilany Hassan",
    author_email="gellanyhassan0@gmail.com",
    description="hybrid plots analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gellanyhassan0/gellany_plots",
    project_urls={
        "Bug Tracker": "https://github.com/gellanyhassan0/gellany_plots/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL V3 License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
