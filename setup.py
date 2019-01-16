from setuptools import setup


setup(
    name="isup",
    version="0.1",
    py_modules=["isup"],
    install_requires=[
        "Click",
        "requests"
    ],
    entry_points="""
        [console_scripts]
        isup=isup:cli
    """
)