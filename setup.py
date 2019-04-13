from setuptools import setup

setup(
    name="tanner_to_eldo",
    version="0.1",
    py_modules=["tanner_to_eldo"],
    include_package_data=True,
    install_requires=["click"],
    entry_points="""
        [console_scripts]
        tanner_to_eldo=tanner_to_eldo.tanner_to_eldo:cli
    """,
)
