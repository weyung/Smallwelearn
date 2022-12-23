import requests as r
import re


def getans(url):
    '''
    et-blank 填空题
    et-tof 判断题
    et-blank block 长填空题
    et-choice 选择题
    '''
    res = r.get(url)
    # \xc3\xa9 = é, &gt; = >, we need to escape them
    txt = res.text.encode('latin-1').decode('utf-8').replace('&gt;', '>').replace('capitolize', 'capitalize')

    pat = [r'<et-blank(?: capitalize)?>(.*?)</et-blank>',
           r'<et-tof key="(\w)">',
           r'<et-blank block>(.*?)</et-blank>',
           r'<et-choice key="(\w)">']
    pattern = [re.compile(i, re.S) for i in pat]
    answer = [re.findall(i, txt) for i in pattern]
    special = '</et-mobile-only>'
    if special in txt:
        answer = [i[:len(i)//2] for i in answer]
    return answer, txt