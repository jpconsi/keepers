#******************************************************************************
# Procedure:   	createVirtualHost
# Description:	Create a new virtual host. If it already exists, modify it by
#			adding a host alias.
# Author:      	Gale Botwick - gbotwick@us.ibm.com
#****************************************************************************** 
import sys
def createVirtualHost ( vhostName, dnsHost, port, env ):

        if dnsHost == 'x': 
           dnsHost= '*'

        if env != '': 
           dnsHost= env + "." + dnsHost 

        print dnsHost

	vhId = getConfigItemId("Cell", cellName, "", "VirtualHost", vhostName)
	if (len(vhId) == 0):
		# create virtual host
		cellId = AdminConfig.getid("/Cell:"+cellName+"/")
		
		try:
			_excp_ = 0
			vHost = AdminConfig.create( "VirtualHost", cellId, [["name", vhostName]] )
		except:
			_type_, _value_, _tbck_ = sys.exc_info()
			vHost = `_value_`
			_excp_ = 1
		#endTry 
		if (_excp_ ):
			print "Caught Exception creating virtual host"
			print vHost
			return
		#endIf 
	#endIf

	addHostAlias(vhostName, dnsHost, port)
	print "saving the configuration"
        AdminConfig.save()

#endDef
#--------------------------------------------------------------------
# Procedure:	getConfigItemId
# Description:	Gets the Config Item Identifier
#
# Parameters:	scope
#			scopeName
#			nodeName    (only used for server scope)
#			objectType
#			item
#
# Returns:	ConfItemId
#--------------------------------------------------------------------
def getConfigItemId (scope, scopeName, nodeName, objectType, item):
	global AdminConfig

	scope = scope.title()
	if (scope == "Cell"):
		confItemId = AdminConfig.getid("/Cell:"+scopeName+"/"+objectType+":"+item)
	elif (scope == "Node"):
		confItemId = AdminConfig.getid("/Node:"+scopeName+"/"+objectType+":"+item)
	elif (scope == "Cluster"):
		confItemId = AdminConfig.getid("/ServerCluster:"+scopeName+"/"+objectType+":"+item)
	elif (scope == "Server"):
		confItemId = AdminConfig.getid("/Node:"+nodeName+"/Server:"+scopeName+"/"+objectType+":"+item)
	#endIf
	return confItemId
#endDef
#--------------------------------------------------------------------
# Procedure:	addHostAlias
# Description:  	Adds host alias if it doesn't already exist
#
# Parameters:	hostName 	(eg: "default_host")
#			dnsHost 	(eg: "*")
#			port 		(eg: 9085)
#
# Returns:	None
#--------------------------------------------------------------------
#import sys
def addHostAlias (hostName, dnsHost, port ):

	
       
	global AdminConfig, AdminControl
	

	hostTarget = findConfigTarget(hostName, "VirtualHost")
	
	if (hostTarget == 0):
		print "Can not find "+hostName
		return
      #endIf

	# determine whether alias exists
	oNeedToDefine = 1
	aliasList = AdminConfig.list("HostAlias", hostTarget).split(lineSeparator)
	if (aliasList != ['']):
		for HAEntry in aliasList:
			oHostName = AdminConfig.showAttribute(HAEntry, "hostname")
			oPort = AdminConfig.showAttribute(HAEntry, "port")
			if oHostName == dnsHost:
				if oPort == port:
					print "The hostname "+hostName+ " has already defined host alias: "+HAEntry
					print "New entry will not be added."
					oNeedToDefine = 0
					break 
 				#endIf 
			#endIf 
		#endFor 
	#endIf

	if (oNeedToDefine == 1):
		attrHA = [["hostname", dnsHost], ["port", port]]
		print "Adding Host Alias to "+hostName
		try:
			_excp_ = 0
			hAlias = AdminConfig.create( "HostAlias", hostTarget, attrHA )
		except:
			_type_, _value_, _tbck_ = sys.exc_info()
			hAlias = `_value_`
			_excp_ = 1
		#endTry 
		if (_excp_ ):
			print "Caught Exception creating host alias"
			print hAlias
			return
		#endIf 

	#endIf 
	
       
	return
#endDef 

#--------------------------------------------------------------------
# Procedure:	findConfigTarget
# Description: 	Determine if there is a config element for given
#			name and type
#
# Parameters:	nameSearch	 
#			type		(Cell, Node, JDBCProvider)
#
# Returns:	targetName = success 
#		0  = does not exist
#--------------------------------------------------------------------
def findConfigTarget ( nameSearch, type ):
        global AdminApp, AdminConfig

        elements = AdminConfig.list(type)
	if (elements == " "):
		return 0
	#endIf
	elementList = elements.split(lineSeparator)
	for element in elementList:
		element=element.rstrip()
		if (len(element) > 0 ):
			name=AdminConfig.showAttribute(element,"name")
			if (nameSearch == name):
				return element
			#endIf
		#endIf
	#endFor
	return 0	
#endDef 

if (len(sys.argv) != 4):
   createVirtualHost(sys.argv[0], sys.argv[1], sys.argv[2], "")
else:
   createVirtualHost(sys.argv[0], sys.argv[1], sys.argv[2], sys.argv[3])
