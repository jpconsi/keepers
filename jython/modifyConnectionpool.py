import sys, java

def modifyjdbcds (abIdent, unusedtime, connTime):

   ds =  AdminConfig.getid('/Cell:psm-cell/ServerCluster:jservices-cluster-' + abIdent + '/JDBCProvider:Oracle JDBC Driver (XA)/DataSource:Orca Datasource/')  

   connPool = AdminConfig.list("ConnectionPool", ds )
   
   AdminConfig.modify(connPool, [["unusedTimeout", unusedtime]])
   AdminConfig.modify(connPool,[["connectionTimeout", connTime]])
 
   AdminConfig.save()

#-----------------------------------------------------------------
# Main
#-----------------------------------------------------------------
if (len(sys.argv) < 2 ):

   print "createMqQueueDestinations: this script requires 2 parameters: "  
   print " a/b identifier, base queue manager id"
   print "e.g.:     modifyConnectionpool.py a 100 10"

else:
 
      modifyjdbcds(sys.argv[0], sys.argv[1], sys.argv[2])
   
#endif