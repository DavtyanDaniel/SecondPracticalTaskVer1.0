# Introduction
#### This is a project that allows user to connect to websocket server
#### and every 10 seconds get the approx coordinates of the moon.
After running the websocket_server you are getting ngrok tcp tunnel
link in terminal, please insert it to your websocket getter software.

#####Please notice that after 1 hour the RA coordinate's accuracy is decreasing.



# Table of Content
* [System Requirements](#system-requirements)
* [Installation](#installation)
* [How To Run](#how-to-run)
​
# System Requirements:
 - python3 
 - pip3
​
# Installation
  - Clone the latest version from https://github.com/DavtyanDaniel/SecondPracticalTaskVer1.0.git 
  - Install the dependencies (It is highly recommended to create isolated environment!)
  ```sh
  python3 -m venv my_env
  source my_env/bin/activate
  pip3 install -r requirements.txt
  ```

# How to run
 ```sh
$ python3 websocket_server.py
 ```