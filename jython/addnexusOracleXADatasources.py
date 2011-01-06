import sys, java

def buildOracleDatasource( abIdent, serverName, portNum, dataBase):

   jdbcId = AdminConfig.getid('/Cell:ws-cell/ServerCluster:jservices-cluster-' + abIdent + '/JDBCProvider:Oracle JDBC Driver (XA)/')
 
   print ""
   print "buildOracleDatasource: create nexus Datasource for jservices-cluster-" + abIdent

   AdminTask.createDatasource(jdbcId, '[-name nexusdb -jndiName jdbc/nexusdb -dataStoreHelperClassName com.ibm.websphere.rsadapter.Oracle10gDataStoreHelper -componentManagedAuthenticationAlias eouser -containerManagedPersistence false -configureResourceProperties [[URL java.lang.String jdbc:oracle:thin:@' + serverName + ':' + portNum + ':' + dataBase + ']]]') 

 #  jdbcId = AdminConfig.getid('/Cell:psm-cell/ServerCluster:solarsupport-cluster-' + abIdent + '/JDBCProvider:Oracle JDBC Driver/')
 
 #  print ""
  # print "buildOracleDatasource: create SolarDSV5 Datasource for solarsupport-cluster-" + abIdent

  # AdminTask.createDatasource(jdbcId, '[-name SolarDSV5 -jndiName jdbc/SolarDSV5 -dataStoreHelperClassName com.ibm.websphere.rsadapter.Oracle10gDataStoreHelper -componentManagedAuthenticationAlias solar -containerManagedPersistence false -configureResourceProperties [[URL java.lang.String jdbc:oracle:thin:@' + serverName + ':' + portNum + ':' + dataBase + ']]]') 

   #--------------------------------------------------------------
   # Save all the changes 
   #--------------------------------------------------------------
   print ""
   print "buildOracleDatasource: saving the configuration"
   AdminConfig.save()
 
#-----------------------------------------------------------------
# Main
#-----------------------------------------------------------------
if (len(sys.argv) != 4):

   print "buildOracleDatasources: this script requires 4 parameters:"
   print "a/b identifier, dbServer, port number, and database"
   print ""
   print "e.g.:     buildOracleDatasources  a lalfimvsql1 1523 mydb" 

else:

   buildOracleDatasource(sys.argv[0], sys.argv[1], sys.argv[2], sys.argv[3])

#endif