# -*- coding = utf-8 -*-
# @Time : 2021/7/25 19:47
# @Author WjNaG
# @File : ClubRankingSpider.py
# @Softname: PyCharm

from bs4 import BeautifulSoup
import urllib.request
import re
import xlwt

Keylist = []
Exllist = []
Nationlist = []

def pre():
    global workbook
    global worksheet
    workbook = xlwt.Workbook(encoding="utf-8")
    worksheet = workbook.add_sheet('sheet1', cell_overwrite_ok=True)

def fin():
    workbook.save('clubRanking5.xls')

def save(year):
    url = "https://kassiesa.net/uefa/data/method5/trank" + str(year) + ".html"
    res = urllib.request.urlopen(url)
    html = str(year)+".html"
    f = open(html,"w",encoding='utf-8')
    f.write(res.read().decode('utf-8'))
    work(year)


def work(year):
    htm = str(year)+".html"
    file = open(htm, "rb")
    html = file.read()
    bs = BeautifulSoup(html, "html.parser")

    # print(bs.head)

    # t_list = bs.find_all(class_="aleft",limit=20)
    # t_list = bs.select(".aleft",limit=20)
    t_list = bs.find_all("td", limit=300)  # 可设定循环周期
    t_list2 = bs.find_all(class_="lgray",limit=30)

    Scorelist = []
    Exllist = ['Real Madrid', 'FC Barcelona', 'Stade de Reims', 'Birmingham City', 'Red Star Belgrade', 'AC Milan', 'Manchester United', 'Young Boys', 'Wiener Sportklub', 'Internazionale', 'CDNA Sofia', 'Glasgow Rangers', 'OGC Nice', 'Leipzig XI', 'Dukla Praha', 'Rapid Wien', 'Eintracht Frankfurt', 'Chelsea', 'Standard Liège', 'Fiorentina', 'Vasas Budapest', 'Belgrade XI', 'IFK Göteborg', 'Wolverhampton Wanderers', 'Atlético Madrid', 'Wismut Karl-Marx-Stadt', 'Ajax', 'Borussia Dortmund', 'AGF Aarhus', 'Athletic Bilbao', 'AS Roma', 'Benfica', 'Hibernian', 'Dinamo Zagreb', 'Köln XI', 'Union Saint-Gilloise', 'Újpest Dózsa', 'Olympique Lyon', 'Valencia', 'Austria Wien', '1.FC Nürnberg', 'Tottenham Hotspur', 'FC Köln', 'Real Zaragoza', 'Juventus', 'Sporting CP Lisbon', 'Slovan Bratislava', 'MTK Budapest', 'Hamburger SV', 'Petrolul Ploiesti', 'Ferencváros', 'CF Os Belenenses', 'Celtic', 'Dunfermline Athletic', 'Everton', 'Dinamo Bucuresti', 'FC Liège', 'Galatasaray', 'TSV 1860 München', 'FC Porto', 'Spartak Brno', 'Anderlecht', 'Liverpool', 'Górnik Zabrze', 'Sparta Praha', 'Leeds United', 'Bologna', 'Vojvodina Novi Sad', 'Napoli', 'Bayern München', 'Olympiakos Piraeus', 'Vitória Setúbal', 'Cardiff City', 'Legia Warsaw', 'FC Zürich', 'Newcastle United', 'Feyenoord', 'Steaua Bucuresti', 'Spartak Trnava', 'Aberdeen', 'Club Brugge', 'Carl Zeiss Jena', 'Borussia Mönchengladbach', 'CSKA Sofia', 'Olympique Marseille', 'FC Twente Enschede', 'Dinamo Kiev', 'Hajduk Split', 'Dynamo Dresden', 'Malmö FF', 'Fenerbahçe', 'PAOK Thessaloniki', 'Derby County', '1.FC Magdeburg', 'PSV Eindhoven', 'RWD Molenbeek', 'Ipswich Town', 'AS Saint-Étienne', 'Grasshoppers Zürich', 'Wacker Innsbruck', 'AEK Athens', 'Dinamo Tbilisi', 'Torino', 'Baník Ostrava', 'VfB Stuttgart', 'Universitatea Craiova', 'AZ Alkmaar', '1.FC Kaiserslautern', 'BFC Dynamo Berlin', 'Dundee United', 'Spartak Moscow', 'Bohemians Praha', 'Lokomotive Leipzig', 'Widzew Lódz', 'Werder Bremen', 'Honvéd Budapest', 'Girondins Bordeaux', 'Dinamo Minsk', 'Xamax Neuchâtel', 'Panathinaikos', 'Partizan Belgrade', 'KV Mechelen', 'Sampdoria', 'Brøndby IF', 'Torpedo Moscow', 'AS Monaco', 'FC Tirol Innsbruck', 'AJ Auxerre', 'Trabzonspor', 'AC Parma', 'Paris Saint-Germain', 'Dinamo Moscow', 'Boavista', 'Lazio', 'Rosenborg BK', 'Slavia Praha', 'Bayer Leverkusen', 'Arsenal', 'Deportivo La Coruña', 'Celta de Vigo', 'Real Mallorca', 'CD Alavés', 'Hertha BSC','Sevilla','Villarreal','Schalke 04','Espanyol','Zenit St. Petersburg','CSKA Moscow', 'Manchester City', 'Shakhtar Donetsk', 'FC Basel']

    cnt = 0
    clubName = ""
    clubNation = ""
    clubScore = 0
    for item in t_list2:
        a = item
        b = t_list[cnt*10+2]
        c = t_list[cnt*10+3]
        cnt += 1

        if (1):
            for s in b:
                clubName = s
        if (1):
            for s in c:
                clubNation = s
        if (1):
            for s in a:
                clubScore = s
                while (len(Exllist) > len(Scorelist)):
                    Scorelist.append(0)
                    Nationlist.append(0)
            print(clubName, clubScore, clubNation,len(Exllist),len(Scorelist))
            if (clubName in Exllist):
                key = Exllist.index(clubName, 0, len(Exllist))
                Nationlist[key] = clubNation
                Scorelist[key] = (clubScore)
            else:
                Exllist.append(clubName)
                Scorelist.append(clubScore)
                Nationlist.append(clubNation)


    # 写入数据，第一个参数‘行’，第二个参数‘列’，第三个参数内容
    worksheet.write(0, year - 2018 + 3, year)
    #print(Nationlist)
    #print(Exllist)
    for i in range(0, len(Exllist)):
        worksheet.write(i+1, 0, Exllist[i])
        worksheet.write(i + 1, 1, Nationlist[i])
        worksheet.write(i + 1, year - 2018 + 3, Scorelist[i])
        # print(i, Exllist[i], Nationlist[i], Scorelist[i])

pre()
for year in range(2018,2022):
    save(year)
fin()