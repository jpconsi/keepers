import sys, java

def buildBusTopicSpaceAndQueueDestinations(abIdent):

   print ""
   print "buildBusQueueDestination: Building the Flare Ejb Action Topic Space"
   AdminTask.createSIBDestination('[-bus "Flare Bus" -name "Flare Ejb Action Topic Space" -type TopicSpace -description -reliability ASSURED_PERSISTENT ]')

   print ""
   print "buildBusQueueDestination: Building the Flare Dynamic Service Queue"
   AdminTask.createSIBDestination('[-bus "Flare Bus" -name "Flare Dynamic Service Queue" -type Queue -cluster flare-cluster-' + abIdent + ' -description -reliability ASSURED_PERSISTENT ]')

   print ""
   print "buildBusQueueDestination: saving the configuration"

   AdminConfig.save()
 
#-----------------------------------------------------------------
# Main
#-----------------------------------------------------------------

if (len(sys.argv) != 1):

   print "buildBusTopicSpaceAndQueueDestinations: this script requires 1 parameter:"
   print "     cluster a/b identifier"
   print ""
   print "e.g.:     buildBusTopicSpaceAndQueueDestinations a" 

else:

   buildBusTopicSpaceAndQueueDestinations(sys.argv[0])

#endif