import sys, java

def createMqQueueConnectionFactories (abIdent, qmName, host, port, channel, id):

   #mqjmsp = AdminConfig.getid('/Cell:psm-cell/ServerCluster:solar-cluster-' + abIdent + '/JMSProvider:WebSphere MQ JMS Provider') 
   mqjmsp = AdminConfig.getid('/Cell:psm-cell/ServerCluster:jservices-cluster-' + abIdent + '/JMSProvider:WebSphere MQ JMS Provider') 
   
   lineseparator = java.lang.System.getProperty('line.separator')
   template = AdminConfig.listTemplates('MQQueueConnectionFactory').split(lineseparator)[0]


   print "Creating Solar Queue Connection Factory"

   nameAttr = ["name", "MQConnectionFactory"]
   jndiAttr = ["jndiName", "jms/MQConnectionFactory"]
   descAttr = ["description", "This ConnectionFactories will produce XA QueueConnections"]
   qmAttr = '["queueManager", "' + qmName + '"]'
   hostAttr = '["host", "' + host + '"]'
   portAttr = '["port", "' + port + '"]'
   channelAttr = '["channel", "' + channel + '"]'
   ttAttr = ["transportType", "CLIENT"]
   cidAttr = '["clientID", "' + id + '"]'
   xaAttrs = ["XAEnabled", "True"]
   #mappAttrs = ["mappingConfigAlias", "DefaultPrincipalMapping"]

   mqqcfAttrs = [nameAttr, jndiAttr, qmAttr, descAttr, hostAttr, portAttr, channelAttr, ttAttr, cidAttr, xaAttrs]

   AdminConfig.createUsingTemplate("MQQueueConnectionFactory", mqjmsp, mqqcfAttrs, template)

  
   AdminConfig.save()


#-----------------------------------------------------------------
# Main
#-----------------------------------------------------------------
if (len(sys.argv) != 6):

   print "createMqQueueConnectionFactories: this script requires 6 parameters: "  
   print "a/b identifier, queue manager name, host name, port, channel, id"
   print "e.g.:wsadmin -lang jython -f e:\install-media\jython\NewFolder\addSolarMqQueueConnectionFactories.py a qmgr host.marriott.com 1421 channelname chuckwubba"

else:
  createMqQueueConnectionFactories(sys.argv[0], sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])

   
