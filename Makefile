CXXFLAGS=-Os -I/usr/include/python2.7
SWIG=/usr/bin/env swig
PYTHON=/usr/bin/env python

_bitset.so: bitset.o bitset_wrap.o
	c++ -shared $^ -o $@
%_wrap.o: %_wrap.cxx
	c++ $(CXXFLAGS) -c $< -o $@
%_wrap.cxx: %.i
	$(SWIG) -python -c++ $<

.PHONY: clean test

clean:
	$(RM) *.o *.so *.cxx *.pyc
test:
	$(PYTHON) test.py < test.dat
