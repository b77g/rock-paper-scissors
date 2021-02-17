# rock-paper-scissors
a simple & extensible rock-paper-scissors CLI game with ascii art.

### dependencies
python's built-in `math`, `random` and `os` modules.

### installation
download the zip folder (or clone the repostory)
and run `rps.py`.

### how to play
* there are three game formats: best-of-one, best-of-three and best-of-five.
* type `quit` or `exit` to quit the game.
* type `help` to see the available options again.

1. select the format you want to play and hit `ENTER`.

```
options: (r)ock, (p)aper, (s)cissors.
best of (1/3/5): 3
```

2. type one of the options and hit `ENTER`.

```
> your choice: p
```

3. the "AI" will randomly choose an option and you will face each other
until the game ends.

```

    +--------------------------------------+
    | your choice              AI's choice |
    | paper                           rock |
    |                                      |
    |     .-.                              |
    |   .-| |-.                            |
    |   | | | |                            |
    |   | | | |-.                          |
    |   | | | | |     WIN         _.-._    |
    |   |_|_|_| |    1 vs 0      | | | |-. |
    |  / )    `-|               / )|_|_|_| |
    | | | `--   |              | |-^-^-^-' |
    | |     ||  |              |     ||  | |
    | \     '   /              \     '   / |
    |  |       |                |       |  |
    |  |       |                |       |  |
    |                                      |
    +--------------------------------------+

> your choice: 
```

### credits
thanks to [ascii.co.uk](https://ascii.co.uk/art/finger) for the ascii art.

### to-do
- [x] show choice name on template
- [x] keyword to show choice options while playing
- [ ] support choices that start with the same first letter/s

### license
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
