import sys
from time import sleep

#--------------------------------------------------------------
# set up globals
#--------------------------------------------------------------
global AdminConfig
global AdminControl
global AdminApp

def addDevCerts():

   print "addWebCerts: Adding Dev-MarriottDevCA1.cer"

   AdminTask.addSignerCertificate('[-keyStoreName CellDefaultTrustStore -keyStoreScope (cell):ws-cell -certificateFilePath e:/install-media/dev-certs/Dev-MarriottDevCA1.cer -certificateAlias Dev-MarriottDevCA1 ]')  

   print "addWebCerts: Saving"

   AdminConfig.save()

   print "addWebCerts: Adding Dev-MarriottDevSubCA1.cer"

   AdminTask.addSignerCertificate('[-keyStoreName CellDefaultTrustStore -keyStoreScope (cell):ws-cell -certificateFilePath e:/install-media/dev-certs/Dev-MarriottDevSubCA1.cer -certificateAlias Dev-MarriottDevSubCA1 ]')  

   print "addWebCerts: Saving"

   AdminConfig.save()

   print "addWebCerts: Adding equifax_marredsdev.cer"

   AdminTask.addSignerCertificate('[-keyStoreName CellDefaultTrustStore -keyStoreScope (cell):ws-cell -certificateFilePath e:/install-media/dev-certs/equifax_marredsdev.cer -certificateAlias equifax_marredsdev ]')  

   print "addWebCerts: Saving"

   AdminConfig.save()

   print "addWebCerts: Adding MVCIWEBDEV_ROOT_CA1.cer"

   AdminTask.addSignerCertificate('[-keyStoreName CellDefaultTrustStore -keyStoreScope (cell):ws-cell -certificateFilePath e:/install-media/dev-certs/MVCIWEBDEV_ROOT_CA1.cer -certificateAlias MVCIWEBDEV_ROOT_CA1 ]')  

   print "addWebCerts: Saving"

   AdminConfig.save()

   print "addWebCerts: Adding OOD-Staging_secure-ausomxhpa.crmondemand.com.cer"

   AdminTask.addSignerCertificate('[-keyStoreName CellDefaultTrustStore -keyStoreScope (cell):ws-cell -certificateFilePath e:/install-media/dev-certs/OOD-Staging_secure-ausomxhpa.crmondemand.com.cer -certificateAlias OOD-Staging_secure-ausomxhpa.crmondemand.com ]')  

   print "addWebCerts: Saving"

   AdminConfig.save()


def addProdCerts():

   print "addWebCerts: Adding Prod-MarriottCA1.cer"

   AdminTask.addSignerCertificate('[-keyStoreName CellDefaultTrustStore -keyStoreScope (cell):ws-cell -certificateFilePath e:/install-media/prod-certs/Prod-MarriottCA1.cer -certificateAlias Prod-MarriottCA1 ]')  

   print "addWebCerts: Saving"

   AdminConfig.save()

   print "addWebCerts: Adding Prod-MarriottSubCA1.cer"

   AdminTask.addSignerCertificate('[-keyStoreName CellDefaultTrustStore -keyStoreScope (cell):ws-cell -certificateFilePath e:/install-media/prod-certs/Prod-MarriottSubCA1.cer -certificateAlias Prod-MarriottSubCA1 ]')  

   print "addWebCerts: Saving"

   AdminConfig.save()

   print "addWebCerts: Adding equifax_marreds.cer"

   AdminTask.addSignerCertificate('[-keyStoreName CellDefaultTrustStore -keyStoreScope (cell):ws-cell -certificateFilePath e:/install-media/prod-certs/equifax_marreds.cer -certificateAlias equifax_marreds ]')  

   print "addWebCerts: Saving"

   AdminConfig.save()

   print "addWebCerts: Adding OOD-Prod_secure-ausomxhoa.crmondemand.com.cer"

   AdminTask.addSignerCertificate('[-keyStoreName CellDefaultTrustStore -keyStoreScope (cell):ws-cell -certificateFilePath e:/install-media/prod-certs/OOD-Prod_secure-ausomxhoa.crmondemand.com.cer -certificateAlias OOD-Prod_secure-ausomxhoa.crmondemand.com ]')  

   print "addWebCerts: Saving"

   AdminConfig.save()


#-----------------------------------------------------------------
# Main
#-----------------------------------------------------------------
if (len(sys.argv) != 1):

   print "addWebCerts: this script requires 1 parameter:"
   print "     prod or nonprod"
   print ""
   print "e.g.:     addSharedLibraries prod" 

else:

   if (sys.argv[0] == 'nonprod'):

      addDevCerts()

   else:

      addProdCerts()

   #endif


