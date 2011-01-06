import sys, java

def createMessageListenerPort(abIdent, nodeNum):

  server = AdminConfig.getid("/Cell:psm-cell/Node:psm-node" + nodeNum + "/Server:solar-node" + nodeNum + '-' + abIdent + "1/")
 
  mls = AdminConfig.list('MessageListenerService', server)
 
  new=AdminConfig.create('ListenerPort',mls,'[[name MQ_LISTENER_PORT][destinationJNDIName jms/LGF.SOLAR.PSI ][connectionFactoryJNDIName jms/MQConnectionFactory][maxMessages 100][maxRetries 0][maxSessions 10]]')
  
  AdminConfig.create('StateManageable', new, [['initialState', 'START']])
 
  AdminConfig.save()

#-----------------------------------------------------------------
# Main
#-----------------------------------------------------------------
if (len(sys.argv) < 2 ):

   print "createMessageListenerPort: this script requires 2 parameters: "  
   print " a/b identifier, nodeNum"
   print "e.g.:     SolarlistenerPort a 1 "

else:
   index = 1

   while ("%s" % (index)) <= sys.argv[1]:

      createMessageListenerPort(sys.argv[0], ("%s" % (index))) 
      index = index + 1

   #endwhile

#endif
 
      