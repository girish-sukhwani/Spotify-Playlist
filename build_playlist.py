def create_playlist(artist, plist_name='Python Playlist'):
  '''Calls `spotify.py` and `scrape.py` modules to create a playlist on Spotify
     containing the latest songs by the `artist`, and the prints a link to that
     playlist.

  Args:
    artist (string): A string containing the name of a musician or band.
    plist_name (string): A string containing the name of the playlist to be
                         created (default value).
  '''

  from scrape import find_songs
  from spotify import generate_playlist

  songs = find_songs(artist)

  if songs:
    plist_url = generate_playlist(songs, plist_name)
  else:
    print('\n\nNo songs found for the artist.'
          'Please try again with a different artist.')
    return

  print('\n\nPlease find the link to the playlist below:')
  print(plist_url + '\n\n')

  return


if __name__ == '__main__':

  print('Hello!!! Welcome to my Spotify playlist app...\n')

  artist_name = input('Enter the name of the artist: ')
  playlist_name = input('Enter the name of the playlist to be created: ')

  if playlist_name == '':
    create_playlist(artist_name)
  else:
    create_playlist(artist_name, playlist_name)
