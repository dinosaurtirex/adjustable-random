import setuptools
  
with open("README.md", "r") as file:
    description = file.read()
  
setuptools.setup(
    name="adjustable_random package",
    version="1.0",
    author="dinosaurtirex",
    author_email="sneakybeaky18@gmail.com",
    packages=[
        "adjustable_random"
    ],
    description="Adjustable random number generator",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/dinosaurtirex/adjustable-random",
    license='MIT',
    python_requires='>=3.10',
    install_requires=[
        'matplotlib'
    ]
)