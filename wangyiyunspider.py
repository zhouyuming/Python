import requests
class Spider():
    def __init__(self):
        self.header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0',
                       'Referer': 'http://music.163.com/'}
        self.url='http://music.163.com/weapi/v1/resource/comments/R_SO_4_531051217?csrf_token='

    def __get_htmls(self,url):
        htmls=requests.get(url)
        print(htmls.status_code)
        return htmls.text

    def run(self):
        self.__get_htmls(self.url)

def main():
    spider=Spider()
    spider.run()

if __name__ == '__main__':
    main()
