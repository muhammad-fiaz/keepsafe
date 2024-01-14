from setuptools import setup, find_packages

VERSION = "0.0.1"

DESCRIPTION = 'Keepsafe: Securely store and distribute sensitive information like passwords and keys.'

with open("README.md", "r", encoding="utf-8") as fh:
    LONG_DESCRIPTION = fh.read()

setup(
    name="keepsafe",
    version=VERSION,
    author="Muhammad Fiaz",
    author_email="",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url='https://github.com/muhammad-fiaz/keepsafe',
    packages=find_packages(),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires='>=3.8',
    install_requires=[
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    license='MIT License',
    project_urls={
        'Source Code': 'https://github.com/muhammad-fiaz/keepsafe',
        'Bug Tracker': 'https://github.com/muhammad-fiaz/keepsafe/issues',
        'Documentation': 'https://github.com/muhammad-fiaz/keepsafe#readme',
    },
)

print("Happy Coding!")
