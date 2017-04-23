# Speech Commands

Speech Commands runs in a Chrome browser under Android, Windows, 
or Linux on whatever computer or phone you are using to control the robot. 
IOS is not supported, as it does not support the Web Speech API.  Speech Commands uses rosbridge to communicate with the robot.

If you use an Android phone, the vocabulary can be downloaded, so speech recognition can take place locally.

The program is contained in a single web page, at present called speechcommands.html, which is loaded from a web server.
The web server (usually) runs on the robot.  Thus the program can be loaded whenever the robot is present.
Because of the use of the microphone, HTTPS must be used, which in turn requires WSS for the web socket to communicate with the robot. Because of this, both the server and rosbridge must be set up to accomodate SSL, hence the extra steps in the installation below.

##Usage
Follow these instructions to install and run speech commands.

### Installation:

* Note the robot's IP address for later use as a url. 
* Install Rosbridge: 

        sudo apt-get install ros-kinetic-rosbridge-suite
* Install the apache2 web server. This also installs the ssl-certs package, which sets up the snakeoil certificate and key.

        sudo apt-get install apache2
* Enable the apache2 ssl module

        sudo a2enmod ssl
* Configure apache2 for HTTPS

	sudo make-ssl-cert generate-default-snakeoil --force-overwrite
        sudo a2ensite default-ssl
* Restart the service. You should not need to enter a passphrase.

        sudo service apache2 restart
* Test the server by addressing it from a browser, for instance http://10.0.0.25/index.html. You should get the apache2 default page.  
* (TODO The default page should be replaced by one that has been customized.)
* Test again using HTTPS.  The result should be a security warning, since you are not using a certified ssl key.
* Copy speechcommands.html from wherever it is to /var/www/html on the robot.
* Copy the /scripts and the /fonts folders as subfolders to /var/www/html on the robot.

Set up a self-signed certificate ("snakeoil") to allow ssl communications between the browser and the robot. 

* Copy /etc/ssl/private/ssl-cert-snakeoil.key to /etc/ssl/certs/  (may need sudo)
* chmod /etc/ssl/certs/ssl-cert-snakeoil.key so it is readable. /etc/ssl/certs/ssl-cert-snakeoil.pem should already be readable. 

        `sudo chmod 644 /etc/ssl/certs/ssl-cert-snakeoil.key`
* Modify these 3 lines of the rosbridge launch file, to tell rosbridge where to find the certificate and key:
	(The rosbridge launch file is at  /opt/ros/kinetic/share/rosbridge_server/launch/rosbridge_websocket.launch)

        <arg name="ssl" default="true" />
		<arg name="certfile" default="/etc/ssl/certs/ssl-cert-snakeoil.pem" />
		<arg name="keyfile" default="/etc/ssl/certs/ssl-cert-snakeoil.key" />

       
* Install tf2_web_republisher

		sudo apt-get install  ros-kinetic-tf2-web-republisher


### Startup

Each time you wish to start using speech commands:

* Bring up your robot.  On Loki, you would run loki_base.

* Launch the rosbridge_server on the robot: (Refer to  http://wiki.ros.org/rosbridge_suite/Tutorials/RunningRosbridge)

        roslaunch rosbridge_server rosbridge_websocket.launch
* Run the tf2_web_republisher on the robot:

        rosrun tf2_web_republisher tf2_web_republisher
* In the Chrome browser on your laptop or Android phone, load the speechcommands.html page, using https with the robot's url. The first time, the browser will respond with an error message, which essentially asks you to OK trusting the self-signed certificate.
* in the speechcommands.html page, enter the url with port number (usually 9090)

        <robot's url>:9090 
into the Robot URL box and click the Connect button.  The button should now say Disconnect, and you should hear "Connected". 
If you intend using speech, use "wss" or "https" for the robot's websocket address; 
otherwise you can still click the arrows if you use "ws" or "http".

### Running
* Click any arrow to move the robot.
* Click the Microphone to use speech. You will be requested to allow the use of the mike.  Do it.
* Say, "forward", or other commands.  Check the Help for valid commands. 
* In environments where there is a lot of competing speech, you can turn on the "Wakeup Word" feature, in Settings.  When it is on, all commands must be prefaced by the wakeup word, "robot". 

#To Do / Issues
Though you can set waypoints, they are not persistent across shutdown/restart.  

#Dependencies

In the robot: rosbridge_server and tf2_web_republisher.
In the browser: See the *link* and *script* statements in the code.  

# Build

# License

# Authors
Joe Landau
jrlandau@gmail.com
7/5/16
