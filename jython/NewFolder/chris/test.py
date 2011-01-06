import xml.dom.minidom
import sys
from com.ibm.ws.scripting import ScriptingException
from time import sleep


def get_document (name="E:/lalfimvd0app07.xml"):

   return xml.dom.minidom.parse(name)

#enddef

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

xmlList = []
clusterList = []
doc=get_document()
root=find_element(doc, "lalfimvd0app07")
node=find_element(root, "node")
sharedLibraries=find_element(node, "shared-libraries")

for i1 in sharedLibraries.childNodes:
 
   if i1.nodeType == i1.ELEMENT_NODE:

      name = ""
      classPath = ""
      nativePath = ""
      
      for i2 in i1.childNodes:

         if i2.localName == "name":

            try:

               name = i2.childNodes[0].nodeValue
               print name

            except IndexError:

               name = ""
               print "addCerts: XML ERROR. Shared library name is empty. Stopping execution."

            #endtry

          #endif

         if i2.localName == "classpath":

            try:

               classPath = i2.childNodes[0].nodeValue
               print classPath

            except IndexError:

               classPath = ""
               print "addCerts: XML ERROR. Shared library classpath is empty. Stopping execution."

            #endtry

          #endif

         if i2.localName == "nativepath":

            try:

               nativePath = i2.childNodes[0].nodeValue


            except IndexError:

               nativePath = ""

            #endtry

            print nativePath

          #endif



#            for i3 in i2.childNodes:

#               print i3.localName

            #xmlList.append(i2.childNodes[0].nodeValue)

#xmlList.sort()

#print xmlList
#print len(xmlList)

#cL=AdminConfig.list('ServerCluster', AdminConfig.getid( '/Cell:ws-cell/'))
#aCL = cL.split(lineSeparator)

#for i in aCL:
#    ip= i[0:i.find("-cluster")]
#
#   if len(clusterList) == 0 or ip.encode('utf-8') != clusterList[len(clusterList)-1]:
           
#         clusterList.append(ip.encode('utf-8'))

#clusterList.sort()

#print clusterList
#print len(xmlList)
    
#c = 0
#x = 0

#while x < len(xmlList):
    
#    while c < len(clusterList):

 #       if xmlList[x] < clusterList[c]:

  #          print xmlList[x] + " will be added"
 #           x = x+1
#            break

#        if xmlList[x] == clusterList[c]:

#            print xmlList[x] + " will be modified"
#            c = c+1
#            x = x+1
#            break

#        if xmlList[x] > clusterList[c]:

#            print clusterList[c] + " will be deleted"
#            c = c+1
#            break
        
            


