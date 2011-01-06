import sys, java

def buildFlareServiceIntegrationBus(abIdent):

   if (abIdent == 'a'):

      print "" 
      print "buildServiceIntegrationBus: Building the Flare Bus"
      AdminTask.createSIBus('[-bus "Flare Bus" -busSecurity false -scriptCompatibility 6.1 ]')

   #endif

   print ""
   print "buildServiceIntegrationBus: modifying the Flare Bus configuration"
   AdminTask.addSIBusMember('[-bus "Flare Bus" -cluster flare-cluster-' + abIdent + ' -fileStore -logSize 100 -minPermanentStoreSize 200 -maxPermanentStoreSize 500 -unlimitedPermanentStoreSize false -permanentStoreDirectory E:/WebSphere/AppServer/profiles/psm-dm/Cluster-' + abIdent + '-JMSMessages -minTemporaryStoreSize 200 -maxTemporaryStoreSize 500 -unlimitedTemporaryStoreSize false -temporaryStoreDirectory E:/WebSphere/AppServer/profiles/psm-dm/Cluster-' + abIdent + '-JMSMessages -logDirectory E:/WebSphere/AppServer/profiles/psm-dm/Cluster-' + abIdent + '-JMSMessages/log ]') 

   print ""
   print "buildServiceIntegrationBus: saving the configuration"

   AdminConfig.save()
 
#-----------------------------------------------------------------
# Main
#-----------------------------------------------------------------

if (len(sys.argv) != 1):

   print "buildFlareServiceIntegrationBus: this script requires 1 parameter:"
   print "a/b identifier"
   print ""
   print "e.g.:     buildFlareServiceIntegrationBus a" 

else:

   buildFlareServiceIntegrationBus(sys.argv[0])

#endif

