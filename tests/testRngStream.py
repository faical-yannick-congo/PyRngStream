import RngStream
from ctypes import *


if __name__ == "__main__":
   germe = [1,1,1,1,1,1]
   # print type(germe)

   g1 = RngStream.createStream("g1")
   g2 = RngStream.createStream("g2")
   g3 = RngStream.createStream("g3")

   summ = RngStream.randU01(g2) + RngStream.randU01(g3)

   RngStream.advanceState(g1, 5, 3) 
   summ += RngStream.randU01(g1)

   RngStream.resetStartStream(g1)

   for i in range(35):
      RngStream.advanceState(g1, 0, 1)
   summ += RngStream.randU01(g1)

   RngStream.resetStartStream(g1)
   sumi = 0
   for i in range(35):
      sumi += RngStream.randInt(g1, 1, 10)
   summ += sumi / 100.0

   sum3 = 0.0
   for i in range(100):
      sum3 += RngStream.randU01(g3)

   summ += sum3 / 10.0

   RngStream.resetStartStream(g3)
   for i in range(5):
      summ += RngStream.randU01(g3)

   for i in range(4):
      RngStream.resetNextSubstream(g3)
   for i in range(5):
      summ += RngStream.randU01(g3)

   RngStream.resetStartSubstream(g3)
   for i in range(5):
      summ += RngStream.randU01(g3)

   RngStream.resetNextSubstream(g2)
   sum3 = 0.0
   for i in range(100000):
      sum3 += RngStream.randU01(g2)
   summ += sum3 / 10000.0

   RngStream.setAntithetic(g3, 1)
   sum3 = 0.0
   for i in range(100000):
      sum3 += RngStream.randU01(g3)
   summ += sum3 / 10000.0

   RngStream.setPackageSeed(germe)
   gar = []
   gar.append(RngStream.createStream("Poisson"))
   gar.append(RngStream.createStream("Laplace"))
   gar.append(RngStream.createStream("Galois"))
   gar.append(RngStream.createStream("Cantor"))

   for i in range(4):
      summ += RngStream.randU01(gar[i])

   RngStream.advanceState(gar[2], -127, 0)
   summ += RngStream.randU01 (gar[2])

   RngStream.resetNextSubstream(gar[2])
   RngStream.increasedPrecis(gar[2], 1)
   sum3 = 0.0
   for i in range(100000):
      sum3 += RngStream.randU01(gar[2])
   summ += sum3 / 10000.0

   RngStream.setAntithetic(gar[2], 1)
   sum3 = 0.0
   for i in range(100000):
      sum3 += RngStream.randU01(gar[2])
   summ += sum3 / 10000.0
   RngStream.setAntithetic(gar[2], 0)

   RngStream.increasedPrecis(gar[2], 0)

   for i in range(4):
      summ += RngStream.randU01(gar[i])

   RngStream.deleteStream (g1)
   RngStream.deleteStream (g2)
   RngStream.deleteStream (g3)

   print "-------------------------------------------\n"
   print "This program should print   39.697547445251\n"
   print "Actual program result =     %.12f\n\n"%summ