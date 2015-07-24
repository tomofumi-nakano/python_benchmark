MAKE=make
PYTHON=python
PIP=pip

all:
	$(MAKE) bench

prepare:
	$(MAKE) install

install:
	$(PIP) install hacking
	$(PIP) install m3-cdecimal
	$(PIP) install gmpy2

test:
	flake8 bench.py

bench: test
	$(PYTHON) bench.py
