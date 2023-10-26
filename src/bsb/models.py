"""Models for the BSB package."""

from dataclasses import dataclass
from enum import Enum
from enum import auto
from typing import Literal

BSBPaymentsFlag = Literal["P", "PE", "PEH", "E", "EH", ""]


@dataclass
class BSBDirectoryRow:

    """A row from the /static/bsb_directory.csv file."""

    bsb: str
    financial_institution_code: str
    name: str | Literal["Closed"]
    street: str
    suburb: str
    state: str
    postcode: str
    payments_flag: BSBPaymentsFlag


@dataclass
class BSBPrefixRule:

    """The prefix rule for a given bank abbreviation - represents a row from the /static/bsb_prefix_rules.csv file."""

    key: str
    abbreviation: str
    bsb_prefixes: list[str]


class NPPSupport(str, Enum):

    """The NPP support status of a given BSB.
    LIKELY_UNSUPPORTED is "likely" because the institution may have supported it since the last time we updated the
    package.
    """

    SUPPORTED = auto()
    LIKELY_UNSUPPORTED = auto()
    UNKNOWN = auto()


@dataclass
class BankInfo:

    """The information for a given BSB number."""

    prefix_rule: BSBPrefixRule | None
    directory_entry: BSBDirectoryRow | None
    npp_support: NPPSupport
