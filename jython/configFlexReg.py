print("configFlexReg: Configuring Flex Registry")

cell = AdminControl.getCell()
sec = AdminConfig.getid("/Cell:" + cell + "/Security:/")
cur = AdminConfig.list("CustomUserRegistry", sec)

attrs = []
attrs.append(["primaryAdminId", "svc-wasadmin"])
attrs.append(["useRegistryServerId", "true"])
attrs.append(["serverId", "svc-wasadmin"])
attrs.append(["serverPassword", "sWrHT*Goy_y8xnbjtW8+-Rq3&"])
attrs.append(["customRegistryClassName", "com.marriott.security.custom.Was5FlexRegistry"])
attrs.append(["ignoreCase", "true"])
AdminConfig.modify(cur, attrs)
 
name = ["name", "flex.properties-file"]
value = ["value", "e:/WebSphere/customreg/flex.properties"]
attrs = [name, value]
AdminConfig.create("Property", cur, attrs )

AdminConfig.save()

print("configFlexReg: Configuring Single Sign On")

am =  AdminConfig.showAttribute(sec, "authMechanisms")
am = am[1:-1]
sso = AdminConfig.showAttribute(am, "singleSignon")

dnAttr = ["domainName", ".my-vacationclub.com"]
enAttr = ["enabled", "true"]
rsslAttr = ["requiresSSL", "false"]
   
attrs = []
attrs.append(dnAttr)
attrs.append(enAttr)
attrs.append(rsslAttr)
AdminConfig.modify(sso, attrs)

AdminConfig.save()

print("configSecurity: Enabling Security")

aURAttr = ["activeUserRegistry" , cur]
eAttr = ["enabled", "true"]
aEAttr = ["appEnabled", "true"]
eJ2SAttr = ["enforceJava2Security", "false"]

attrs = []
attrs.append(aURAttr)
attrs.append(eAttr)
attrs.append(aEAttr)
attrs.append(eJ2SAttr)
AdminConfig.modify(sec, attrs)

AdminConfig.save()



