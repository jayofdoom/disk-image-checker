"""Python setup.py for disk_image_checker package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("disk_image_checker", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="disk_image_checker",
    version=read("disk_image_checker", "VERSION"),
    description="Awesome disk_image_checker created by jayofdoom",
    url="https://github.com/jayofdoom/disk-image-checker/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="jayofdoom",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["disk_image_checker = disk_image_checker.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
