# Root Makefile — delegates to cpp_simulator/

all: build

build:
	$(MAKE) -C cpp_simulator

run: build
	cd cpp_simulator && ./lcct_simulator

clean:
	$(MAKE) -C cpp_simulator clean

.PHONY: all build run clean
