#Speech Commands

This module has to date been tested only on Loki.

It consists of HTML and Javascript that utilizes the HTML5 Web Speech API.  This API runs only in browsers that support it. At present, this means Chrome on Windows, Linux, and Android. In other browsers, commands may be issued by clicking arrows on the screen.

After Loki is initialized so it can launch the ros-arduino-bridge, follow these instructions in order to install and run speech commands.

##Installation:

Note the Loki's IP address for later use as a url. 

Install Rosbridge:  sudo apt-get install ros-indigo-rosbridge-suite
Install the apache2 web server (sudo apt-get install apache2).  This also installs the ssl-certs package, which sets up the snakeoil certificate and key.
Enable the ssl module (sudo a2enmod ssl)
Configure apache2 for HTTPS (sudo a2ensite default-ssl)
Restart the service (sudo service apache2 restart). You should not need to enter a passphrase.
Test the server by addressing it from a browser, for instance http://10.0.0.25/index.html. You should get the apache2 default page.  
(TODO The default page should be replaced by one that features Ubiquity Robotics.)
Test again using HTTPS.  The result should be a security warnings, since you are not using an officially generated ssl key.
Copy speechcommands.html from wherever it is to /var/www/html on the robot.
Copy the /scripts and the /fonts folders as subfolders to /var/www/html on the robot.

Copy /etc/ssl/private/ssl-cert-snakeoil.key to /etc/ssl/certs/  (may need sudo)
chmod /etc/ssl/certs/ssl-cert-snakeoil.key so it is readable. /etc/ssl/certs/ssl-cert-snakeoil.pem should already be readable. 
	(sudo chmod 644 /etc/ssl/certs/ssl-cert-snakeoil.key)
Modify these 3 lines of the rosbridge launch file:
	(The rosbridge launch file is at  /opt/ros/indigo/share/rosbridge_server/launch/rosbridge_websocket.launch)
  <arg name="ssl" default="true" />
  <arg name="certfile" default="/home/ubuntu/ssl-cert-snakeoil.pem" />
  <arg name="keyfile" default="/home/ubuntu/ssl-cert-snakeoil.key" />


##Startup

On each Loki bringup:
* Set up the RasPi2 serial port: 
> sudo mgetty -s 115200 /dev/ttyAMA0
* Hit the reset switch on the Loki near the green leds and then launch the ros-arduino bridge: 
> roslaunch ros_arduino_python arduino.launch
* Launch the rosbridge_server: (Refer to  http://wiki.ros.org/rosbridge_suite/Tutorials/RunningRosbridge)
> roslaunch rosbridge_server rosbridge_websocket.launch.
* Run the tf2_web_republisher
> rosrun tf2_web_republisher tf2_web_republisher
* In the Chrome browser on your laptop or Android phone, load the speechcommands.html page, using https with the robot's url.
* in the speechcommands.html page, enter the url <robot's url>:9090 into the Robot URL box and click the Connect button.  The button should now say Disconnect. If you intend using speech, use "wss" or "https" for the robot's websocket address; otherwise you may use "ws" or "http".
##Running
* Click any arrow to move the robot.
* Click the Microphone to use speech. You will be requested to allow the use of the mike.  Do it.
* Say, "forward", or other commands.  Check the Help for valid commands.



