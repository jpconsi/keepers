import sys, java

def createMqQueueConnectionFactories (abIdent, host, port, channel, id):

   mqjmsp = AdminConfig.getid('/Cell:psm-cell/ServerCluster:solar-cluster-' + abIdent + '/JMSProvider:WebSphere MQ JMS Provider') 
   lineseparator = java.lang.System.getProperty('line.separator')
   template = AdminConfig.listTemplates('MQQueueConnectionFactory').split(lineseparator)[0]


   print "Creating Solar Queue Connection Factory"

   nameAttr = ["name", "MQConnectionFactory"]
   jndiAttr = ["jndiName", "jms/MQConnectionFactory"]
   hostAttr = '["host", "' + host + '"]'
   portAttr = '["port", "' + port + '"]'
   channelAttr = '["channel", "' + channel + '"]'
   ttAttr = ["transportType", "CLIENT"]
   cidAttr = '["clientID", "' + id + '"]'

   mqqcfAttrs = [nameAttr, jndiAttr, hostAttr, portAttr, channelAttr, ttAttr, cidAttr]

   AdminConfig.createUsingTemplate("MQQueueConnectionFactory", mqjmsp, mqqcfAttrs, template)

   print "Creating Solar Support Queue Connection Factory"

   mqjmsp = AdminConfig.getid('/Cell:psm-cell/ServerCluster:solarsupport-cluster-' + abIdent + '/JMSProvider:WebSphere MQ JMS Provider') 

   nameAttr = ["name", "jmsServerConn"]
   jndiAttr = ["jndiName", "jms/jmsServerConn"]
   descAttr = ["description", "Connects to local QM"]
   qmAttr = ["queueManager", "mvcisolar1"]
   hostAttr = ["host", "localhost"]
   ttAttr = ["transportType", "BINDINGS"] 
   mqqcfAttrs = [nameAttr, jndiAttr, descAttr, qmAttr, hostAttr, ttAttr]

   AdminConfig.createUsingTemplate("MQQueueConnectionFactory", mqjmsp, mqqcfAttrs, template)

   AdminConfig.save()


#-----------------------------------------------------------------
# Main
#-----------------------------------------------------------------
if (len(sys.argv) != 5):

   print "createMqQueueConnectionFactories: this script requires 5 parameters: "  
   print "a/b identifier, host name, port, channel, id"
   print "e.g.:     createMqQueueConnectionFactories a host.marriott.com 1421 channelname chuckwubba"

else:
  createMqQueueConnectionFactories(sys.argv[0], sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

   
