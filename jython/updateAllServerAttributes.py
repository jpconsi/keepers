import sys
from time import sleep

def updateAllServerAttributes(nodeNum):

   #--------------------------------------------------------------
   # set up globals
   #--------------------------------------------------------------

   global AdminConfig
   global AdminControl
   global AdminApp

   #---------------------------------------------------------
   # We assume that there is only one cell, and we are on it
   #---------------------------------------------------------

   print

   print "updateBobWebBusServerAttributes:updating bobwebbus-node" + nodeNum + "-a1/"

   serverName = AdminConfig.getid("/Node:psm-node" + nodeNum + "/Server:bobwebbus-node" + nodeNum + "-a1/")

   if (serverName): 

      osr = AdminConfig.showAttribute(serverName, "outputStreamRedirect")
      AdminConfig.modify(osr, [['rolloverType', 'TIME']])
      AdminConfig.modify(osr, [['maxNumberOfBackupFiles', '5']])

      esr = AdminConfig.showAttribute(serverName, "errorStreamRedirect")
      AdminConfig.modify(esr, [['rolloverType', 'TIME']])
      AdminConfig.modify(esr, [['maxNumberOfBackupFiles', '5']])

      pd =  AdminConfig.showAttribute(serverName, "processDefinitions")
      pd = pd[1:-1]
      mp = AdminConfig.showAttribute(pd, "monitoringPolicy")
      AdminConfig.modify(mp, [['nodeRestartState', 'RUNNING']])

      print "saving"
      AdminConfig.save()

   else:

         print "updateBobWebBusServerAttributes:bobwebbus-node" + nodeNum + "-a1/ does not exist."

   #endif

   print


   print "updateJservicesServerAttributes:updating jservices-node" + nodeNum + "-a1/"

   serverName = AdminConfig.getid("/Node:psm-node" + nodeNum + "/Server:jservices-node" + nodeNum + "-a1/")

   if (serverName): 

      osr = AdminConfig.showAttribute(serverName, "outputStreamRedirect")
      AdminConfig.modify(osr, [['rolloverType', 'TIME']])
      AdminConfig.modify(osr, [['maxNumberOfBackupFiles', '5']])

      esr = AdminConfig.showAttribute(serverName, "errorStreamRedirect")
      AdminConfig.modify(esr, [['rolloverType', 'TIME']])
      AdminConfig.modify(esr, [['maxNumberOfBackupFiles', '5']])

      pd =  AdminConfig.showAttribute(serverName, "processDefinitions")
      pd = pd[1:-1]
      mp = AdminConfig.showAttribute(pd, "monitoringPolicy")
      AdminConfig.modify(mp, [['nodeRestartState', 'RUNNING']])

      print "saving"
      AdminConfig.save()

   else:

         print "updateJservicesServerAttributes:jservices-node" + nodeNum + "-a1/ does not exist."

   #endif

   print


   print "updateMaatServerAttributes:maat-node" + nodeNum + "-a1/"

   serverName = AdminConfig.getid("/Node:psm-node" + nodeNum + "/Server:maat-node" + nodeNum + "-a1/")

   if (serverName): 

      osr = AdminConfig.showAttribute(serverName, "outputStreamRedirect")
      AdminConfig.modify(osr, [['rolloverType', 'TIME']])
      AdminConfig.modify(osr, [['maxNumberOfBackupFiles', '5']])

      esr = AdminConfig.showAttribute(serverName, "errorStreamRedirect")
      AdminConfig.modify(esr, [['rolloverType', 'TIME']])
      AdminConfig.modify(esr, [['maxNumberOfBackupFiles', '5']])

      pd =  AdminConfig.showAttribute(serverName, "processDefinitions")
      pd = pd[1:-1]
      mp = AdminConfig.showAttribute(pd, "monitoringPolicy")
      AdminConfig.modify(mp, [['nodeRestartState', 'RUNNING']])

      print "saving"
      AdminConfig.save()

   else:

         print "updateMaatServerAttributes:maat-node" + nodeNum + "-a1/ does not exist."

   #endif

   print


   print "updateSolarServerAttributes:solar-node" + nodeNum + "-a1/"

   serverName = AdminConfig.getid("/Node:psm-node" + nodeNum + "/Server:solar-node" + nodeNum + "-a1/")

   if (serverName): 

      osr = AdminConfig.showAttribute(serverName, "outputStreamRedirect")
      AdminConfig.modify(osr, [['rolloverType', 'TIME']])
      AdminConfig.modify(osr, [['maxNumberOfBackupFiles', '5']])

      esr = AdminConfig.showAttribute(serverName, "errorStreamRedirect")
      AdminConfig.modify(esr, [['rolloverType', 'TIME']])
      AdminConfig.modify(esr, [['maxNumberOfBackupFiles', '5']])

      pd =  AdminConfig.showAttribute(serverName, "processDefinitions")
      pd = pd[1:-1]
      mp = AdminConfig.showAttribute(pd, "monitoringPolicy")
      AdminConfig.modify(mp, [['nodeRestartState', 'RUNNING']])

      print "saving"
      AdminConfig.save()

   else:

         print "updateSolarServerAttributes:solar-node" + nodeNum + "-a1/ does not exist."

   #endif

   print


   print "updateSolarSupportServerAttributes:updating solarsupport-node" + nodeNum + "-a1/"

   serverName = AdminConfig.getid("/Node:psm-node" + nodeNum + "/Server:solarsupport-node" + nodeNum + "-a1/")

   if (serverName): 

      osr = AdminConfig.showAttribute(serverName, "outputStreamRedirect")
      AdminConfig.modify(osr, [['rolloverType', 'TIME']])
      AdminConfig.modify(osr, [['maxNumberOfBackupFiles', '5']])

      esr = AdminConfig.showAttribute(serverName, "errorStreamRedirect")
      AdminConfig.modify(esr, [['rolloverType', 'TIME']])
      AdminConfig.modify(esr, [['maxNumberOfBackupFiles', '5']])

      pd =  AdminConfig.showAttribute(serverName, "processDefinitions")
      pd = pd[1:-1]
      mp = AdminConfig.showAttribute(pd, "monitoringPolicy")
      AdminConfig.modify(mp, [['nodeRestartState', 'RUNNING']])

      print "saving"
      AdminConfig.save()

   else:

         print "updateSolarSupportServerAttributes:solarsupport-node" + nodeNum + "-a1/ does not exist."

   #endif

   print


   print "updateBobWebBusServerAttributes:updating bobwebbus-node" + nodeNum + "-b1/"

   serverName = AdminConfig.getid("/Node:psm-node" + nodeNum + "/Server:bobwebbus-node" + nodeNum + "-b1/")

   if (serverName): 

      osr = AdminConfig.showAttribute(serverName, "outputStreamRedirect")
      AdminConfig.modify(osr, [['rolloverType', 'TIME']])
      AdminConfig.modify(osr, [['maxNumberOfBackupFiles', '5']])

      esr = AdminConfig.showAttribute(serverName, "errorStreamRedirect")
      AdminConfig.modify(esr, [['rolloverType', 'TIME']])
      AdminConfig.modify(esr, [['maxNumberOfBackupFiles', '5']])

      pd =  AdminConfig.showAttribute(serverName, "processDefinitions")
      pd = pd[1:-1]
      mp = AdminConfig.showAttribute(pd, "monitoringPolicy")
      AdminConfig.modify(mp, [['nodeRestartState', 'RUNNING']])

      print "saving"
      AdminConfig.save()

   else:

         print "updateBobWebBusServerAttributes:bobwebbus-node" + nodeNum + "-b1/ does not exist."

   #endif

   print


   print "updateJservicesServerAttributes:updating jservices-node" + nodeNum + "-b1/"

   serverName = AdminConfig.getid("/Node:psm-node" + nodeNum + "/Server:jservices-node" + nodeNum + "-b1/")

   if (serverName): 

      osr = AdminConfig.showAttribute(serverName, "outputStreamRedirect")
      AdminConfig.modify(osr, [['rolloverType', 'TIME']])
      AdminConfig.modify(osr, [['maxNumberOfBackupFiles', '5']])

      esr = AdminConfig.showAttribute(serverName, "errorStreamRedirect")
      AdminConfig.modify(esr, [['rolloverType', 'TIME']])
      AdminConfig.modify(esr, [['maxNumberOfBackupFiles', '5']])

      pd =  AdminConfig.showAttribute(serverName, "processDefinitions")
      pd = pd[1:-1]
      mp = AdminConfig.showAttribute(pd, "monitoringPolicy")
      AdminConfig.modify(mp, [['nodeRestartState', 'RUNNING']])

      print "saving"
      AdminConfig.save()

   else:

         print "updateJservicesServerAttributes:jservices-node" + nodeNum + "-b1/ does not exist."

   #endif

   print


   print "updateMaatServerAttributes:maat-node" + nodeNum + "-b1/"

   serverName = AdminConfig.getid("/Node:psm-node" + nodeNum + "/Server:maat-node" + nodeNum + "-b1/")

   if (serverName): 

      osr = AdminConfig.showAttribute(serverName, "outputStreamRedirect")
      AdminConfig.modify(osr, [['rolloverType', 'TIME']])
      AdminConfig.modify(osr, [['maxNumberOfBackupFiles', '5']])

      esr = AdminConfig.showAttribute(serverName, "errorStreamRedirect")
      AdminConfig.modify(esr, [['rolloverType', 'TIME']])
      AdminConfig.modify(esr, [['maxNumberOfBackupFiles', '5']])

      pd =  AdminConfig.showAttribute(serverName, "processDefinitions")
      pd = pd[1:-1]
      mp = AdminConfig.showAttribute(pd, "monitoringPolicy")
      AdminConfig.modify(mp, [['nodeRestartState', 'RUNNING']])

      print "saving"
      AdminConfig.save()

   else:

         print "updateMaatServerAttributes:maat-node" + nodeNum + "-b1/ does not exist."

   #endif

   print


   print "updateSolarServerAttributes:solar-node" + nodeNum + "-b1/"

   serverName = AdminConfig.getid("/Node:psm-node" + nodeNum + "/Server:solar-node" + nodeNum + "-b1/")

   if (serverName): 

      osr = AdminConfig.showAttribute(serverName, "outputStreamRedirect")
      AdminConfig.modify(osr, [['rolloverType', 'TIME']])
      AdminConfig.modify(osr, [['maxNumberOfBackupFiles', '5']])

      esr = AdminConfig.showAttribute(serverName, "errorStreamRedirect")
      AdminConfig.modify(esr, [['rolloverType', 'TIME']])
      AdminConfig.modify(esr, [['maxNumberOfBackupFiles', '5']])

      pd =  AdminConfig.showAttribute(serverName, "processDefinitions")
      pd = pd[1:-1]
      mp = AdminConfig.showAttribute(pd, "monitoringPolicy")
      AdminConfig.modify(mp, [['nodeRestartState', 'RUNNING']])

      print "saving"
      AdminConfig.save()

   else:

         print "updateSolarServerAttributes:solar-node" + nodeNum + "-b1/ does not exist."

   #endif

   print


   print "updateSolarSupportServerAttributes:updating solarsupport-node" + nodeNum + "-b1/"

   serverName = AdminConfig.getid("/Node:psm-node" + nodeNum + "/Server:solarsupport-node" + nodeNum + "-b1/")

   if (serverName): 

      osr = AdminConfig.showAttribute(serverName, "outputStreamRedirect")
      AdminConfig.modify(osr, [['rolloverType', 'TIME']])
      AdminConfig.modify(osr, [['maxNumberOfBackupFiles', '5']])

      esr = AdminConfig.showAttribute(serverName, "errorStreamRedirect")
      AdminConfig.modify(esr, [['rolloverType', 'TIME']])
      AdminConfig.modify(esr, [['maxNumberOfBackupFiles', '5']])

      pd =  AdminConfig.showAttribute(serverName, "processDefinitions")
      pd = pd[1:-1]
      mp = AdminConfig.showAttribute(pd, "monitoringPolicy")
      AdminConfig.modify(mp, [['nodeRestartState', 'RUNNING']])

      print "saving"
      AdminConfig.save()

   else:

         print "updateSolarSupportServerAttributes:solarsupport-node" + nodeNum + "-b1/ does not exist."

   #endif

   print


   print "updateAsiaPacificServerAttributes:updating asia-pacific-node" + nodeNum + "-a1/"

   serverName = AdminConfig.getid("/Node:ws-node" + nodeNum + "/Server:asia-pacific-node" + nodeNum + "-a1/")

   if (serverName): 

      osr = AdminConfig.showAttribute(serverName, "outputStreamRedirect")
      AdminConfig.modify(osr, [['rolloverType', 'TIME']])
      AdminConfig.modify(osr, [['maxNumberOfBackupFiles', '5']])

      esr = AdminConfig.showAttribute(serverName, "errorStreamRedirect")
      AdminConfig.modify(esr, [['rolloverType', 'TIME']])
      AdminConfig.modify(esr, [['maxNumberOfBackupFiles', '5']])

      pd =  AdminConfig.showAttribute(serverName, "processDefinitions")
      pd = pd[1:-1]
      mp = AdminConfig.showAttribute(pd, "monitoringPolicy")
      AdminConfig.modify(mp, [['nodeRestartState', 'RUNNING']])

      print "saving"
      AdminConfig.save()

   else:

         print "updateAsiaPacificServerAttributes:asia-pacific-node" + nodeNum + "-a1/ does not exist."

   #endif

   print


   print "updateOwnerServicesServerAttributes:updating owner-services-node" + nodeNum + "-a1/"

   serverName = AdminConfig.getid("/Node:ws-node" + nodeNum + "/Server:owner-services-node" + nodeNum + "-a1/")

   if (serverName): 

      osr = AdminConfig.showAttribute(serverName, "outputStreamRedirect")
      AdminConfig.modify(osr, [['rolloverType', 'TIME']])
      AdminConfig.modify(osr, [['maxNumberOfBackupFiles', '5']])

      esr = AdminConfig.showAttribute(serverName, "errorStreamRedirect")
      AdminConfig.modify(esr, [['rolloverType', 'TIME']])
      AdminConfig.modify(esr, [['maxNumberOfBackupFiles', '5']])

      pd =  AdminConfig.showAttribute(serverName, "processDefinitions")
      pd = pd[1:-1]
      mp = AdminConfig.showAttribute(pd, "monitoringPolicy")
      AdminConfig.modify(mp, [['nodeRestartState', 'RUNNING']])

      print "saving"
      AdminConfig.save()

   else:

         print "updateOwnerServicesServerAttributes:owner-services-node" + nodeNum + "-a1/ does not exist."

   #endif

   print


   print "updateWebMarketingServerAttributes:updating web-marketing-node" + nodeNum + "-a1/"

   serverName = AdminConfig.getid("/Node:ws-node" + nodeNum + "/Server:web-marketing-node" + nodeNum + "-a1/")

   if (serverName): 

      osr = AdminConfig.showAttribute(serverName, "outputStreamRedirect")
      AdminConfig.modify(osr, [['rolloverType', 'TIME']])
      AdminConfig.modify(osr, [['maxNumberOfBackupFiles', '5']])

      esr = AdminConfig.showAttribute(serverName, "errorStreamRedirect")
      AdminConfig.modify(esr, [['rolloverType', 'TIME']])
      AdminConfig.modify(esr, [['maxNumberOfBackupFiles', '5']])

      pd =  AdminConfig.showAttribute(serverName, "processDefinitions")
      pd = pd[1:-1]
      mp = AdminConfig.showAttribute(pd, "monitoringPolicy")
      AdminConfig.modify(mp, [['nodeRestartState', 'RUNNING']])

      print "saving"
      AdminConfig.save()

   else:

         print "updateWebMarketingServerAttributes:web-marketing-node" + nodeNum + "-a1/ does not exist."

   #endif

   print


   print "updateWebServicesServerAttributes:updating web-services-node" + nodeNum + "-a1/"

   serverName = AdminConfig.getid("/Node:ws-node" + nodeNum + "/Server:web-services-node" + nodeNum + "-a1/")

   if (serverName): 

      osr = AdminConfig.showAttribute(serverName, "outputStreamRedirect")
      AdminConfig.modify(osr, [['rolloverType', 'TIME']])
      AdminConfig.modify(osr, [['maxNumberOfBackupFiles', '5']])

      esr = AdminConfig.showAttribute(serverName, "errorStreamRedirect")
      AdminConfig.modify(esr, [['rolloverType', 'TIME']])
      AdminConfig.modify(esr, [['maxNumberOfBackupFiles', '5']])

      pd =  AdminConfig.showAttribute(serverName, "processDefinitions")
      pd = pd[1:-1]
      mp = AdminConfig.showAttribute(pd, "monitoringPolicy")
      AdminConfig.modify(mp, [['nodeRestartState', 'RUNNING']])

      print "saving"
      AdminConfig.save()

   else:

         print "updateWebMarketingServerAttributes:web-services-node" + nodeNum + "-a1/ does not exist."

   #endif

   print


   print "updateAsiaPacificServerAttributes:updating asia-pacific-node" + nodeNum + "-b1/"

   serverName = AdminConfig.getid("/Node:ws-node" + nodeNum + "/Server:asia-pacific-node" + nodeNum + "-b1/")

   if (serverName): 

      osr = AdminConfig.showAttribute(serverName, "outputStreamRedirect")
      AdminConfig.modify(osr, [['rolloverType', 'TIME']])
      AdminConfig.modify(osr, [['maxNumberOfBackupFiles', '5']])

      esr = AdminConfig.showAttribute(serverName, "errorStreamRedirect")
      AdminConfig.modify(esr, [['rolloverType', 'TIME']])
      AdminConfig.modify(esr, [['maxNumberOfBackupFiles', '5']])

      pd =  AdminConfig.showAttribute(serverName, "processDefinitions")
      pd = pd[1:-1]
      mp = AdminConfig.showAttribute(pd, "monitoringPolicy")
      AdminConfig.modify(mp, [['nodeRestartState', 'RUNNING']])

      print "saving"
      AdminConfig.save()

   else:

         print "updateAsiaPacificServerAttributes:asia-pacific-node" + nodeNum + "-b1/ does not exist."

   #endif

   print


   print "updateOwnerServicesServerAttributes:updating owner-services-node" + nodeNum + "-b1/"

   serverName = AdminConfig.getid("/Node:ws-node" + nodeNum + "/Server:owner-services-node" + nodeNum + "-b1/")

   if (serverName): 

      osr = AdminConfig.showAttribute(serverName, "outputStreamRedirect")
      AdminConfig.modify(osr, [['rolloverType', 'TIME']])
      AdminConfig.modify(osr, [['maxNumberOfBackupFiles', '5']])

      esr = AdminConfig.showAttribute(serverName, "errorStreamRedirect")
      AdminConfig.modify(esr, [['rolloverType', 'TIME']])
      AdminConfig.modify(esr, [['maxNumberOfBackupFiles', '5']])

      pd =  AdminConfig.showAttribute(serverName, "processDefinitions")
      pd = pd[1:-1]
      mp = AdminConfig.showAttribute(pd, "monitoringPolicy")
      AdminConfig.modify(mp, [['nodeRestartState', 'RUNNING']])

      print "saving"
      AdminConfig.save()

   else:

         print "updateOwnerServicesServerAttributes:owner-services-node" + nodeNum + "-b1/ does not exist."

   #endif

   print


   print "updateWebMarketingServerAttributes:updating web-marketing-node" + nodeNum + "-b1/"

   serverName = AdminConfig.getid("/Node:ws-node" + nodeNum + "/Server:web-marketing-node" + nodeNum + "-b1/")

   if (serverName): 

      osr = AdminConfig.showAttribute(serverName, "outputStreamRedirect")
      AdminConfig.modify(osr, [['rolloverType', 'TIME']])
      AdminConfig.modify(osr, [['maxNumberOfBackupFiles', '5']])

      esr = AdminConfig.showAttribute(serverName, "errorStreamRedirect")
      AdminConfig.modify(esr, [['rolloverType', 'TIME']])
      AdminConfig.modify(esr, [['maxNumberOfBackupFiles', '5']])

      pd =  AdminConfig.showAttribute(serverName, "processDefinitions")
      pd = pd[1:-1]
      mp = AdminConfig.showAttribute(pd, "monitoringPolicy")
      AdminConfig.modify(mp, [['nodeRestartState', 'RUNNING']])

      print "saving"
      AdminConfig.save()

   else:

         print "updateWebMarketingServerAttributes:web-marketing-node" + nodeNum + "-b1/ does not exist."

   #endif

   print


   print "updateWebServicesServerAttributes:updating web-services-node" + nodeNum + "-b1/"

   serverName = AdminConfig.getid("/Node:ws-node" + nodeNum + "/Server:web-services-node" + nodeNum + "-b1/")

   if (serverName): 

      osr = AdminConfig.showAttribute(serverName, "outputStreamRedirect")
      AdminConfig.modify(osr, [['rolloverType', 'TIME']])
      AdminConfig.modify(osr, [['maxNumberOfBackupFiles', '5']])

      esr = AdminConfig.showAttribute(serverName, "errorStreamRedirect")
      AdminConfig.modify(esr, [['rolloverType', 'TIME']])
      AdminConfig.modify(esr, [['maxNumberOfBackupFiles', '5']])

      pd =  AdminConfig.showAttribute(serverName, "processDefinitions")
      pd = pd[1:-1]
      mp = AdminConfig.showAttribute(pd, "monitoringPolicy")
      AdminConfig.modify(mp, [['nodeRestartState', 'RUNNING']])

      print "saving"
      AdminConfig.save()

   else:

         print "updateWebMarketingServerAttributes:web-services-node" + nodeNum + "-b1/ does not exist."

   #endif

   print


#-----------------------------------------------------------------
# Main
#-----------------------------------------------------------------

index=1

while (index <= 3):

   updateAllServerAttributes(("%s" % (index)))

   index=index + 1

#endwhile
