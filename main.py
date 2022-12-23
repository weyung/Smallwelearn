import json
import asyncio
from pyppeteer import launch
from pyppeteer_stealth import stealth

COURSE = {
    1: {'cid': 297, 'classid': 000000},
    2: {'cid': 296, 'classid': 306558},
    3: {'cid': 295, 'classid': 362790},
}


async def next_class(page):
    f = page.frames[0]
    btn_next = '#form1 > div.courseware_sidebar_2 > ul.c_s_3 > li.c_s_3_2 > a'  # 若 selector 有变，可在此修改
    await f.click(btn_next)

async def fill_ans(page, answer, unit, idx):
    ans, raw = answer
    if not ans[0]:  # 若非填空题则跳过
        return
    ans = ans[0]    # 取答案中的填空题部分

    f = page.frames[0].childFrames[0]
    optionsPicker = await f.J('div.optionsPicker')
    if optionsPicker is None:
        logger.warning('\033[33mUnit {}\033[0m \033[32m{}\033[0m No optionsPicker'.format(unit, idx))    # 无选项
        return
    options = await optionsPicker.JJ('li')
    option_elements = {}
    for option in options:
        content = await f.evaluate('(element) => element.textContent', option)
        opt = await f.evaluate('(element) => element.getAttribute("option")', option)
        if opt:
            content = opt
        option_elements[content.lower()] = option

    for i in range(len(ans)):
        blank = await f.J('et-blank[et-index="%d"]' % (i+1))
        if blank is None:
            i = 0
            continue
        sp = await blank.J('span.wrapper')
        spsp = await sp.J('span')
        txt = await f.evaluate('(element) => element.textContent', spsp)
        if txt != ans[i]:       # 若该空已填写正确答案则跳过
            await sp.click()    # 点击空，弹出选项表
            ans[i] = ans[i].lower()
            if ans[i] not in option_elements:
                logger.error('\033[33mUnit {}\033[0m \033[32m{}\033[0m No answer: {}'.format(unit, idx, ans[i]))    # 答案不在选项中
            await option_elements[ans[i]].click()
    logger.info('\033[33mUnit {}\033[0m \033[32m{}\033[0m Answers filled'.format(unit, idx))
    input("Press Enter to continue...")


async def main(args):
    browser = await launch({
        'executablePath': args['chrome_path'],
        'headless': False,
        'args': ['--no-sandbox', '--window-size=1920,999', '--disable-features=IsolateOrigins,site-per-process', '--disable-web-security']
    })
    page = await browser.newPage()
    await page.setViewport({'width': 1900, 'height': 888})
    await stealth(page)

    # 登录
    logger.debug('Logging in...')
    await page.goto('https://welearn.sflep.com/user/prelogin.aspx?loginret=http%3a%2f%2fwelearn.sflep.com%2fuser%2floginredirect.aspx')
    await page.waitForSelector('#username')
    await page.type('#username', args['username'])
    await page.type('#password', args['password'])
    await page.click('#login')

    # 课程首页
    await page.waitForNavigation()
    logger.info('Logged in')

    # 课程使用说明页面
    cid, classid = COURSE[args['course']]['cid'], COURSE[args['course']]['classid']
    await page.goto('https://welearn.sflep.com/student/StudyCourse.aspx?cid={}&classid={}'.format(cid, classid))

    from getans import getans
    await asyncio.sleep(2)
    await next_class(page)

    while True:
        url = page.frames[0].childFrames[0].url
        unit, idx = url.split('?')[0].split('/')[-2:]
        logger.info('\033[33mUnit {}\033[0m \033[32m{}\033[0m Start'.format(unit, idx))
        answer = getans(
            'https://centercourseware.sflep.com/New College English Viewing Listening Speaking {}/data/{}/{}.html'.format(args['course'],unit, idx))
        logger.info('\033[33mUnit {}\033[0m \033[32m{}\033[0m Answer got'.format(unit, idx))
        await fill_ans(page, answer, unit, idx)
        await next_class(page)

    # await asyncio.sleep(200)
    # await browser.close()

from log import logger

# 加载配置
with open('settings.json', 'r') as f:
    args = json.load(f)
asyncio.get_event_loop().run_until_complete(main(args))