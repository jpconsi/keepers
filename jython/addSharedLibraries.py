import sys
from time import sleep

#--------------------------------------------------------------
# set up globals
#--------------------------------------------------------------
global AdminConfig
global AdminControl
global AdminApp

def addClassloaders(logicalMachineNumber, abIdent):

   #---------------------------------------------------------
   # We assume that there is only one cell, and we are on it
   #---------------------------------------------------------

   print "addSharedLibraries: Creating classloaders"
   
   serv = AdminConfig.getid("/Node:ws-node" + logicalMachineNumber + "/Server:owner-services-node" + logicalMachineNumber + '-' + abIdent + "1/")
   appServer = AdminConfig.list('ApplicationServer', serv)
   classLoader1 = AdminConfig.create('Classloader', appServer, [['mode',  'PARENT_FIRST']])
   AdminConfig.create('LibraryRef', classLoader1, [['libraryName', 'entrust'], ['sharedClassloader', 'true']])

   serv = AdminConfig.getid("/Node:ws-node" + logicalMachineNumber + "/Server:web-marketing-node" + logicalMachineNumber + '-' + abIdent + "1/")
   appServer = AdminConfig.list('ApplicationServer', serv)
   classLoader1 = AdminConfig.create('Classloader', appServer, [['mode',  'PARENT_FIRST']])
   AdminConfig.create('LibraryRef', classLoader1, [['libraryName', 'entrust'], ['sharedClassloader', 'true']])

   serv = AdminConfig.getid("/Node:ws-node" + logicalMachineNumber + "/Server:web-services-node" + logicalMachineNumber + '-' + abIdent + "1/")
   appServer = AdminConfig.list('ApplicationServer', serv)
   classLoader1 = AdminConfig.create('Classloader', appServer, [['mode',  'PARENT_FIRST']])
   AdminConfig.create('LibraryRef', classLoader1, [['libraryName', 'entrust'], ['sharedClassloader', 'true']])

   AdminConfig.save()


def addClusterLevelSharedLibraries(abIdent):

   #---------------------------------------------------------
   # We assume that there is only one cell, and we are on it
   #---------------------------------------------------------

   print "addSharedLibraries: Creating cluster level libraries"

   cellName = AdminControl.getCell()

   cluster = AdminConfig.getid("/Cell:" + cellName + "/ServerCluster:owner-services-cluster-" + abIdent + "/")

   AdminConfig.create('Library', cluster, [['name', 'entrust'], ['classPath', 'E:/mpcm/lib'], ['nativePath', 'E:/mpcm/lib/win32/ualjni.dll']])

   cluster = AdminConfig.getid("/Cell:" + cellName + "/ServerCluster:web-marketing-cluster-" + abIdent + "/")

   AdminConfig.create('Library', cluster, [['name', 'entrust'], ['classPath', 'E:/mpcm/lib'], ['nativePath', 'E:/mpcm/lib/win32/ualjni.dll']])

   cluster = AdminConfig.getid("/Cell:" + cellName + "/ServerCluster:web-services-cluster-" + abIdent + "/")

   AdminConfig.create('Library', cluster, [['name', 'entrust'], ['classPath', 'E:/mpcm/lib'], ['nativePath', 'E:/mpcm/lib/win32/ualjni.dll']])

   AdminConfig.save()


