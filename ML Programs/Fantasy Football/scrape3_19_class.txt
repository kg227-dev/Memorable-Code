#!/usr/bin/env python

#Adrian Peterson Min - RB  Player Note
#Sun 1:00 pm @ Det 
# 	FA	340.17	100%	1	1	0	0	0	2097	12	40	217	1	0	1	2
#	owner	points	owned	rank	actual	passyds	passtds	int	runyds	runtd	rec	recyds	rectds	returntd 2pt	fumble
#
#<td class="Bdrend">FA</td>		owner	
#<td class="Alt Fw-b">340.17</td>	points	
#<td class="Bdrend">100%</td>		owner%		3
#<td class="Alt Selected">1</td>	projected	4 
#<td class="Bdrend">1</td>		actual		5 
#<td class="Alt">0</td>			passyds		6
#<td class="">0</td>			passtds		7
#<td class="Alt">0</td>			int		8
#<td class="">2097</td>			runyds		9
#<td class="Alt">12</td>		runtd		10
#<td class="">40</td>			rec		11
#<td class="Alt">217</td>		recyds		12
#<td class="">1</td>			rectds		13
#<td class="Alt">0</td>			returntd
#<td class="Last">1</td>		2pt
#<td class="Alt">2</td>			fumble		16

import csv
import base64
from bs4 import BeautifulSoup
import http.cookiejar
import urllib.request


# do file output
dataset = []
outfile = open('ff_data19.csv','w')
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
    l_gp=[]
    l_points = []
    l_owners=[]
    l_project=[]
    l_actual=[]
    
    l_passyds=[]
    l_passtd=[]
    l_passint=[]
    
    # rush att
    l_rushyds=[]
    l_rushtd=[]    
    l_rush1st=[]

    # rec tgt
    l_recepts=[]
    l_recyds=[]
    l_rectd=[]
    l_rec1st=[]
    
    l_returnyds=[]
    l_returntd=[]
    
    l_2pt = []
    l_fumble=[]
    
    
    p_stats = soup.findAll('td', attrs={'class' : 'Alt Bdrend'})
    
    for row in p_stats:
      l_gp.append(str(row.nextSibling.nextSibling.nextSibling.string))
      l_points.append(str(row.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.string))
      l_owners.append(str(row.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.string))
      l_project.append(str(row.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.string))
      l_actual.append(str(row.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.string))
      
      l_passyds.append(str(row.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.string))
      l_passtd.append(str(row.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.string))
      l_passint.append(str(row.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.string))
      
      # rush att
      l_rushyds.append(str(row.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.string))
      l_rushtd.append(str(row.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.string))
      l_rush1st.append(str(row.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.string))
      
      #rec tgt
      l_recepts.append(str(row.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.string))
      l_recyds.append(str(row.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.string))
      l_rectd.append(str(row.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.string))
      l_rec1st.append(str(row.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.string))
      
      l_returnyds.append(str(row.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.string))       
      l_returntd.append(str(row.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.string))       
      
      #2pt
      l_2pt.append(str(row.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.string))       
      l_fumble.append(str(row.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.string))             
      
    
    transposer = zip(l_names, l_team, l_pos, l_gp, l_points, l_owners, l_project, l_actual, l_passyds, l_passtd, l_passint, l_rushyds, l_rushtd, l_rush1st, l_recepts, l_recyds, l_rectd, l_rec1st, l_returnyds, l_returntd, l_2pt, l_fumble)
    
    for i in transposer:
        dataset.append(i)
    
    #dataset.append(l_names)
    #dataset.append(l_points)
    #dataset.append(l_owners)
    #dataset.append(l_passyds)
    #dataset.append(l_passtd)
    #dataset.append(l_inter)
    #dataset.append(l_rush)
    #dataset.append(l_rushtd)
    #dataset.append(l_recepts)
    #dataset.append(l_recyds)
    #dataset.append(l_receptstd)
    #dataset.append(l_to)
    return 0

# main
# make sure to change the league number -- currently 38053 for this season -- and the year -- which is in each page html
#MAKE SURE TO CHANGE THE YEAR TOO
getpage("http://football.fantasysports.yahoo.com/f1/38053/players")
getpage("http://football.fantasysports.yahoo.com/f1/38053/players?status=A&pos=O&cut_type=9&stat1=S_S_2018&myteam=0&sort=PR&sdir=1&count=25")
getpage("http://football.fantasysports.yahoo.com/f1/38053/players?status=A&pos=O&cut_type=9&stat1=S_S_2018&myteam=0&sort=PR&sdir=1&count=50")
getpage("http://football.fantasysports.yahoo.com/f1/38053/players?status=A&pos=O&cut_type=9&stat1=S_S_2018&myteam=0&sort=PR&sdir=1&count=75")
getpage("http://football.fantasysports.yahoo.com/f1/38053/players?status=A&pos=O&cut_type=9&stat1=S_S_2018&myteam=0&sort=PR&sdir=1&count=100")
getpage("http://football.fantasysports.yahoo.com/f1/38053/players?status=A&pos=O&cut_type=9&stat1=S_S_2018&myteam=0&sort=PR&sdir=1&count=125")
getpage("http://football.fantasysports.yahoo.com/f1/38053/players?status=A&pos=O&cut_type=9&stat1=S_S_2018&myteam=0&sort=PR&sdir=1&count=150")
getpage("http://football.fantasysports.yahoo.com/f1/38053/players?status=A&pos=O&cut_type=9&stat1=S_S_2018&myteam=0&sort=PR&sdir=1&count=175")
getpage("http://football.fantasysports.yahoo.com/f1/38053/players?status=A&pos=O&cut_type=9&stat1=S_S_2018&myteam=0&sort=PR&sdir=1&count=200")
getpage("http://football.fantasysports.yahoo.com/f1/38053/players?status=A&pos=O&cut_type=9&stat1=S_S_2018&myteam=0&sort=PR&sdir=1&count=225")
getpage("http://football.fantasysports.yahoo.com/f1/38053/players?status=A&pos=O&cut_type=9&stat1=S_S_2018&myteam=0&sort=PR&sdir=1&count=250")
getpage("http://football.fantasysports.yahoo.com/f1/38053/players?status=A&pos=O&cut_type=9&stat1=S_S_2018&myteam=0&sort=PR&sdir=1&count=275")
getpage("http://football.fantasysports.yahoo.com/f1/38053/players?status=A&pos=O&cut_type=9&stat1=S_S_2018&myteam=0&sort=PR&sdir=1&count=300")

# write rows and close file
for i in dataset:
    write.writerow(i)
outfile.close()
