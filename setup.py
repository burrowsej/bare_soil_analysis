from setuptools import find_packages, setup

__title__ = "bare_soil_analysis"
__description__ = "Analysis of bare soil across England"
__author_email__ = "Edward Burrows"
__author__ = "burrowsej@gmail.com"
__version__ = "0.1"
__licence__ = "MIT"

REQUIRED_PACKAGES = [
    "rasterio>=1.3.6",
    "pandas>=1.5.3",
    "seaborn>=0.12.2",
    "contextily>=1.3.0",
]

TEST_PACKAGES = [
    "black>=23.1.0",
    "flake8>=6.0.0",
    "isort>=5.12.0",
    "pytest>=7.2.1",
]

DEV_PACKAGES = [
    *TEST_PACKAGES,
    "pylint>=2.16.2",
    "ipython>=8.10.0",
    "ipykernel>=6.21.2",
    "ipywidgets>=8.0.4",
    "dbx>=0.7.0",
]


setup(
    name=__title__,
    description=__description__,
    version=__version__,
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    install_requires=REQUIRED_PACKAGES,
    extras_require={"test": TEST_PACKAGES, "dev": DEV_PACKAGES},
    author=__author__,
    author_email=__author_email__,
    licence=__licence__,
)
