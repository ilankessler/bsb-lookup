"""Used to update the .csv files that store BSB prefixes and the directory of BSBs."""
import os

from auspaynet_ftp_service import fetch_latest_file


def _update_file(src_prefix: str, src_type: str, dest: str) -> str:
    file_bytes, file_name = fetch_latest_file(prefix=src_prefix, file_type=src_type)

    with open(dest, "wb") as f:
        f.write(file_bytes)

    return file_name


if __name__ == "__main__":
    prefix_file_name = _update_file(
        src_prefix="KEY TO ABBREVIATIONS AND BSB NUMBERS", src_type=".csv", dest="./src/bsb/static/bsb_prefix_rules.csv"
    )
    directory_file_name: str = _update_file(
        src_prefix="BSBDirectory", src_type=".csv", dest="./src/bsb/static/bsb_directory.csv"
    )
    with open(os.environ["GITHUB_OUTPUT"], "a") as output:
        print(f"bsb_prefix_file={prefix_file_name}", file=output)
        print(f"bsb_directory_file={directory_file_name}", file=output)
