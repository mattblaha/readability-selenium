import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="readability-selenium",
    version="0.0.4",
    author="Matt Blaha",
    author_email="github@mattblaha.com",
    description="Extract output of Readability.js with Selenium",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://https://github.com/mattblaha/readability-selenium",
    packages=setuptools.find_packages(),
    install_requires = requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
)
