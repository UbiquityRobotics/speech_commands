Speech Commands

This module has to date been prepared only for Loki.

It consists of HTML and Javascript that utilizes the HTML5 Web Speech API.  It runs only in browsers that support this API. At present, this means Chrome on Windows, Linux, and Android.

After Loki is initialized so it can launch the ros-arduino-bridge, follow these instructions in order to install and run speech commands.

Note the Loki's IP address for later use as a url. 

install Rosbridge:  sudo apt-get install ros-indigo-rosbridge-suite
install the apache2 web server (sudo apt-get install apache2).  This also installs the ssl-certs package, which sets up the snakeoil certificate and key.
Enable the ssl module (sudo a2enmod ssl)
Configure apache2 for HTTPS (sudo a2ensite default-ssl)
Restart the service (sudo service apache2 restart). You should not need to enter a passphrase.
Test the server by addressing it from a browser, for instance http://10.0.0.25/index.html. You should get the apache2 default page.  
(The default page should be replaced by one that features Ubiquity Robotics.)
Test again using HTTPS.  The result should be lots of security warnings.
Copy speechteleop.html from wherever it is to /var/www/html on Loki

Copy /etc/ssl/certs/ssl-cert-snakeoil.pem and etc/ssl/certs/ssl-cert-snakeoil.key to /home/ubuntu
chmod ssl-cert-snakeoil.key so it is readable. /ssl-cert-snakeoil.pem should already be readable. (644)
Modify the rosbridge launch file with these 3 lines
  <arg name="ssl" default="true" />
  <arg name="certfile" default="/home/ubuntu/ssl-cert-snakeoil.pem" />
  <arg name="keyfile" default="/home/ubuntu/ssl-cert-snakeoil.key" />
The rosbridge launch file is at  /opt/ros/indigo/share/rosbridge_server/launch/rosbridge_websocket.launch

On each Loki bringup:


	* Set up the RasPi2 serial port: 


sudo mgetty -s 115200 /dev/ttyAMA0


	* Hit the reset switch on the Loki near the green leds and then launch the ros-arduino bridge: 


roslaunch ros_arduino_python arduino.launch


	* Launch the rosbridge_server: (Refer to  http://wiki.ros.org/rosbridge_suite/Tutorials/RunningRosbridge)


roslaunch rosbridge_server rosbridge_websocket.launch.


	* In the Chrome browser on your laptop or Android phone, load the speechteleop.html page, using https with the Loki url 

  

	* in the speechteleop.html page, enter the url https://10.0.0.25:9090 into the Robot URL box and click the Connect button.  It should now say Disconnect.


Click any arrow to move the robot.
Click the Microphone to use speech. You will be requested to Allow the use of the mike.  Do it.
Say, "forward".  Check the Help for valid commands.



