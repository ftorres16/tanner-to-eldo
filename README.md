# tanner-to-eldo

TannerEDA spice files are not compatible with Mentor Eldo by default. This script aims to make the work seamless.

## Installation

- Git clone this repository
- `pip install -e <path to this repository>`

## Usage

Run `tanner_to_eldo <path to your tanner netlist> <path to desired eldo netlist>`.

If you want the converted file to import a SPICE library, you can do so by settign the environment variable `CONVERTER_PDK`, and you can choose which library option with `CONVERTER_PDK_OPTIONS`.

For example, if you want to include the typical means (`tm`) case for a library of resistors (`res.lib`) you would do `export CONVERTER_PDK="res.lib"` and `export CONVERTER_PDK_OPTIONS="tm"` before running `tanner_to_eldo`.

## Supported analyses
- tran
- dc
- ac

## Related repos

If you find this repo useful, there's a good chance you may want to check some of my other related work as well.

- [tannner_to_eldo](https://github.com/ftorres16/tanner_to_eldo) can transform Tanner generated SPICE netlists into ELDO compatible ones.
- [plot_eldo_sims](https://github.com/ftorres16/plot_eldo_sims) can plot the JSON output of this command using Python's matlplotlib.
