"""Parser for BSB data files store in static/ directory.
The data files are sourced from https://bsb.auspaynet.com.au/public/BSB_DB.NSF/publicBSB.xsp and updated regularly.
"""

from __future__ import annotations

import csv
import os
from collections.abc import Callable
from typing import TypeVar
from typing import cast

from bsb.models import BSBDirectoryRow
from bsb.models import BSBPaymentsFlag
from bsb.models import BSBPrefixRule

T = TypeVar("T")

BSB_DIRECTORY_PATH = "static/bsb_directory.csv"
NPP_SUPPORTED_PATH = "static/npp_supported.csv"
NPP_UNSUPPORTED_PATH = "static/npp_unsupported.csv"
BSB_PREFIX_RULES_PATH = "static/bsb_prefix_rules.csv"

current_dir = os.path.dirname(__file__)


def _parse_bsb_directory_csv() -> list[BSBDirectoryRow]:
    return _parse(BSB_DIRECTORY_PATH, _parse_row_to_bsb_directory_row)


def _parse_npp_supported_csv() -> list[str]:
    return _parse(NPP_SUPPORTED_PATH, _parse_row_to_bsb_str)


def _parse_npp_unsupported_csv() -> list[str]:
    return _parse(NPP_UNSUPPORTED_PATH, _parse_row_to_bsb_str)


def _parse_bsb_prefix_rules_csv() -> list[BSBPrefixRule]:
    return _parse(BSB_PREFIX_RULES_PATH, _parse_bsb_prefix_rule)


def _parse(filename: str, parse_row: Callable[[list[str]], T]) -> list[T]:
    csv_file_path = os.path.join(current_dir, filename)
    with open(csv_file_path, newline="", encoding="utf-8") as csvfile:
        return [parse_row(row) for row in csv.reader(csvfile)]


def _parse_row_to_bsb_directory_row(row: list[str]) -> BSBDirectoryRow:
    bsb, financial_institution_code, name, street, suburb, state, postcode, payments_flag = row

    return BSBDirectoryRow(
        bsb=bsb.replace("-", ""),
        financial_institution_code=financial_institution_code,
        name=name,
        street=street,
        suburb=suburb,
        state=state,
        postcode=postcode,
        payments_flag=cast(BSBPaymentsFlag, payments_flag),
    )


def _parse_row_to_bsb_str(row: list[str]) -> str:
    return str(row[0])


def _parse_bsb_prefix_rule(row: list[str]) -> BSBPrefixRule:
    key, abbreviation, bsb_prefixes = row
    return BSBPrefixRule(key=key, abbreviation=abbreviation, bsb_prefixes=bsb_prefixes.split(","))
