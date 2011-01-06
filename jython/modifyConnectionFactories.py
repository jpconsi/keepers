import sys, java

def createMqQueueConnectionFactories (abIdent, host, port, channel, qmgr):

   
   mqjmsp = AdminConfig.getid('/Cell:psm-cell/ServerCluster:solar-cluster-' + abIdent + '/JMSProvider:WebSphere MQ JMS Provider/MQQueueConnectionFactory:MQConnectionFactory') 
   
   print "modifying Solar Queue Connection Factory"

   AdminConfig.modify(mqjmsp, [["mapping", [["mappingConfigAlias", "DefaultPrincipalMapping"]]]])
   AdminConfig.modify(mqjmsp, [["host", host]])
   AdminConfig.modify(mqjmsp, [["port", port]])
   AdminConfig.modify(mqjmsp, [["transportType", "CLIENT"]])
   AdminConfig.modify(mqjmsp, [["channel", channel]])
   AdminConfig.modify(mqjmsp, [["XAEnabled", "True"]])
   AdminConfig.modify(mqjmsp, [["queueManager", qmgr]])
   
     
   AdminConfig.save()


#-----------------------------------------------------------------
# Main
#-----------------------------------------------------------------
if (len(sys.argv) != 5):

   print "modifyMqQueueConnectionFactories: this script requires 5 parameters: "  
   print "a/b identifier, host name, port, channel"
   print "e.g.:     createMqQueueConnectionFactories a Qmgr"
#wsadmin -lang jython -f C:\Solar\addSolarMqQueueXAConnectionFactories.py a host.marriott.com portno channelname qmgr
else:
  createMqQueueConnectionFactories(sys.argv[0], sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

   
