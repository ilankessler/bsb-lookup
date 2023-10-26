"""BSB Enricher.

A library designed to enrich BSB numbers with additional information.
"""

__version__ = "0.0.1"

from bsb.bank_info import dataset as dataset
from bsb.bank_info import to_bank_info as to_bank_info
from bsb.bank_info import to_bsb_prefix_rule as to_bsb_prefix_rule
from bsb.bank_info import to_directory_entry as to_directory_entry
from bsb.bank_info import to_npp_support as to_npp_support
from bsb.exceptions import InvalidBSBFormatException as InvalidBSBFormatException
from bsb.models import BankInfo as BankInfo
from bsb.models import BSBDirectoryRow as BSBDirectoryRow
from bsb.models import BSBPrefixRule as BSBPrefixRule
from bsb.models import NPPSupport as NPPSupport
