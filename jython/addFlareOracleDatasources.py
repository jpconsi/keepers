import sys, java

def buildOracleDatasources(abIdent, dsUrl, nXaDsUrl):

   jdbcId = AdminConfig.getid('/Cell:psm-cell/ServerCluster:flare-cluster-' + abIdent + '/JDBCProvider:Oracle JDBC Driver (XA)/')

   print "" 
   print "buildOracleDatasources: create Flare Datasource"

   newDS = AdminTask.createDatasource(jdbcId, '[-name "Flare Datasource" -jndiName com.vacationclub.solar.usage.datasource_jndi -dataStoreHelperClassName com.ibm.websphere.rsadapter.Oracle10gDataStoreHelper -componentManagedAuthenticationAlias flare -containerManagedPersistence false -xaRecoveryAuthAlias flare -configureResourceProperties [[URL java.lang.String ' + dsUrl + ']]]')

   maxConAttr = ['maxConnections', '20']
   cpAttrs = [maxConAttr]

   AdminConfig.create('ConnectionPool', newDS, cpAttrs)
   
   print ""
   print "buildOracleDatasources: create Flare Non-XA Datasource"

   newDS = AdminTask.createDatasource(jdbcId, '[-name "Flare Non-XA Datasource" -jndiName jdbc/FlareNonXADS -dataStoreHelperClassName com.ibm.websphere.rsadapter.Oracle10gDataStoreHelper -componentManagedAuthenticationAlias flare -containerManagedPersistence false -xaRecoveryAuthAlias flare -configureResourceProperties [[URL java.lang.String ' + nXaDsUrl + ']]]')

   maxConAttr = ['maxConnections', '20']
   cpAttrs = [maxConAttr]

   AdminConfig.create('ConnectionPool', newDS, cpAttrs)
   
   flareds = AdminConfig.getid('/ServerCluster:flare-cluster-' + abIdent + '/JDBCProvider:Oracle JDBC Driver (XA)/DataSource:Flare Non-XA Datasource')

   propSet = AdminConfig.showAttribute(flareds, 'propertySet') 

   ntdsNameAttr = [ 'name', 'nonTransactionalDataSource']
   ntdsTypeAttr = ['type', 'java.lang.Boolean']
   ntdsValueAttr = ['value', 'true'] 
   rpAttrs = [ntdsNameAttr, ntdsTypeAttr, ntdsValueAttr]

   print "Creating Custom Properties"

   AdminConfig.create('J2EEResourceProperty', propSet, rpAttrs)

   print "buildOracleDatasources: saving the configuration"
   AdminConfig.save()
 
#-----------------------------------------------------------------
# Main
#-----------------------------------------------------------------
if (len(sys.argv) != 7):

   print "buildFlareOracleDatasources: this script requires 7 parameters:"
   print "a/b identifier, Flare Datasource server, port & db"
   print "Flare Non-XA Datasource server, port & db"
   print ""
   print "e.g.:     buildFlareOracleDatasources a DSserver 1521 DSdbName DSNXAserver 1521 DSNAdb" 

else:

   u1 = 'jdbc:oracle:thin:@' + sys.argv[1] + ':' + sys.argv[2] + ':' + sys.argv[3]
   u2 = 'jdbc:oracle:thin:@' + sys.argv[4] + ':' + sys.argv[5] + ':' + sys.argv[6]
   buildOracleDatasources(sys.argv[0], u1, u2)

#endif