def addNodeLevelSharedLibraries(logicalMachineNumber, abIdent):

   #---------------------------------------------------------
   # We assume that there is only one cell, and we are on it
   #---------------------------------------------------------
   cellName = AdminControl.getCell()
   node = AdminConfig.getid("/Cell:" + cellName + "/Node:ws-node" + logicalMachineNumber + "/")

   if (abIdent == 'a'):

      print "addSharedLibraries: Creating node level libraries"

      AdminConfig.create('Library', node, [['name', 'acm-webservices-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/acm-webservices-ear']])
      AdminConfig.create('Library', node, [['name', 'admin-photogallery-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/admin-photogallery-ear']])
      AdminConfig.create('Library', node, [['name', 'admin-rcc-reservations-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/admin-rcc-reservations-ear']])
      AdminConfig.create('Library', node, [['name', 'admin-referrals-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/admin-referrals-ear']])
      AdminConfig.create('Library', node, [['name', 'admin-superuser-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/admin-superuser-ear']])
      AdminConfig.create('Library', node, [['name', 'admin-tipboard-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/admin-tipboard-ear']])
      AdminConfig.create('Library', node, [['name', 'admin-top10-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/admin-top10-ear']])
      AdminConfig.create('Library', node, [['name', 'admin-travel-insurance-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/admin-travel-insurance-ear']])
      AdminConfig.create('Library', node, [['name', 'admin-webuser-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/admin-webuser-ear']])
      AdminConfig.create('Library', node, [['name', 'authentication-service-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/authentication-service-ear']])
      AdminConfig.create('Library', node, [['name', 'authentication-webservices-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/authentication-webservices-ear']])
      AdminConfig.create('Library', node, [['name', 'careers-mvc-com-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/careers-mvc-com-ear']])
      AdminConfig.create('Library', node, [['name', 'client-exception-service-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/client-exception-service-ear']])
      AdminConfig.create('Library', node, [['name', 'customer-webservices-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/customer-webservices-ear']])
      AdminConfig.create('Library', node, [['name', 'di-scheduler-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/di-scheduler-ear']])
      AdminConfig.create('Library', node, [['name', 'friendshare-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/friendshare-ear']])
      AdminConfig.create('Library', node, [['name', 'friendshare-webservices-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/friendshare-webservices-ear']])
      AdminConfig.create('Library', node, [['name', 'golf-instruction-marriott-vacations-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/golf-instruction-marriott-vacations-ear']])
      AdminConfig.create('Library', node, [['name', 'grc-com-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/grc-com-ear']])
      AdminConfig.create('Library', node, [['name', 'grc-com-form-service-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/grc-com-form-service-ear']])
      AdminConfig.create('Library', node, [['name', 'grc-com-registration-service-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/grc-com-registration-service-ear']])
      AdminConfig.create('Library', node, [['name', 'keyring-webservices-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/keyring-webservices-ear']])
      AdminConfig.create('Library', node, [['name', 'loanservicing-webservices-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/loanservicing-webservices-ear']])
      AdminConfig.create('Library', node, [['name', 'logging-webservices-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/logging-webservices-ear']])
      AdminConfig.create('Library', node, [['name', 'marriott-asia-holidays-forms-service-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/marriott-asia-holidays-forms-service-ear']])
      AdminConfig.create('Library', node, [['name', 'marriott-friends-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/marriott-friends-ear']])
      AdminConfig.create('Library', node, [['name', 'marriott-pride-service-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/marriott-pride-service-ear']])
      AdminConfig.create('Library', node, [['name', 'marriott-timeshare-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/marriott-timeshare-ear']])
      AdminConfig.create('Library', node, [['name', 'marriott-vacation-club-forms-service-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/marriott-vacation-club-forms-service-ear']])
      AdminConfig.create('Library', node, [['name', 'marriott-vacations-classic-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/marriott-vacations-classic-ear']])
      AdminConfig.create('Library', node, [['name', 'marriott-vacations-forms-service-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/marriott-vacations-forms-service-ear']])
      AdminConfig.create('Library', node, [['name', 'marriott-vacations-prearrival-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/marriott-vacations-prearrival-ear']])
      AdminConfig.create('Library', node, [['name', 'marriott-villas-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/marriott-villas-ear']])
      AdminConfig.create('Library', node, [['name', 'marriott-villas-forms-service-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/marriott-villas-forms-service-ear']])
      AdminConfig.create('Library', node, [['name', 'marsha-proxy-com-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/marsha-proxy-com-ear']])
      AdminConfig.create('Library', node, [['name', 'mq-series'], ['classPath', 'E:/MQSeries/java/lib']])
      AdminConfig.create('Library', node, [['name', 'mt-com-301-servlet-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/mt-com-301-servlet-ear']])
      AdminConfig.create('Library', node, [['name', 'mt-forms-service-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/mt-forms-service-ear']])
      AdminConfig.create('Library', node, [['name', 'mvacations-forms-service-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/mvacations-forms-service-ear']])
      AdminConfig.create('Library', node, [['name', 'mvci-grm-registration-service-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/mvci-grm-registration-service-ear']])
      AdminConfig.create('Library', node, [['name', 'mvci-marsha-proxy-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/mvci-marsha-proxy-ear']])
      AdminConfig.create('Library', node, [['name', 'mvci-nexus-proxy-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/mvci-nexus-proxy-ear']])
      AdminConfig.create('Library', node, [['name', 'mvci-optin-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/mvci-optin-ear']])
      AdminConfig.create('Library', node, [['name', 'mvci-registration-service-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/mvci-registration-service-ear']])
      AdminConfig.create('Library', node, [['name', 'mvci-vcap-registration-service-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/mvci-vcap-registration-service-ear']])
      AdminConfig.create('Library', node, [['name', 'mv-com-prearrival-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/mv-com-prearrival-ear']])
      AdminConfig.create('Library', node, [['name', 'my-rcc-com-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/my-rcc-com-ear']])
      AdminConfig.create('Library', node, [['name', 'my-vc-com-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/my-vc-com-ear']])
      AdminConfig.create('Library', node, [['name', 'nexus-proxy-com-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/nexus-proxy-com-ear']])
      AdminConfig.create('Library', node, [['name', 'nexus-rcc-webservices-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/nexus-rcc-webservices-ear']])
      AdminConfig.create('Library', node, [['name', 'och-web-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/och-web-ear']])
      AdminConfig.create('Library', node, [['name', 'online-marketing-admin-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/online-marketing-admin-ear']])
      AdminConfig.create('Library', node, [['name', 'optin-admin-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/optin-admin-ear']])
      AdminConfig.create('Library', node, [['name', 'owner-info-service-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/owner-info-service-ear']])
      AdminConfig.create('Library', node, [['name', 'pipeline-webservices-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/pipeline-webservices-ear']])
      AdminConfig.create('Library', node, [['name', 'pos-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/pos-ear']])
      AdminConfig.create('Library', node, [['name', 'proxy-webservices-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/proxy-webservices-ear']])
      AdminConfig.create('Library', node, [['name', 'producer-webservices-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/producer-webservices-ear']])
      AdminConfig.create('Library', node, [['name', 'rcc-forms-service-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/rcc-forms-service-ear']])
      AdminConfig.create('Library', node, [['name', 'rcc-scheduler-ear'], ['classPath', 'E:/WebSphere/Appserver/mvci/config/rcc-scheduler-ear']])
      AdminConfig.create('Library', node, [['name', 'resort-service-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/resort-service-ear']])
      AdminConfig.create('Library', node, [['name', 'ritz-carlton-club-forms-services-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/ritz-carlton-club-forms-services-ear']])
      AdminConfig.create('Library', node, [['name', 'ritz-carlton-real-estate-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/ritz-carlton-real-estate-ear']])
      AdminConfig.create('Library', node, [['name', 'scheduler-com-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/scheduler-com-ear']])
      AdminConfig.create('Library', node, [['name', 'scheduler-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/scheduler-ear']])
      AdminConfig.create('Library', node, [['name', 'single-sign-on-com-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/single-sign-on-com-ear']])
      AdminConfig.create('Library', node, [['name', 'soa-admin-offerbuilder-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/soa-admin-offerbuilder-ear']])
      AdminConfig.create('Library', node, [['name', 'soa-authentication-services-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/soa-authentication-services-ear']])
      AdminConfig.create('Library', node, [['name', 'soa-csatravel-insurance-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/soa-csatravel-insurance-ear']])
      AdminConfig.create('Library', node, [['name', 'soa-euoffers-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/soa-euoffers-ear']])
      AdminConfig.create('Library', node, [['name', 'soa-ownerservices-services-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/soa-ownerservices-services-ear']])
      AdminConfig.create('Library', node, [['name', 'soa-reservation-services-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/soa-reservation-services-ear']])
      AdminConfig.create('Library', node, [['name', 'sso-webservices-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/sso-webservices-ear']])
      AdminConfig.create('Library', node, [['name', 'soa-webuser-services-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/soa-webuser-services-ear']])
      AdminConfig.create('Library', node, [['name', 'support-for-blue-2.1'], ['classPath', 'E:/WebSphere/AppServer/mvci/ear-environments/support-for-blue-2.1']])
      AdminConfig.create('Library', node, [['name', 'support-for-brown-2.1'], ['classPath', 'E:/WebSphere/AppServer/mvci/ear-environments/support-for-brown-2.1']])
      AdminConfig.create('Library', node, [['name', 'support-for-web-services-1.0'], ['classPath', 'E:/WebSphere/AppServer/mvci/ear-environments/support-for-web-services-1.0']])
      AdminConfig.create('Library', node, [['name', 'vacation-club-admin-form-service-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/vacation-club-admin-form-service-ear']])
      AdminConfig.create('Library', node, [['name', 'vacation-club-ap-tipboard-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/vacation-club-ap-tipboard-ear']])
      AdminConfig.create('Library', node, [['name', 'vacation-club-owners-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/vacation-club-owners-ear']])
      AdminConfig.create('Library', node, [['name', 'vc-com-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/vc-com-ear']])
      AdminConfig.create('Library', node, [['name', 'vc-com-prearrival-admin-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/vc-com-prearrival-admin-ear']])
      AdminConfig.create('Library', node, [['name', 'vc-com-prearrival-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/vc-com-prearrival-ear']])
      AdminConfig.create('Library', node, [['name', 'vcap-com-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/vcap-com-ear']])
      AdminConfig.create('Library', node, [['name', 'vcap-registration-service-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/vcap-registration-service-ear']])
      AdminConfig.create('Library', node, [['name', 'viewer-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/viewer-ear']])
      AdminConfig.create('Library', node, [['name', 'wcities-service-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/wcities-service-ear']])
      AdminConfig.create('Library', node, [['name', 'weather-service-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/weather-service-ear']])
      AdminConfig.create('Library', node, [['name', 'web-crm-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/web-crm-ear']])
      AdminConfig.create('Library', node, [['name', 'wmf-webservices-ear'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/wmf-webservices-ear']])

      AdminConfig.save()

   #endif


#-----------------------------------------------------------------
# Main
#-----------------------------------------------------------------
if (len(sys.argv) != 2):

   print "addSharedLibraries: this script requires 2 parameters:"
   print "     number of nodes, and cluster a/b identifier"

   print ""
   print "e.g.:     addSharedLibraries  4 a" 

else:

   addClusterLevelSharedLibraries(sys.argv[1])
   index = 1

   while ("%s" % (index)) <= sys.argv[0]:

      addNodeLevelSharedLibraries(("%s" % (index)), sys.argv[1])
      addClassloaders(("%s" % (index)), sys.argv[1])
      index = index + 1

   #endwhile

#endif
