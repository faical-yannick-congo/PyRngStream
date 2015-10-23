%module RngStream

%{
#define SWIG_FILE_WITH_INIT
#include "RngStream.h"
%}

//%{
//typedef struct InfoState * RngStream;
//struct InfoState {};
//%}

%typemap(in) unsigned long seed[ANY] {
  int i;
  if (!PySequence_Check($input)) {
    PyErr_SetString(PyExc_ValueError,"Expected a sequence");
    return NULL;
  }
  if (PySequence_Length($input) != 6) {
    PyErr_SetString(PyExc_ValueError,"Size mismatch. Expected 6 elements");
    return NULL;
  }
  $1 = (unsigned long *) malloc(6*sizeof(unsigned long));
  for (i = 0; i < 6; i++) {
    PyObject *o = PySequence_GetItem($input,i);
    if (PyNumber_Check(o)) {
      $1[i] = (unsigned long) PyFloat_AsDouble(o);
    } else {
      PyErr_SetString(PyExc_ValueError,"Sequence elements must be numbers");      
      free($1);
      return NULL;
    }
  }
}
%typemap(freearg) unsigned long seed[ANY] {
   if ($1) free($1);
}

%typemap(out) unsigned long seed[ANY] {
  int i;
  $result = PyList_New($1_dim0);
  for (i = 0; i < $1_dim0; i++) {
    PyObject *o = PyFloat_FromDouble((double) $1[i]);
    PyList_SetItem($result,i,o);
  }
}


int setPackageSeed (unsigned long seed[6]);

RngStream createStream (const char name[]);

void deleteStream (RngStream *pg);

void resetStartStream (RngStream g);

void resetStartSubstream (RngStream g);

void resetNextSubstream (RngStream g);

void setAntithetic (RngStream g, int a);

void increasedPrecis (RngStream g, int incp);

int setSeed (RngStream g, unsigned long seed[6]);

void advanceState (RngStream g, long e, long c);

void getState (RngStream g, unsigned long seed[6]);

void writeState (RngStream g);

void writeStateFull (RngStream g);

double randU01 (RngStream g);

int randInt (RngStream g, int i, int j);

 

