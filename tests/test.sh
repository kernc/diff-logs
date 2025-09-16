#!/bin/bash
set -eu
cd "${0%/*}"
diff test.out.txt <(../diff-logs < test.in.txt)
