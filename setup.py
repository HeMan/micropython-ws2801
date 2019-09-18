import sys

# Remove current dir from sys.path, otherwise setuptools will peek up our
# module instead of system.
sys.path.pop(0)
from setuptools import setup

setup(
    name="micropython-ws2801",
    py_modules=["ws2801"],
    version="1.0.0",
    description="MicroPython library for WS2801.",
    long_description="This library lets you control strands of WS2801 RGB LEDs.",
    keywords="ws2801 rgb led micropython",
    url="https://github.com/HeMan/micropython-ws2801",
    author="Jimmy Hedman",
    author_email="jimmy.hedman@gmail.com",
    maintainer="Jimmy Hedman",
    maintainer_email="jimmy.hedman@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: Implementation :: MicroPython",
        "License :: OSI Approved :: MIT License",
    ],
)
