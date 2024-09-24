# PDF Largest Number Finder

This tool helps you find the largest number in a PDF document, applying appropriate multipliers such as "in millions," "in billions," or "in thousands" to the numbers found in charts or tables. The tool is designed to process documents that contain financial summaries, technical tables, and other large-number data.

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

