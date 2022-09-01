import re
import time
import asyncio
import HackRequests
from datetime import date
from pyppeteer import launch

async def getJSESSIONID():
    # browser = await launch(headless=False, args=['--disable-infobars'])
    browser = await launch()
    page = await browser.newPage()
    # 绕过 WebDriver 的检测，在每次加载网页的时候执行语句，执行将 WebDriver 隐藏的命令
    await page.evaluateOnNewDocument('Object.defineProperty(navigator, "webdriver", {get: () => undefined})')
    # 设置页面视图大小
    await page.setViewport(viewport={'width': 1280, 'height': 800})
    # 是否启用JS，enabled设为False，则无渲染效果
    await page.setJavaScriptEnabled(enabled=True)
    res = await page.goto('https://ehall.nuaa.edu.cn/infoplus/form/YQFKXSFXLSCX_CS/start?theme=nuaa_new')
    await page.waitForSelector("#login_submit")
    await page.type('#username', username)
    await page.type('#password', password)
    await page.click('#login_submit')
    await page.waitForSelector("#preview_start_button")
    # 打印页面cookies
    cookie = await page.cookies()
    # print(cookie[1]["value"])
    # 关闭浏览器
    await browser.close()
    return cookie[1]["value"]

hack = HackRequests.hackRequests()

leaveday = '2022-9-6'
fieldAfdy = "161940233"
# fieldAfdy = "151930106"
# 0515000 航天学院
# Studept = "0515000"
# username = '151930106'
# password = '11209966xY'
# 0518000 长空学院
Studept = "0518000"
username ='161940233'
password = 'yym68686@Inuaa'

jsessionID = asyncio.get_event_loop().run_until_complete(getJSESSIONID())
print("jsessionID", jsessionID)
today = str(date.today()).split("-")
todaymonth = today[1]
todayday = today[2]
timestamp = int(time.time())
csrfToken = "tkx6BTNaH8Fy4hNKawyjhDMVDBdvrD2i"
leaveSchool_timestamp = int(time.mktime(time.strptime(leaveday + ' 00:00:00', '%Y-%m-%d %H:%M:%S')))

