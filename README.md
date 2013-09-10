# Welcome to RoMIE #

> **NOTE:** RoMIE use an arduino UNO board and bluetooth to communicate
> between the RoMIE server and the RoMIE robot. In this moments we are
> trying to communicate with the RN-151 WiFLY board on arduino! :-)

The actual version is 1.0.1.

RoMIE is a WebLab-Deusto Remote Laboratory for Serious Games deployment based on a Mobile Robot Platform.
RoMIE integrate electronics, computers and wireless technologies in a remote laboratory to manage a robot inside a labyrinth from your home. This experiment has a replica in the Museum of Sciences and Technology of Sofia, Bulgaria. The above images shows the experiment working.

![Exhibition1](https://raw.github.com/gmartinvela/RoMIE/master/robot_app/static/images/exhibition1.jpg)

![Exhibition2](https://raw.github.com/gmartinvela/RoMIE/master/robot_app/static/images/exhibition2.jpg)

There are many different Technologies implied like [Python](http://python.org) ,[Django](https://www.djangoproject.com/‎), [JavaScript](http://http://en.wikipedia.org/wiki/JavaScript/‎), [JQuery](http://jquery.com/‎), [HTML](http://en.wikipedia.org/wiki/HTML), [CSS3](http://en.wikipedia.org/wiki/CSS3#CSS_3), [Arduino](www.arduino.cc/), [RFID](http://en.wikipedia.org/wiki/Radio-frequency_identification/‎), [Bluetooth](http://www.bluetooth.com/), ...

**Hey, check out WebLab-Deusto project! <http://weblab.deusto.es>**

## Requirements ##

RoMIE is developed on a Ubuntu 12.04 system, running:

   * [Python 2.7](http://docs.python.org/2/)
   * [Django 1.5.1](https://www.djangoproject.com/‎)
   * [python-mysqldb 1.2.3](http://mysql-python.sourceforge.net/MySQLdb.html)
   * [mysql-server 5.5.32](http://www.mysql.com)
   * [PyBluez](http://code.google.com/p/pybluez/‎)
   * [Supervisord](http://http://supervisord.org/)

It might work with other versions.

> **NOTE:** RoMIE is currently working in Bulgaria in a Windows 7 machine.
> The library used for the translation from UNIX system to Windows system 
> were Py2Exe and works very fine.

## Setting up the environment and config ##

Put your terminal in the root directory of the project and type:

	$ python manage.py syncdb

and put the file supervisord.conf in the path: 

	cp [RoMIE_root_path]/supervisord.conf /etc/supervisord.conf

put the file supervisord in /etc/init.d and configure it:

	cp [RoMIE_root_path]/supervisord /etc/init.d/supervisord
	sudo chmod +x /etc/init.d/supervisord
	sudo update-rc.d supervisord defaults
	sudo service supervisord start

and run in a terminal: 

	sudo unlink /tmp/supervisor.sock
	supervisord -c /etc/supervisord.conf

You can access to the interface in the same machine on:

	0.0.0.0:80/RoMIE

or in another machine (i.e. a mobile device) connected to the same LAN on:

	[MachineLanIP]:80/RoMIE

> **NOTE:** It is necessary a Bluetooth dongle in the computer and in the 
> arduino to work. Therefore, you need to change the Bluetooth MAC in the 
> views.py to work with your device.

## Interface of the laboratory ##

![Index](https://raw.github.com/gmartinvela/RoMIE/master/robot_app/static/images/index_screen.png)

BLOCKLY Interface

![Blockly](https://raw.github.com/gmartinvela/RoMIE/master/robot_app/static/images/blockly_screen.png)

## Credits and License ##

This program is free software: you can redistribute it and/or modify it
under the terms of the  GNU  Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or (at
your option) any later version.



