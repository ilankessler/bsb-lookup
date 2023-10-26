"""Provides functions to fetch information about a BSB number."""

from __future__ import annotations

import re

from bsb.dataset import DataSet
from bsb.exceptions import InvalidBSBFormatException
from bsb.models import BankInfo
from bsb.models import BSBDirectoryRow
from bsb.models import BSBPrefixRule
from bsb.models import NPPSupport

dataset = DataSet()


def _bsb_format_validator(func):
    def wrapper(bsb: str):
        if not re.match(r"^\d{6}$", bsb):
            raise InvalidBSBFormatException(bsb)
        return func(bsb)

    return wrapper


@_bsb_format_validator
def to_bank_info(bsb: str) -> BankInfo:
    """Fetch information from the most up to date CSV of BSB rules provided by the Australian Payment
     Network https://bsb.auspaynet.com.au/public/BSB_DB.NSF/publicBSB.xsp.

    Args:
    ----
        bsb (str): The BSB number to fetch information for.

    Returns:
    -------
        BankInfo: The bank information for the given BSB number.
    """
    return BankInfo(
        prefix_rule=to_bsb_prefix_rule(bsb=bsb),
        npp_support=to_npp_support(bsb=bsb),
        directory_entry=to_directory_entry(bsb=bsb),
    )


@_bsb_format_validator
def to_bsb_prefix_rule(bsb: str) -> BSBPrefixRule | None:
    """Fetch bsb prefix rule from the most up to date CSV of BSB rules provided by the Australian Payment Network."""
    return next(
        (
            prefix_rule
            for prefix_rule in dataset.bsb_prefix_rules
            for bsb_prefix in prefix_rule.bsb_prefixes
            if bsb.startswith(bsb_prefix)
        ),
        None,
    )


@_bsb_format_validator
def to_directory_entry(bsb: str) -> BSBDirectoryRow | None:
    """Fetch directory entry from the most up to date CSV of BSB rules provided by the Australian Payment Network."""
    return dataset.bsb_directory.get(bsb)


@_bsb_format_validator
def to_npp_support(bsb: str) -> NPPSupport:
    """Fetch NPP support status from the most up to date CSV of BSB rules provided by the Australian Payment Network as
    well as some other known data sources.

    It is important to note that this data is not 100% accurate and should be used as a guide only as support may vary
    over time
    """
    if bsb in dataset.npp_supported_bsbs:
        return NPPSupport.SUPPORTED

    if bsb in dataset.npp_unsupported_bsbs:
        return NPPSupport.LIKELY_UNSUPPORTED

    directory = dataset.bsb_directory.get(bsb)

    if directory is not None and directory.payments_flag == "P":  # PAPER ONLY
        return NPPSupport.LIKELY_UNSUPPORTED

    return NPPSupport.UNKNOWN
