#!/bin/bash
apt-get update
apt-get install -y python3 python3-pip git
pip3 install concurrency
pip3 install logging
pip3 install pillow
pip3 install numpy
pip3 install Flask
pip3 install jsonpickle
pip3 install requests
apt-get install python3-pip
pip3 install pika
pip3 install redis
python3 /rest-install/serverj.py rest-install