raw = '''
POST /infoplus/interface/start HTTP/1.1
Host: ehall.nuaa.edu.cn
Cookie: INGRESSCOOKIE={3}.529.4359.639598; JSESSIONID={4}
Content-Length: 1771
Sec-Ch-Ua: " Not A;Brand";v="99", "Chromium";v="104"
Accept: application/json, text/javascript, */*; q=0.01
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://ehall.nuaa.edu.cn
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://ehall.nuaa.edu.cn/infoplus/form/YQFKXSFXLSCX_CS/start?theme=nuaa_new
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close

idc=YQFKXSFXLSCX_CS&release=&csrfToken={2}&formData=%7B%22_VAR_ACTION_ACCOUNT%22%3A%22162010219%22%2C%22_VAR_ACTION_INDEP_ORGANIZES_Codes%22%3A%22{5}%22%2C%22_VAR_ACTION_REALNAME%22%3A%22%E5%BC%A0%E4%B8%89%E4%B8%89%22%2C%22_VAR_ACTION_INDEP_ORGANIZES_Names%22%3A%22%E9%95%BF%E7%A9%BA%E5%AD%A6%E9%99%A2%22%2C%22_VAR_OWNER_ACCOUNT%22%3A%22162010219%22%2C%22_VAR_ACTION_ORGANIZES_Names%22%3A%22%E9%95%BF%E7%A9%BA%E5%AD%A6%E9%99%A2%22%2C%22_VAR_ACTION_ORGANIZE%22%3A%22{5}%22%2C%22_VAR_OWNER_PHONE%22%3A%2218261064509%22%2C%22_VAR_OWNER_USERCODES%22%3A%22162010219%22%2C%22_VAR_NOW_DAY%22%3A%22{1}%22%2C%22_VAR_ACTION_INDEP_ORGANIZE%22%3A%22{5}%22%2C%22_VAR_OWNER_REALNAME%22%3A%22%E5%BC%A0%E4%B8%89%E4%B8%89%22%2C%22_VAR_ACTION_INDEP_ORGANIZE_Name%22%3A%22%E9%95%BF%E7%A9%BA%E5%AD%A6%E9%99%A2%22%2C%22_VAR_NOW%22%3A%221661949791%22%2C%22_VAR_ACTION_ORGANIZE_Name%22%3A%22%E9%95%BF%E7%A9%BA%E5%AD%A6%E9%99%A2%22%2C%22_VAR_OWNER_ORGANIZES_Codes%22%3A%22{5}%22%2C%22_VAR_ADDR%22%3A%2210.100.117.20%22%2C%22_VAR_URL_Attr%22%3A%22%7B%5C%22theme%5C%22%3A%5C%22nuaa_new%5C%22%7D%22%2C%22_VAR_ENTRY_NUMBER%22%3A%22-1%22%2C%22_VAR_POSITIONS%22%3A%22{5}%3A11%3A162010219%22%2C%22_VAR_ACTION_PHONE%22%3A%2218261064509%22%2C%22_VAR_OWNER_ORGANIZES_Names%22%3A%22%E9%95%BF%E7%A9%BA%E5%AD%A6%E9%99%A2%22%2C%22_VAR_URL%22%3A%22https%3A%2F%2Fehall.nuaa.edu.cn%2Finfoplus%2Fform%2FYQFKXSFXLSCX_CS%2Fstart%3Ftheme%3Dnuaa_new%22%2C%22_VAR_RELEASE%22%3A%22true%22%2C%22_VAR_TODAY%22%3A%221661875200%22%2C%22_VAR_NOW_MONTH%22%3A%22{0}%22%2C%22_VAR_ACTION_USERCODES%22%3A%22162010219%22%2C%22_VAR_ACTION_ORGANIZES_Codes%22%3A%22{5}%22%2C%22_VAR_NOW_YEAR%22%3A%222022%22%2C%22_VAR_ENTRY_NAME%22%3A%22%22%2C%22_VAR_ENTRY_TAGS%22%3A%22%22%7D&lang=zh
'''
stepId = ""
for _ in range(3):
    hh = hack.httpraw(raw.format(todaymonth, todayday, csrfToken, timestamp, jsessionID, Studept),ssl=type)
    test_str = hh.text()
    if ("SAFETY_PROTECTION_CSRF" in test_str):
        csrfToken = re.findall(r"\[\"(.*?)\"]", test_str)[0]
        print("csrfToken", csrfToken)
    elif ("SYSTEM_BUSY" in test_str):
        print("system busy...")
        exit(0)
    elif ("USER_LOGIN_REQUIRED" in test_str):
        print("need login, JSESSIONID expired...")
        exit(0)
    else:
        print(test_str)
        stepId = re.findall(r"form/(.*?)/render", test_str)[0]
        if not stepId:
            print("get step id error!")
            exit(0)
        print("stepId", stepId)
        break

# yzhraw = '''
# POST /infoplus/interface/doAction HTTP/1.1
# Host: ehall.nuaa.edu.cn
# Cookie: JSESSIONID={3}
# Content-Length: 6388
# Sec-Ch-Ua: " Not A;Brand";v="99", "Chromium";v="104"
# Accept: application/json, text/javascript, */*; q=0.01
# Content-Type: application/x-www-form-urlencoded; charset=UTF-8
# X-Requested-With: XMLHttpRequest
# Sec-Ch-Ua-Mobile: ?0
# User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36
# Sec-Ch-Ua-Platform: "Windows"
# Origin: https://ehall.nuaa.edu.cn
# Sec-Fetch-Site: same-origin
# Sec-Fetch-Mode: cors
# Sec-Fetch-Dest: empty
# Referer: https://ehall.nuaa.edu.cn/infoplus/form/{0}/render?theme=nuaa_new
# Accept-Encoding: gzip, deflate
# Accept-Language: zh-CN,zh;q=0.9
# Connection: close

