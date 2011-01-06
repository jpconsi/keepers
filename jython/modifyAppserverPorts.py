import sys

def modifyAppserverPorts(appName, abIdent, hostName, nodeNum, serverNum):

   nodeName = 'ws-node' + nodeNum
   appsrvName = appName + '-node' + nodeNum + '-' + abIdent + serverNum
   node = AdminConfig.getid('/Node:' + nodeName + '/')

   print ""
   print "modifyAppserverPorts: Updating port settings on " + appsrvName

   if (abIdent == 'a'):

      if (appName == 'asia-pacific'):

         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName BOOTSTRAP_ADDRESS -host ' + hostName + ' -port 19813 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName CSIV2_SSL_MUTUALAUTH_LISTENER_ADDRESS -host ' + hostName + ' -port 19415 -modifyShared true]')
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName CSIV2_SSL_SERVERAUTH_LISTENER_ADDRESS -host ' + hostName + ' -port 19414 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName DCS_UNICAST_ADDRESS -host * -port 19360 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName ORB_LISTENER_ADDRESS -host ' + hostName + ' -port 0 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SAS_SSL_SERVERAUTH_LISTENER_ADDRESS -host ' + hostName + ' -port 19413 -modifyShared true]')
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SIB_ENDPOINT_ADDRESS -host ' + hostName + ' -port 17280]')
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SIB_ENDPOINT_SECURE_ADDRESS -host ' + hostName + ' -port 17289]')
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SIB_MQ_ENDPOINT_ADDRESS -host * -port 15561 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SIB_MQ_ENDPOINT_SECURE_ADDRESS -host * -port 15581 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SIP_DEFAULTHOST -host * -port 15066 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SIP_DEFAULTHOST_SECURE -host * -port 15067 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SOAP_CONNECTOR_ADDRESS -host ' + hostName + ' -port 18886 -modifyShared true]')
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName WC_adminhost -host * -port 19064 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName WC_adminhost_secure -host * -port 19047 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName WC_defaulthost -host ' + hostName + ' -port 19083]')
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName WC_defaulthost_secure -host * -port 19446 -modifyShared true]') 

      #endif

      if (appName == 'owner-services'):

         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName BOOTSTRAP_ADDRESS -host ' + hostName + ' -port 19811 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName CSIV2_SSL_MUTUALAUTH_LISTENER_ADDRESS -host ' + hostName + ' -port 19409 -modifyShared true]')
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName CSIV2_SSL_SERVERAUTH_LISTENER_ADDRESS -host ' + hostName + ' -port 19408 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName DCS_UNICAST_ADDRESS -host * -port 19358 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName ORB_LISTENER_ADDRESS -host ' + hostName + ' -port 0 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SAS_SSL_SERVERAUTH_LISTENER_ADDRESS -host ' + hostName + ' -port 19407 -modifyShared true]')
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SIB_ENDPOINT_ADDRESS -host ' + hostName + ' -port 17278]')
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SIB_ENDPOINT_SECURE_ADDRESS -host ' + hostName + ' -port 17287]')
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SIB_MQ_ENDPOINT_ADDRESS -host * -port 15559 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SIB_MQ_ENDPOINT_SECURE_ADDRESS -host * -port 15579 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SIP_DEFAULTHOST -host * -port 15062 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SIP_DEFAULTHOST_SECURE -host * -port 15063 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SOAP_CONNECTOR_ADDRESS -host ' + hostName + ' -port 18884 -modifyShared true]')
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName WC_adminhost -host * -port 19062 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName WC_adminhost_secure -host * -port 19045 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName WC_defaulthost -host ' + hostName + ' -port 19081]')
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName WC_defaulthost_secure -host * -port 19444 -modifyShared true]') 

      #endif

      if (appName == 'web-marketing'):

         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName BOOTSTRAP_ADDRESS -host ' + hostName + ' -port 19810 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName CSIV2_SSL_MUTUALAUTH_LISTENER_ADDRESS -host ' + hostName + ' -port 19406 -modifyShared true]')
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName CSIV2_SSL_SERVERAUTH_LISTENER_ADDRESS -host ' + hostName + ' -port 19405 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName DCS_UNICAST_ADDRESS -host * -port 19357 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName ORB_LISTENER_ADDRESS -host ' + hostName + ' -port 0 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SAS_SSL_SERVERAUTH_LISTENER_ADDRESS -host ' + hostName + ' -port 19404 -modifyShared true]')
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SIB_ENDPOINT_ADDRESS -host ' + hostName + ' -port 17276]')
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SIB_ENDPOINT_SECURE_ADDRESS -host ' + hostName + ' -port 17286]')
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SIB_MQ_ENDPOINT_ADDRESS -host * -port 15558 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SIB_MQ_ENDPOINT_SECURE_ADDRESS -host * -port 15578 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SIP_DEFAULTHOST -host * -port 15060 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SIP_DEFAULTHOST_SECURE -host * -port 15061 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SOAP_CONNECTOR_ADDRESS -host ' + hostName + ' -port 18883 -modifyShared true]')
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName WC_adminhost -host * -port 19061 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName WC_adminhost_secure -host * -port 19044 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName WC_defaulthost -host ' + hostName + ' -port 19080]')
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName WC_defaulthost_secure -host * -port 19443 -modifyShared true]') 

      #endif

      if (appName == 'web-services'):

         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName BOOTSTRAP_ADDRESS -host ' + hostName + ' -port 19812 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName CSIV2_SSL_MUTUALAUTH_LISTENER_ADDRESS -host ' + hostName + ' -port 19412 -modifyShared true]')
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName CSIV2_SSL_SERVERAUTH_LISTENER_ADDRESS -host ' + hostName + ' -port 19411 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName DCS_UNICAST_ADDRESS -host * -port 19359 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName ORB_LISTENER_ADDRESS -host ' + hostName + ' -port 0 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SAS_SSL_SERVERAUTH_LISTENER_ADDRESS -host ' + hostName + ' -port 19410 -modifyShared true]')
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SIB_ENDPOINT_ADDRESS -host ' + hostName + ' -port 17279]')
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SIB_ENDPOINT_SECURE_ADDRESS -host ' + hostName + ' -port 17288]')
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SIB_MQ_ENDPOINT_ADDRESS -host * -port 15560 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SIB_MQ_ENDPOINT_SECURE_ADDRESS -host * -port 15580 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SIP_DEFAULTHOST -host * -port 15064 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SIP_DEFAULTHOST_SECURE -host * -port 15065 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SOAP_CONNECTOR_ADDRESS -host ' + hostName + ' -port 18885 -modifyShared true]')
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName WC_adminhost -host * -port 19063 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName WC_adminhost_secure -host * -port 19046 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName WC_defaulthost -host * -port 19082]')
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName WC_defaulthost_secure -host * -port 19445 -modifyShared true]') 

         tsName = AdminConfig.getid("/Cell:ws-cell/Node:" + nodeName + "/Server:" + appsrvName + "/TransportChannelService:/")
         epName = AdminTask.createTCPEndPoint(tsName , '[-name proxy-marsha -host * -port 19086]')
         AdminTask.createChain(tsName, '[-template "WebContainer(templates/chains|webcontainer-chains.xml#Chain_1)" -name proxy-marsha -endPoint ' + epName + ']')

         epName = AdminTask.createTCPEndPoint(tsName , '[-name proxy-nexus -host * -port 19087]')
         AdminTask.createChain(tsName, '[-template "WebContainer(templates/chains|webcontainer-chains.xml#Chain_1)" -name proxy-nexus -endPoint ' + epName + ']')

      #endif

   #endif

   else:  # abIdent = b

      if (appName == 'asia-pacific'):

         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName BOOTSTRAP_ADDRESS -host ' + hostName + ' -port 29813 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName CSIV2_SSL_MUTUALAUTH_LISTENER_ADDRESS -host ' + hostName + ' -port 29415 -modifyShared true]')
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName CSIV2_SSL_SERVERAUTH_LISTENER_ADDRESS -host ' + hostName + ' -port 29414 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName DCS_UNICAST_ADDRESS -host * -port 29360 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName ORB_LISTENER_ADDRESS -host ' + hostName + ' -port 0 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SAS_SSL_SERVERAUTH_LISTENER_ADDRESS -host ' + hostName + ' -port 29413 -modifyShared true]')
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SIB_ENDPOINT_ADDRESS -host ' + hostName + ' -port 27280]')
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SIB_ENDPOINT_SECURE_ADDRESS -host ' + hostName + ' -port 27289]')
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SIB_MQ_ENDPOINT_ADDRESS -host * -port 25561 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SIB_MQ_ENDPOINT_SECURE_ADDRESS -host * -port 25581 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SIP_DEFAULTHOST -host * -port 25066 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SIP_DEFAULTHOST_SECURE -host * -port 25067 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SOAP_CONNECTOR_ADDRESS -host ' + hostName + ' -port 28886 -modifyShared true]')
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName WC_adminhost -host * -port 29064 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName WC_adminhost_secure -host * -port 29047 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName WC_defaulthost -host ' + hostName + ' -port 29083]')
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName WC_defaulthost_secure -host * -port 29446 -modifyShared true]') 

      #endif

      if (appName == 'owner-services'):

         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName BOOTSTRAP_ADDRESS -host ' + hostName + ' -port 29811 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName CSIV2_SSL_MUTUALAUTH_LISTENER_ADDRESS -host ' + hostName + ' -port 29409 -modifyShared true]')
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName CSIV2_SSL_SERVERAUTH_LISTENER_ADDRESS -host ' + hostName + ' -port 29408 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName DCS_UNICAST_ADDRESS -host * -port 29358 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName ORB_LISTENER_ADDRESS -host ' + hostName + ' -port 0 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SAS_SSL_SERVERAUTH_LISTENER_ADDRESS -host ' + hostName + ' -port 29407 -modifyShared true]')
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SIB_ENDPOINT_ADDRESS -host ' + hostName + ' -port 27278]')
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SIB_ENDPOINT_SECURE_ADDRESS -host ' + hostName + ' -port 27287]')
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SIB_MQ_ENDPOINT_ADDRESS -host * -port 25559 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SIB_MQ_ENDPOINT_SECURE_ADDRESS -host * -port 25579 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SIP_DEFAULTHOST -host * -port 25062 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SIP_DEFAULTHOST_SECURE -host * -port 25063 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SOAP_CONNECTOR_ADDRESS -host ' + hostName + ' -port 28884 -modifyShared true]')
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName WC_adminhost -host * -port 29062 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName WC_adminhost_secure -host * -port 29045 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName WC_defaulthost -host ' + hostName + ' -port 29081]')
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName WC_defaulthost_secure -host * -port 29444 -modifyShared true]') 

      #endif

      if (appName == 'web-marketing'):

         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName BOOTSTRAP_ADDRESS -host ' + hostName + ' -port 29810 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName CSIV2_SSL_MUTUALAUTH_LISTENER_ADDRESS -host ' + hostName + ' -port 29406 -modifyShared true]')
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName CSIV2_SSL_SERVERAUTH_LISTENER_ADDRESS -host ' + hostName + ' -port 29405 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName DCS_UNICAST_ADDRESS -host * -port 29357 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName ORB_LISTENER_ADDRESS -host ' + hostName + ' -port 0 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SAS_SSL_SERVERAUTH_LISTENER_ADDRESS -host ' + hostName + ' -port 29404 -modifyShared true]')
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SIB_ENDPOINT_ADDRESS -host ' + hostName + ' -port 27276]')
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SIB_ENDPOINT_SECURE_ADDRESS -host ' + hostName + ' -port 27286]')
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SIB_MQ_ENDPOINT_ADDRESS -host * -port 25558 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SIB_MQ_ENDPOINT_SECURE_ADDRESS -host * -port 25578 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SIP_DEFAULTHOST -host * -port 25060 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SIP_DEFAULTHOST_SECURE -host * -port 25061 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SOAP_CONNECTOR_ADDRESS -host ' + hostName + ' -port 28883 -modifyShared true]')
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName WC_adminhost -host * -port 29061 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName WC_adminhost_secure -host * -port 29044 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName WC_defaulthost -host ' + hostName + ' -port 29080]')
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName WC_defaulthost_secure -host * -port 29443 -modifyShared true]') 

      #endif

      if (appName == 'web-services'):

         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName BOOTSTRAP_ADDRESS -host ' + hostName + ' -port 29812 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName CSIV2_SSL_MUTUALAUTH_LISTENER_ADDRESS -host ' + hostName + ' -port 29412 -modifyShared true]')
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName CSIV2_SSL_SERVERAUTH_LISTENER_ADDRESS -host ' + hostName + ' -port 29411 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName DCS_UNICAST_ADDRESS -host * -port 29359 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName ORB_LISTENER_ADDRESS -host ' + hostName + ' -port 0 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SAS_SSL_SERVERAUTH_LISTENER_ADDRESS -host ' + hostName + ' -port 29410 -modifyShared true]')
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SIB_ENDPOINT_ADDRESS -host ' + hostName + ' -port 27279]')
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SIB_ENDPOINT_SECURE_ADDRESS -host ' + hostName + ' -port 27288]')
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SIB_MQ_ENDPOINT_ADDRESS -host * -port 25560 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SIB_MQ_ENDPOINT_SECURE_ADDRESS -host * -port 25580 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SIP_DEFAULTHOST -host * -port 25064 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SIP_DEFAULTHOST_SECURE -host * -port 25065 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SOAP_CONNECTOR_ADDRESS -host ' + hostName + ' -port 28885 -modifyShared true]')
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName WC_adminhost -host * -port 29063 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName WC_adminhost_secure -host * -port 29046 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName WC_defaulthost -host * -port 29082]')
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName WC_defaulthost_secure -host * -port 29445 -modifyShared true]') 

         tsName = AdminConfig.getid("/Cell:ws-cell/Node:" + nodeName + "/Server:" + appsrvName + "/TransportChannelService:/")
         epName = AdminTask.createTCPEndPoint(tsName , '[-name proxy-marsha -host * -port 29086]')
         AdminTask.createChain(tsName, '[-template "WebContainer(templates/chains|webcontainer-chains.xml#Chain_1)" -name proxy-marsha -endPoint ' + epName + ']')

         epName = AdminTask.createTCPEndPoint(tsName , '[-name proxy-nexus -host * -port 29087]')
         AdminTask.createChain(tsName, '[-template "WebContainer(templates/chains|webcontainer-chains.xml#Chain_1)" -name proxy-nexus -endPoint ' + epName + ']')

      #endif

   #endif

   print ""
   print "modifyAppserverPorts: Saving configuration changes" 
   AdminConfig.save()

#-----------------------------------------------------------------
# Main
#-----------------------------------------------------------------
if (len(sys.argv) != 5):

   print "modifyAppserverPorts: this script requires 4 parameters:"
   print "app name, a/b identifier, host name, logical machine #, and"
   print "number of servers per node"
   print ""
   print "e.g.:     modifyAppserverPorts solar a lalfimvd0app03 1 1"

else:

   index = 1

   while ("%s" % (index)) <= sys.argv[4]:   # servers per node

      modifyAppserverPorts(sys.argv[0], sys.argv[1], sys.argv[2], sys.argv[3], ("%s" % (index)))
      index = index +1

    #endwhile

#endif
