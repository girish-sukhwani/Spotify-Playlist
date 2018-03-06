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
    divs_list = get_divs(request_obj)
  except AssertionError as err:
    print(err)

  print(divs_list)
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
  assert div_tags, 'Failed to find events!!!'

  return div_tags
