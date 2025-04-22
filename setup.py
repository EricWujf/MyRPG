from setuptools import setup, find_packages

setup(
    name="my_rpg",
    version="0.1a1",
    packages=find_packages(),
    description="A custom RPG game system package",
    author="EricWu",
    author_email="ericwu.jf15@email.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)