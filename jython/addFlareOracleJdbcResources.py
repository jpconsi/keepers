import sys, java

def buildOracleJdbcResource(abIdent):

   print""
   print "buildOracleJdbcResource: adding Flare JDBC Resources"
   AdminTask.createJDBCProvider('[-scope Cluster=flare-cluster-' + abIdent + ' -databaseType Oracle -providerType "Oracle JDBC Driver" -implementationType "XA data source" -name "Oracle JDBC Driver (XA)" -description "Oracle JDBC Driver (XA)" -classpath ${ORACLE_JDBC_DRIVER_PATH}/ojdbc14.jar -nativePath ]') 

   #--------------------------------------------------------------
   # Save all the changes 
   #--------------------------------------------------------------
   print "buildOracleJdbcResource: saving the configuration"
   AdminConfig.save()
 
#-----------------------------------------------------------------
# Main
#-----------------------------------------------------------------

if (len(sys.argv) != 1):

   print "buildFlareOracleDatasources: this script requires 1 parameter:"
   print "a/b identifier"
   print ""
   print "e.g.:     buildOracleJdbcResource a" 

else:

   buildOracleJdbcResource(sys.argv[0])

#endif


