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
 static double wrapCheck(float phi1, float phi2);
 static bool isInsideRCut(float eta1, float eta2, float phi1, float phi2,float deltaR_Max);
 private:


};

#endif
