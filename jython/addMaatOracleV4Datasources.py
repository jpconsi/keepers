import sys, java

def createV4DataSource (abIdent, dbServer, dbPort, dbName):

   global AdminApp, AdminConfig

   newjdbc = AdminConfig.getid('/ServerCluster:maat-cluster-' + abIdent + '/JDBCProvider:Oracle JDBC Driver/')

   nameAttr = ['name', 'MIGLDS']
   jndiAttr = ['jndiName', 'jdbc/oceans']
   dbNameAttr = ['databaseName', dbServer]
   defaultUserAttr = ['defaultUser', 'matrixuser']
   defaultPwAttr = ['defaultPassword', 'matrixuser']
   ds4Attrs = [nameAttr, jndiAttr, dbNameAttr, defaultUserAttr, defaultPwAttr]

   print "Creating WAS40 Datasource for maat-cluster-" + abIdent

   new40ds = AdminConfig.create('WAS40DataSource', newjdbc, ds4Attrs)

   # minpsAttr = ['minimumPoolSize', '1']
   # maxpsAttr = ['maximumPoolSize', '50']
   # connAttr = ['connectionTimeout', '180']
   # idleAttr = ['idleTimeout', '600']
   # orphanAttr = ['orphanTimeout', '1200']
   # scsAttr = ['statementCacheSize', '18']
   # dACCAttr = ['disableAutoConnectionCleanup', 'false']
   # cpAttrs = [minpsAttr, maxpsAttr, connAttr, idleAttr, orphanAttr, scsAttr, dACCAttr]

   # print "Creating WAS40 Connection Pool"

   # AdminConfig.create('WAS40ConnectionPool', new40ds, cpAttrs)

   propSet = AdminConfig.showAttribute(new40ds, 'propertySet') 

   urlNameAttr = [ 'name', 'URL']
   urlTypeAttr = ['type', 'java.lang.string']
   urlValueAttr = ['value', 'jdbc:oracle:thin:@' + dbServer + ':' + dbPort + ':' + dbName] 
   rpAttrs = [urlNameAttr, urlTypeAttr, urlValueAttr]

   print "Creating Custom Properties"

   AdminConfig.create('J2EEResourceProperty', propSet, rpAttrs)

   print "Saving Configuration"

   AdminConfig.save()

#-----------------------------------------------------------------
# Main
#-----------------------------------------------------------------
if (len(sys.argv) != 4):

   print "createV4DataSource: this script requires 4 parameters:"  
   print "a/b identifier, dbServer, dbPort, dbName"
   print ""
   print "e.g.:     createV4DataSource a lalwvtstsql1 1523 eieio" 

else:

   createV4DataSource(sys.argv[0], sys.argv[1], sys.argv[2], sys.argv[3])

   
