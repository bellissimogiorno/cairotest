This is a brief demo of the Cairo smart test framework.

## Install

Make sure you have `cairotest` installed by typing
```
pip3 cairotest
```

## Running the demo

To run the demo directly, type:
```
python3 -i test_simple_cairo_function.py
```

To run the demo via `pytest`, type:
```
pytest -svrPA test_simple_cairo_function.py
```

Examples of more advanced usage are noted in the file `../README.md`.  See also any file in [`ls ../int_fixedwidth/test*.py`](https://github.com/bellissimogiorno/cairo-integer-types/tree/main/int_fixedwidth) or [`ls ../int_unbounded/test*.py`](https://github.com/bellissimogiorno/cairo-integer-types/tree/main/int_unbounded).
