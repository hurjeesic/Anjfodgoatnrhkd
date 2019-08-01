import requests
from xml.etree import ElementTree
from bs4 import BeautifulSoup

def dialect_parsing():
    dialect_lst = []
    page = 1
    while True:
        url = 'http://www.jeju.go.kr/rest/JejuDialectService/getJejuDialectServiceList?page={0}'.format(page)

        response = requests.get(url)

        # HTTP 응답 코드는 status_code 에 저장됨
        if(response.status_code == 200):
            root = ElementTree.fromstring(response.content)

            lst = root.findall('list/item')

            if (len(lst) == 0):
                break

            for item in lst:
                standard = item.find('contents').text
                jeju = item.find('siteName').text
                if standard.find('&') == -1 and jeju.find('&') == -1 and \
                   standard.find('⇒') == -1 and jeju.find('⇒') == -1:
                    dialect_lst.append({'standard': standard, 'jeju': jeju})

        else:
            dialect_lst.append({'standard': "Error Code:{0}".format(response.status_code), 'jeju': ''})
            break

        page += 1

    return dialect_lst

def proverb_parsing():
    index = 1
    character = '가'
    proverb_lst = []
    while True:
        url = 'https://ko.wiktionary.org/w/index.php?title=%EB%B6%84%EB%A5%98:%ED%95%9C%EA%B5%AD%EC%96%B4_%EC%86%8D%EB%8B%B4&from={0}'.format(character)

        response = requests.get(url)

        # HTTP 응답 코드는 status_code 에 저장됨
        if(response.status_code == 200):
            data = response.text
            bs = BeautifulSoup(data, 'html.parser')
            url_tags = bs.select(".plainlinks td a")

            content_tags = bs.select(".mw-category a")
            for tag in content_tags:
                proverb_lst.append(tag.contents[0])
        else:
            proverb_lst.append("Error Code:{0}".format(response.status_code))
            break

        index += 1
        if index >= len(url_tags):
            break
        else:
            character = url_tags[index].contents[0]

    return list(set(proverb_lst))
