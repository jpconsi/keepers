import sys
from time import sleep

def updateServerAttributes(abIdent, nodeNum):

   #--------------------------------------------------------------
   # set up globals
   #--------------------------------------------------------------

   global AdminConfig
   global AdminControl
   global AdminApp

   #---------------------------------------------------------
   # We assume that there is only one cell, and we are on it
   #---------------------------------------------------------

   print "updateServerAttributes:updating asia-pacific server attributes on node " + nodeNum 

   serverName = AdminConfig.getid("/Node:ws-node" + nodeNum + "/Server:asia-pacific-node" + nodeNum + '-' + abIdent + "1/")

   osr = AdminConfig.showAttribute(serverName, "outputStreamRedirect")
   AdminConfig.modify(osr, [['rolloverType', 'TIME']])

   esr = AdminConfig.showAttribute(serverName, "errorStreamRedirect")
   AdminConfig.modify(esr, [['rolloverType', 'TIME']])

   jvm = AdminConfig.list('JavaVirtualMachine', serverName)
   AdminConfig.modify(jvm, [['verboseModeGarbageCollection', 'true'], ['initialHeapSize', '64'], ['maximumHeapSize', '128'], ['genericJvmArguments', '-Xgcpolicy:optavgpause']])

   wc = AdminConfig.list('WebContainer', serverName)
   nameAttr = ['name', 'prependSlashToResource']
   valueAttr = ['value', 'true']

   attrs = []
   attrs.append(nameAttr)
   attrs.append(valueAttr)

   property = ['properties', [attrs]]
   AdminConfig.modify(wc, [property])

   print "saving"
   AdminConfig.save()

   print "updateServerAttributes:updating owner-services server attributes on node " + nodeNum 

   serverName = AdminConfig.getid("/Node:ws-node" + nodeNum + "/Server:owner-services-node" + nodeNum + '-' + abIdent + "1/")

   osr = AdminConfig.showAttribute(serverName, "outputStreamRedirect")
   AdminConfig.modify(osr, [['rolloverType', 'TIME']])

   esr = AdminConfig.showAttribute(serverName, "errorStreamRedirect")
   AdminConfig.modify(esr, [['rolloverType', 'TIME']])
 
   jvm = AdminConfig.list('JavaVirtualMachine', serverName)
   AdminConfig.modify(jvm, [['verboseModeGarbageCollection', 'true'], ['initialHeapSize', '512'], ['maximumHeapSize', '1024'], ['genericJvmArguments', '-Xgcpolicy:optavgpause -Dmpcm.home.dir=E:\mpcm -Duser.home=E:\mpcm\logs -Djava.util.logging.config.file=E:\mpcm\conf\logging.properties -Dproperties.filename=E:\mpcm\conf\mpcm.properties']])

   wc = AdminConfig.list('WebContainer', serverName)
   nameAttr = ['name', 'prependSlashToResource']
   valueAttr = ['value', 'true']

   attrs = []
   attrs.append(nameAttr)
   attrs.append(valueAttr)

   property = ['properties', [attrs]]
   AdminConfig.modify(wc, [property])

   print "saving"
   AdminConfig.save()

   print "updateServerAttributes:updating web-marketing server attributes on node " + nodeNum 

   serverName = AdminConfig.getid("/Node:ws-node" + nodeNum + "/Server:web-marketing-node" + nodeNum + '-' + abIdent + "1/")

   osr = AdminConfig.showAttribute(serverName, "outputStreamRedirect")
   AdminConfig.modify(osr, [['rolloverType', 'TIME']])

   esr = AdminConfig.showAttribute(serverName, "errorStreamRedirect")
   AdminConfig.modify(esr, [['rolloverType', 'TIME']])
 
   jvm = AdminConfig.list('JavaVirtualMachine', serverName)
   AdminConfig.modify(jvm, [['verboseModeGarbageCollection', 'true'], ['initialHeapSize', '256'], ['maximumHeapSize', '512'], ['genericJvmArguments', '-Xgcpolicy:optavgpause -Dmpcm.home.dir=E:\\mpcm -Duser.home=E:\\mpcm\\logs -Djava.util.logging.config.file=E:\\mpcm\\conf\\logging.properties -Dproperties.filename=E:\\mpcm\\conf\\mpcm.properties']])

   wc = AdminConfig.list('WebContainer', serverName)
   nameAttr = ['name', 'prependSlashToResource']
   valueAttr = ['value', 'true']

   attrs = []
   attrs.append(nameAttr)
   attrs.append(valueAttr)

   property = ['properties', [attrs]]
   AdminConfig.modify(wc, [property])

   print "saving"
   AdminConfig.save()

   print "updateServerAttributes:updating web-services server attributes on node " + nodeNum 

   serverName = AdminConfig.getid("/Node:ws-node" + nodeNum + "/Server:web-services-node" + nodeNum + '-' + abIdent + "1/")

   osr = AdminConfig.showAttribute(serverName, "outputStreamRedirect")
   AdminConfig.modify(osr, [['rolloverType', 'TIME']])

   esr = AdminConfig.showAttribute(serverName, "errorStreamRedirect")
   AdminConfig.modify(esr, [['rolloverType', 'TIME']])
 
   jvm = AdminConfig.list('JavaVirtualMachine', serverName)
   AdminConfig.modify(jvm, [['verboseModeGarbageCollection', 'true'], ['initialHeapSize', '256'], ['maximumHeapSize', '512'], ['genericJvmArguments', '-Xgcpolicy:optavgpause -Dmpcm.home.dir=E:\mpcm -Duser.home=E:\mpcm\logs -Djava.util.logging.config.file=E:\mpcm\conf\logging.properties -Dproperties.filename=E:\mpcm\conf\mpcm.properties']])

   wc = AdminConfig.list('WebContainer', serverName)
   nameAttr = ['name', 'prependSlashToResource']
   valueAttr = ['value', 'true']

   attrs = []
   attrs.append(nameAttr)
   attrs.append(valueAttr)

   property = ['properties', [attrs]]
   AdminConfig.modify(wc, [property])

   print "saving"
   AdminConfig.save()


#-----------------------------------------------------------------
# Main
#-----------------------------------------------------------------
if (len(sys.argv) != 2):

   print "updateSolarServerAttributes: this script requires 2 parameters:"
   print "a/b identifier and number of nodes"

else:

   index=1

   while ("%s" % (index)) <= sys.argv[1]:

      updateServerAttributes(sys.argv[0], ("%s" % (index)))
      index=index + 1

   #endwhile

#endif
