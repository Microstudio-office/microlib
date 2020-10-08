import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="microlib", # Replace with your own username
    version="0.0.1",
    author="Microstudio",
    author_email="xiaozhouzhou2010@163.com",
    description="由微机工作室开发的一款便捷库",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="hhttps://github.com/Microstudio-office/microlib/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
