import sys, java

def buildOracleJdbcResource(abIdent):

   print""
   print "buildOracleJdbcResource: adding Solar JDBC Resources"
   AdminTask.createJDBCProvider('[-scope Cluster=solar-cluster-' + abIdent + ' -databaseType Oracle -providerType "Oracle JDBC Driver" -implementationType "XA data source" -name "Oracle JDBC Driver (XA)" -description "Oracle JDBC Driver (XA)" -classpath ${ORACLE_JDBC_DRIVER_PATH}/ojdbc14.jar -nativePath ]')

   print""
 #  print "buildOracleJdbcResource: adding SolarSupport JDBC Resources"
 #  AdminTask.createJDBCProvider('[-scope Cluster=solarsupport-cluster-' + abIdent + ' -databaseType Oracle -providerType "Oracle JDBC Driver" -implementationType "Connection pool data source" -name "Oracle JDBC Driver" -description "Oracle JDBC Driver" -classpath ${ORACLE_JDBC_DRIVER_PATH}/ojdbc14.jar -nativePath ]')
  
   #--------------------------------------------------------------
   # Save all the changes 
   #--------------------------------------------------------------
   print "buildOracleJdbcResource: saving the configuration"
   AdminConfig.save()
 
#-----------------------------------------------------------------
# Main
#-----------------------------------------------------------------

if (len(sys.argv) != 1):

   print "buildOracleDatasources: this script requires 1 parameter:"
   print "a/b identifier"
   print ""
   print "e.g.:     buildOracleDatasources  a" 

else:

   buildOracleJdbcResource(sys.argv[0])

#endif
