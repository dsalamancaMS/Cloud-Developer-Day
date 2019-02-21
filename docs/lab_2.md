# Lab 2 - Application Migration

In this lab we will be migrating a monolythic application to a Platform as a Service Environment hosted in Azure App Service.

## Tools used in this lab

  - [Visual Studio Code](https://code.visualstudio.com/)
  - [Windows Subsystem For Linux](https://docs.microsoft.com/en-us/windows/wsl/enterprise)
  - [Microsoft Azure App Service](https://azure.microsoft.com/en-us/services/app-service/?v=18.51)

## Migrating the application

In this step of the workshop, you will have to collect all the application files and migrate them to an Azure App Service. All you know is that the application lives in */usr/local/flask*, in the same server as the database.

All the steps in this lab are performed in the Azure Lab Service workstation.

1. On Azure Lab Service Workstation, open the Ubuntu Windows Subsystem for Linux app in your taskbar:
   
    ![ubuntuwsl](img/lab2/ubuntuwsl.png)
2. Once open type the following command to connect to the application server: 
  ```bash
  ssh <UserAssigned>@<IP>
  ```

3. Check the application files under the indicated directory by running:

  ```bash
  ls -lath /usr/local/flask/
  ```
 
4. Check if the following files are present:
   * static
   * templates
   * estusflask.py
  
5. Log out from the server by running: 
   ```bash
   exit
   ```
6. Once you  are back on the WSL prompt, extract the files from the application server by running the following commands: 
   ```bash
   cd /mnt/c/Users/LabUser/Documents
   mkdirk app
   cd app
   scp -r <user>@<ip>:/usr/local/flask/*  .
   ```
7. Now with the files on your local machine, open Visual Studio Code to begin with the migration process:
   
   ```bash
   code .
   ```

8. We now need to download the appropiate extensions in order to be able to publish our application to azure. Click on the extensions option in VS Code: ![ext](img/lab2/extension.png)  
9. In the Extensions Marketplace look for the Azure Account Extension and click on **Install**: ![azracnt](img/lab2/azureaccnt.png)
10. Do the same as in the previous step but for the Azure App Service Extension: ![appsvc](img/lab2/appsvc.png)
    
11. Once both extensions have been installed, an Azure icon will appear on the left: ![azr](img/lab2/azricn.png). Click on it and login to your subscription:
    
  <img src="img/lab2/login.png" alt="login" align="middle">