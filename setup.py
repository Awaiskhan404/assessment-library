import os
import re
from setuptools import setup, find_packages


def get_version():
    """
    Retrieve the version from fastyrcore/__init__.py.

    Returns:
        str: The version string.

    Raises:
        RuntimeError: If the version string is not found.
    """
    version_file = os.path.join('fastyrcore', '__init__.py')
    with open(version_file, 'r') as f:
        content = f.read()
        match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", content, re.M)
        if match:
            return match.group(1)
        raise RuntimeError("Unable to find version string.")


def parse_long_description(file_path):
    """
    Read and return the content of a given file.

    Args:
        file_path (str): Path to the file containing the long description.

    Returns:
        str: File content as a string.
    """
    with open(file_path, "r", encoding="utf-8") as fh:
        return fh.read()


REQUIRED_PACKAGES = [
    "requests",
    "pydantic",
    "python-dotenv",
    ""
]

EXTRAS = {
    'dev': ['pytest>=6.0.0', 'black'],
    'docs': ['sphinx', 'sphinx-rtd-theme'],
}

setup(
    name="fastyrcore",
    version=get_version(),
    author="Awais khan",
    author_email="contact@awaiskhan.com.pk",
    description="Fastyrcore acts as an interface between the three stages of an AI phone call pipeline. STT, LLM, TTS",
    long_description=parse_long_description("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/your-repo/fastyrcore",
    packages=find_packages(exclude=["tests*", "examples*"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=REQUIRED_PACKAGES,
    extras_require=EXTRAS,
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'fastyrcore-cli=fastyrcore.cli:main',
        ],
    },
)