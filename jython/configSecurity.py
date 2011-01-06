def configSecurity(env):
   
   print("configSecurity: Configuring Admin Console AD connection")

   cell = AdminControl.getCell()
   sec = AdminConfig.getid("/Cell:" + cell + "/Security:/")
   ldap = AdminConfig.showAttribute(sec, "userRegistries").split(' ')
   ldapId=ldap[2]
   hId = AdminConfig.showAttribute(ldapId, "hosts")
   hostsId = hId[1:-1]
   searchFilterId = AdminConfig.showAttribute(ldapId, "searchFilter")

   hAttr = ["host", "lalfimvp0adc05.mv.marrcorp.marriott.com"]
   pAttr = ["port", "389"]
   hpAttr = [hAttr, pAttr]

   AdminConfig.modify(hostsId, hpAttr)

   ufAttr = ["userFilter", "(&(sAMAccountName=%v)(objectcategory=user))"]
   gfAttr = ["groupFilter", "(&(cn=%v)(objectcategory=group))"]
   uimAttr = ["userIdMap", "user:sAMAccountName"]
   gimAttr = ["groupIdMap", "*:cn"]
   gmimAttr = ["groupMemberIdMap", "memberof:member"]
   cmmAttr = ["certificateMapMode", "EXACT_DN"]
   cfAttr = ["certificateFilter", ""]

   attrs = []
   attrs.append(ufAttr)
   attrs.append(gfAttr)
   attrs.append(uimAttr)
   attrs.append(gimAttr)
   attrs.append(gmimAttr)
   attrs.append(cmmAttr)
   attrs.append(cfAttr)

   AdminConfig.modify(searchFilterId, attrs)

   realmAttr = ["realm", "lalfimvp0adc05.mv.marrcorp.marriott.com:389"]
   uRSIDAttr = ["useRegistryServerId", "false"]
   IdAttr = ["primaryAdminId", "svc-wasadmin"]
   typeAttr = ["type", "ACTIVE_DIRECTORY"]
   baseDnAttr = ["baseDN", "DC=mv,DC=marrcorp,DC=marriott,DC=com"]
   bindDnAttr = ["bindDN", "CN=svc-wasadmin,OU=Service Accounts,DC=mv,DC=marrcorp,DC=marriott,DC=com"]
   # bindPWAttr = ["bindPassword", "{xor}LAgtFwt1GDAmACZnJzE9NSsIZ3RyDS5seQ=="]
   bindPWAttr = ["bindPassword", "sWrHT*Goy_y8xnbjtW8+-Rq3&"]

   attrs = []
   attrs.append(realmAttr)
   attrs.append(uRSIDAttr)
   attrs.append(IdAttr)
   attrs.append(typeAttr)
   attrs.append(baseDnAttr)
   attrs.append(bindDnAttr)
   attrs.append(bindPWAttr)
 
   AdminConfig.modify(ldapId, attrs)

   AdminConfig.save()

   aURAttr = ["activeUserRegistry" , ldapId]
   eAttr = ["enabled", "true"]
   aEAttr = ["appEnabled", "false"]
   eJ2SAttr = ["enforceJava2Security", "false"]

   attrs = []
   attrs.append(aURAttr)
   #attrs.append(eAttr)
   attrs.append(aEAttr)
   attrs.append(eJ2SAttr)

   AdminConfig.modify(sec, attrs)

   AdminConfig.save()

   ata = AdminConfig.getid("/Cell:" + cell + "/AuthorizationTableExt:/").split('\n')
   ate = ""

   for i in ata:

      if i[:6] == 'naming':

         ate = i

      #endif

   #endfor

   auth = AdminConfig.showAttribute(ate, 'authorizations')
   auth = auth[1:-1]
   authArray = auth.split(' ')

   for i in authArray:

      ss = AdminConfig.showAttribute(i, 'specialSubjects')
      ss = ss[1:-1]
      ssArray = ss.split(' ')

      if len(ssArray) == 1:

         AdminConfig.create('EveryoneExt', i, '[]', 'specialSubjects')

      #endif

   #endfor

   AdminConfig.save()

   if (env == 'nonprod'):

      print("configSecurity: Configuring cleartran qa cert")
      AdminTask.retrieveSignerFromPort('[-host cleartran.qa.mellon.com -port 443 -keyStoreName CellDefaultTrustStore -keyStoreScope (cell):ws-cell -sslConfigName CellDefaultSSLSettings -sslConfigScopeName (cell):ws-cell -certificateAlias cleartranqa ]')

   else:

      print("configSecurity: Configuring cleartran prod cert")
      AdminTask.retrieveSignerFromPort('[-host cleartran.mellon.com -port 443 -keyStoreName CellDefaultTrustStore -keyStoreScope (cell):ws-cell -sslConfigName CellDefaultSSLSettings -sslConfigScopeName (cell):ws-cell -certificateAlias cleartran ]')

   #endif

   print("configSecurity: Configuring cnpjax cert")

   AdminTask.retrieveSignerFromPort('[-host www.cnpjax.com -port 443 -keyStoreName CellDefaultTrustStore -keyStoreScope (cell):ws-cell -sslConfigName CellDefaultSSLSettings -sslConfigScopeName (cell):ws-cell -certificateAlias cnpjax ]')

   AdminConfig.save()


#-----------------------------------------------------------------
# Main
#-----------------------------------------------------------------
if (len(sys.argv) != 1):

   print "configSecurity: this script requires 1 parameter:"
   print "prod or nonprod"
   print ""
   print "e.g.:     configSecurity nonprod"

else:

   if (sys.argv[0] == "prod" or sys.argv[0] == "nonprod"):
      
      configSecurity(sys.argv[0])

   else:

      print("configSecurity: Invalid parameter. Must be 'prod' or 'nonprod'.")

   #endif

#endif
