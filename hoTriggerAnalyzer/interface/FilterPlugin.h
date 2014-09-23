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

  /*
   * Takes the difference of two phis, makes
   * sure they are not more than 2 pi.
   */
 static HORecHitCollection cleanHoRecHits(HORecHitCollection, double);

 private:


};

#endif
