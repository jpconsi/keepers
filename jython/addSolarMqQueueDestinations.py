import sys, java

def createMqQueueDestinations (abIdent, baseQueueMgrName, queueExtId):

   mqjmsp = AdminConfig.getid('/Cell:psm-cell/ServerCluster:solar-cluster-' + abIdent + '/JMSProvider:WebSphere MQ JMS Provider') 

   lineseparator = java.lang.System.getProperty('line.separator')
   template = AdminConfig.listTemplates('MQQueue').split(lineseparator)[0]

   if (queueExtId != ''):

      queueExtId = '.' + queueExtId

   #endif

   nameAttr = ['name', 'PSI.AT.AMRE']
   jndiAttr = ['jndiName', 'jms/PSI.AT.AMRE']
   bqnAttr = ['baseQueueName', 'PSI.AT.AMRE' + queueExtId]
   bqmnAttr = ['baseQueueManagerName', '']
   tcAttr = ['targetClient', 'MQ']
   mqqAttrs = [nameAttr, jndiAttr, bqnAttr, bqmnAttr, tcAttr]

   AdminConfig.createUsingTemplate('MQQueue', mqjmsp, mqqAttrs, template)

   nameAttr = ['name', 'AMRE.AT.PSI']
   jndiAttr = ['jndiName', 'jms/AMRE.AT.PSI']
   bqnAttr = ['baseQueueName', 'AMRE.AT.PSI']
   bqmnAttr = ['baseQueueManagerName', baseQueueMgrName]
   tcAttr = ['targetClient', 'MQ']
   mqqAttrs = [nameAttr, jndiAttr, bqnAttr, bqmnAttr, tcAttr]

   AdminConfig.createUsingTemplate('MQQueue', mqjmsp, mqqAttrs, template)

   nameAttr = ['name', 'AMRE.ATSER.PSI']
   jndiAttr = ['jndiName', 'jms/AMRE.ATSER.PSI']
   bqnAttr = ['baseQueueName', 'AMRE.ATSER.PSI']
   bqmnAttr = ['baseQueueManagerName', baseQueueMgrName]
   tcAttr = ['targetClient', 'MQ']
   mqqAttrs = [nameAttr, jndiAttr, bqnAttr, bqmnAttr, tcAttr]

   AdminConfig.createUsingTemplate('MQQueue', mqjmsp, mqqAttrs, template)

   nameAttr = ['name', 'PSI.AT.SOLAR']
   jndiAttr = ['jndiName', 'jms/PSI.AT.SOLAR']
   bqnAttr = ['baseQueueName', 'PSI.AT.SOLAR']
   bqmnAttr = ['baseQueueManagerName', baseQueueMgrName]
   tcAttr = ['targetClient', 'MQ']
   mqqAttrs = [nameAttr, jndiAttr, bqnAttr, bqmnAttr, tcAttr]

   AdminConfig.createUsingTemplate('MQQueue', mqjmsp, mqqAttrs, template)

   nameAttr = ['name', 'PSI.STREQ.AMRE']
   jndiAttr = ['jndiName', 'jms/PSI.STREQ.AMRE']
   bqnAttr = ['baseQueueName', 'PSI.STREQ.AMRE' + queueExtId]
   bqmnAttr = ['baseQueueManagerName', '']
   tcAttr = ['targetClient', 'MQ']
   mqqAttrs = [nameAttr, jndiAttr, bqnAttr, bqmnAttr, tcAttr]

   AdminConfig.createUsingTemplate('MQQueue', mqjmsp, mqqAttrs, template)  

   nameAttr = ['name', 'PSI.STRPY.SOLAR']
   jndiAttr = ['jndiName', 'jms/PSI.STRPY.SOLAR']
   bqnAttr = ['baseQueueName', 'PSI.STRPY.SOLAR']
   bqmnAttr = ['baseQueueManagerName', baseQueueMgrName]
   tcAttr = ['targetClient', 'MQ']
   mqqAttrs = [nameAttr, jndiAttr, bqnAttr, bqmnAttr, tcAttr]

   AdminConfig.createUsingTemplate('MQQueue', mqjmsp, mqqAttrs, template)

   nameAttr = ['name', 'SOLAR.AT.PSI']
   jndiAttr = ['jndiName', 'jms/SOLAR.AT.PSI']
   bqnAttr = ['baseQueueName', 'SOLAR.AT.PSI']
   bqmnAttr = ['baseQueueManagerName', baseQueueMgrName]
   tcAttr = ['targetClient', 'MQ']
   mqqAttrs = [nameAttr, jndiAttr, bqnAttr, bqmnAttr, tcAttr]

   AdminConfig.createUsingTemplate('MQQueue', mqjmsp, mqqAttrs, template)

   nameAttr = ['name', 'SOLAR.STREQ.PSI']
   jndiAttr = ['jndiName', 'jms/SOLAR.STREQ.PSI']
   bqnAttr = ['baseQueueName', 'SOLAR.STREQ.PSI']
   bqmnAttr = ['baseQueueManagerName', baseQueueMgrName]
   tcAttr = ['targetClient', 'MQ']
   mqqAttrs = [nameAttr, jndiAttr, bqnAttr, bqmnAttr, tcAttr]

   AdminConfig.createUsingTemplate('MQQueue', mqjmsp, mqqAttrs, template)

   nameAttr = ['name', 'AMRE.STRPY.PSI']
   jndiAttr = ['jndiName', 'jms/AMRE.STRPY.PSI']
   bqnAttr = ['baseQueueName', 'AMRE.STRPY.PSI']
   bqmnAttr = ['baseQueueManagerName', baseQueueMgrName]
   tcAttr = ['targetClient', 'MQ']
   mqqAttrs = [nameAttr, jndiAttr, bqnAttr, bqmnAttr, tcAttr]

   AdminConfig.createUsingTemplate('MQQueue', mqjmsp, mqqAttrs, template)

   mqjmsp = AdminConfig.getid('/Cell:psm-cell/ServerCluster:solarsupport-cluster-' + abIdent + '/JMSProvider:WebSphere MQ JMS Provider') 

   nameAttr = ['name', 'jmsPsiAtQ']
   jndiAttr = ['jndiName', 'jms/jmsPsiAtQ']
   descAttr = ['description', "AMRE.AT.PSI queue"]
   pAttr = ['persistence', 'PERSISTENT']
   eAttr = ['expiry', 'UNLIMITED']
   bqnAttr = ['baseQueueName', 'AMRE.AT.PSI']
   bqmnAttr = ['baseQueueManagerName', baseQueueMgrName]
   tcAttr = ['targetClient', 'MQ']
   mqqAttrs = [nameAttr, jndiAttr, descAttr, pAttr, eAttr, bqnAttr, bqmnAttr, tcAttr]

   AdminConfig.createUsingTemplate('MQQueue', mqjmsp, mqqAttrs, template)

   AdminConfig.save()

#-----------------------------------------------------------------
# Main
#-----------------------------------------------------------------
if (len(sys.argv) < 2 or len(sys.argv) > 3):

   print "createMqQueueDestinations: this script requires 2 or 3 parameters: "  
   print " a/b identifier, base queue manager id, and queue extension identifier (optional)"
   print "e.g.:     createMqQueueDestinations a LALFIMVD3APP03 L14"

else:

   if (len(sys.argv) == 2):
   
      createMqQueueDestinations(sys.argv[0], sys.argv[1], '')

   else:

      createMqQueueDestinations(sys.argv[0], sys.argv[1], sys.argv[2])

   #endif

#endif