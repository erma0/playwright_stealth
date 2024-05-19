import setuptools

with open("README.md", "r",encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="playwright-stealth",
    version="1.0.7",
    author="AtuboDad",
    author_email="lcjasas@sina.com",
    description="playwright stealth",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AtuboDad/playwright_stealth",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_data={"playwright_stealth": ["js/*.js"]},
    python_requires=">=3, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*",
    install_requires=[
        "playwright",
    ],
    extras_require={
        "test": [
            "pytest",
        ]
    },
)
