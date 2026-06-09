from setuptools import setup, find_packages

setup(
    name="juxtacrine-ot",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "xenium-filter=juxtacrine_ot.cli.xenium_filter:main",
        ],
    },
)