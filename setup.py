from setuptools import find_packages, setup


setup(
    name="dwys",
    packages=find_packages("src"),
    package_dir={"": "src"},
)
