from base_generator import BaseGenerator
import os


class DatabaseGenerator(BaseGenerator):
    # temporary placeholder, fix after finding info on yaml side
    SB_DIRECTORY_PATH = "static/bsb_directory.csv"

    def __init__(self):
        super().__init__()
        self.file_name = self.latest_file('BSBDirectory', '.txt')

    def update_database(self):
        # print(self.SB_DIRECTORY_PATH)
        file_path = self.SB_DIRECTORY_PATH
        with open(file_path, 'wb') as f:
            self.ftp.retrbinary(f'RETR {self.file_name}', f.write)
            f.close()


if __name__ == '__main__':
    dbg = DatabaseGenerator()
    print(dbg.update_database())