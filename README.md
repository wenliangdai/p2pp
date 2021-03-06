# p2pp

[![](https://img.shields.io/badge/python-2.7+-blue.svg?style=for-the-badge)](https://www.python.org/downloads/)
[![PyPI](https://img.shields.io/pypi/v/p2pp?style=for-the-badge)](https://pypi.org/project/p2pp/)
[![PyPI - Wheel](https://img.shields.io/pypi/wheel/p2pp?style=for-the-badge)](https://pypi.org/project/p2pp/)
[![PyPI - License](https://img.shields.io/pypi/l/p2pp?color=yellow&style=for-the-badge)](https://opensource.org/licenses/MIT)

A light weight library that can help you to convert a word from present tense to present participle tense, i.e. the "ing" form.

## Install

```bash
pip install p2pp
```

## Example
```python
from p2pp import p2pp

words = ['go', 'give', 'be', 'lie', 'hit']
for word in words:
    print(f'{word} -> {p2pp(word)}')
```

Output:

```
go -> going
give -> giving
be -> being
lie -> lying
hit -> hitting
```

## Requirements
Support both Python2 and Python3.

## License
MIT.
