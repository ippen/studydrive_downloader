import re
import fcntl


def get_lol_url(url: str):
    return url.replace('.net/', '.lol/')


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
