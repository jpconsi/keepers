import sys, java

def buildMssqlJdbcResource(abIdent):

   print""
   print "buildOracleJdbcResource: adding Web JDBC Resources"

   AdminTask.createJDBCProvider('[-scope Cluster=asia-pacific-cluster-' + abIdent + ' -databaseType "SQL Server" -providerType "WebSphere embedded ConnectJDBC driver for MS SQL Server" -implementationType "Connection pool data source" -name "WebSphere embedded ConnectJDBC driver for MS SQL Server" -description "IBM WebSphere Connect JDBC driver for MS SQL Server." -classpath ${WAS_LIBS_DIR}/sqlserver.jar;${WAS_LIBS_DIR}/base.jar;${WAS_LIBS_DIR}/util.jar;${WAS_LIBS_DIR}/spy.jar -nativePath ]') 

   AdminTask.createJDBCProvider('[-scope Cluster=owner-services-cluster-' + abIdent + ' -databaseType "SQL Server" -providerType "WebSphere embedded ConnectJDBC driver for MS SQL Server" -implementationType "Connection pool data source" -name "WebSphere embedded ConnectJDBC driver for MS SQL Server" -description "IBM WebSphere Connect JDBC driver for MS SQL Server." -classpath ${WAS_LIBS_DIR}/sqlserver.jar;${WAS_LIBS_DIR}/base.jar;${WAS_LIBS_DIR}/util.jar;${WAS_LIBS_DIR}/spy.jar -nativePath ]') 

   AdminTask.createJDBCProvider('[-scope Cluster=web-marketing-cluster-' + abIdent + ' -databaseType "SQL Server" -providerType "WebSphere embedded ConnectJDBC driver for MS SQL Server" -implementationType "Connection pool data source" -name "WebSphere embedded ConnectJDBC driver for MS SQL Server" -description "IBM WebSphere Connect JDBC driver for MS SQL Server." -classpath ${WAS_LIBS_DIR}/sqlserver.jar;${WAS_LIBS_DIR}/base.jar;${WAS_LIBS_DIR}/util.jar;${WAS_LIBS_DIR}/spy.jar -nativePath ]') 

   AdminTask.createJDBCProvider('[-scope Cluster=web-services-cluster-' + abIdent + ' -databaseType "SQL Server" -providerType "WebSphere embedded ConnectJDBC driver for MS SQL Server" -implementationType "Connection pool data source" -name "WebSphere embedded ConnectJDBC driver for MS SQL Server" -description "IBM WebSphere Connect JDBC driver for MS SQL Server." -classpath ${WAS_LIBS_DIR}/sqlserver.jar;${WAS_LIBS_DIR}/base.jar;${WAS_LIBS_DIR}/util.jar;${WAS_LIBS_DIR}/spy.jar -nativePath ]') 


   #--------------------------------------------------------------
   # Save all the changes 
   #--------------------------------------------------------------
   print "buildMssqlJdbcResource: saving the configuration"
   AdminConfig.save()
 
#-----------------------------------------------------------------
# Main
#-----------------------------------------------------------------

if (len(sys.argv) != 1):

   print "buildMssqlJDBCResource: this script requires 1 parameter:"
   print "a/b identifier"
   print ""
   print "e.g.:     buildMssqlJdbcResource a" 

else:

   buildMssqlJdbcResource(sys.argv[0])

#endif


