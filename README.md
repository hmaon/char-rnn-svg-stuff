# char-rnn-svg-stuff
tools and miscellaneous stuff surrounding my attempts to feed SVG to char-rnn and get SVG back out

clone https://github.com/dmandreev/char-rnn and get that working

mkdir data/_yourstuff_
copy some SVG files to data/_yourstuff_
in data/_yourstuff_ run ../../svgprep.sh to make an input.txt file

train char-rnn on your input.txt file with a command line reminiscent of: lua train.lua -rnn_size 666 -data_dir data/_yourstuff_

mkdir ./_yourstuff_
sample output into a file using genemoji.bat as a an example

e.g., `genemoji.bat > _yourstuff_\output.txt`
in _yourstuff_/ run `../nlautosvg.py < output.txt` to split file into SVG files and generate PNGs from them using Inkscape
you'll need Inkscape installed and in the path for PNG generation to work

Everything was done on Windows in a mix of cmd and bash environments so good luck.
