# nixplot: A real-time graphing tool for \*nix systems

_nixplot_ follows the UNIX philosophy of 'do one thing well' - Get data from stdin and plot it in real time. _nixplot_ can also plot data from files.

## Requirements
_nixplot_ is written in python3. It uses matplotlib version 3.4.1.

## Usage
To test it out:

```shell
$ ./nixplot test/data/sin.txt
$ #OR
$ ./nixplot < test/data/sin.txt
$ #OR
$ ./test/script/sin.py | ./nixplot 
```

## TODOs
- Add a configuration framework to change hardcoded parameters
- Add dynamic window support
- Add option to save input data to a log

## License
This repository is licenced under `MIT Licence`
