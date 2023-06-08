#!/usr/bin/env python
from setuptools import dist
dist.Distribution().fetch_build_eggs(['setuptools_rust'])
from setuptools import setup
from setuptools_rust import Binding, RustExtension


setup(
    name="fibonacci_rust",
    version="0.1",
    rust_extensions=[RustExtension(
        ".fibonacci_rust.fibonacci_rust",
        path="Cargo.toml", binding=Binding.PyO3)],
    packages=["fibonacci_rust"],
    zip_safe=False,
)
