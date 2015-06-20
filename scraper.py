from bs4 import BeautifulSoup
import requests
from urlparse import urlparse, urljoin
from robotparser import RobotFileParser

def getRobots(url):
    parsed = urlparse(url)
    robots_url = parsed.scheme + '://' + parsed.netloc + '/robots.txt'
    if robots_url not in robots:
        rp = RobotFileParser()
        try:
            r = requests.get(robots_url, verify=False, timeout=1)
            r.raise_for_status()
        except Exception:
            rp.parse('')
        else:
            rp.parse(r.text)
        #print "  new robot at " + robots_url
        robots[robots_url] = rp
    return robots[robots_url]

start = ""
