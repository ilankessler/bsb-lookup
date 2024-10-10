"""Used to update the .csv files that store BSB prefixes and the directory of BSBs."""

import http.client
import os
import urllib.parse

_STATIC_BSB_DIRECTORY_URL = "https://bsb.auspaynet.com.au/Public/BSB_DB.NSF/getBSBFullCSV?OpenAgent"
_STATIC_KEY_TO_ABBREVIATION_URL = "https://bsb.auspaynet.com.au/Public/BSB_DB.NSF/getKeytoACSV?OpenAgent"


def _update_file(static_url: str, dest: str) -> str:
    parsed_url = urllib.parse.urlparse(static_url)

    conn = http.client.HTTPSConnection(parsed_url.netloc)

    conn.request("GET", parsed_url.path + "?" + parsed_url.query)
    response = conn.getresponse()

    if response.status != 302:
        raise Exception(f"Unexpected response status: {response.status}")

    redirect_url = response.getheader("Location")
    assert redirect_url is not None

    parsed_redirect_url = urllib.parse.urlparse(redirect_url)

    file_name = os.path.basename(parsed_redirect_url.path)

    conn = http.client.HTTPSConnection(parsed_redirect_url.netloc)
    conn.request("GET", parsed_redirect_url.path)
    response = conn.getresponse()

    file_bytes = response.read()

    with open(dest, "wb") as f:
        f.write(file_bytes)

    return file_name


if __name__ == "__main__":
    prefix_file_name = _update_file(
        static_url=_STATIC_KEY_TO_ABBREVIATION_URL, dest="./src/bsb/static/bsb_prefix_rules.csv"
    )

    directory_file_name: str = _update_file(
        static_url=_STATIC_BSB_DIRECTORY_URL, dest="./src/bsb/static/bsb_directory.csv"
    )

    with open(os.environ["GITHUB_OUTPUT"], "a") as output:
        print(f"bsb_prefix_file={prefix_file_name}", file=output)
        print(f"bsb_directory_file={directory_file_name}", file=output)
