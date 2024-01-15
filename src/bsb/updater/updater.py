from auspaynet_ftp_service import AuspaynetFTPService


def _update_file(src_prefix: str, src_type: str, dest: str) -> None:
    auspaynet_file: bytes = AuspaynetFTPService.fetch_latest_file(prefix=src_prefix, file_type=src_type)

    with open(dest, 'wb') as f:
        f.write(auspaynet_file)


if __name__ == '__main__':
    _update_file(src_prefix='KEY TO ABBREVIATIONS AND BSB NUMBERS', src_type='.csv', dest='static/bsb_prefix_rules.csv')
    _update_file(src_prefix='BSBDirectory', src_type='.csv', dest='static/bsb_directory.csv')

