from setuptools import setup, find_packages

VERSION = "0.0.1"  # Version of your package
DESCRIPTION = 'Keepsafe: Securely store and distribute sensitive information like passwords and keys.'

# Reading the long description from the README file
with open("README.md", "r", encoding="utf-8") as fh:
    LONG_DESCRIPTION = fh.read()

# Setup function for your package
setup(
    name="keepsafe",  # Name of your package
    version=VERSION,  # Package version
    author="Muhammad Fiaz",  # Author name
    author_email="contact@muhammadfiaz.com",  # Author's email
    description=DESCRIPTION,  # Short description
    long_description=LONG_DESCRIPTION,  # Detailed description from README.md
    long_description_content_type="text/markdown",  # The format of the long description
    url='https://github.com/muhammad-fiaz/keepsafe',  # URL to the project's GitHub page
    packages=find_packages(),  # Automatically find all packages in the directory
    classifiers=[  # List of classifiers to categorize your package
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires='>=3.8',  # Minimum Python version required
    install_requires=[  # Any dependencies that are required to run your library
    'cryptography', 'pytest'
    ],
    setup_requires=['pytest-runner'],  # For running tests during installation
    tests_require=['pytest'],  # Specify dependencies needed for running tests
    license='MIT License',  # License under which the project is released
    project_urls={  # Additional URLs related to your project
        'Source Code': 'https://github.com/muhammad-fiaz/keepsafe',
        'Bug Tracker': 'https://github.com/muhammad-fiaz/keepsafe/issues',
        'Documentation': 'https://github.com/muhammad-fiaz/keepsafe#readme',
    },
)

print("Happy Safe!")
