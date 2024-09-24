from setuptools import setup, find_packages

setup(
    name="pdf_parser",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        'PyPDF2',
        'click',
    ],
    entry_points={
        'console_scripts': [
            'largest-number=pdf_parser.main:main',  # Command-line tool name
        ],
    },
)