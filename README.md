# color-mask
This is a script that will mask a PNG image with a specified color. The default option will replace all non-transparent pixels with the inputed color, which is handy for editing single color icons. You can also replace a specified color inside the image using the `-r` (*replace*) option.

## Get Started
```
# Setup
pip3 install -r requirements.txt

# Usage
 ./color-mask ./PATH_TO_INPUT_FILE ./PATH_FOR_OUTPUT '#HEXCODE' [OPTIONS]
    (The Input file should be a PNG image)

* OPTIONS:
  -s            : Show a preview of the new Image at the end.
  -r '#HEXCODE' : Replace only pixels matching the following HEXCODE.
```
