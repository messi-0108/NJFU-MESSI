import requests
from bs4 import BeautifulSoup
import json



class Base:
    def __init__(self, name, url) -> None:
        self.name = name
        self.url = url
        self.info_list = []

    def get_html(self):
        r = requests.get(self.url)
        self.html = r.text

    def get_info(self):
        pass

    def write_file(self):
        with open(self.name+".csv", 'w') as f:
            for row in self.info_list:
                f.write(row)

    def run(self):
        self.get_html()
        self.get_info()
        self.write_file()


class NJU(Base):
    def get_info(self):
        soup = BeautifulSoup(self.html, 'html.parser')
        for target in soup.find_all('li', class_='news'):
            t = target.contents
            self.info_list.append(t[1].contents[0].get_text()+","+r"https://yzb.nju.edu.cn/" + "," +
                                  t[1].contents[0]['href']+","+t[3].get_text()+"\n")


class NJFU(Base):
    def get_html(self):
        r = requests.get(self.url)
        r.encoding='utf-8'
        self.html = r.text
    def get_info(self):
        soup = BeautifulSoup(self.html, 'html.parser')
        for target in soup.find_all('script'):
            if "dataList=" in target.get_text():
                start_index = target.get_text().find("dataList=")+len("dataLsit=")
                end_index = target.get_text().find("var pagesData=")
                info = json.loads(target.get_text()[start_index:end_index].rstrip().rstrip(";"))
                for row in info:
                    for result in row['infolist']:
                        self.info_list.append(
                            result["title"]+","+result["url"]+","+result["daytime"]+"\n")
        return super().get_info()

            
        

if __name__ == "__main__":
    # nju = NJU("nju","https://yzb.nju.edu.cn/47863/list.htm")
    # nju.run()

    njfu = NJFU("njfu","https://yz.njfu.edu.cn/sszs/")
    njfu.run()
    ##r = requests.get("https://yz.njfu.edu.cn/sszs/")
    ##r.encoding = 'utf-8'
    # print(r.text)
    ##soup = BeautifulSoup(r.text, 'html.parser')
    ##for target in soup.find_all('script'):
    ##    if "dataList=" in target.get_text():
            # print(target.get_text().find("dataList="))
            # print(target.get_text()[108:])
            # print(target.get_text().find("var pagesData="))
    ##        start_index = target.get_text().find("dataList=")+len("dataLsit=")
    ##        end_index = target.get_text().find("var pagesData=")
    ##        info = json.loads(target.get_text()[start_index:end_index].rstrip().rstrip(";"))
    ##        for row in info:
    ##            for result in row['infolist']:
    ##                print(result["title"],result["url"],result["daytime"])

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