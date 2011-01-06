import sys, java

def buildOracleDatasources(abIdent, dsUrl):

   jdbcId = AdminConfig.getid('/Cell:psm-cell/ServerCluster:orca-cluster-' + abIdent + '/JDBCProvider:Oracle JDBC Driver (XA)/')

   print "" 
   print "buildOracleDatasources: create Orca Datasource"

   newDS = AdminTask.createDatasource(jdbcId, '[-name "Orca Datasource" -jndiName jdbc/orca -dataStoreHelperClassName com.ibm.websphere.rsadapter.Oracle10gDataStoreHelper -componentManagedAuthenticationAlias orca -containerManagedPersistence false -xaRecoveryAuthAlias flare -configureResourceProperties [[URL java.lang.String ' + dsUrl + ']]]')

   print "buildOracleDatasources: saving the configuration"
   AdminConfig.save()
 
#-----------------------------------------------------------------
# Main
#-----------------------------------------------------------------
if (len(sys.argv) != 4):

   print "buildOrcaOracleDatasources: this script requires 4 parameters:"
   print "a/b identifier, Orca Datasource server, port & db"
   print ""
   print "e.g.:     buildOrcaOracleDatasources a DSserver 1521 DSdbName" 

else:

   u1 = 'jdbc:oracle:thin:@' + sys.argv[1] + ':' + sys.argv[2] + ':' + sys.argv[3]
   buildOracleDatasources(sys.argv[0], u1)

#endif