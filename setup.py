#!/usr/bin/env python

# This is a shim to hopefully allow GitHub to detect the package.
# The build is done with Poetry.
# I don't think we need this

import setuptools

if __name__ == "__main__":
    setuptools.setup(name="pytest-mqtt")
