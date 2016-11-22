# coding=utf-8

import sys
import os
import codecs
import urllib
import urllib2
import re
import time
import base64
from BeautifulSoup import BeautifulSoup


def WriteRes(malName, malTitle, malDesc, malAuthor, malDate, malSrc):
    if not os.path.exists('malcode'):
        os.makedirs('malcode')

    malTitle = malTitle.replace('<em>', '').replace('</em>', '').replace('<strong>', '').replace('</strong>', '')
    malDesc = malDesc.replace('<em>', '').replace('</em>', '').replace('<strong>', '').replace('</strong>', '')
    malAuthor = malAuthor.replace('<em>', '').replace('</em>', '').replace('<strong>', '').replace('</strong>', '')
    malDate = malDate.replace('<em>', '').replace('</em>', '').replace('<strong>', '').replace('</strong>', '')

    content = '\n'.join([malName, malTitle, malDesc, malAuthor, malDate, malSrc])

    file_path = os.path.join('malcode', malName)

    with codecs.open(file_path, 'w', 'utf-8') as file:
        file.write(content)
    # file = codecs.open(file_path, 'a+', 'utf-8')
    # file.write(content + '\n')
    # file.close

'''
def PrintRes(news_id, news_title, news_link, news_desc=''):
    print '[+]', news_id, news_title
    print '[+]', news_link
    print '[+]', news_desc
    print ''
'''


def GetPage(url):
    htmlpage = urllib2.urlopen(url).read()
    soup = BeautifulSoup(htmlpage)

    return soup


def GetFile(url, file):
    # url = ''.join(['http://vxheaven.org/dl/', file])

    if not os.path.exists('malcode/src'):
        os.makedirs('malcode/src')

    file_path = os.path.join('malcode', file)

    print '[+] start downloading ', file
    urllib.urlretrieve(url, file_path)


def GetMalInfo(url):
    soup = GetPage(url)
    # print soup

    malName = url[33:-4]

    result = soup.find('div', {'class': 's2'})
    # print result

    tmp = result.find('h2')
    if tmp:
        malTitle = tmp.renderContents()

    malDesc = ''
    malAuthor = ''
    malDate = ''

    tmp = result.findAll('p')
    lenth = len(tmp)

    if (lenth > 0):
        malDesc = tmp[0].renderContents()

        if (lenth > 1):
            malAuthor = tmp[1].renderContents()

            if (lenth > 2):
                malDate = tmp[2].renderContents()

    # tmp = result.find('form')
    tmp = result.find('input', {'type': 'hidden'}, {
                      'name': 'file'}).get('value')
    tmp = tmp.replace('@', '=')
    malFile = base64.b64decode(tmp)
    malSrc = ''.join(['http://vxheaven.org/dl/', malFile])

    WriteRes(malName, malTitle, malDesc, malAuthor, malDate, malSrc)
    GetFile(malSrc, malFile)


def GetMalcode(url):
    soup = GetPage(url)
    # print soup

    results = soup.findAll('a', {'href': re.compile(r'/src.php\?info=(.+)')})
    for result in results:
        tmp = result.get('href')
        src_url = ''.join(['http://vxheaven.org', tmp])
        GetMalInfo(src_url)

        # print tmp
    '''
        news_id = result.get('id')
        tmp_a = result.find('a')
        news_title = tmp_a.renderContents()
        news_link = str(tmp_a.get('href'))
        tmp_p = result.find("div").renderContents()
        # print tmp_p
        match = re.search(r'(</p>.+<span)', tmp_p)
        tmp_desc = match.group()
        news_desc = tmp_desc[4:-5]
        # news_desc = result.find("div", {"class": "c-summary"}).renderContents()
        # WriteRes(news_id, news_title, news_link, news_desc, year)
        # PrintRes(news_id, news_title, news_link, news_desc)
    # return len(results)
    '''

if __name__ == '__main__':
    baseurl = "http://vxheaven.org/src.php?show=all"
    # SearchNews()
    GetMalcode(baseurl)
