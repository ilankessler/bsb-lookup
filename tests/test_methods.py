"""Tests for the methods module."""
from __future__ import annotations

import pytest
from bsb import BankInfo
from bsb import BSBDirectoryRow
from bsb import BSBPrefixRule
from bsb import InvalidBSBFormatException
from bsb import NPPSupport
from bsb import dataset
from bsb import to_bank_info


def test_invalid_format_bsb():
    """Ensure that an invalid BSB raises an InvalidBSBFormatException."""
    with pytest.raises(InvalidBSBFormatException):
        to_bank_info(bsb="1123")

    with pytest.raises(InvalidBSBFormatException):
        to_bank_info(bsb="1123123123")


def test_valid_format_bsb():
    """Ensure that a valid BSB returns a BankInfo object."""
    result = to_bank_info(bsb="082055")
    assert result == BankInfo(
        prefix_rule=BSBPrefixRule(key="NAB", abbreviation="National Australia Bank Limited", bsb_prefixes=["08"]),
        directory_entry=BSBDirectoryRow(
            bsb="082055",
            financial_institution_code="NAB",
            name="Private NSW Banking Suite",
            street="Level 5 2 Carrington St",
            suburb="Sydney",
            state="NSW",
            postcode="2000",
            payments_flag="PEH",
        ),
        npp_support=NPPSupport.SUPPORTED,
    )


def test_not_found():
    """Ensure that a BSB that is not found returns None."""
    result = to_bank_info(bsb="000000")
    assert result == BankInfo(prefix_rule=None, directory_entry=None, npp_support=NPPSupport.UNKNOWN)


def test_csv_data_sane():
    """Ensure that the CSV data is sane."""
    all_bsb = set(dataset.bsb_directory.keys())

    assert dataset.npp_unsupported_bsbs - all_bsb == set()
    # assert dataset.npp_supported_bsbs - all_bsb == set()
