<h1>Aquifer</h1><p align="center">
<h3>Innovative instruments for the integrated management of groundwater in a context of increasing scarcity of water resources</h3></p>
<p align="center"><img align="center" src="https://github.com/C-R-C-C/Sudoe_AQUIFER/blob/7943a2ce40d12c08c771c9c4349af5c0bcc747a9/images/LOGO_sudoe.png"></p>
<img src="https://github.com/C-R-C-C/Sudoe_AQUIFER/blob/7943a2ce40d12c08c771c9c4349af5c0bcc747a9/images/footer.png">
Groundwaters are an essential element of the hydrological cycle. In that regard, the scientific community has stated that several fields of knowledge need improvement. Namely, our knowledge on aquifers, on the implementation of reliable monitoring networks, and about the implication of the public sector in the hydraulic management and that of the end-users in the sustainable management of aquifers. The main aim of AQUIFER is to capitalize, test, disseminate and transfer innovative practices for the preservation, monitoring and integrated management of the aquifers. All this in order to provide support to the decision-making processes on groundwater resources management, to improve the technological transfer towards the local agents, to create new synergies, and to develop common tools in a context of scarcity of hydrological resources and environmental threats.

The main innovative element of AQUIFER is a global consideration of the abovementioned problems. Firstly, this includes the experimentation about the key elements of “quality” and “quantity” of water through tools such as the management of aquifers recharge and the networks for hydrological monitoring and modelling. Secondly, the detection, testing and implementation of innovations by the three water clusters, which are connected to a network of water stakeholders and start-ups. Thirdly, the creation of a decision support tool and a good practices showcasing. This will be materialized in a permanent and free webpage for all water stakeholders.

The project has three fundamental aims:

To establish relationships among groundwater resources, surficial waters and / or saline waters, in a context of global change.
To test and develop innovative solutions for groundwater management, to face the risks related to the water cycle sustainability.
To identify, analyse and disseminate innovative solutions to be used for relevant stakeholders in the decision-making processes.
 
 <h2>Realtime Groundwater Monitoring System</h2>
 
 In this repository you have access to configuration files and a small setup guide to recreate a system that receives data from OTT ecoLog probes family, store it in a MySQL database and visualize it with Grafana. Eveything using different open source software. The configuration showed is just one way
 of doing it, as with many software and hardware projects there are many ways. The method used here works perfectly as of May of 2022.
 
 <img src="https://github.com/C-R-C-C/Sudoe_AQUIFER/blob/c07b741be2d2685c0466f9e38c8451c479a72d8e/Esquema.png">
 
 <h3>Steps:</h3>
 
 <h4> 1- Setup OTT ecoLogs </h4>
 It is required to select the "OTT MIS" data format and "HTTP POST" Protocol type, as part of the "Settings Modem" configuration.
 <img src="https://github.com/C-R-C-C/Sudoe_AQUIFER/blob/e89bc1921ed5e133799dc9058e8e250d74ff626b/images/OTT_CONFIG_CRCC2.png">
 <p>Then, you have to config the URL and port where your python server script is going to be, ie, http://mydomain/cgi-bin/logger.cgi</p>
 <img src="https://github.com/C-R-C-C/Sudoe_AQUIFER/blob/e89bc1921ed5e133799dc9058e8e250d74ff626b/images/OTT_CONFIG_CRCC.png">
 
 <h4> 2- Setup Python script </h4>
 This python script receives the call from the ecoLog probe, searches for raw data and publish it to a Mqtt broker. The script could be changed to store data directly to the database thus not requiring the Mqtt and Node-red part, but because this network it is been setup for many different kind of probes and other IoT devices, the ubiquitous MQTT route has been selected.
 There are many guides on Internet on how to setup a <i>Linux+Apache+Mosquitto Broker</i> or <i>Linux+Nginx+Mosquitto Broker</i> to execute python scripts. Once you have tested the setup, you can install the logger.cgi script and wait for the ecoLog to send data, with a basic mqtt monitor command (mosquitto_sub, for example, you could see raw sensor data coming from the probes).
 
 <h4> 3- Mysql </h4>
  You need a Mysql Server installed, in the Mysql folder you have a script to create the tables needed for this setup. Basicly there are three tables:
  <li> datos_campo (id, timestamp,topic,data) where you store the raw data coming from the probes </li>
  <li> sensor (id, name) where you store the descriptions for every sensor that each probe sent, ir, 0001, Water level, 0002, Temperature, and so on.</li>
  <li> sites (id, name, utmX, utmY,code ...) this is an optional table to show information about the sites.
  The nodered script will store data here for every sensor mqtt message received.
 
 <h4> 4- NodeRed </h4>
 You need to havr a Node-Red server installed to deploy the script (json based, import) that resides in the nodered folder.
 This script gets the raw data from the mqtt message and builds an INSERT query to execute it in the DB server. It also has debug output and optional formatting for dashboard visualization.
 <img src="https://github.com/C-R-C-C/Sudoe_AQUIFER/blob/9d2b1eca88820da170d62e30e1c4c699b8dee29d/images/NodeRED_flow.png">
 
 <h4> 5- Grafana </h4>
 There are many guides on Internet as well to install a Grafana server. Once you have it installed, you can import the dashboard from the grafana folder of the repository. There has to be a datasource with the name <i>"IoT_piezos"</i> pointing at your Mysql database where the tables and data from the previous points is. In order for the panels to show the correct information you should have put the correct "zb", "pi" and "z" info of each installation site. For a reference look a the installation pic:
 <img src="https://github.com/C-R-C-C/Sudoe_AQUIFER/blob/33336a49239fdab39c36a1c6ae8b99ef71f4a73e/images/Aquifer%20CRCC%20-%20Grafana%203.png">
 
 If everything went well you should be able to see a dashboard like this:
 
 <img src="https://github.com/C-R-C-C/Sudoe_AQUIFER/blob/33336a49239fdab39c36a1c6ae8b99ef71f4a73e/images/Aquifer%20CRCC%20-%20Grafana.png">
 <p> and </p>
 <img src="https://github.com/C-R-C-C/Sudoe_AQUIFER/blob/33336a49239fdab39c36a1c6ae8b99ef71f4a73e/images/Aquifer%20CRCC%20-%20Grafana%202.png">
 
 
 <b>@ 2022 - Comunidad de Regantes del Campo de Cartagena </b>
 
 
 
 
 
 
 
 
 
 
 