# actionId=20&formData=%7B%22_VAR_EXECUTE_INDEP_ORGANIZE_Name%22%3A%22%E8%88%AA%E5%A4%A9%E5%AD%A6%E9%99%A2%22%2C%22_VAR_ACTION_INDEP_ORGANIZES_Codes%22%3A%22{6}%22%2C%22_VAR_ACTION_REALNAME%22%3A%22%E9%B1%BC%E6%BB%8B%E6%83%A0%22%2C%22_VAR_ACTION_ORGANIZE%22%3A%22{6}%22%2C%22_VAR_EXECUTE_ORGANIZE%22%3A%22{6}%22%2C%22_VAR_ACTION_INDEP_ORGANIZE%22%3A%22{6}%22%2C%22_VAR_ACTION_INDEP_ORGANIZE_Name%22%3A%22%E8%88%AA%E5%A4%A9%E5%AD%A6%E9%99%A2%22%2C%22_VAR_ACTION_ORGANIZE_Name%22%3A%22%E8%88%AA%E5%A4%A9%E5%AD%A6%E9%99%A2%22%2C%22_VAR_EXECUTE_ORGANIZES_Names%22%3A%22%E8%88%AA%E5%A4%A9%E5%AD%A6%E9%99%A2%22%2C%22_VAR_OWNER_ORGANIZES_Codes%22%3A%22{6}%22%2C%22_VAR_ADDR%22%3A%2210.100.237.40%22%2C%22_VAR_OWNER_ORGANIZES_Names%22%3A%22%E8%88%AA%E5%A4%A9%E5%AD%A6%E9%99%A2%22%2C%22_VAR_URL%22%3A%22https%3A%2F%2Fehall.nuaa.edu.cn%2Finfoplus%2Fform%2F{0}%2Frender%3Ftheme%3Dnuaa_new%22%2C%22_VAR_EXECUTE_ORGANIZE_Name%22%3A%22%E8%88%AA%E5%A4%A9%E5%AD%A6%E9%99%A2%22%2C%22_VAR_RELEASE%22%3A%22true%22%2C%22_VAR_TODAY%22%3A%22{5}%22%2C%22_VAR_NOW_MONTH%22%3A%229%22%2C%22_VAR_ACTION_USERCODES%22%3A%22151930106%22%2C%22_VAR_ACTION_ACCOUNT%22%3A%22151930106%22%2C%22_VAR_ACTION_INDEP_ORGANIZES_Names%22%3A%22%E8%88%AA%E5%A4%A9%E5%AD%A6%E9%99%A2%22%2C%22_VAR_OWNER_ACCOUNT%22%3A%22151930106%22%2C%22_VAR_ACTION_ORGANIZES_Names%22%3A%22%E8%88%AA%E5%A4%A9%E5%AD%A6%E9%99%A2%22%2C%22_VAR_STEP_CODE%22%3A%22SQR%22%2C%22_VAR_OWNER_PHONE%22%3A%2218093639980%22%2C%22_VAR_OWNER_USERCODES%22%3A%22151930106%22%2C%22_VAR_EXECUTE_ORGANIZES_Codes%22%3A%22{6}%22%2C%22_VAR_NOW_DAY%22%3A%221%22%2C%22_VAR_OWNER_REALNAME%22%3A%22%E9%B1%BC%E6%BB%8B%E6%83%A0%22%2C%22_VAR_ENTRY_TAGS%22%3A%2201-%E7%96%AB%E6%83%85%E9%98%B2%E6%8E%A7%E6%9C%8D%E5%8A%A1%2C%E7%A7%BB%E5%8A%A8%E7%AB%AF%22%2C%22_VAR_NOW%22%3A%221662038857%22%2C%22_VAR_URL_Attr%22%3A%22%7B%5C%22theme%5C%22%3A%5C%22nuaa_new%5C%22%7D%22%2C%22_VAR_ENTRY_NUMBER%22%3A%2213358164%22%2C%22_VAR_EXECUTE_INDEP_ORGANIZES_Names%22%3A%22%E8%88%AA%E5%A4%A9%E5%AD%A6%E9%99%A2%22%2C%22_VAR_ENTRY_NAME%22%3A%22_%E7%96%AB%E6%83%85%E9%98%B2%E6%8E%A7%E6%9C%9F%E5%AD%A6%E7%94%9F%E9%9B%B6%E6%98%9F%E8%BF%9B%E5%87%BA%E6%A0%A1%E7%94%B3%E8%AF%B7%22%2C%22_VAR_STEP_NUMBER%22%3A%22{0}%22%2C%22_VAR_POSITIONS%22%3A%22{6}%3A11%3A151930106%22%2C%22_VAR_ACTION_PHONE%22%3A%2218093639980%22%2C%22_VAR_EXECUTE_INDEP_ORGANIZES_Codes%22%3A%22{6}%22%2C%22_VAR_EXECUTE_POSITIONS%22%3A%22{6}%3A11%3A151930106%22%2C%22_VAR_ACTION_ORGANIZES_Codes%22%3A%22{6}%22%2C%22_VAR_EXECUTE_INDEP_ORGANIZE%22%3A%22{6}%22%2C%22_VAR_NOW_YEAR%22%3A%222022%22%2C%22groupQWDDList%22%3A%5B0%5D%2C%22fieldHMDFZ%22%3A%222%22%2C%22fieldXSSF%22%3A%22%E6%9C%AC%E7%A7%91%E7%94%9F%22%2C%22fieldSQSJ%22%3A1662038857%2C%22fieldAxm%22%3A%22151930106%22%2C%22fieldAxm_Name%22%3A%22%E9%B1%BC%E6%BB%8B%E6%83%A0%22%2C%22fieldAxy%22%3A%22{6}%22%2C%22fieldAxy_Name%22%3A%22%E8%88%AA%E5%A4%A9%E5%AD%A6%E9%99%A2%22%2C%22fieldAxh%22%3A%22151930106%22%2C%22fieldAlxdh%22%3A%2218093639980%22%2C%22fieldAfdy%22%3A%22{1}%22%2C%22fieldAfdy_Name%22%3A%22%E5%86%AF%E6%9E%9C%E6%9E%9C%22%2C%22fieldDS%22%3A%22%22%2C%22fieldDS_Name%22%3A%22%22%2C%22fieldASFZHM%22%3A%22622201200009110320%22%2C%22fieldASZXQ%22%3A%222%22%2C%22fieldASZXQ_Name%22%3A%22%E5%B0%86%E5%86%9B%E8%B7%AF%E6%A0%A1%E5%8C%BA%22%2C%22fieldXSLX%22%3A%22%E4%BD%8F%E6%A0%A1%22%2C%22fieldXSLX_Name%22%3A%22%E4%BD%8F%E6%A0%A1%22%2C%22fieldSFYGLS%22%3A%22%22%2C%22fieldTZSFJK%22%3A%22%22%2C%22fieldSKM%22%3A%22%7B%5C%22id%5C%22%3A%5C%22177b0983-9d7b-4e0f-b9e0-0d15d6984881%5C%22%2C%5C%22name%5C%22%3A%5C%221.png%5C%22%2C%5C%22size%5C%22%3A1%2C%5C%22uri%5C%22%3A%5C%22https%3A%2F%2Fehall.nuaa.edu.cn%2Ffile%2F177b0983-9d7b-4e0f-b9e0-0d15d6984881%5C%22%2C%5C%22mime%5C%22%3A%5C%22image%2Fpng%5C%22%7D%22%2C%22fieldXCM%22%3A%22%7B%5C%22id%5C%22%3A%5C%227720438c-ca96-4d84-818e-ea49a65e54b6%5C%22%2C%5C%22name%5C%22%3A%5C%221.png%5C%22%2C%5C%22size%5C%22%3A1%2C%5C%22uri%5C%22%3A%5C%22https%3A%2F%2Fehall.nuaa.edu.cn%2Ffile%2F7720438c-ca96-4d84-818e-ea49a65e54b6%5C%22%2C%5C%22mime%5C%22%3A%5C%22image%2Fpng%5C%22%7D%22%2C%22fieldHSBG%22%3A%22%7B%5C%22id%5C%22%3A%5C%22640235a2-162e-4fe5-a156-5c9bfc7878b7%5C%22%2C%5C%22name%5C%22%3A%5C%221.png%5C%22%2C%5C%22size%5C%22%3A1%2C%5C%22uri%5C%22%3A%5C%22https%3A%2F%2Fehall.nuaa.edu.cn%2Ffile%2F640235a2-162e-4fe5-a156-5c9bfc7878b7%5C%22%2C%5C%22mime%5C%22%3A%5C%22image%2Fpng%5C%22%7D%22%2C%22fieldBLHTS%22%3A%22%22%2C%22fieldCXRQ%22%3A{5}%2C%22fieldJSSJ%22%3A{5}%2C%22fieldCXSJFROM%22%3A0%2C%22fieldCXSJTO%22%3A0%2C%22fieldCXSY%22%3A%22...%22%2C%22fieldCXLB%22%3A%221%22%2C%22fieldAcxxc%22%3A%222%22%2C%22fieldAds%22%3A%221%22%2C%22fieldAshengs%22%3A%5B%22%22%5D%2C%22fieldAshengs_Name%22%3A%5B%22%22%5D%2C%22fieldAshis%22%3A%5B%22%22%5D%2C%22fieldAshis_Name%22%3A%5B%22%22%5D%2C%22fieldAshis_Attr%22%3A%5B%22%7B%5C%22_parent%5C%22%3A%5C%22%5C%22%7D%22%5D%2C%22fieldAjtdd%22%3A%5B%22%22%5D%2C%22fieldCN%22%3Atrue%2C%22fieldAhidden%22%3A%22%22%2C%22fieldCyj3%22%3A%22%22%2C%22fieldCshr3%22%3A%22%22%2C%22fieldCshr3_Name%22%3A%22%22%2C%22fieldCshdate3%22%3A%22%22%2C%22fieldFYZSH%22%3A%22%22%2C%22fieldFYZSHR%22%3A%22%22%2C%22fieldFYZSHR_Name%22%3A%22%22%2C%22fieldFYZSHRQ%22%3A%22%22%2C%22fieldCyj4%22%3A%22%22%2C%22fieldCshr4%22%3A%22%22%2C%22fieldCshr4_Name%22%3A%22%22%2C%22fieldCshdate4%22%3A%22%22%2C%22fieldCyj5%22%3A%22%22%2C%22fieldCshr5%22%3A%22%22%2C%22fieldCshr5_Name%22%3A%22%22%2C%22fieldCshsj5%22%3A%22%22%2C%22fieldTOKEN%22%3A%22%22%2C%22fieldCXRQSTR%22%3A%22%22%2C%22fieldCXRQFrom%22%3A1662038857%2C%22fieldFZZD%22%3A%22%22%7D&remark=&rand=852.489790496718&nextUsers=%7B%222%2C%22%3A%22836c8201-c95e-11e9-9127-0050568a281f%22%7D&stepId={0}&timestamp={2}&boundFields=fieldCXSJTO%2CfieldASZXQ%2CfieldCXRQ%2CfieldAshengs%2CfieldAcxxc%2CfieldAxh%2CfieldFZZD%2CfieldCXRQSTR%2CfieldSKM%2CfieldAxm%2CfieldAlxdh%2CfieldCXRQFrom%2CfieldDS%2CfieldXCM%2CfieldTOKEN%2CfieldXSLX%2CfieldSFYGLS%2CfieldHMDFZ%2CfieldBLHTS%2CfieldAhidden%2CfieldFYZSH%2CfieldJSSJ%2CfieldCXLB%2CfieldSQSJ%2CfieldCshr3%2CfieldTZSFJK%2CfieldASFZHM%2CfieldCN%2CfieldFYZSHRQ%2CfieldCXSJFROM%2CfieldFYZSHR%2CfieldCshdate3%2CfieldXSSF%2CfieldCshsj5%2CfieldAjtdd%2CfieldAxy%2CfieldHSBG%2CfieldCshdate4%2CfieldAfdy%2CfieldCXSY%2CfieldAds%2CfieldCshr4%2CfieldCshr5%2CfieldCyj3%2CfieldCyj5%2CfieldCyj4%2CfieldAshis&csrfToken={4}&lang=zh
# '''.format(stepId, fieldAfdy, timestamp, jsessionID, csrfToken, leaveSchool_timestamp, Studept)
# hh = hack.httpraw(yzhraw,ssl=type)
# test_str = hh.text()
# print(test_str)


