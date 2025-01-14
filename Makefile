# Compiler and flags
CXX = g++

# Source files and output
SRC = main.cpp modules_cpp/day6_lib.cpp
OUT = main

# Build target
$(OUT): $(SRC)
	$(CXX) $(CXXFLAGS) -o $(OUT) $(SRC)

# Clean target
clean:
	rm -f $(OUT)
