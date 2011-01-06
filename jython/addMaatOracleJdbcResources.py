import sys, java

def buildOracleJdbcResource(abIdent):

   print""
   print "buildOracleJdbcResource: adding MAAT JDBC Resources"
   AdminTask.createJDBCProvider('[-scope Cluster=maat-cluster-' + abIdent + ' -databaseType Oracle -providerType "Oracle JDBC Driver" -implementationType "Connection pool data source" -name "Oracle JDBC Driver" -description "Oracle JDBC Driver" -classpath ${ORACLE_JDBC_DRIVER_PATH}/classes12.jar -nativePath ]')

   #--------------------------------------------------------------
   # Save all the changes 
   #--------------------------------------------------------------
   print "buildOracleJdbcResource: saving the configuration"
   AdminConfig.save()
 
#-----------------------------------------------------------------
# Main
#-----------------------------------------------------------------

if (len(sys.argv) != 1):

   print "buildOracleJdbcResource: this script requires 1 parameter:"
   print "a/b identifier"
   print ""
   print "e.g.:     buildOracleJdbcResource a" 

else:

   buildOracleJdbcResource(sys.argv[0])

#endif
