myRole = 'deployer'


cell = AdminControl.getCell()
ata = AdminConfig.getid("/Cell:" + cell + "/AuthorizationTableExt:/").split('\r')

ate = ""

for i in ata:

   if i[:5] == 'admin':

      ate = i

   #endif

#endfor

auth = AdminConfig.showAttribute(ate, 'authorizations')
auth = auth[1:-1]
authArray = auth.split(' ')

for i in authArray:

    role = AdminConfig.showAttribute(i, 'role')
    roleName = AdminConfig.showAttribute(role, 'roleName')

    if roleName == myRole:

      AdminConfig.create('UserExt', i, [['name', 'joe']], 'users')

      ss = AdminConfig.showAttribute(i, 'specialSubjects')
      ss = ss[1:-1]
      ssArray = ss.split(' ')

      if len(ssArray) == 1:

         AdminConfig.create('ServerExt', i, '[]', 'specialSubjects')
         AdminConfig.create('PrimaryAdminExt', i, '[]', 'specialSubjects')

      #endif

   #endif

#endfor

AdminConfig.save()