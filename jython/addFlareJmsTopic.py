import sys, java

def buildJmsTopic(abIdent):

   print ""
   print "buildJmsTopic: create Ejb Action Topic"
   AdminTask.createSIBJMSTopic('flare-cluster-' + abIdent + '(cells/psm-cell/clusters/flare-cluster-' + abIdent + '|cluster.xml)', '[-name "Ejb Action Topic" -jndiName com.vacationclub.solar.usage.bean_event_topic_jndi -description -topicSpace "Flare Ejb Action Topic Space" -topicName -deliveryMode Application -readAhead AsConnection -busName "Flare Bus"]')

   print ""
   print "buildJmsTopic: saving the configuration"
   AdminConfig.save()
 
#-----------------------------------------------------------------
# Main
#-----------------------------------------------------------------
if (len(sys.argv) != 1):

   print "buildJmsTopic: this script requires 1 parameter:"
   print "a/b identifier"
   print ""
   print "e.g.:     buildJmsTopic a" 

else:

   buildJmsTopic(sys.argv[0])

#endif