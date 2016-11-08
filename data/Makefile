CXXFLAGS = -Wall -O2 -std=c++11
SOURCES=$(wildcard *.cpp)
OBJECTS=$(SOURCES:.cpp=.o)
EXECUTABLE=new

all: $(EXECUTABLE)

.cpp.o:
	$(CXX) $(CXXFLAGS) -c $< -o $@

$(EXECUTABLE): $(OBJECTS)
	$(CXX) $(CXXFLAGS) $^ -o $@

clean:
	$(RM) $(OBJECTS) $(EXECUTABLE)

.PHONY: clean all