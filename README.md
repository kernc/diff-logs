`diff-logs`
===========
[![Build Status](https://img.shields.io/github/actions/workflow/status/kernc/diff-logs/ci.yml?branch=master&style=for-the-badge)](https://github.com/kernc/diff-logs/actions)
[![Language: Perl](https://img.shields.io/badge/lang-Perl-056?style=for-the-badge)](https://github.com/kernc/diff-logs)
[![Source lines of code](https://img.shields.io/endpoint?url=https://ghloc.vercel.app/api/kernc/diff-logs/badge?filter=diff-logs$&style=for-the-badge&color=greenyellow&label=SLOC)](https://github.com/kernc/diff-logs)
[![Script size](https://img.shields.io/github/languages/code-size/kernc/diff-logs?style=for-the-badge&color=greenyellow)](https://github.com/kernc/diff-logs)
[![Bug tracker](https://img.shields.io/github/issues/kernc/diff-logs?style=for-the-badge)](https://github.com/kernc/diff-logs/issues)

A command-line utility for diff'ing log files.

Quickly find **difference lines** in **all kinds of logs**,
namely build/CI logs, server/container logs, or any similar such.
Figure out quickly **what changed** and _why exactly_ your shit is failing.

The script works by simply replacing common stochastic string [patterns],
such as datetime timestamps, download speeds, temporary filenames,
HTTP header values, UUIDs, hash digests etc. etc. with known fixed
values that a tool such as `diff` can then easily skip.

[patterns]: https://github.com/kernc/diff-logs/blob/master/diff-logs


Installation
------------
First, check if your OS distro already provides an installable `diff-logs` package.

Otherwise:
1. Star, [download](https://github.com/kernc/diff-logs/archive/refs/heads/master.zip)
   or clone repo. 🫶
2. Put `diff-logs` script into your bin-dir or elsewhere on `$PATH`:
   ```shell
   curl -vL https://github.com/kernc/diff-logs/raw/refs/heads/master/diff-logs
       sudo tee /usr/local/bin/diff-logs
   sudo chmod +x /usr/local/bin/diff-logs
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

#### Diff two log files
```shell
diff-logs FILE1 FILE2    # Invokes `diff`
# or
export DIFFTOOL=meld
diff-logs FILE1 FILE2    # Invokes `meld`
```

#### Diff-friendly-format a single log file
```shell
diff-logs < FILE1 > FILE1.clean
```

Notes
-----
This once was Python, but Perl is even more ubiquituous.

-----
Finally, we can diff our logs with ease! 🥳

Improvements and additions welcome!
