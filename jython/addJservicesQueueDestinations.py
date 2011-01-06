import sys, java

def buildJsBusQueueDestinations(abIdent):

   print "buildJsBusQueueDestination: Building the JServices SIB Queue Destinations"

   AdminTask.createSIBDestination('[-bus "jsbus" -name "jsbus-enrollment-in1-qd" -type Queue -cluster jservices-cluster-' + abIdent + ' -description -reliability ASSURED_PERSISTENT ]')
   AdminTask.createSIBDestination('[-bus "jsbus" -name "jsbus-enrollment-out1-qd" -type Queue -cluster jservices-cluster-' + abIdent + ' -description -reliability ASSURED_PERSISTENT ]')
   AdminTask.createSIBDestination('[-bus "jsbus" -name "jsbus-enrollment-err1-qd" -type Queue -cluster jservices-cluster-' + abIdent + ' -description -reliability ASSURED_PERSISTENT ]')

   AdminTask.createSIBDestination('[-bus "jsbus" -name "jsbus-uvupdate-in1-qd" -type Queue -cluster jservices-cluster-' + abIdent + ' -description -reliability ASSURED_PERSISTENT ]')
   AdminTask.createSIBDestination('[-bus "jsbus" -name "jsbus-uvupdate-out1-qd" -type Queue -cluster jservices-cluster-' + abIdent + ' -description -reliability ASSURED_PERSISTENT ]')
   AdminTask.createSIBDestination('[-bus "jsbus" -name "jsbus-uvupdate-err1-qd" -type Queue -cluster jservices-cluster-' + abIdent + ' -description -reliability ASSURED_PERSISTENT ]')

   print ""
   print "buildJsBusQueueDestination: saving the configuration"

   AdminConfig.save()
 
#-----------------------------------------------------------------
# Main
#-----------------------------------------------------------------

if (len(sys.argv) != 1):

   print "buildJsBusQueueDestinations: this script requires 1 parameter:"
   print "     cluster a/b identifier"
   print ""
   print "e.g.:     buildJsBusQueueDestinations a" 

else:

   buildJsBusQueueDestinations(sys.argv[0])

#endif