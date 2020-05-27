import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="p2pp", # Replace with your own username
    version="0.0.6",
    author="Wenliang Dai",
    author_email="wenliang.dai.1995@gmail.com",
    description="Convert word from present tense to present participle tense",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wenliangdai/p2pp",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
)