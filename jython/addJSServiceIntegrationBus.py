import sys, java

def buildJservicesServiceIntegrationBus(abIdent):

   if (abIdent == 'a'):

      print "" 
      print "buildJservicesServiceIntegrationBus: Building the JServices Bus"
      AdminTask.createSIBus('[-bus "jsbus" -busSecurity false -scriptCompatibility 6.1 ]')

   #endif

   print ""
   print "buildServiceIntegrationBus: modifying the JServices Bus configuration"
   AdminTask.addSIBusMember('[-bus "jsbus" -cluster jservices-cluster-' + abIdent + ' -fileStore -logSize 100 -minPermanentStoreSize 200 -maxPermanentStoreSize 500 -unlimitedPermanentStoreSize false -permanentStoreDirectory E:/WebSphere/AppServer/profiles/psm-dm/Cluster-' + abIdent + '-JMSMessages -minTemporaryStoreSize 200 -maxTemporaryStoreSize 500 -unlimitedTemporaryStoreSize false -temporaryStoreDirectory E:/WebSphere/AppServer/profiles/psm-dm/Cluster-' + abIdent + '-JMSMessages -logDirectory E:/WebSphere/AppServer/profiles/psm-dm/Cluster-' + abIdent + '-JMSMessages/log ]') 

   print ""
   print "buildServiceIntegrationBus: saving the configuration"

   AdminConfig.save()
 
#-----------------------------------------------------------------
# Main
#-----------------------------------------------------------------

if (len(sys.argv) != 1):

   print "buildJServicesServiceIntegrationBus: this script requires 1 parameter:"
   print "a/b identifier"
   print ""
   print "e.g.:     buildJServicesServiceIntegrationBus a" 

else:

   buildJservicesServiceIntegrationBus(sys.argv[0])

#endif

