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
  print(user_data)

  return ''


def get_user_info():
  '''Prompts the user for input data required to connect
     to the `spotipy` API and returns the data as a python
     dictionaty.

  Returns:
    A Python dictionary containing the username, client id,
    client secret and whether to create a public or a private
    playlist.
  '''

  user_info = {}
  print('\n\nPlease enter the requested information below.\n\n'
        'NOTE:\n\n'
        "1. If you haven't already done so, setup a developer\n"
        'account by going to https://developer.spotify.com/\n'
        'and create an app to get the Client ID and the\n'
        'Client Secret to authorize this application to\n'
        'create and modify a playlist using your account.\n\n'
        '2. Also, the default URL where you can view and listen\n'
        'to your playlist is http://localhost:8888/callback.\n'
        'You can provide an alternative URL below or just\n'
        'press ENTER to use the default URL.\n\n')

  user_info['username'] = input('Enter Spotify Username: ')
  user_info['client_id'] = input('Enter the Client ID: ')
  user_info['client_secret'] = input('Enter the Client Secret: ')

  redirect_url = input('Enter the URL to access the playlist or'
                       ' press ENTER to use the default URL: ')
  if redirect_url == '':
    redirect_url = 'http://localhost:8888/callback'
  user_info['redirect_url'] = redirect_url

  scope_option = int(input('Please choose one of the options '
                           'for the kind of playlist you want'
                           ' to create.\n\n1. Public\n2. Private'
                           '\n\nEnter the number corresponding to'
                           ' the option you want to choose:')
                           .strip())
  scope_dict = {1: 'playlist-modify-public',
                2: 'playlist-modify-private'}
  while scope_option not in scope_dict:
    scope_option = int(input('Not a valid option.\n'
                             'Please enter a valid option: ').strip())
  user_info['scope'] = scope_dict[scope_option]

  return user_info
