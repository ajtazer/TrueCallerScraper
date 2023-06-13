import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "TrueCallerScraper",
    version = "1.0.0",
    author = "TAZER",
    author_email = "tazeryeah@gmail.com",
    description = "TrueCallerScraper is a Python script that automates the extraction of profile names from the TrueCaller app using ADB and OCR",
    long_description=long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/ajtazer/TrueCallerScraper",
    project_urls = {
        "Documentation": "https://ajtazer.github.io/TrueCallerScraper/",
        "Bug Tracker": "https://github.com/ajtazer/TrueCallerScraper/issues",
        "Instagram": "https://www.instagram.com/anujrawatazer/"
    },
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        "Topic :: Software Development :: Libraries",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords='sample setuptools development Phone number search, TrueCaller, Missing digits, Automation, Python script, Data extraction, ADB, Android, Linux, Hacking, Python programming, Phone number lookup, Contact information, Reconnect, Missed calls',
    python_requires = ">=3.6",
    py_modules=["TrueCallerScraper"],
    package_dir={'':'src'}
)