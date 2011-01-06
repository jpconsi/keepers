print "configFlexRegistry: Applying the Flex Registry settings"

AdminTask.applyWizardSettings('[-secureApps true -secureLocalResources false -userRegistryType CustomUserRegistry -customRegistryClass com.marriott.security.custom.Was5FlexRegistry -customProps flex.properties-file=e:/was61/customreg/flex.properties; -adminName svc-wasadmin -ignoreCase false ]')

print "configFlexRegistry: Saving Flex Registry settings"

AdminConfig.save()

