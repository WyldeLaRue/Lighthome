# Lighthome
Web interface and automation tools for controlling a neopixel strip through a Raspberry Pi. Backend in Python/Pyramid, frontend in React.

This is an updated version of my previous project [Tristan-IOT](https://github.com/jgarff/rpi_ws281x).
The entire codebase was rewritten into React/Pyramid with a more focused design. There are a few features that still haven't been migrated over.





### Strip Simulator
I also wrote a simulator for this project in tkinter so that it can be run/debugged when I am not at home or don't want to mess around with the physical lights. As of now, it looks at your OS to determine whether or not to run in simulation mode. If you are running Linux, it is possible there will be issues for this reason. I have not tested this.

### Alarm

The 'Light Alarm' feature turns on the lights 30 minutes before the set wakeup time, slowly getting brighter for an hour. The timing and color was adjusted to be what I found comfortable, so it may be what everyone else wants. Currently these preferences are hard-coded.

### Hardware
I'm currently using a RGBW SK6812 strip. If you want to follow this setup, be very careful to follow the instructions for soldering and using a level converter to get the right voltage from the RPi. If you connect it to the RPi directly, you run the risk of damaging your strip and your raspberry pi. It also will not work. 

I also am using etekcity remote controlled outlets along with a transmitter/receiver for copying the signal. After much investigation, this appears to be the cheapest (around $14) method for constructed IOT enabled power outlets. This comes at the downside of relying on a radio signal, so everything must be roughly in the same room as the RPi without doing anything more creative.


First we need to install wiringPi, which allows us to write to the GPIO pins.
```
cd ~
git clone git://git.drogon.net/wiringPi
cd wiringPi
./build
```
This can also be done via apt-get which is probably a better choice.


Now the 433 utils to use the RF receiver/sender
```
cd ~
git clone https://github.com/ninjablocks/433Utils
cd 433Utils 
make
mv ./codesend /usr/bin
```
Since we already know what our RF codes look like, we don't need the RFsniffer for now. And lets add ourselves to the gpio group. 


reference:
https://chester.me/archives/2017/12/controlling-rf-outlets-from-a-raspberry-pi/



Now we install homebdrige using the instructions in the wiki. First we need GCC 8.

```https://github.com/nfarina/homebridge/wiki/Running-HomeBridge-on-a-Raspberry-Pi```

We use systemd to have it run at startup. Following this guide  
```https://timleland.com/setup-homebridge-to-start-on-bootup/```

made it to step 4


### Dependencies
This project heavily relies on the wonderful [rpi_ws281x](https://github.com/jgarff/rpi_ws281x) library to interface between the raspberry pi and light strip.




## Running Locally

#### Setting up the Pyramid server locally:

First we need to setup our virtual environment environment.
```
python3.7 -m venv ./venv
source venv/bin/activate
pip3 install --upgrade pip
pip3 install --upgrade setuptools
```

Now we install the dependencies:
```
pip3 install "pyramid==1.9.2" waitress
pip3 install pyramid_debugtoolbar
```

And now to add our Pyramid server to our virtual environment:
```
pip3 install -e .
```

and we can start it in development mode with 
```
pserve development.ini
```

### Webpack
navigate to ```homepage/frontend``` and then ```npm run watch```

