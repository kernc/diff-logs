`diff-logs`
===========
[![Build Status](https://img.shields.io/github/actions/workflow/status/kernc/diff-logs/ci.yml?branch=master&style=for-the-badge)](https://github.com/kernc/diff-logs/actions)
[![Language: shell](https://img.shields.io/badge/lang-Shell-skyblue?style=for-the-badge)](https://github.com/kernc/diff-logs)
[![Language: Python](https://img.shields.io/badge/lang-Python-skyblue?style=for-the-badge)](https://github.com/kernc/diff-logs)
[![Source lines of code](https://img.shields.io/endpoint?url=https://ghloc.vercel.app/api/kernc/diff-logs/badge?filter=diff-logs.py,diff-logs$&style=for-the-badge&color=skyblue&label=SLOC)](https://github.com/kernc/diff-logs)
[![Script size](https://img.shields.io/github/languages/code-size/kernc/diff-logs?style=for-the-badge&color=skyblue)](https://github.com/kernc/diff-logs)
[![](https://img.shields.io/github/issues/kernc/diff-logs?style=for-the-badge)](#)

A command-line utility for diff'ing log files.

Quickly find diffing lines in all kinds of logs,
namely build/CI logs, server/container logs or any such.
Figure out _why exactly_ the shit is failing quickly.

The script works by replacing common stochastic string [patterns],
such as datetime timestamps, download speeds, temporary files,
HTTP header values, UUIDs, hash digests etc., with known fixed
values that a tool such as `diff` can then easily skip.

[patterns]: https://github.com/kernc/diff-logs/blob/master/diff-logs.py


Installation
------------
First, check if your OS distro already provides an installable `diff-logs` package.

Otherwise:
1. Star, [download](https://github.com/kernc/diff-logs/archive/refs/heads/master.zip)
   or clone repo.
2. (Optional) Create a symlink in your bin-dir pointing to `diff-logs` shell script:
   ```shell
   mkdir -p ~/.local/bin
   export PATH="~/.local/bin:$PATH"    # Also put in .bashrc or similar
   # Link script into your bin
   ln -s ~/path/to/diff-logs/diff-logs ~/.local/bin/diff-logs
   ```


Usage
-----
```shell
$ diff-logs --help

Usage: diff-logs < FILE1.log           # Print log file diff-friendly
       diff-logs FILE1.log FILE2.log   # Invoke $DIFFTOOL (e.g. diff)
```


Examples
--------
### Diff two log files
```shell
diff-logs FILE1 FILE2    # Invokes `diff`
# or
export DIFFTOOL=meld
diff-logs FILE1 FILE2    # Invokes `meld`
```

### Diff-friendly-format a single log file
```shell
diff-logs < FILE1 > FILE1.clean
```

-----
Finally, we can diff our logs with ease! 🥳

Improvements welcome!
