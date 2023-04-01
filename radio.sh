#!/usr/bin/bash
#Arguments: 1. Frequency, 2. Gain 3. Sampling rate 4. squelch level
# 5.  
rtl_fm -f 144.8M -g 42 -s 22050 -l 0 - | multimon -t raw -a AFSK1200 /dev/stdin > test.txt

