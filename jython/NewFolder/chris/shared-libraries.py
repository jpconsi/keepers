import xml.dom.minidom
import sys
from com.ibm.ws.scripting import ScriptingException
from time import sleep


#------------------------------------
# Load the XML configuration document
#------------------------------------

def get_document (name):

   return xml.dom.minidom.parse(name)

#enddef


#------------------------------------------------------------
# Find a particular element in the XML configuration document
#------------------------------------------------------------

def find_element(doc, name):

    element = None

    for i in doc.childNodes:

        if i.nodeType == i.ELEMENT_NODE and i.localName == name:

            element = i
            break

        #endif

    #endfor
        
    return element

#enddef


#---------------------
# Add a shared library
#---------------------

def add_shared_library (nodenum, cellType,  paramlist):

   print ""
   print "add_shared_library: Creating " + paramlist[0] + " shared library on node " + cellType + "-node" + nodenum
  
   if len(paramlist) == 3:

      AdminConfig.create('Library', AdminConfig.getid('/Cell:' + cellType + '-cell/Node:' + cellType + '-node' + nodenum + '/'), [['name', paramlist[0]], ['classPath', paramlist[1]], ['nativePath', paramlist[2]]])

   else:

      AdminConfig.create('Library', AdminConfig.getid('/Cell:' + cellType + '-cell/Node:' + cellType + '-node' + nodenum + '/'), [['name', paramlist[0]], ['classPath', paramlist[1]]])

   #endif

   print "add_shared_library: Saving Configuration"
   print ""
   AdminConfig.save()

#enddef


#------------------------------------
# Compare and update a shared library
#------------------------------------

def compare_shared_libraries (nodenum, cellType, xmlParamlist, slParamlist):

   if xmlParamlist != slParamlist:

      print "compare_shared_libraries: Updating " + xmlParamlist[0] + " shared library on node " + cellType + "-node" + nodenum 

      AdminConfig.remove(AdminConfig.getid('/Cell:' + cellType + '-cell/Node:' + cellType + '-node' + nodenum + '/Library:' + xmlParamlist[0] + '/'))
      
      if len(xmlParamlist) == 3:

         AdminConfig.create('Library', AdminConfig.getid('/Cell:' + cellType + '-cell/Node:' + cellType + '-node' + nodenum + '/'), [['name', xmlParamlist[0]], ['classPath', xmlParamlist[1]], ['nativePath', xmlParamlist[2]]])

      else:

         AdminConfig.create('Library', AdminConfig.getid('/Cell:' + cellType + '-cell/Node:' + cellType + '-node' + nodenum + '/'), [['name', xmlParamlist[0]], ['classPath', xmlParamlist[1]]])

      #endif

      print "compare_shared_libraries: Saving configuration"
      print ""
      AdminConfig.save()

   #endif

#enddef


#------------------------
# Delete a shared library
#------------------------

def delete_shared_library (nodenum, cellType, paramlist):

   print ""
   print "delete_shared_library: Deleting " + paramlist[0] + " shared library on node " + cellType + "-node" + nodenum
   AdminConfig.remove(AdminConfig.getid('/Cell:' + cellType + '-cell/Node:' + cellType + '-node' + nodenum + '/Library:' + paramlist[0] + '/'))
   print "delete_shared_library: Saving Configuration"
   print ""
   AdminConfig.save()


#enddef




#----------------------------------------------------
#   Main
#----------------------------------------------------

if (len(sys.argv) != 2):

   print "shared-libraries: this script requires 2 parameter:"
   print "     hostname and number of nodes"
   print ""
   print "e.g.:     shared-libraries lalfimvd0app07 4" 

else:

   if sys.argv[0][-2:-1] != "0" and sys.argv[0][-2:-1] != "6":

      print sys.argv[0] + ":shared-libraries:ERROR Unknown host type - not web(0) or solar(6) - Ending"

   else:

      if sys.argv[0][-2:-1] == "0": 

         cellType = "ws"

      elif sys.argv[0][-2:-1] == "6":

         CellType = "psm"

      #endif

      xmlList = []
      sharedLibList = []
      rowList = []

      doc = get_document("E:/" + sys.argv[0] + ".xml")
      root = find_element(doc, sys.argv[0])
      node = find_element(root, "node")
      sharedLibraries = find_element(node, "shared-libraries")

      for i1 in sharedLibraries.childNodes:
 
         if i1.nodeType == i1.ELEMENT_NODE:

            for i2 in i1.childNodes:

               if i2.localName == "name":

                  if len(rowList) != 0:
                        
                     xmlList.append(rowList)
                     rowList = []

                  #endif

                  try:

                     rowList.append(i2.childNodes[0].nodeValue)

                  except IndexError:

                     print "shared-libraries: XML ERROR. Shared library name is empty. Stopping execution."

                  #endtry

               #endif

               if i2.localName == "classpath":

                  try:

                     rowList.append(i2.childNodes[0].nodeValue)
                      
                  except IndexError:

                     print "shared-libraries: XML ERROR. Shared library classpath is empty. Stopping execution."
               
                  #endtry

               #endif
                     
               if i2.localName == "nativepath":

                  try:

                     rowList.append(i2.childNodes[0].nodeValue)

                  except IndexError:

                     continue
               
                  #endtry

               #endif

            #endfor

         #endif

      #endfor

      xmlList.append(rowList)

      i = 1

      while ("%s" % (i)) <= sys.argv[1]:

         lL=AdminConfig.list('Library', AdminConfig.getid( '/Cell:' + cellType + '-cell/Node:' + cellType + '-node' + ("%s" % (i)) + '/'))
         aLL = lL.split(lineSeparator)

         for i1 in aLL:

            rowList = []
            text = AdminConfig.showAttribute(i1, 'name')
            rowList.append(text.encode('utf-8'))
            text = AdminConfig.showAttribute(i1, 'classPath')
            rowList.append(text.encode('utf-8'))

            if AdminConfig.showAttribute(i1,'nativePath') != '[]':

               text = AdminConfig.showAttribute(i1, 'nativePath')
               rowList.append(text.encode('utf-8'))

            #endif

            sharedLibList.append(rowList)

         #endfor
                           
         i = i + 1
         
      #endwhile

      xmlList.append('~~~')
      xmlList.sort()
      sharedLibList.append('~~~')
      sharedLibList.sort()
      
      s = 0
      x = 0
      sRow = []
      xRow = []

      while x < len(xmlList):
    
         while s < len(sharedLibList):

            if xmlList[x][0] < sharedLibList[s][0]:

               i = 1

               while ("%s" % (i)) <= sys.argv[1]:

                     add_shared_library(("%s" % (i)), cellType, xmlList[x])
                     i = i+1

               #endwhile

               x = x + 1
               break

            #endif

            if xmlList[x][0] == sharedLibList[s][0]:

               i = 1

               if xmlList[x] != 'zzz':
                  
                  while ("%s" % (i)) <= sys.argv[1]:

                     compare_shared_libraries(("%s" % (i)), cellType, xmlList[x], sharedLibList[s])
                     i = i+1

                  #endwhile

               #endif
               
               s = s + 1
               x = x + 1
               break

            #endif

            if xmlList[x][0] > sharedLibList[s][0]:

               i = 1

               while ("%s" % (i)) <= sys.argv[1]:

                  delete_shared_library(("%s" % (i)), cellType, sharedLibList[s])
                  i = i + 1

                #endwhile
               
               s = s + 1
               break

            #endif

         #endwhile

      #endwhile
                              
   #endif

#endif
