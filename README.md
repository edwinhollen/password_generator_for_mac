# CLI password generator script for Mac

A simple dictionary-based password generator script for python3 on Mac OS. I wanted a way to quickly generate batches of readable passwords- this script can generate 1 or 1,000+ passwords, seeds the random module with bits of entropy from /dev/urandom, and uses the Mac OS built-in dictionary to pick words.

Requires python3

**Usage:** 

* Generate 1 password: `python3 generator.py`
* Generate 100 passwords: `python3 generator.py 100`

**Example:**

```
>python3 ./generator.py
dehgan glaumrie hydrocyst barkpeel unmatchably
```

```
>python3 ./generator.py 3
adelphian ectocardia voltameter unmoderately tribometer
venturia platine tediousness niobite claimer
cannon disparaging panthelematism pareiasauri unpraying
```
