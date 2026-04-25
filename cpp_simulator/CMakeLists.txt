cmake_minimum_required(VERSION 3.10)
project(lcct_simulator CXX)

# Require C++17 for std::filesystem and modern features
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Enable all warnings — clean code requirement
if(MSVC)
    add_compile_options(/W4)
else()
    add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# Include directories
include_directories(include)
include_directories(simulator)

# Source files
add_executable(lcct_simulator
    src/main.cpp
)

# Install target (optional)
install(TARGETS lcct_simulator DESTINATION bin)
