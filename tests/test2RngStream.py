import RngStream
from ctypes import *


if __name__ == "__main__":

   summ = 0.0
   summ3 = 0.0
   summi = 0
   gar = []
   germe = [1,1,1,1,1,1]
   # print type(germe)

   g1 = RngStream.createStream("g1")
   g2 = RngStream.createStream("g2")
   g3 = RngStream.createStream("g3")

   print "Initial states of g1, g2, and g3:\n\n"
   RngStream.writeState(g1)
   RngStream.writeState(g2)
   RngStream.writeState(g3)

   summ = RngStream.randU01(g2) + RngStream.randU01(g3)
   for i in range(12345):
      RngStream.randU01(g2)

   RngStream.advanceState(g1, 5, 3) 
   print "State of g1 after advancing by 2^5 + 3 = 35 steps:\n"
   RngStream.writeState(g1)
   print "RandU01 (g1) = %12.8f\n\n"%RngStream.randU01(g1)

   RngStream.resetStartStream(g1)
   for i in range(35):    
      RngStream.advanceState(g1, 0, 1)
   print "State of g1 after reset and advancing 35 times by 1:\n"
   RngStream.writeState(g1)
   print "RandU01 (g1) = %12.8f\n\n"%RngStream.randU01(g1)

   RngStream.resetStartStream(g1)
   for i in range(35):   
      summi += RngStream.randInt(g1, 1, 10)
   print "State of g1 after reset and 35 calls to RandInt (1, 10):\n"
   RngStream.writeState(g1)
   print "   sum of 35 integers in [1, 10] = %ld\n\n"%summi
   summ += summi / 100.0;
   print "RandU01 (g1) = %12.8f\n\n"%RngStream.randU01(g1)

   summ3 = 0.0
   RngStream.resetStartStream(g1)
   RngStream.increasedPrecis(g1, 1)
   summi = 0
   for i in range(17):     
      summi += RngStream.randInt(g1, 1, 10)
   print "State of g1 after reset, IncreasedPrecis (1) and 17 calls  to RandInt (1, 10):\n"
   RngStream.writeState(g1)
   RngStream.increasedPrecis(g1, 0)
   RngStream.randInt(g1, 1, 10)
   print "State of g1 after IncreasedPrecis (0) and 1 call to RandInt\n"
   RngStream.writeState(g1)
   summ3 = summi / 10.0

   RngStream.resetStartStream(g1)
   RngStream.increasedPrecis(g1, 1)
   for i in range(17):   
      summ3 += RngStream.randU01(g1)
   print "State of g1 after reset, IncreasedPrecis (1) and 17 calls  to RandU01:\n"
   RngStream.writeState(g1)
   RngStream.increasedPrecis(g1, 0)
   RngStream.randU01(g1)
   print "State of g1 after IncreasedPrecis (0) and 1 call to RandU01\n"
   RngStream.writeState(g1)
   summ += summ3 / 10.0

   summ3 = 0.0;
   print "Sum of first 100 output values from stream g3:\n"
   for i in range(100):
      summ3 += RngStream.randU01(g3)

   print "   sum = %12.6f\n\n"%summ3
   summ += summ3 / 10.0;

   print "\nReset stream g3 to its initial seed.\n"
   RngStream.resetStartSubstream(g3)
   print "First 5 output values from stream g3:\n"
   for i in range(1, 6):
      print "%12.8f\n"%RngStream.randU01(g3)
   summ += RngStream.randU01(g3)

   print "\nReset stream g3 to the next Substream, 4 times.\n" 
   for i in range(1, 4):
      RngStream.resetNextSubstream(g3)
   print "First 5 output values from stream g3, fourth Substream:\n"
   for i in range(1, 6):
      print"%12.8f\n"%RngStream.randU01(g3)
   summ += RngStream.randU01(g3)

   print "\nReset stream g2 to the beginning of Substream.\n" 
   RngStream.resetStartSubstream(g2)
   print " Sum of 100000 values from stream g2 with double precision:   " 
   RngStream.increasedPrecis(g2, 1)
   summ3 = 0.0
   for i in range(1, 100001):
      summ3 += RngStream.randU01(g2)
   print "%12.4f\n"%summ3
   summ += summ3 / 10000.0
   RngStream.increasedPrecis(g2, 0)

   RngStream.setAntithetic(g3, 1)
   print " Sum of 100000 antithetic output values from stream g3:   "
   summ3 = 0.0
   for i in range(1, 100001):
      summ3 += RngStream.randU01(g3)
   print "%12.4f\n"%summ3
   summ += summ3 / 10000.0

   RngStream.deleteStream(g3)
   RngStream.deleteStream(g2)
   RngStream.deleteStream(g1)

   print "\nSetPackageSeed to seed = [ 1, 1, 1, 1, 1, 1 ]\n"
   RngStream.setPackageSeed(germe)

   print "\nCreate an array of 4 named streams and write their full state\n"
   gar.append(RngStream.createStream("Poisson"))
   gar.append(RngStream.createStream("Laplace"))
   gar.append(RngStream.createStream("Galois"))
   gar.append(RngStream.createStream("Cantor"))
   
   for i in range(4):
      RngStream.writeStateFull(gar[i])

   print "Jump stream Galois by 2^127 steps backward\n"
   RngStream.advanceState(gar[2], -127, 0)
   RngStream.writeState(gar[2])
   RngStream.resetNextSubstream(gar[2])

   for i in range(4):
      summ += RngStream.randU01(gar[i])

   print "--------------------------------------\n"
   print "Final Sum = %.6f\n\n"%summ
