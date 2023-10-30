# StudyDrive Downloader

This is a simple web application and Python library for downloading files from StudyDrive, a platform for sharing study materials and documents. With this tool, you can easily download study materials and generate preview links for documents hosted on StudyDrive.

## Getting Started

Follow the instructions below to get started with the StudyDrive Downloader:

### Prerequisites

- Python 3.7 or higher
- Flask (for web application)
- Requests (for web scraping)

### Installation

1. Clone this repository to your local machine:

```bash
git clone https://github.com/ippen/studydrive_downloader.git
```

2. Change to the project directory:

```bash
cd studydrive_downloader
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Starting the Website

To run the web application, use the following command:

```bash
python3 -m flask -A studydrive_downloader.py run
```

This will start a local web server that allows you to download files from StudyDrive.

### Using the Python Function

If you prefer to use the Python function to generate preview links, follow these steps:

1. Import the `get_file_preview_url` function from the `processing` module:

```python
from processing import get_file_preview_url
```

2. Use the function to generate a preview link by passing the StudyDrive URL as an argument:

```python
url = "https://www.studydrive.net/de/doc/formelsammlung-et2-ss20/923040"
preview_url = get_file_preview_url(url)
print("Preview URL:", preview_url)
```

This function will return the preview link for the document, which you can use to view the document without downloading it.

