import sys, java

def removeDatasource( abIdent):

  # jdbcId = AdminConfig.getid('/Cell:psm-cell/ServerCluster:solar-cluster-' + abIdent + '/JDBCProvider:Oracle JDBC Driver (XA)/')
   ds = AdminConfig.getid('/Cell:ws-cell/ServerCluster:solar-cluster-' + abIdent + '/JDBCProvider:Oracle JDBC Driver/DataSource:SolarDSV5/')

   print ""
   print "removeDatasource: remove SolarDSV5 Datasource for solar-cluster-" + abIdent

   AdminConfig.remove(ds) 

 #  jdbcId = AdminConfig.getid('/Cell:psm-cell/ServerCluster:solarsupport-cluster-' + abIdent + '/JDBCProvider:Oracle JDBC Driver/')
 
 #  print ""
  # print "buildOracleDatasource: create SolarDSV5 Datasource for solarsupport-cluster-" + abIdent

  # AdminTask.createDatasource(jdbcId, '[-name SolarDSV5 -jndiName jdbc/SolarDSV5 -dataStoreHelperClassName com.ibm.websphere.rsadapter.Oracle10gDataStoreHelper -componentManagedAuthenticationAlias solar -containerManagedPersistence false -configureResourceProperties [[URL java.lang.String jdbc:oracle:thin:@' + serverName + ':' + portNum + ':' + dataBase + ']]]') 

   #--------------------------------------------------------------
   # Save all the changes 
   #--------------------------------------------------------------
   print ""
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