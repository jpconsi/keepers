import sys, java

def removeDatasource( abIdent):

  
   ds = AdminConfig.getid('/Cell:psm-cell/ServerCluster:jservices-cluster-' + abIdent + '/JDBCProvider:Oracle JDBC Driver (XA)/DataSource:nexusdb/')

   print ""
   print "removeDatasource: remove nexusdb Datasource for jservices-cluster-" + abIdent

   AdminConfig.remove(ds) 


   #--------------------------------------------------------------
   # Save all the changes 
   #--------------------------------------------------------------

   print "removeDatasource: saving the configuration"

   AdminConfig.save()
 
#-----------------------------------------------------------------
# Main
#-----------------------------------------------------------------
if (len(sys.argv) != 1):

   print "removeDatasource: this script requires 1 parameters:"
   print "a/b identifier"
   print ""
   print "e.g.:     removeDatasource  a " 

else:

   removeDatasource(sys.argv[0])

#endif