# nixplot: A real-time graphing tool for \*nix systems

_nixplot_ follows the UNIX philosophy of 'do one thing well' - Get data from stdin and plot it in real time. _nixplot_ can also plot data from files. This can have several potential use cases:
- Plotting dynamic stock prices in real time
- Understanding network packet latencies
- Add option to save input data to a log

## Requirements
_nixplot_ is written in python3. It uses matplotlib version 3.4.1.

## Usage
_nixplot_ is meant to take graphing input data as and when it is dynamically produced. When used with classic UNIX utilities such as _awk_ and _sed_, it is very easy to plot almost any statistics with minimal effort.

To test _nixplot_:
```shell
$ ./nixplot test/data/sin.txt
$ #OR
$ ./nixplot < test/data/sin.txt
$ #OR
$ ./test/script/sin.py | ./nixplot 
```

## TODOs
- a configuration framework to change hardcoded parameters
- dynamic sliding window support
- option to save input data to a log
- multiple graphs plotted live

## License
This repository is licenced under `MIT Licence`
