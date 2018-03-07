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
  '''

  try:
    request_obj = get_request(artist)
    divs_list = get_divs(request_obj)
    setlist_link = get_link(divs_list)
  except AssertionError as err:
    print(err)

  print(setlist_link)
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
  assert (req.ok == True), 'ERROR: Failed Request!!!'

  return req


def get_divs(req_obj):
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


def get_link(divs):
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
      return div.a['href']

  assert None, 'ERROR: Failed to find non-empty setlists!!!'
