from setuptools import setup

setup(
    name="autotrade",
    version="0.1.0",
    description="Auto Trade Bot",
    author="Karunakar Gadireddy",
    author_email="karu2412@gmail.com",
    packages=["autotrade"],
    package_data={"": ["*.so", "*.dll"]},
    include_package_data=True,
)
