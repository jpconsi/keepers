import sys, java

def buildJservicesQueues(abIdent):

   print ""
   print "buildJservicesQueues: create Jservices Queue"

   AdminTask.createSIBJMSQueue('jservices-cluster-' + abIdent + '(cells/psm-cell/clusters/jservices-cluster-' + abIdent + '|cluster.xml)', '[-name jsbus-enrollment-in1 -jndiName jms/jsbus-enrollment-in1 -description -queueName jsbus-enrollment-in1-qd -deliveryMode Application -readAhead AsConnection -busName "jsbus"]')
   AdminTask.createSIBJMSQueue('jservices-cluster-' + abIdent + '(cells/psm-cell/clusters/jservices-cluster-' + abIdent + '|cluster.xml)', '[-name jsbus-enrollment-out1 -jndiName jms/jsbus-enrollment-out1 -description -queueName jsbus-enrollment-out1-qd -deliveryMode Application -readAhead AsConnection -busName "jsbus"]')
   AdminTask.createSIBJMSQueue('jservices-cluster-' + abIdent + '(cells/psm-cell/clusters/jservices-cluster-' + abIdent + '|cluster.xml)', '[-name jsbus-enrollment-err1 -jndiName jms/jsbus-enrollment-err1 -description -queueName jsbus-enrollment-err1-qd -deliveryMode Application -readAhead AsConnection -busName "jsbus"]')

   AdminTask.createSIBJMSQueue('jservices-cluster-' + abIdent + '(cells/psm-cell/clusters/jservices-cluster-' + abIdent + '|cluster.xml)', '[-name jsbus-uvupdate-in1 -jndiName jms/jsbus-uvupdate-in1 -description -queueName jsbus-uvupdate-in1-qd -deliveryMode Application -readAhead AsConnection -busName "jsbus"]')
   AdminTask.createSIBJMSQueue('jservices-cluster-' + abIdent + '(cells/psm-cell/clusters/jservices-cluster-' + abIdent + '|cluster.xml)', '[-name jsbus-uvupdate-out1 -jndiName jms/jsbus-uvupdate-out1 -description -queueName jsbus-uvupdate-out1-qd -deliveryMode Application -readAhead AsConnection -busName "jsbus"]')
   AdminTask.createSIBJMSQueue('jservices-cluster-' + abIdent + '(cells/psm-cell/clusters/jservices-cluster-' + abIdent + '|cluster.xml)', '[-name jsbus-uvupdate-err1 -jndiName jms/jsbus-uvupdate-err1 -description -queueName jsbus-uvupdate-err1-qd -deliveryMode Application -readAhead AsConnection -busName "jsbus"]')


   print ""
   print "buildJmsQueue: saving the configuration"
   AdminConfig.save()
 
#-----------------------------------------------------------------
# Main
#-----------------------------------------------------------------
if (len(sys.argv) != 1):

   print "buildJservicesQueue: this script requires 1 parameter:"
   print "a/b identifier"
   print ""
   print "e.g.:     buildJservicesQueue a" 

else:

   buildJservicesQueues(sys.argv[0])

#endif