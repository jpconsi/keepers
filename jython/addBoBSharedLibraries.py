import sys
from time import sleep

#--------------------------------------------------------------
# set up globals
#--------------------------------------------------------------
global AdminConfig
global AdminControl
global AdminApp

def addNodeLevelSharedLibraries(logicalMachineNumber, abIdent):

   #---------------------------------------------------------
   # We assume that there is only one cell, and we are on it
   #---------------------------------------------------------
   cellName = AdminControl.getCell()
   node = AdminConfig.getid("/Cell:" + cellName + "/Node:ws-node" + logicalMachineNumber + "/")

   if (abIdent == 'a'):

      print "addSharedLibraries: Creating node level libraries"

      AdminConfig.create('Library', node, [['name', 'mvcp-bob-extension-app'], ['classPath', 'E:/WebSphere/AppServer/mvci/config/mvcp-bob-extension-app']])

      AdminConfig.save()

   #endif


#-----------------------------------------------------------------
# Main
#-----------------------------------------------------------------
if (len(sys.argv) != 2):

   print "addEnrollmentSharedLibraries: this script requires 2 parameters:"
   print "     number of nodes, and cluster a/b identifier"
   print ""
   print "e.g.:     addSharedLibraries  4 a" 

else:

   index = 1

   while ("%s" % (index)) <= sys.argv[0]:

      addNodeLevelSharedLibraries(("%s" % (index)), sys.argv[1])
      index = index + 1

   #endwhile

#endif
