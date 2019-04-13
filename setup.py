from setuptools import setup

setup(
    name="tanner-to-eldo",
    version="0.1",
    py_modules=["tanner-to-eldo"],
    include_package_data=True,
    install_requires=["click"],
    entry_points="""
        [console_scripts]
        tanner-to-eldo=tanner-to-eldo.tanner-to-eldo:cli
    """,
)
