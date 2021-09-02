# Webscraper for Hardwarezone

This webscraper is created to crawl posts and threads from a PC Gaming forum in Hardwarezone. It is created using Scrapy and with the use of spiders.

# Getting Started
Before running the webscraper to crawl threads from Hardwarezone, ensure that you have the following modules and systems installed over WSL2:

* python-is-python3
`sudo apt-get install python-is-python3`
* python3
`sudo apt-get install python3-pip`
* virtualenv
`pip install virtualenv`
* mongoDB
`sudo apt-get install mongodb`
* folder for mongoDB
 
  * `sudo mkdir /data`
 
  * `sudo mkdir /data/db`
* write permission for the folder
`sudo chown -R `id -un` /data/db`

After installing the above, start mongoDB with the following command:

`mongod &`

Then proceed to install python3-venv: 

`sudo apt-get install python3-venv`

# Clone the repository
Once the installations are completed, clone this repository into your local site folder:

`git clone git@github.com:tyh2312/Webscraper.git`

# Create a virtual environment
Create a virtual environment and activate it.

`virtualenv .`

After creating a virtual environment, enter the following command to activate it.

`source bin/activate`

# Installations in virtual environment
The following installations need to then be installed inside the activated virtual environment.

* Scrapy

`pip install scrapy`

* pymongo

`pip install pymongo`
