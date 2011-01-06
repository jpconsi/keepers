import sys

def buildJ2cAuth(alias, id, pw): 


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
   print "buildJ2cAuth: create " + alias + " j2c alias" 

   aliasAttr = '["alias", "' + alias + '"]'
   useridAttr = '["userId", "' + id + '"]'
   passwordAttr = '["password", "' + pw + '"]'
   attrs = []
   attrs.append(aliasAttr)
   attrs.append(useridAttr)
   attrs.append(passwordAttr)
 
   appauthdata = AdminConfig.create("JAASAuthData", sec, attrs) 


   #--------------------------------------------------------------
   # Save changes 
   #--------------------------------------------------------------
   print "buildJ2cAuth: saving the configuration"
   AdminConfig.save()


#-----------------------------------------------------------------
# Main
#-----------------------------------------------------------------
if (len(sys.argv) != 3):

   print "buildJ2cAuth: this script requires 3 parameters:"
   print "alias name, id, password"
   print ""
   print "e.g.:     buildJ2cAuth acm acmid acmpw"

else:

   buildJ2cAuth(sys.argv[0], sys.argv[1], sys.argv[2])

#endif
