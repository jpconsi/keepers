import sys, java

def buildMssqlDatasources(appservName, abIdent, datasourceName, datasourceJndiName, datasourceJ2c, datasourceDb, datasourceDbServer, datasourceDbServerPort):

   jdbcId = AdminConfig.getid('/Cell:ws-cell/ServerCluster:' + appservName + '-cluster-' + abIdent + '/JDBCProvider:WebSphere embedded ConnectJDBC driver for MS SQL Server/')
 
   print ""
   print "buildMssqlDatasource: create mssql " + datasourceName + " datasource for " + appservName + "-cluster-" + abIdent

   newDS = AdminTask.createDatasource(jdbcId, '[-name ' + datasourceName + ' -jndiName jdbc/' + datasourceJndiName + ' -dataStoreHelperClassName com.ibm.websphere.rsadapter.WSConnectJDBCDataStoreHelper -componentManagedAuthenticationAlias ' + datasourceJ2c + ' -containerManagedPersistence false -configureResourceProperties [[databaseName java.lang.String ' + datasourceDb +'] [serverName java.lang.String ' + datasourceDbServer + '] [portNumber java.lang.Integer ' + datasourceDbServerPort + ']]]')

   conTimeoutAttr = ['connectionTimeout', '15']
   maxConAttr = ['maxConnections', '0']
   minConAttr = ['minConnections', '1']
   reapTimeAttr = ['reapTime', '60']
   unusedTimeoutAttr = ['unusedTimeout', '120']
   agedTimeoutAttr = ['agedTimeout', '120']
   ppAttr = ['purgePolicy', 'FailingConnectionOnly']
   cpAttrs = [conTimeoutAttr, maxConAttr, minConAttr, reapTimeAttr, unusedTimeoutAttr, agedTimeoutAttr, ppAttr]

   AdminConfig.create('ConnectionPool', newDS, cpAttrs)

   #--------------------------------------------------------------
   # Save the changes 
   #--------------------------------------------------------------
   print ""
   print "buildMssqlDatasource: saving the configuration"
   AdminConfig.save()

    
#-----------------------------------------------------------------
# Main
#-----------------------------------------------------------------
if (len(sys.argv) != 8):

   print "buildMssqlDatasources: this script requires 8 parameters:"
   print "appservername, a/b identifier, datasource name, datasource JNDI name, datasource J2C authentication,"
   print "datasource database, datasource database server, datasource database server port"
   print ""
   print "e.g.:     buildOracleDatasources web-services a webdb webdb webdb sqllwbdd01 lalwvuatsql3 1433" 

else:

   buildMssqlDatasources(sys.argv[0], sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7])

#endif