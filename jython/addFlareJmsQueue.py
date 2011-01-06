import sys, java

def buildJmsQueue(abIdent):

   print ""
   print "buildJmsQueue: create Flare Dynamic Service Queue"
   AdminTask.createSIBJMSQueue('flare-cluster-' + abIdent + '(cells/psm-cell/clusters/flare-cluster-' + abIdent + '|cluster.xml)', '[-name "Flare Dynamic Service Queue" -jndiName com.vacationclub.solar.usage.manager.dynamic_service_queue_jndi -description -queueName "Flare Dynamic Service Queue" -deliveryMode Application -readAhead AsConnection -busName "Flare Bus"]')

   print ""
   print "buildJmsQueue: saving the configuration"
   AdminConfig.save()
 
#-----------------------------------------------------------------
# Main
#-----------------------------------------------------------------
if (len(sys.argv) != 1):

   print "buildJmsQueue: this script requires 1 parameter:"
   print "a/b identifier"
   print ""
   print "e.g.:     buildJmsQueue a" 

else:

   buildJmsQueue(sys.argv[0])

#endif