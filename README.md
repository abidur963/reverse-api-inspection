# Reverse API Inspection and Data Extraction

## Project Overview

This project demonstrates how to inspect a public REST API, understand HTTP requests and response headers, retrieve data using Python HTTPX, and extract records into a JSON file.

The project uses [JSONPlaceholder](https://jsonplaceholder.typicode.com/), a free public API for testing and learning.

## Learning Objectives

- Inspect API requests using browser Developer Tools.
- Understand HTTP request and response headers.
- Learn how HTTP status codes work.
- Send GET requests using Python HTTPX.
- Build a reusable API service wrapper.
- Extract and validate API records.
- Save extracted data in JSON format.

## API Information

**API Name:** JSONPlaceholder

**Base URL:** https://jsonplaceholder.typicode.com

**Posts Endpoint:** https://jsonplaceholder.typicode.com/posts

**Single Post Endpoint:** https://jsonplaceholder.typicode.com/posts/5

The posts endpoint returns 100 sample records. This public testing API does not require an authentication token.

## Technologies Used

- Python
- HTTPX
- JSON
- Visual Studio Code
- Google Chrome Developer Tools
- Git and GitHub

## Project Structure

```text
reverse-api-inspection/
│
├── app/
│   ├── __init__.py
│   └── service_wrapper.py
│
├── main.py
├── header_practice.py
├── data_extraction.py
├── extracted_posts.json
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd reverse-api-inspection
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## Running the Project

### Test HTTP headers and API connection

```bash
python header_practice.py
```

### Test the API service wrapper

```bash
python main.py
```

### Run the data extraction script

```bash
python data_extraction.py
```

## Data Extraction Process

The `data_extraction.py` script:

1. Connects to the JSONPlaceholder API.
2. Retrieves all posts.
3. Extracts the `id`, `userId`, `title`, and `body` fields.
4. Validates the extracted records.
5. Saves the records to `extracted_posts.json`.

## Test Results

The data extraction test completed successfully:

- API connection: SUCCESS
- Total records received: 100
- Valid records: 100
- Extracted records saved: 100
- Output file: `extracted_posts.json`

## Authentication Note

JSONPlaceholder is a public testing API and does not require an authentication token. No real API credentials are needed for this project.

## Security

The `.gitignore` file excludes local environment files, virtual environments, and Python cache files.

Never upload passwords, API keys, or private access tokens to GitHub.

## Conclusion

This project demonstrates basic reverse API inspection, HTTP request handling, Python-based API integration, and structured data extraction using HTTPX.