# Spotify-Playlist
Building a Python app that creates a playlist on Spotify, featuring an artist's latest setlist


## Project Overview
In this project, we will use Web Scraping to extract an artist's setlist from one of the recent events and create a Spotify playlist using **spotipy**, a Python API package developed for Spotify, to build a playlist.


## Project Highlights
This project is designed to give a hands-on experience with Web Scraping and handling API communication using Python.


## Description
This project is divided into 3 separate modules that will call each other when necessary. The description of all the modules is as given below.

### Module 1: scrape.py
This module contains functions to extract an artist's setlist from one of the recent events, from http://www.setlist.fm. This module performs Web Scraping. A user input is requested for the artist's name, and a list containing strings with the corresponding song names is returned. The Python library BeautifulSoup is used for Web Scraping.

### Module 2: spotify.py
This module contains functions to read a list of songs returned from **scrape.py** module and generates a link to a Spotify playlist containing those songs. A Python API package called **spotipy** is used to build the Spotify playlist. **spotipy** is basically just a wrapper for the Python **requests** package, which is a great way to communicate with APIs of any description.

**NOTE:** The **spotipy** component will require that you set up a developer account on Spotify, by going to https://developer.spotify.com. You'll create an app, and then use the Client ID and Client Secret (these two together constitute your API key) to authorize your **spotipy** call. You'll have to add a redirect URI on your Spotify app page to make it work. The default URI used in the project is http://localhost:8888/callback. The Client ID and the Client Secret will be requested as user input.

### Module 3: build_playlist.py
This module contains functions to call the **spotify.py** and **scrape.py** modules to create a playlist on Spotify containing the latest songs by the artist, and prints a link to the playlist.


## Softwares and Libraries
This project uses the following softwares and Python libraries:

- Software-1
- Software-2
- and so on...

If you do not have Python installed yet, it is highly recommended that you install the [Anaconda](https://www.anaconda.com/download/) distribution of Python, which already has the above packages and more included. Make sure you select the Python 3.x installer and not the Python 2.7 installer.


## Running the Project
To successfully run the app and create a playlist, use the following command and enter all the requested details correctly:

```
python build_playlist.py
```
