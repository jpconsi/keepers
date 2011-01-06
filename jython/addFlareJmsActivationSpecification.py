import sys, java

def buildJmsActivationSpecification(abIdent):

   print ""
   print "buildJmsActivationSpecification: create DynamicServiceManagerBeanSpec"
   AdminTask.createSIBJMSActivationSpec('flare-cluster-' + abIdent + '(cells/psm-cell/clusters/flare-cluster-' + abIdent + '|cluster.xml)', '[-name DynamicServiceManagerBeanSpec -jndiName com.vacationclub.solar.usage.manager.dynamic_service_spec_jndi -destinationJndiName com.vacationclub.solar.usage.manager.dynamic_service_queue_jndi -description -acknowledgeMode Auto-acknowledge -authenticationAlias -busName "Flare Bus" -clientId -durableSubscriptionHome -messageSelector -subscriptionDurability NonDurable -subscriptionName -readAhead Default -target -targetType BusMember -targetSignificance Preferred -targetTransportChain -shareDataSourceWithCMP false]')

   print ""
   print "buildJmsActivationSpecification: saving the configuration"
   AdminConfig.save()
 
#-----------------------------------------------------------------
# Main
#-----------------------------------------------------------------

if (len(sys.argv) != 1):

   print "buildJmsActivationSpecification: this script requires 1 parameter:,"
   print "a/b identifier"
   print ""
   print "e.g.:     buildJmsActivationSpecification a" 

else:

   buildJmsActivationSpecification(sys.argv[0])

#endif