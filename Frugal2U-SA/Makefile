CXX=g++
#CXXFLAGS=-std=c++14 -Wall -Wextra -g -fsanitize=address
CXXFLAGS=-std=c++14 -O3
EXECUTABLES= frugal2u-sa 

all: $(EXECUTABLES)

frugal2u-sa: frugal2u-sa.cpp
	$(CXX) $(CXXFLAGS) -o $@ frugal2u-sa.cpp 

clean:
	rm -f $(EXECUTABLES) *.o *~
