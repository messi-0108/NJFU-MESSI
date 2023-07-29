 # r = requests.get('https://yzb.nju.edu.cn/47863/list.htm')
    # soup = BeautifulSoup(r.text, 'html.parser')
    # f = open("nju.csv", 'w')
    # for target in soup.find_all('li', class_='news'):
    # t = target.contents
    # f.write(t[1].contents[0].get_text()+","+r"https://yzb.nju.edu.cn/" +
    #        ","+t[1].contents[0]['href']+","+t[3].get_text()+"\n")
    # print(t[1].contents[0].get_text(), r"https://yzb.nju.edu.cn/" +
    #      t[1].contents[0]['href'], t[3].get_text())
    # print(t[1].contents[0].get_text())
    # print(r"https://yzb.nju.edu.cn/"+target.contents[1].contents[0]['href'])
    # print(target.contents[3].get_text())
    # f.close()
