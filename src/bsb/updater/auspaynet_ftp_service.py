from ftplib import FTP
BASE_DIR = "/~auspaynetftp/bsb"


def fetch_latest_file(prefix: str, file_type: str):
    with FTP("bsb.hostedftp.com") as ftp:
        ftp.login()

        files = ftp.mlsd(BASE_DIR)

        ordered_files = sorted(files, key=lambda x: x[1]['modify'])

        matching_filename = next(
            (filename for filename, _ in ordered_files if
             filename.startswith(prefix) and filename.endswith(file_type)),
            None,
        )

        if matching_filename is None:
            return None

        bytes_file = bytearray()
        ftp.retrbinary(f"RETR {BASE_DIR}/{matching_filename}", lambda data: bytes_file.extend(data))

        return bytes_file
