# python files wrapper

this python lib can wrap several files into one single file and vice versa.

__NOTE__: the format of files is not standard.

## format specification

`wrap` function gets some filenames and outputs a single file or a chunk of binary data.

output file has some header lines seperated by `'\n'` characters.

first line is number of original files stored in it. which is a string of decimal number encoded in `ascii` coding. let's say the number is `n`.

the next `2*n` lines of the file are as follows:

```
{filename}\n
{filesize(in bytes)}\n
```

then data of the files are concatenated after that.

## TODO

- make better functions.
- make tests.
- write some docs.
- make an installable package.
