_base_url = 'http://www.setlist.fm/'


def find_songs(artist):
  '''Requests user input for the artist's name
     and returns a list of songs from one of the
     artist's recent setlist.

  Args:
    artist (string): A string containing the
           name of a musician or band.

  Returns:
    A list of strings containing the names of
    the songs of the artist's latest setlist.

  Raises:
    AssertionError: If a request fails.
    AssertionError: If there are no events.
    AssertionError: If there are no non-empty setlists.
  '''

  try:
    artist_url = _get_artist_query_link(artist)
    artist_req = _get_request(artist_url)
    divs_list = _get_divs(artist_req)
    setlist_link = _get_link(divs_list)
    setlist_req = _get_request(setlist_link)
  except AssertionError as err:
    raise err

  return _get_songs(setlist_req)


def _get_artist_query_link(artist):
  '''Constructs the query URL for the given artist.

  Args:
    artist (string): A string containing the name
           of a musician or band.

  Returns:
    A string containing the URL with the artist
    query string.
  '''

  artist_query = '+'.join(artist.split(' '))
  url = '{}search?query={}'.format(_base_url,
                                   artist_query)
  return url


def _get_request(url):
  '''Sends HTTP GET request to the setlist.fm URL
     and returns the HTTP response object.

  Args:
    url (string): A string containing the URL.

  Returns:
    An HTTP Response object.

  Raises:
    AssertionError: If the request fails.
  '''

  from requests import get as get_req

  req = get_req(url)
  assert (req.ok == True), 'ERROR: Failed Request!!!'

  return req


def _get_divs(req_obj):
  '''Performs web scraping on the web page retrieved
     to retrieve details of all the events related
     to the artist.

  Args:
    req_obj (HTTP Response): An HTTP Response object.

  Returns:
    A list of div tags representing recent events
    related to the artists.

  Raises:
    AssertionError: If there are no events.
  '''

  from bs4 import BeautifulSoup

  soup = BeautifulSoup(req_obj.text, 'html.parser')
  div_attrs = {'class': 'col-xs-12 setlistPreview'}
  div_tags = soup.find_all('div', attrs=div_attrs)
  assert div_tags, 'ERROR: Failed to find events!!!'

  return div_tags


def _get_link(divs):
  '''Retrieves a URL to the non-empty setlist of
     the latest event.

  Args:
    divs (list): A list containing the div tag
         contents corresponding to the artist's
         events.

  Returns:
    A URL to a non-empty setlist.

  Raises:
    AssertionError: If there are no non-empty setlists.
  '''

  ol_attr = {'class': 'list-inline'}
  for div in divs:
    if div.find('ol', attrs=ol_attr):
      return _base_url + div.a['href']

  assert None, 'ERROR: Failed to find non-empty setlists!!!'


def _get_songs(req_obj):
  '''Retrieves a list of song names from the setlist webpage.

  Args:
    req_obj (HTTP Response): An HTTP Response object.

  Returns:
    A list of strings containing the names of the songs.
  '''

  from bs4 import BeautifulSoup

  soup = BeautifulSoup(req_obj.text, 'html.parser')
  songs_attr = {'class': 'songLabel'}
  setlist = soup.find_all('a', attrs=songs_attr)

  return [song.text for song in setlist]
