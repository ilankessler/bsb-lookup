from bank_list_generator import BankListGenerator
from database_generator import DatabaseGenerator

if __name__ == '__main__':
    try:
        dbg = DatabaseGenerator()
        dbg.update_database()
        dbg.close_ftp()
    except Exception:
        raise f"Unable to update BSB Database, raised exception: {Exception}"

    try:
        blg = BankListGenerator()
        blg.update_banklist()
        blg.close_ftp()
    except Exception:
        raise f"Unable to update prefix rules, raised exception: {Exception}"