def find_songs(artist):
  '''Requests user input for the artist's name 
     and returns a list of songs from one of 
     the artist's recent setlist.

  Args:
    artist (string): A string containing the
           name of a musician or band.

  Returns:
    A list of strings containing the names of
    the songs of the artist's latest setlist.
  '''

  try:
    request_obj = get_request(artist)
  except AssertionError as err:
    print(err)

  print(request_obj)
  return []


def get_request(artist):
  '''Sends HTTP GET request to the setlist.fm URL and
     returns the HTTP response object.

  Args:
    artist (string): A string containing the name
           of a musician or a band.

  Returns:
    An HTTP Response object.

  Raises:
    AssertionError: If the request fails.
  '''

  from requests import get as get_req

  base_url = 'http://www.setlist.fm/'
  artist_query = '+'.join(artist.split(' '))
  url = '{}search?query={}'.format(base_url,
                                   artist_query)

  req = get_req(url)
  assert (req.ok == True), 'Failed Request!!!'

  return req
