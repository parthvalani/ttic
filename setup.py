import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="ttic",
    version="1.0.1",
    description="Convert tabular data to image for DCNN",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/parthvalani/ttic",
    author="Parth Valani",
    author_email="parthnvalani@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["img"],
    include_package_data=True,
    install_requires=["keras","Pillow","numpy"],
    entry_points={
        "console_scripts": [
            "img=img.__main__:main",
        ]
    },
)