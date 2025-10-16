import urllib.parse


def join_url(base_url: str, url: str) -> str:
    return urllib.parse.urljoin(base_url, url)
