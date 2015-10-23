 
/* RngStream.h for ANSI C */
#ifndef RNGSTREAM_H
#define RNGSTREAM_H
 


typedef struct InfoState * RngStream;

struct InfoState {
   double Cg[6], Bg[6], Ig[6];
   int Anti;
   int IncPrec;
   char *name;
};


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
 

#endif
 

