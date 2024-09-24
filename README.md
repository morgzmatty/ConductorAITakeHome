# PDF Largest Number Finder

This tool helps you find the largest number in a PDF document. It could also apply the appropriate multipliers such as "in millions," "in billions," or "in thousands" to the numbers found in charts or tables. The tool is designed to process documents that contain financial summaries, technical tables, and other large-number data.

## Features

- Automatically applies multipliers based on the context (e.g., "in millions").
- Handles PDF documents with tables or charts.
- Resets multipliers when encountering sentences or textual boundaries.
- Provides the largest number and the page it was found on.

## Installation

To install and run the project, follow the steps below.

### 1. Clone this repository

Clone the repository using Git:

```bash
git clone git@github.com:morgzmatty/ConductorAITakeHome.git
cd ConductorAITakeHome
```

### 2. Install Requirements

Install the required dependencies using pip:

```bash
pip install .
```

## Usage

Once installed, you can use the tool by running the following command:

```bash
largest-number path/to/your/document.pdf
```
Replace path/to/your/document.pdf with the actual path to the PDF file you’d like to analyze.

To find the largest number when taking natural language guidance from the document into consideration,
you can run the command with the ```--include-bonus``` flag:

```bash
largest-number path/to/your/document.pdf --include-bonus`
```

## Development

If you want to modify or contribute to the project, follow these steps:

### 1. Install the project in “editable” mode

To install the project in a way that allows you to edit it while testing, run:

```bash
pip install -e .
```
This allows you to make changes to the code and immediately see the effects without reinstalling the package.

### 2. Running the script directly

You can also run the script directly by executing:

```bash
python -m my_project.main path/to/your/document.pdf
```