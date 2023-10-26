"""Cached data sets for the BSB library."""

from functools import cached_property

from bsb.models import BSBPrefixRule
from bsb.parser import BSBDirectoryRow
from bsb.parser import _parse_bsb_directory_csv
from bsb.parser import _parse_bsb_prefix_rules_csv
from bsb.parser import _parse_npp_supported_csv
from bsb.parser import _parse_npp_unsupported_csv


class DataSet:

    """Cached data sets for the BSB library. Allows lazy loading of the data in from csv only when it is requested."""

    @cached_property
    def bsb_prefix_rules(self) -> list[BSBPrefixRule]:
        """Cached BSB prefix rules from the /static/bsb_prefix_rules.csv file."""
        return _parse_bsb_prefix_rules_csv()

    @cached_property
    def npp_supported_bsbs(self) -> set[str]:
        """Cached BSBs from the /static/npp_supported.csv file."""
        bsbs = _parse_npp_supported_csv()
        return set(bsbs)

    @cached_property
    def npp_unsupported_bsbs(self) -> set[str]:
        """Cached BSBs from the /static/npp_unsupported.csv file."""
        bsbs = _parse_npp_unsupported_csv()
        return set(bsbs)

    @cached_property
    def bsb_directory(self) -> dict[str, BSBDirectoryRow]:
        """Cached BSB directory rows from the /static/bsb_directory.csv file."""
        directory_rows = _parse_bsb_directory_csv()
        return {row.bsb: row for row in directory_rows}
