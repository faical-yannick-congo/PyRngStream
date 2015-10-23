# PyRngStream
Python Module wrapping L'Ecuyer's C interface to the RngStreams. The backbone generator is the combined multiple recursive generator (CMRG) Mrg32k3a implemented in 64-bit floating-point arithmetic.

To be able to build and install this module you are required to install "SWIG".
It is a code wrapper in this case is wrapping the C interface into a python one.

For anaconda users it is simple to install SWIG: conda install swig.
For other users please go [swig_home](http://www.swig.org/index.php "here") to find the appropriate way to install swig on your platform.
NOTE: This module has been tested with SWIG v3.0.2

