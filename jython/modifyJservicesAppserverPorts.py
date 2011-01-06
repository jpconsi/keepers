import sys

def modifyAppserverPorts(appName, abIdent, hostName, nodeNum, serverNum):

   nodeName = 'psm-node' + nodeNum
   appsrvName = appName + '-node' + nodeNum + '-' + abIdent + serverNum
   node = AdminConfig.getid('/Node:' + nodeName + '/')

   print ""
   print "modifyAppserverPorts: Updating port settings on " + appsrvName

   if (abIdent == 'a'):

      if (appName == 'jservices'):

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
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName WC_defaulthost -host ' + hostName + ' -port 19082]')
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName WC_defaulthost_secure -host * -port 19445 -modifyShared true]') 

      #endif


   #endif

   else:  # abIdent = b

      if (appName == 'jservices'):

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
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName WC_defaulthost -host ' + hostName + ' -port 29082]')
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName WC_defaulthost_secure -host * -port 29445 -modifyShared true]') 

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