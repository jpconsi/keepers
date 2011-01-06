import sys

def buildJ2cAuth(): 


   #--------------------------------------------------------------
   # set up globals
   #--------------------------------------------------------------

   global AdminConfig
   global AdminControl

   #---------------------------------------------------------
   # Get the config id for the Cell's Security object 
   #---------------------------------------------------------

   cell = AdminControl.getCell()
   sec = AdminConfig.getid("/Cell:" + cell + "/Security:/")

   #---------------------------------------------------------
   # Create a JAASAuthData object for component-managed authentication 
   #---------------------------------------------------------

   print ""
   print "buildJ2cAuth: create nexus J2CAuth objects" 

   aliasAttr = ["alias", "eouser"]
   useridAttr = ["userId", "eouser"]
   passwordAttr = ["password", "eouser"]
   attrs = []
   attrs.append(aliasAttr)
   attrs.append(useridAttr)
   attrs.append(passwordAttr)
 
   appauthdata = AdminConfig.create("JAASAuthData", sec, attrs) 

   # print ""
   # print "buildJ2cAuth: create Flare J2CAuth objects" 


   # aliasAttr = ["alias", "flare"]
   # useridAttr = ["userId", "flare"]
   # passwordAttr = ["password", "flare"]
   # attrs = []
   # attrs.append(aliasAttr)
   # attrs.append(useridAttr)
   # attrs.append(passwordAttr)
 
   # appauthdata = AdminConfig.create("JAASAuthData", sec, attrs) 
 



   #--------------------------------------------------------------
   # Save all the changes 
   #--------------------------------------------------------------
   print "buildJ2cAuth: saving the configuration"
   AdminConfig.save()


#-----------------------------------------------------------------
# Main
#-----------------------------------------------------------------
buildJ2cAuth()
