"""Provides a function to determine the most recent file posted on auspaynet ftp and retrieve it."""
from ftplib import FTP

BASE_DIR = "/~auspaynetftp/bsb"


def fetch_latest_file(prefix: str, file_type: str) -> tuple[bytearray, str]:
    """:param prefix: the prefix of the desired file i.e. 'BSBDirectory'
    :param file_type: the extension of the desired file i.e. '.csv'
    :return: a tuple consisting of the file contents in a bytearray and the name of the file
    """
    with FTP("bsb.hostedftp.com") as ftp:
        ftp.login()

        files = ftp.mlsd(BASE_DIR)

        ordered_files = sorted(files, reverse=True, key=lambda x: x[1]["modify"])

        matching_filename = next(
            (
                filename
                for filename, _ in ordered_files
                if filename.startswith(prefix) and filename.endswith(file_type)
            ),
            None,
        )

        if matching_filename is None:
            raise Exception(f"Unable to find matching file, file_prefix={prefix}, file_type={file_type}")

        bytes_file = bytearray()
        ftp.retrbinary(
            f"RETR {BASE_DIR}/{matching_filename}", lambda data: bytes_file.extend(data)
        )

        return bytes_file, matching_filename
