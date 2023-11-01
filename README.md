# BSB Lookup

[![pypi](https://img.shields.io/pypi/v/bsb-lookup.svg)](https://pypi.python.org/pypi/bsb-lookup)
[![versions](https://img.shields.io/pypi/pyversions/bsb-lookup.svg)](https://github.com/ilankessler/bsb-lookup)
[![license](https://img.shields.io/github/license/ilankessler/bsb-lookup.svg)](https://github.com/ilankessler/bsb-lookup/blob/main/LICENSE)
![downloads](https://static.pepy.tech/badge/bsb-lookup)
[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Linting: Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

Australian Bank State Branch number enricher used for validating and looking up bank names given a BSB number. Ideal for financial applications, banking software, and fintech solutions.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Background](#background)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Installation

Before installing, ensure you have Python 3.x installed on your system. You can install BSB Lookup using pip:

```bash
pip install bsb-lookup
```

## Usage

Here's a simple example to get started with BSB Lookup:

```py
from bsb import to_bank_info

result = to_bank_info(bsb="082055")

print(result)

# >>> BankInfo(
# ...     prefix_rule=BSBPrefixRule(key="NAB", abbreviation="National Australia Bank Limited", bsb_prefixes=["08"]),
# ...     directory_entry=BSBDirectoryRow(
# ...         bsb="082055",
# ...         financial_institution_code="NAB",
# ...         name="Private NSW Banking Suite",
# ...         street="Level 5 2 Carrington St",
# ...         suburb="Sydney",
# ...         state="NSW",
# ...         postcode="2000",
# ...         payments_flag="PEH",
# ...     ),
# ...     npp_support=NPPSupport.SUPPORTED,
# ... )

```

## Background
A BSB, or Bank State Branch number, is a six-digit code used to identify the specific branch of an Australian bank or financial institution. The BSB is normally used in association with the account number system used by each financial institution.

<img width="400" alt="image" src="https://github.com/ilankessler/bsb-lookup/assets/11990626/e026f52e-5e0b-43a5-b124-bfa65d84f3f1">

## Contributing

Contributions are welcome! If you have a suggestion or want to contribute code, please follow these steps:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -am 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a pull request


## License

This project is licensed under the [MIT License](https://github.com/ilankessler/bsb-lookup/blob/main/LICENSE) - see the LICENSE file for details.

## Contact

For support or queries, reach out to ilan@refundid.com
