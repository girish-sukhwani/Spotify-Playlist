_public = False

_intro = '''\n\nPlease enter the requested information below.\n
NOTE:\n
1. If you haven't already done so, setup a developer account by
going to https://developer.spotify.com/ and create an app to
get the Client ID and the Client Secret to authorize this
application to create and modify a playlist using your account.\n
2. Also, the default URL where you can view and listen to your
playlist is http://localhost:8888/callback. You can provide an
alternate URL below or just press ENTER to use the default URL.\n
3. The input for Client ID and Client Secret is hidden. So, don't
be alarmed if you see no text showing up.\n\n'''


def generate_playlist(songs, pname='py_playlist'):
  '''Reads in a list of songs and generates a link to a
     Spotify playlist.

  Args:
    songs (list): A list of strings containing the names
          of the songs.
    pname (string): A string conatining the name of the
          playlist to be created (default = 'py_playlist').

  Returns:
    A string containing the URL to the Spotify playlist
    containing the specified songs.
  '''

  user_data = get_user_info()
  api_connect = get_api_connection(user_data['username'],
                                   user_data['scope'],
                                   user_data['client_id'],
                                   user_data['client_secret'],
                                   user_data['redirect_url'])

  tracks = get_track_ids(api_connect, songs)

  if user_data['scope'] == 'playlist-modify-public':
    _public = True

  playlist_url = construct_playlist(api_connect, pname, tracks,
                                    user_data['username'], _public)

  return playlist_url


def get_user_info():
  '''Prompts the user for input data required to connect
     to the `spotipy` API and returns the data as a python
     dictionaty.

  Returns:
    A Python dictionary containing the username, client id,
    client secret and whether to create a public or a private
    playlist.
  '''

  from getpass import getpass

  user_info = {}
  print(_intro)

  user_info['username'] = input('Enter Spotify Username: ')
  user_info['client_id'] = getpass('Enter the Client ID: ')
  user_info['client_secret'] = getpass('Enter the Client Secret: ')

  redirect_url = input('Enter the URL to access the playlist or'
                       ' press ENTER to use the default URL: ')
  if redirect_url == '':
    redirect_url = 'http://localhost:8888/callback'
  user_info['redirect_url'] = redirect_url

  scope_option = int(input('\nPlease choose one of the options '
                           'for the kind of playlist you want'
                           ' to create.\n\n1. Public\n2. Private'
                           '\n\nEnter the number corresponding to'
                           ' the option you want to choose: ')
                           .strip())
  scope_dict = {1: 'playlist-modify-public',
                2: 'playlist-modify-private'}
  while scope_option not in scope_dict:
    scope_option = int(input('Not a valid option.\n'
                             'Please enter a valid option: ').strip())
  user_info['scope'] = scope_dict[scope_option]

  return user_info


def get_api_connection(username, scope, client_id,
                       client_secret, redirect_uri):
  '''Connects to the spotipy api and returns the Spotify object.

  Args:
    username (string): A string containing the Spotify username.
    scope (string): A string containing scope identifier for access.
    client_id (string): A string containing the client_id.
    client_secret (string): A string containing the client_secret.
    redirect_uri (string): A string containing the redirect URI.

  Return:
    A Spotify object after completing authentication.
  '''

  from time import sleep
  from spotipy import util
  from spotipy import Spotify

  print('\n\nAfter you authorize the application to allow it to'
        ' make changes, you will be asked to copy the URL that '
        'you are redirected to and paste it on the screen here.')
  sleep(10)
  token = util.prompt_for_user_token(username,
                                     scope=scope,
                                     client_id=client_id,
                                     client_secret=client_secret,
                                     redirect_uri=redirect_uri)
  spot_obj = Spotify(auth=token)

  return spot_obj


def get_track_ids(spotify, songs):
  '''Searches spotify for the songs and returns their track ids.

  Args:
    spotify: A Spotify connection object.
    songs (list): A list of strings containing the names of the songs.

  Returns:
    A list of strings containing the track ids of the songs.
  '''

  track_ids = []
  for song in songs:
    for track in spotify.search('track:' + song)['tracks']['items']:
      if song in track['name']:
        track_ids.append(track['id'])
        break

  return track_ids


def construct_playlist(spotify, pname, tracks,
                       username, public=False):
  '''Creates a Spotify playlist and adds tracks to the playlist and 
     returns the link to the playlist.

  Args:
    spotify: A Spotify connection object.
    pname (string): A string representing the name of the playlist.
    tracks (list): A list of strings containing the ids of the tracks.
    username (string): A string containing the Spotify username.
    public (boolean): A boolean value representing whether the
                      playlist is public or not.

  Returns:
    A link to the created Spotify playlist.
  '''

  playlist = spotify.user_playlist_create(username,
                                          pname,
                                          public=public)
  plist_id = playlist['id']
  plist_url = playlist['external_urls']['spotify']
  spotify.user_playlist_add_tracks(username, plist_id, tracks)

  return plist_url
