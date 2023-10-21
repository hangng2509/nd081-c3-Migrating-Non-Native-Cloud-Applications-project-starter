#Resource Group
resourceGroup="lab-3-rg"
location="eastus"
#PostgreSQL
postgreServerName="techconfdb-server-lab-3"
postgreSkuName="B_Gen5_1"
postgreAdminUser="admin123"
postgreAdminPassword="admin@Ne123"
postgreDatabaseName="techconfdb"
postgreFirewallRuleName="AllowAllIPs"
#Service Bus 
uniqueId=20231018
resourceGroup="lab-3-rg"
location="eastus"
storageAccount="techconfstoragelab3" 
serviceBus="servicebus$uniqueId"
quque="notificationqueue"
#Storage
storageAccount="techconfstoragelab3"
storageSku="Standard_LRS"
#Function App
funcApp="techconf-function-app-lab-3"
functionVersion="4"
functionOsType="Linux"
functionRuntime="python"
#Service App
appServicePlanName="techconf-service-plan"
appName="techconf-lab-3"
appSku="F1"
appRuntime="PYTHON:3.11"