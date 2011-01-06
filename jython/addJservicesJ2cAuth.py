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
   print "buildJ2cAuth: create Jservices J2CAuth objects" 

   aliasAttr = ["alias", "jservices"]
   useridAttr = ["userId", "jservicesuser"]
   passwordAttr = ["password", "jservicesuser"]
   attrs = []
   attrs.append(aliasAttr)
   attrs.append(useridAttr)
   attrs.append(passwordAttr)
 
   appauthdata = AdminConfig.create("JAASAuthData", sec, attrs) 


   #--------------------------------------------------------------
   # Save all the changes 
   #--------------------------------------------------------------
   print "buildJ2cAuth: saving the configuration"
   AdminConfig.save()


#-----------------------------------------------------------------
# Main
#-----------------------------------------------------------------
buildJ2cAuth()
