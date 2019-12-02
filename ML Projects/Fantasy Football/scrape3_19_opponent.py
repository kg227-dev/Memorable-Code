import csv
import base64
from bs4 import BeautifulSoup
import http.cookiejar
import urllib.request


# do file output
dataset = []
outfile = open('opponents.csv','w')
write = csv.writer(outfile)


# Store the cookies and create an opener that will hold them
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

# Add our headers
opener.addheaders = [('User-agent', 'yahoo-test')]

# Install our opener (note that this changes the global opener to the one
# we just made, but you can also just call opener.open() if you want)
urllib.request.install_opener(opener)

# The action/ target from the form
authentication_url = 'https://login.yahoo.com/config/login?.src=spt&.intl=us&.lang=en-US&.done=http://football.fantasysports.yahoo.com/'

# Input parameters we are going to send
payload = {
  'login': 'your_login',
  'passwd': 'your_pass'
  }

# Use urllib to encode the payload
data = urllib.parse.urlencode(payload).encode('utf-8')

# Build our Request object (supplying 'data' makes it a POST)
req = urllib.request.Request(authentication_url, data)

# Make the request and read the response
resp = urllib.request.urlopen(req)
contents = resp.read()

def getpage(player_page):
    
    handle = urllib.request.urlopen(player_page)
    
    
    html = handle.read()
    soup=BeautifulSoup(html, "html5lib")
    
    
    # get names
    l_names=[]
    
    # get position and team
    l_pos=[]
    l_team=[]
    temp_split=[]
    
    p_names = soup.findAll('div', attrs={'class' : 'ysf-player-name Nowrap Grid-u Relative Lh-xs Ta-start'})
    for row in p_names:
        l_names.append(str(row.find('a').string))
        print (str(row.find('a').string))
        temp_split.append(str(row.find('span', attrs={'class' : 'Fz-xxs'}).string))
        print (str(row.find('span', attrs={'class' : 'Fz-xxs'}).string))
        
    for i in temp_split:
        temp=i.split(" - ")
        l_team.append(temp[0])
        l_pos.append(temp[1])
       
    # get points
    # not needed on new yahoo pages
    #l_points=[]
    
    #p_points = soup.findAll('td', attrs={'class' : 'Ta-end Nowrap'})
    
    #for row in p_points:
    #    l_points.append(str(row.string))
    
        
    
    # get stats
    l_opp1 = []
    l_opp2=[]
    l_opp3=[]
    l_opp4=[]
    l_opp5=[]
    l_opp6=[]
    l_opp7=[]
    l_opp8=[]
    l_opp9=[]
    l_opp10=[]
    l_opp11=[]
    l_opp12=[]
    l_opp13=[]
    l_opp14=[]
    l_opp15=[]
    l_opp16=[]
    l_opp17=[]
    
    

    p_stats = soup.findAll('td', attrs={'class' : 'Alt Bdrend'})
    for row in p_stats:

      l_opp1.append(str(row.nextSibling.nextSibling.nextSibling.nextSibling.string))
      
      l_opp2.append(str(row.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.string))
      l_opp3.append(str(row.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.string))
      l_opp4.append(str(row.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.string))
      l_opp5.append(str(row.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.string))
      
      l_opp6.append(str(row.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.string))
      l_opp7.append(str(row.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.string))
      l_opp8.append(str(row.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.string))
      l_opp9.append(str(row.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.string))
      # rush att
      l_opp10.append(str(row.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.string))
      l_opp11.append(str(row.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.string))
      l_opp12.append(str(row.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.string))
      l_opp13.append(str(row.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.string))
      #rec tgt
      l_opp14.append(str(row.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.string))
      l_opp15.append(str(row.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.string))
      l_opp16.append(str(row.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.string))
      l_opp17.append(str(row.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.string))
     
           
      
    
    transposer = zip(l_names, l_pos, l_team, l_opp1, l_opp2, l_opp3, l_opp4, l_opp5, l_opp6, l_opp7, l_opp8, l_opp9, l_opp10, l_opp11, l_opp12,l_opp13,l_opp14,l_opp15, l_opp16, l_opp17)
    
    for i in transposer:
        dataset.append(i)
    return 0
getpage("https://football.fantasysports.yahoo.com/f1/38053/players?&sort=AR&sdir=1&status=T&pos=O&stat1=O_O&jsenabled=1")
getpage("https://football.fantasysports.yahoo.com/f1/38053/players?status=T&pos=O&cut_type=9&stat1=O_O&myteam=0&sort=AR&sdir=1&count=25")
getpage("https://football.fantasysports.yahoo.com/f1/38053/players?status=T&pos=O&cut_type=9&stat1=O_O&myteam=0&sort=AR&sdir=1&count=50")
getpage("https://football.fantasysports.yahoo.com/f1/38053/players?status=T&pos=O&cut_type=9&stat1=O_O&myteam=0&sort=AR&sdir=1&count=75")
getpage("https://football.fantasysports.yahoo.com/f1/38053/players?status=T&pos=O&cut_type=9&stat1=O_O&myteam=0&sort=AR&sdir=1&count=100")
getpage("https://football.fantasysports.yahoo.com/f1/38053/players?status=T&pos=O&cut_type=9&stat1=O_O&myteam=0&sort=AR&sdir=1&count=125")
getpage("https://football.fantasysports.yahoo.com/f1/38053/players?status=T&pos=O&cut_type=9&stat1=O_O&myteam=0&sort=AR&sdir=1&count=150")
getpage("https://football.fantasysports.yahoo.com/f1/38053/players?status=T&pos=O&cut_type=9&stat1=O_O&myteam=0&sort=AR&sdir=1&count=175")
getpage("https://football.fantasysports.yahoo.com/f1/38053/players?status=T&pos=O&cut_type=9&stat1=O_O&myteam=0&sort=AR&sdir=1&count=200")
getpage("https://football.fantasysports.yahoo.com/f1/38053/players?status=T&pos=O&cut_type=9&stat1=O_O&myteam=0&sort=AR&sdir=1&count=225")
getpage("https://football.fantasysports.yahoo.com/f1/38053/players?status=T&pos=O&cut_type=9&stat1=O_O&myteam=0&sort=AR&sdir=1&count=250")



# write rows and close file
for i in dataset:
    write.writerow(i)
outfile.close()
