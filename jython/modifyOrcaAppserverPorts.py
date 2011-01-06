import sys

def modifyAppserverPorts(appName, abIdent, hostName, nodeNum, serverNum):

   nodeName = 'psm-node' + nodeNum
   appsrvName = appName + '-node' + nodeNum + '-' + abIdent + serverNum
   node = AdminConfig.getid('/Node:' + nodeName + '/')

   print ""
   print "modifyAppserverPorts: Updating port settings on " + appsrvName

   if (abIdent == 'a'):

      if (appName == 'orca'):

         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName BOOTSTRAP_ADDRESS -host ' + hostName + ' -port 19814 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName CSIV2_SSL_MUTUALAUTH_LISTENER_ADDRESS -host ' + hostName + ' -port 19418 -modifyShared true]')
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName CSIV2_SSL_SERVERAUTH_LISTENER_ADDRESS -host ' + hostName + ' -port 19417 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName DCS_UNICAST_ADDRESS -host * -port 19361 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName ORB_LISTENER_ADDRESS -host ' + hostName + ' -port 0 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SAS_SSL_SERVERAUTH_LISTENER_ADDRESS -host ' + hostName + ' -port 19416 -modifyShared true]')
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SIB_ENDPOINT_ADDRESS -host ' + hostName + ' -port 17281]')
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SIB_ENDPOINT_SECURE_ADDRESS -host ' + hostName + ' -port 17290]')
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SIB_MQ_ENDPOINT_ADDRESS -host * -port 15562 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SIB_MQ_ENDPOINT_SECURE_ADDRESS -host * -port 15582 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SIP_DEFAULTHOST -host * -port 15068 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SIP_DEFAULTHOST_SECURE -host * -port 15069 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SOAP_CONNECTOR_ADDRESS -host ' + hostName + ' -port 18887 -modifyShared true]')
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName WC_adminhost -host * -port 19065 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName WC_adminhost_secure -host * -port 19048 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName WC_defaulthost -host ' + hostName + ' -port 19084]')
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName WC_defaulthost_secure -host * -port 19447 -modifyShared true]') 

      #endif


   #endif

   else:  # abIdent = b

      if (appName == 'orca'):

         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName BOOTSTRAP_ADDRESS -host ' + hostName + ' -port 29814 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName CSIV2_SSL_MUTUALAUTH_LISTENER_ADDRESS -host ' + hostName + ' -port 29418 -modifyShared true]')
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName CSIV2_SSL_SERVERAUTH_LISTENER_ADDRESS -host ' + hostName + ' -port 29417 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName DCS_UNICAST_ADDRESS -host * -port 29361 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName ORB_LISTENER_ADDRESS -host ' + hostName + ' -port 0 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SAS_SSL_SERVERAUTH_LISTENER_ADDRESS -host ' + hostName + ' -port 29416 -modifyShared true]')
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SIB_ENDPOINT_ADDRESS -host ' + hostName + ' -port 27281]')
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SIB_ENDPOINT_SECURE_ADDRESS -host ' + hostName + ' -port 27290]')
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SIB_MQ_ENDPOINT_ADDRESS -host * -port 25562 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SIB_MQ_ENDPOINT_SECURE_ADDRESS -host * -port 25582 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SIP_DEFAULTHOST -host * -port 25068 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SIP_DEFAULTHOST_SECURE -host * -port 25069 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName SOAP_CONNECTOR_ADDRESS -host ' + hostName + ' -port 28887 -modifyShared true]')
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName WC_adminhost -host * -port 29065 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName WC_adminhost_secure -host * -port 29048 -modifyShared true]') 
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName WC_defaulthost -host ' + hostName + ' -port 29084]')
         AdminTask.modifyServerPort (appsrvName, '[-nodeName ' + nodeName + ' -endPointName WC_defaulthost_secure -host * -port 29447 -modifyShared true]') 

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