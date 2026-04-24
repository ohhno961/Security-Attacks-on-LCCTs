# Makefile for LCCT Security Attack Simulator
# Simple alternative to CMake for quick builds.
#
# Usage:
#   make          — build the simulator
#   make run      — build and run
#   make clean    — remove build artifacts

CXX      = g++
CXXFLAGS = -std=c++17 -Wall -Wextra -Iinclude -Isimulator
TARGET   = lcct_simulator
SRC      = src/main.cpp

# Default target: build the simulator
$(TARGET): $(SRC)
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(SRC)
	@echo "Build successful: ./$(TARGET)"

# Build and run immediately
run: $(TARGET)
	./$(TARGET)

# Remove build artifacts
clean:
	rm -f $(TARGET)
	rm -rf output/filename_proxy/*.py
	rm -rf output/cross_file/*.py
	rm -rf output/hierarchical_level1/*.py
	rm -rf output/hierarchical_level2/*.py
	rm -rf output/privacy_extraction/*.py
	@echo "Clean complete"

.PHONY: run clean