yymraw = '''
POST /infoplus/interface/doAction HTTP/1.1
Host: ehall.nuaa.edu.cn
Cookie: JSESSIONID={3}
Content-Length: 6508
Sec-Ch-Ua: " Not A;Brand";v="99", "Chromium";v="104"
Accept: application/json, text/javascript, */*; q=0.01
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://ehall.nuaa.edu.cn
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://ehall.nuaa.edu.cn/infoplus/form/{0}/render?theme=nuaa_new
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close

actionId=20&formData=%7B%22_VAR_EXECUTE_INDEP_ORGANIZE_Name%22%3A%22%E9%95%BF%E7%A9%BA%E5%AD%A6%E9%99%A2%22%2C%22_VAR_ACTION_INDEP_ORGANIZES_Codes%22%3A%22{6}%22%2C%22_VAR_ACTION_REALNAME%22%3A%22%E5%BC%A0%E4%B8%89%E4%B8%89%22%2C%22_VAR_ACTION_ORGANIZE%22%3A%22{6}%22%2C%22_VAR_EXECUTE_ORGANIZE%22%3A%22{6}%22%2C%22_VAR_ACTION_INDEP_ORGANIZE%22%3A%22{6}%22%2C%22_VAR_ACTION_INDEP_ORGANIZE_Name%22%3A%22%E9%95%BF%E7%A9%BA%E5%AD%A6%E9%99%A2%22%2C%22_VAR_ACTION_ORGANIZE_Name%22%3A%22%E9%95%BF%E7%A9%BA%E5%AD%A6%E9%99%A2%22%2C%22_VAR_EXECUTE_ORGANIZES_Names%22%3A%22%E9%95%BF%E7%A9%BA%E5%AD%A6%E9%99%A2%22%2C%22_VAR_OWNER_ORGANIZES_Codes%22%3A%22{6}%22%2C%22_VAR_ADDR%22%3A%2210.100.237.40%22%2C%22_VAR_LAST_ACTION%22%3A%22Submit%22%2C%22_VAR_OWNER_ORGANIZES_Names%22%3A%22%E9%95%BF%E7%A9%BA%E5%AD%A6%E9%99%A2%22%2C%22_VAR_URL%22%3A%22https%3A%2F%2Fehall.nuaa.edu.cn%2Finfoplus%2Fform%2F{0}%2Frender%3Ftheme%3Dnuaa_new%22%2C%22_VAR_EXECUTE_ORGANIZE_Name%22%3A%22%E9%95%BF%E7%A9%BA%E5%AD%A6%E9%99%A2%22%2C%22_VAR_RELEASE%22%3A%22true%22%2C%22_VAR_TODAY%22%3A%22{5}%22%2C%22_VAR_NOW_MONTH%22%3A%229%22%2C%22_VAR_ACTION_USERCODES%22%3A%22162010219%22%2C%22_VAR_ACTION_ACCOUNT%22%3A%22162010219%22%2C%22_VAR_ACTION_INDEP_ORGANIZES_Names%22%3A%22%E9%95%BF%E7%A9%BA%E5%AD%A6%E9%99%A2%22%2C%22_VAR_OWNER_ACCOUNT%22%3A%22162010219%22%2C%22_VAR_ACTION_ORGANIZES_Names%22%3A%22%E9%95%BF%E7%A9%BA%E5%AD%A6%E9%99%A2%22%2C%22_VAR_STEP_CODE%22%3A%22SQR%22%2C%22_VAR_OWNER_PHONE%22%3A%2218261064509%22%2C%22_VAR_OWNER_USERCODES%22%3A%22162010219%22%2C%22_VAR_EXECUTE_ORGANIZES_Codes%22%3A%22{6}%22%2C%22_VAR_NOW_DAY%22%3A%221%22%2C%22_VAR_OWNER_REALNAME%22%3A%22%E5%BC%A0%E4%B8%89%E4%B8%89%22%2C%22_VAR_ENTRY_TAGS%22%3A%2201-%E7%96%AB%E6%83%85%E9%98%B2%E6%8E%A7%E6%9C%8D%E5%8A%A1%2C%E7%A7%BB%E5%8A%A8%E7%AB%AF%22%2C%22_VAR_NOW%22%3A%221662033008%22%2C%22_VAR_PARTICIPANTS%22%3A%22%2C162010219%2C%22%2C%22_VAR_URL_Attr%22%3A%22%7B%5C%22theme%5C%22%3A%5C%22nuaa_new%5C%22%7D%22%2C%22_VAR_ENTRY_NUMBER%22%3A%2213357383%22%2C%22_VAR_EXECUTE_INDEP_ORGANIZES_Names%22%3A%22%E9%95%BF%E7%A9%BA%E5%AD%A6%E9%99%A2%22%2C%22_VAR_ENTRY_NAME%22%3A%22%E5%BC%A0%E4%B8%89%E4%B8%89_%E7%96%AB%E6%83%85%E9%98%B2%E6%8E%A7%E6%9C%9F%E5%AD%A6%E7%94%9F%E9%9B%B6%E6%98%9F%E8%BF%9B%E5%87%BA%E6%A0%A1%E7%94%B3%E8%AF%B7%22%2C%22_VAR_STEP_NUMBER%22%3A%22{0}%22%2C%22_VAR_POSITIONS%22%3A%22{6}%3A11%3A162010219%22%2C%22_VAR_ACTION_PHONE%22%3A%2218261064509%22%2C%22_VAR_EXECUTE_INDEP_ORGANIZES_Codes%22%3A%22{6}%22%2C%22_VAR_EXECUTE_POSITIONS%22%3A%22{6}%3A11%3A162010219%22%2C%22_VAR_ACTION_ORGANIZES_Codes%22%3A%22{6}%22%2C%22_VAR_EXECUTE_INDEP_ORGANIZE%22%3A%22{6}%22%2C%22_VAR_NOW_YEAR%22%3A%222022%22%2C%22groupQWDDList%22%3A%5B0%5D%2C%22fieldHMDFZ%22%3A%222%22%2C%22fieldXSSF%22%3A%22%E6%9C%AC%E7%A7%91%E7%94%9F%22%2C%22fieldSQSJ%22%3A1662033008%2C%22fieldAxm%22%3A%22162010219%22%2C%22fieldAxm_Name%22%3A%22%E5%BC%A0%E4%B8%89%E4%B8%89%22%2C%22fieldAxy%22%3A%22{6}%22%2C%22fieldAxy_Name%22%3A%22%E9%95%BF%E7%A9%BA%E5%AD%A6%E9%99%A2%22%2C%22fieldAxh%22%3A%22162010219%22%2C%22fieldAlxdh%22%3A%2218261064509%22%2C%22fieldAfdy%22%3A%22{1}%22%2C%22fieldAfdy_Name%22%3A%22%E9%99%B6%E7%84%B6%E9%9B%81%22%2C%22fieldDS%22%3A%22%22%2C%22fieldDS_Name%22%3A%22%22%2C%22fieldASFZHM%22%3A%22111111111111111111%22%2C%22fieldASZXQ%22%3A%222%22%2C%22fieldASZXQ_Name%22%3A%22%E5%B0%86%E5%86%9B%E8%B7%AF%E6%A0%A1%E5%8C%BA%22%2C%22fieldXSLX%22%3A%22%E4%BD%8F%E6%A0%A1%22%2C%22fieldXSLX_Name%22%3A%22%E4%BD%8F%E6%A0%A1%22%2C%22fieldSFYGLS%22%3A%22%22%2C%22fieldTZSFJK%22%3A%22%22%2C%22fieldSKM%22%3A%22%7B%5C%22id%5C%22%3A%5C%221fa984e7-8a42-4099-903c-101f65d329f4%5C%22%2C%5C%22name%5C%22%3A%5C%221.png%5C%22%2C%5C%22size%5C%22%3A1%2C%5C%22uri%5C%22%3A%5C%22https%3A%2F%2Fehall.nuaa.edu.cn%2Ffile%2F1fa984e7-8a42-4099-903c-101f65d329f4%5C%22%2C%5C%22mime%5C%22%3A%5C%22image%2Fpng%5C%22%7D%22%2C%22fieldXCM%22%3A%22%7B%5C%22id%5C%22%3A%5C%22b590f1df-050b-432b-99ec-8d66356607df%5C%22%2C%5C%22name%5C%22%3A%5C%221.png%5C%22%2C%5C%22size%5C%22%3A1%2C%5C%22uri%5C%22%3A%5C%22https%3A%2F%2Fehall.nuaa.edu.cn%2Ffile%2Fb590f1df-050b-432b-99ec-8d66356607df%5C%22%2C%5C%22mime%5C%22%3A%5C%22image%2Fpng%5C%22%7D%22%2C%22fieldHSBG%22%3A%22%7B%5C%22id%5C%22%3A%5C%2226846052-cb59-4cad-b39a-8cb04f9a572d%5C%22%2C%5C%22name%5C%22%3A%5C%221.png%5C%22%2C%5C%22size%5C%22%3A1%2C%5C%22uri%5C%22%3A%5C%22https%3A%2F%2Fehall.nuaa.edu.cn%2Ffile%2F26846052-cb59-4cad-b39a-8cb04f9a572d%5C%22%2C%5C%22mime%5C%22%3A%5C%22image%2Fpng%5C%22%7D%22%2C%22fieldBLHTS%22%3A%22%22%2C%22fieldCXRQ%22%3A{5}%2C%22fieldJSSJ%22%3A{5}%2C%22fieldCXSJFROM%22%3A0%2C%22fieldCXSJTO%22%3A300%2C%22fieldCXSY%22%3A%22...%22%2C%22fieldCXLB%22%3A%221%22%2C%22fieldAcxxc%22%3A%222%22%2C%22fieldAds%22%3A%221%22%2C%22fieldAshengs%22%3A%5B%22%22%5D%2C%22fieldAshengs_Name%22%3A%5B%22%22%5D%2C%22fieldAshis%22%3A%5B%22%22%5D%2C%22fieldAshis_Name%22%3A%5B%22%22%5D%2C%22fieldAshis_Attr%22%3A%5B%22%7B%5C%22_parent%5C%22%3A%5C%22%5C%22%7D%22%5D%2C%22fieldAjtdd%22%3A%5B%22%22%5D%2C%22fieldCN%22%3Atrue%2C%22fieldAhidden%22%3A%22%22%2C%22fieldCyj3%22%3A%22%22%2C%22fieldCshr3%22%3A%22%22%2C%22fieldCshr3_Name%22%3A%22%22%2C%22fieldCshdate3%22%3A%22%22%2C%22fieldFYZSH%22%3A%22%22%2C%22fieldFYZSHR%22%3A%22%22%2C%22fieldFYZSHR_Name%22%3A%22%22%2C%22fieldFYZSHRQ%22%3A%22%22%2C%22fieldCyj4%22%3A%22%22%2C%22fieldCshr4%22%3A%22%22%2C%22fieldCshr4_Name%22%3A%22%22%2C%22fieldCshdate4%22%3A%22%22%2C%22fieldCyj5%22%3A%22%22%2C%22fieldCshr5%22%3A%22%22%2C%22fieldCshr5_Name%22%3A%22%22%2C%22fieldCshsj5%22%3A%22%22%2C%22fieldTOKEN%22%3A%22%22%2C%22fieldCXRQSTR%22%3A%22%22%2C%22fieldCXRQFrom%22%3A{5}%2C%22fieldFZZD%22%3A%22%22%7D&remark=&rand=365.70270905983597&nextUsers=%7B%222%2C%22%3A%227c94c0c3-c95e-11e9-9127-0050568a281f%22%7D&stepId={0}&timestamp={2}&boundFields=fieldCXSJTO%2CfieldASZXQ%2CfieldCXRQ%2CfieldAshengs%2CfieldAcxxc%2CfieldAxh%2CfieldFZZD%2CfieldCXRQSTR%2CfieldSKM%2CfieldAxm%2CfieldAlxdh%2CfieldCXRQFrom%2CfieldDS%2CfieldXCM%2CfieldTOKEN%2CfieldXSLX%2CfieldSFYGLS%2CfieldHMDFZ%2CfieldBLHTS%2CfieldAhidden%2CfieldFYZSH%2CfieldJSSJ%2CfieldCXLB%2CfieldSQSJ%2CfieldCshr3%2CfieldTZSFJK%2CfieldASFZHM%2CfieldCN%2CfieldFYZSHRQ%2CfieldCXSJFROM%2CfieldFYZSHR%2CfieldCshdate3%2CfieldXSSF%2CfieldCshsj5%2CfieldAjtdd%2CfieldAxy%2CfieldHSBG%2CfieldCshdate4%2CfieldAfdy%2CfieldCXSY%2CfieldAds%2CfieldCshr4%2CfieldCshr5%2CfieldCyj3%2CfieldCyj5%2CfieldCyj4%2CfieldAshis&csrfToken={4}&lang=zh
'''.format(stepId, fieldAfdy, timestamp, jsessionID, csrfToken, leaveSchool_timestamp, Studept)
hh = hack.httpraw(yymraw,ssl=type)
test_str = hh.text()
print(test_str)