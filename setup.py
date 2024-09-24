from setuptools import setup, find_packages

setup(
    name="my_project",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        'PyPDF2',  # Add other dependencies if needed
    ],
    entry_points={
        'console_scripts': [
            'largest-number=my_project.main:main',  # Command-line tool name
        ],
    },
)