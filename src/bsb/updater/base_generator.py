import csv
from ftplib import FTP


class BaseGenerator:
    MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    def __init__(self):
        # initialises the ftp connection
        try:
            self.ftp = FTP('bsb.hostedftp.com')
            self.ftp.login()
            super()
        except Exception:
            raise ConnectionError

    def close_ftp(self):
        self.ftp.close()

    def latest_file(self, matching_filename, file_format):
        try:
            self.ftp.dir()
            self.ftp.cwd('/~auspaynetftp/bsb')

            search_criteria = [matching_filename, file_format]

            try:
                # uses list comprehension to get all files that match the given search criteria
                directory = [file for file in self.ftp.mlsd() if all(x in file[0] for x in search_criteria)]

                # gets the file with the latest timestamp
                current_file = max(directory, key=lambda x: x[1]['modify'])
                file_name = current_file[0]

                return file_name
            except Exception:
                raise "Could not find valid file"
        except Exception:
            raise ConnectionError