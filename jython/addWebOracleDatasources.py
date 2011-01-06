import sys, java

def buildOracleDatasource(appsrvName, abIdent, dataSourceName, jndiName, j2cAlias, dbName, serverName, port):

   jdbcId = AdminConfig.getid('/Cell:ws-cell/ServerCluster:' + appsrvName + '-cluster-' + abIdent + '/JDBCProvider:Oracle JDBC Driver/')
 
   print ""
   print "buildOracleDatasource: create psar datasources for " + appsrvName + "-cluster-" + abIdent

   newDS = AdminTask.createDatasource(jdbcId, '[-name ' + dataSourceName + ' -jndiName jdbc/' + jndiName + ' -dataStoreHelperClassName com.ibm.websphere.rsadapter.Oracle10gDataStoreHelper -componentManagedAuthenticationAlias ' + j2cAlias + ' -containerManagedPersistence false -configureResourceProperties [[URL java.lang.String jdbc:oracle:thin:@' + serverName + ':' + port + ':' + dbName + ']]]') 

   minConAttr = ['minConnections', '0']
   ppAttr = ['purgePolicy', 'FailingConnectionOnly']
   cpAttrs = [minConAttr, ppAttr]

   AdminConfig.create('ConnectionPool', newDS, cpAttrs)


   #--------------------------------------------------------------
   # Save all the changes 
   #--------------------------------------------------------------
   print ""
   print "buildOracleDatasource: saving the configuration"
   AdminConfig.save()
 
#-----------------------------------------------------------------
# Main
#-----------------------------------------------------------------
if (len(sys.argv) != 8):

   print "buildOracleDatasources: this script requires 8 parameters:"
   print "appserver name, a/bIdent datasource name, datasource jndi name,"
   print "datasource j2c alias, db name, server name, port"
   print ""
   print "e.g.:     buildOracleDatasources owner-services a psar psar psar psardb psarserver 1234" 

else:

   buildOracleDatasource(sys.argv[0], sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7])

#endif