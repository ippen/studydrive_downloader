import requests
import re
import fcntl


def get_file_preview_url(url):
    # Send an HTTP GET request to the website
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Access the HTML source code of the website
        html_source = response.text
        # Use regular expressions to extract the "file_preview" URL
        html_source = html_source.replace('\n', '')
        pattern = r'"file_preview":"(.*?)"'
        matches = re.search(pattern, html_source)

        if matches:
            file_preview_url = matches.group(1)
            # Replace backslashes with forward slashes and "teaser" with "original"
            file_preview_url = file_preview_url.replace('\\', '')

            if requests.get(file_preview_url.replace('teaser', 'original')).status_code == 200:
                url_result = file_preview_url.replace('teaser', 'original')

            elif requests.get(file_preview_url.replace('teaser', 'converted')).status_code == 200:
                url_result = file_preview_url.replace('teaser', 'converted')
            else:
                # Use regex to find the value of "filename"
                pattern_filename = r'"filename":\s*"([^"]+)"'
                match_filename = re.search(pattern_filename, html_source)
                if match_filename:
                    # Extract the value of "filename"
                    filename_value = match_filename.group(1)
                    filename_value = filename_value.encode('utf-8').decode('unicode_escape').replace(' ', '%20')

                    # Define the regex pattern
                    pattern_pdf_id = r'\d+\.pdf'
                    # Replace the matched pattern with filename_value

                    file_url_with_name = re.sub(pattern_pdf_id, filename_value, file_preview_url)

                if requests.get(file_url_with_name.replace('teaser', 'original')).status_code == 200:
                    url_result = file_url_with_name.replace('teaser', 'original')
                elif requests.get(file_url_with_name.replace('teaser', 'converted')).status_code == 200:
                    url_result = file_url_with_name.replace('teaser', 'converted')
                else:
                    url_result = -1


            return url_result

        else:
            return None
    else:
        return None


def ensure_https_www_prefix(url):
    # If the URL does not start with 'http://' or 'https://', add 'https://'
    if url is not None:
        if not re.match(r'^(https?://)', url):
            url = 'https://' + url

        # If the URL does not contain 'www.', add it
        if not re.search(r'www\.', url):
            url = url.replace('https://', 'https://www.')

    return url

def is_valid_url(url):
    # Define a regular expression pattern for the specified URL format
    pattern = r'^https://www\.studydrive\.net/[a-z]+/doc/.+/\d+(?:\?.*)?$'


    # Use re.match() to check if the URL matches the pattern
    if re.match(pattern, url):
        return True
    else:
        return False


def counter_increase():
    with open('counter.txt', 'r+') as f:
        # Acquire an exclusive lock on the file
        fcntl.flock(f, fcntl.LOCK_EX)

        counter = int(f.read())
        counter += 1

        # Move the file cursor to the beginning and truncate the file
        f.seek(0)
        f.truncate()
        f.write(str(counter))

        # Release the lock
        fcntl.flock(f, fcntl.LOCK_UN)

def get_counter():
    with open('counter.txt', 'r') as f:
        # Acquire a shared lock on the file
        fcntl.flock(f, fcntl.LOCK_SH)

        counter = int(f.read())

        # Release the lock
        fcntl.flock(f, fcntl.LOCK_UN)

    return counter
