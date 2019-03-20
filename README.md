# Log Analysis Project

## Overview

This project is aimed at creating multiple SQL queries to obtain information from a news database. The code is expected to have single query to answer individual requests. The objective is to test SQL skills. (This project is for Logs Analysis from Udacity Full Stack Developer Nanodegree)

### Requirements

* Python 2 - version 2.7.12
* Vagrant
* VirtualBox
* Git

### Project Objectives

The project has three objectives,
* Most popular article of all time
* Most popular article author of all time
* Day on which more than 1% requests led to error

### To run the Project
* Install Vagrant and VirtualBox
* Vagrant can be installed using configurations provided by Udacity from <a href="https://classroom.udacity.com/nanodegrees/nd004/parts/51200cee-6bb3-4b55-b469-7d4dd9ad7765/modules/c57b57d4-29a8-4c5f-9bb8-5d53df3e48f4/lessons/5475ecd6-cfdb-4418-85a2-f2583074c08d/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0">here</a>
* Clone this repo
> `git clone https://github.com/prkksh/Logs-Analysis/`
* Open terminal and cd in to the folder vagrant is installed and run 'vagrant up' to launch the linux VM. Once its done, login using 'vagrant ssh' command.
* The files are inside the vagrant folder. To access the files, run
>`cd /vagrant`

* Download the database from <a href = "https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip">here</a>. Move this file in to the vagrant folder.
* From terminal run
>`psql -d news -f newsdata.sql`
* Once the database is set, connect to the database using
>`psql -d news`
* Run the module with
>`python logs.py`
