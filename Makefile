# Root Makefile for LCCT Security Attack Simulator

build:
	$(MAKE) -C cpp_simulator
	cp cpp_simulator/lcct_simulator ./lcct_simulator
	mkdir -p output/filename_proxy output/cross_file output/hierarchical_level1 output/hierarchical_level2 output/privacy_extraction

run: build
	./lcct_simulator

clean:
	$(MAKE) -C cpp_simulator clean
	rm -f ./lcct_simulator

.PHONY: build run clean
EOF
