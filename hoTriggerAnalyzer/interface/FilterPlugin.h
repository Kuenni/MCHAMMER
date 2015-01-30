#ifndef __FILTERPLUGIN_H__
#define __FILTERPLUGIN_H__

/*
 * Common Functions Class
 * Author Andreas Kuensken
 * 23. 09. 2014
 */

#include "DataFormats/HcalRecHit/interface/HcalRecHitCollections.h"

class FilterPlugin {

 public:

 static HORecHitCollection cleanHoRecHits(HORecHitCollection, double);
 /*
  * Takes the difference of two phis, makes
  * sure they are not more than 2 pi.
  */
 static double wrapCheck(double phi1, double phi2);
 static bool isInsideDeltaR(double eta1, double eta2, double phi1, double phi2,double deltaR_Max);
 private:


};

#endif
