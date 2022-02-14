import requests,random,secrets
from telebot import types
import telebot
from user_agent import generate_user_agent
""""
برمجة https://ren9_botkabby

فكرة https://t.me/YIIlIH

"""
token = input("Enter_TOKEN:")

bot = telebot.TeleBot(token)
bot.remove_webhook()

@bot.message_handler(commands=['start'])
def send_wel(message):
    inline = types.InlineKeyboardMarkup(row_width=3)
    make = types.InlineKeyboardButton("صنع وهمي",callback_data="start")
    pr = types.InlineKeyboardButton("صنع من ايميل خاص",callback_data="ptmail")
    inline.add(make,pr)
    bot.send_message(chat_id=(message.chat.id),text=f'*مرحبا بك في يا { message.from_user.first_name} في بوت صنع الاستضافه*',reply_markup=inline,parse_mode='markdown')

@bot.callback_query_handler(func=(lambda call:True))
def call(call):
    if call.data == "start":
        url = 'https://dashboard.pantheon.io/register'
        head = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Length': '199',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': '_ga=GA1.2.1442978344.1631760627; _gid=GA1.2.801729137.1631760627; __utmc=97458314; __utmz=97458314.1631760627.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _mkto_trk=id:316-GSV-089&token:_mch-dashboard.pantheon.io-1631760627584-29222; ajs_anonymous_id=%22fcf4b685-5a66-43f6-b3d5-6278cba8fcdf%22; pantheon_tracking=%7B%22utm_source%22%3A%22No%20UTM%22%2C%22utm_medium%22%3A%22No%20UTM%22%2C%22utm_device%22%3A%22No%20UTM%22%2C%22utm_content%22%3A%22No%20UTM%22%2C%22utm_campaign%22%3A%22No%20UTM%22%2C%22utm_term%22%3A%22No%20UTM%22%2C%22utm_ad_group_name%22%3A%22No%20UTM%22%2C%22dtl%22%3A%22%22%2C%22referrer_url%22%3A%22%22%7D; pantheon_tracking=%7B%22utm_source%22%3A%22No%20UTM%22%2C%22utm_medium%22%3A%22No%20UTM%22%2C%22utm_device%22%3A%22No%20UTM%22%2C%22utm_content%22%3A%22No%20UTM%22%2C%22utm_campaign%22%3A%22No%20UTM%22%2C%22utm_term%22%3A%22No%20UTM%22%2C%22utm_ad_group_name%22%3A%22No%20UTM%22%2C%22dtl%22%3A%22%22%2C%22referrer_url%22%3A%22%22%7D; __utma=97458314.1442978344.1631760627.1631760627.1631763283.2; OptanonAlertBoxClosed=2021-09-16T03:35:41.701Z; _vwo_uuid_v2=D85586077E6C3CC18432718487186C7FF|db298eece003160e44d7fe53c2338d53; _vis_opt_s=1%7C; _vis_opt_test_cookie=1; _vwo_uuid=D85586077E6C3CC18432718487186C7FF; _vwo_ds=3%241631763524%3A1.13392115%3A%3A; _mkto_trk=id:316-GSV-089&token:_mch-pantheon.io-1631763528037-90938; _biz_sid=2a927e; _fbp=fb.1.1631763533718.266134017; _biz_uid=07537b0f05734e6795dddd255832c1b5; intercom-id-xkegk7cr=86cffc78-56ca-4239-9750-aefa9bb43ff3; intercom-session-xkegk7cr=; OptanonAlertBoxClosed=2021-09-16T03:39:16.803Z; _biz_flagsA=%7B%22Version%22%3A1%2C%22Mkto%22%3A%221%22%2C%22ViewThrough%22%3A%221%22%2C%22XDomain%22%3A%221%22%2C%22Frm%22%3A%221%22%7D; _vis_opt_exp_135_combi=1; _vis_opt_exp_141_combi=2; _vis_opt_exp_116_combi=2; _vis_opt_exp_116_goal_210=1; _biz_ABTestA=%5B1054094750%5D; _vis_opt_exp_141_goal_200=1; _vis_opt_exp_135_goal_200=1; _vis_opt_exp_116_goal_200=1; _vis_opt_exp_141_goal_212=1; _vis_opt_exp_135_goal_212=1; _vis_opt_exp_116_goal_212=1; _vis_opt_exp_141_goal_213=1; _vis_opt_exp_135_goal_213=1; _vis_opt_exp_116_goal_213=1; _csrf=eOFR7mv0u3d1sWGlWFzFQ1nK; __utmt=1; __utmb=97458314.4.10.1631763283; OptanonConsent=isIABGlobal=false&datestamp=Thu+Sep+16+2021+07%3A05%3A05+GMT%2B0300+(%D8%A7%D9%84%D8%AA%D9%88%D9%82%D9%8A%D8%AA+%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A+%D8%A7%D9%84%D8%B1%D8%B3%D9%85%D9%8A)&version=6.0.0&landingPath=NotLandingPage&groups=0_224028%3A1%2C1%3A1%2C2%3A1%2C0_224029%3A1%2C3%3A1%2C0_224030%3A1%2C0_224031%3A1%2C4%3A1%2C0_224032%3A1%2C0_224034%3A1%2C0_224036%3A1%2C0_224037%3A1%2C0_224039%3A1%2C0_224040%3A1%2C0_224041%3A1%2C0_224042%3A1%2C0_224043%3A1%2C0_224044%3A1%2C0_224045%3A1%2C0_224046%3A1%2C0_224047%3A1%2C0_263828%3A1%2C0_263832%3A1%2C0_224048%3A1%2C0_263836%3A1%2C0_263840%3A1%2C0_264785%3A1%2C0_263827%3A1%2C0_263831%3A1%2C0_224035%3A1%2C0_268794%3A1%2C0_263835%3A1%2C0_263839%3A1%2C0_263843%3A1%2C0_268773%3A1%2C0_268777%3A1%2C0_224038%3A1%2C0_263826%3A1%2C0_263830%3A1%2C0_263834%3A1%2C0_263838%3A1%2C0_268772%3A1%2C0_263842%3A1%2C0_263829%3A1%2C0_263833%3A1%2C0_263837%3A1%2C0_263292%3A1%2C0_263841%3A1%2C0_268771%3A1&consentId=61e45c1e-77a9-414d-8432-fd89a4b20575&AwaitingReconsent=false; OptanonConsent=isIABGlobal=false&datestamp=Thu+Sep+16+2021+07%3A05%3A41+GMT%2B0300+(%D8%A7%D9%84%D8%AA%D9%88%D9%82%D9%8A%D8%AA+%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A+%D8%A7%D9%84%D8%B1%D8%B3%D9%85%D9%8A)&version=6.7.0&landingPath=NotLandingPage&groups=0_224028%3A1%2C1%3A1%2C2%3A1%2C0_224029%3A1%2C3%3A1%2C0_224030%3A1%2C0_224031%3A1%2C4%3A1%2C0_224032%3A1%2C0_224034%3A1%2C0_224036%3A1%2C0_224037%3A1%2C0_224039%3A1%2C0_224040%3A1%2C0_224041%3A1%2C0_224042%3A1%2C0_224043%3A1%2C0_224044%3A1%2C0_224045%3A1%2C0_224046%3A1%2C0_224047%3A1%2C0_263828%3A1%2C0_263832%3A1%2C0_224048%3A1%2C0_263836%3A1%2C0_263840%3A1%2C0_264785%3A1%2C0_263827%3A1%2C0_263831%3A1%2C0_224035%3A1%2C0_268794%3A1%2C0_263835%3A1%2C0_263839%3A1%2C0_263843%3A1%2C0_268773%3A1%2C0_268777%3A1%2C0_224038%3A1%2C0_263826%3A1%2C0_263830%3A1%2C0_263834%3A1%2C0_263838%3A1%2C0_268772%3A1%2C0_263842%3A1%2C0_263829%3A1%2C0_263833%3A1%2C0_263837%3A1%2C0_263292%3A1%2C0_263841%3A1%2C0_268771%3A1&consentId=61e45c1e-77a9-414d-8432-fd89a4b20575&AwaitingReconsent=false; _vwo_sn=0%3A6%3A%3A%3A1; _uetsid=9baee920169f11ecb2033115ddab655c; _uetvid=9bb06660169f11ec8868995204769a69; _gat=1; _biz_nA=50; _biz_pendingA=%5B%22m%2Fblr%3Fe%3DsqGQFYB9WwcHq%252FX6lLc9F7AgGHBLcTdZFq0ehN6ILEhw%252FFqnXDRUFCmcfTujd%252FtIC%252B18sZmtvN%252F%252BYiXuesSkt6t%252BGq%252BfXT9iXAyNwZ1Bl5dmxt6XNCI2or7cn0y9veS2zq5ioPF95Gbu3Mk2exWd0J9fLtRjcNs6YTIvap4ECOA%253D%26frm_c%3D-1955448038%26eMail%3Ddsfdfdsfdfdsf%2540gmail.com%26eventSource%3DonClick-Button%26rnd%3Dba40548024594471bb0e7f2e71fcb67c%26_biz_u%3D07537b0f05734e6795dddd255832c1b5%26_biz_s%3D2a927e%26_biz_l%3Dhttps%253A%252F%252Fpantheon.io%252Fregister%26_biz_t%3D1631765171511%26_biz_i%3DRegister%2520%257C%2520Pantheon%26_biz_n%3D47%22%2C%22m%2Ffrm%3Fe%3DsqGQFYB9WwcHq%252FX6lLc9F7AgGHBLcTdZFq0ehN6ILEhw%252FFqnXDRUFCmcfTujd%252FtIC%252B18sZmtvN%252F%252BYiXuesSkt6t%252BGq%252BfXT9iXAyNwZ1Bl5dmxt6XNCI2or7cn0y9veS2zq5ioPF95Gbu3Mk2exWd0J9fLtRjcNs6YTIvap4ECOA%253D%26eMail%3Ddsfdfdsfdfdsf%2540gmail.com%26eventSource%3DAjaxIntercept%26rnd%3Dba40548024594471bb0e7f2e71fcb67c%26_biz_u%3D07537b0f05734e6795dddd255832c1b5%26_biz_s%3D2a927e%26_biz_l%3Dhttps%253A%252F%252Fpantheon.io%252Fregister%26_biz_t%3D1631765171652%26_biz_i%3DRegister%2520%257C%2520Pantheon%26_biz_n%3D48%22%2C%22m%2Ffrm%3Fe%3DsqGQFYB9WwcHq%252FX6lLc9F7AgGHBLcTdZFq0ehN6ILEhw%252FFqnXDRUFCmcfTujd%252FtIC%252B18sZmtvN%252F%252BYiXuesSkt6t%252BGq%252BfXT9iXAyNwZ1Bl5dmxt6XNCI2or7cn0y9veS2zq5ioPF95Gbu3Mk2exWd0J9fLtRjcNs6YTIvap4ECOA%253D%26frm_c%3D-1955448038%26eMail%3Ddsfdfdsfdfdsf%2540gmail.com%26eventSource%3DsubmitJQ%26rnd%3Dba40548024594471bb0e7f2e71fcb67c%26_biz_u%3D07537b0f05734e6795dddd255832c1b5%26_biz_s%3D2a927e%26_biz_l%3Dhttps%253A%252F%252Fpantheon.io%252Fregister%26_biz_t%3D1631765171842%26_biz_i%3DRegister%2520%257C%2520Pantheon%26_biz_n%3D49%22%5D',
            'Host': 'dashboard.pantheon.io',
            'Origin': 'https://pantheon.io',
            'Pragma': 'no-cache',
            'Referer': 'https://pantheon.io/',
            'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': "Windows",
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-site',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',             
        }
        rand = str(''.join(random.choice("zxcvbnmasdfghjklqwertyuiop1234567890")for i in range(10)))
        data = {
            'pda_campaign':'{}',
            'firstname': 'Ibrahem',
            'lastname': 'ALkabby',
            'company': 'raple',
            'title': '{}',
            'email':f'{rand}@emailnax.com',
            'password': 'FN#kC_GdkecH6ja',
            'agency': 'agency',
            'edu': 'edu',
            'tos': 'tos',
            '_csrf': 'bl25T4Su-VrvpiI0Pjme3ObuIig4Q08ZrdNs',
                }
        R = requests.post(url,headers=head,data=data)
        weblogin = "<a href='https://pantheon.auth0.com/login?state=hKFo2SBKblczb3JaS3V6RHBTdnRUME5SbWdaMXFkRnVQaVljUKFupWxvZ2luo3RpZNkgU3M4S3B6YTJlUGRQaU1GRUNlaTJ3aDlfR1VDbU1mV06jY2lk2SBxOWZXajl4blB4NE9BQVk5SU5ZZGNmaVlJVGtHdmFIcg&client=q9fWj9xnPx4OAAY9INYdcfiYITkGvaHr&protocol=oauth2&response_type=code&redirect_uri=https%3A%2F%2Fdashboard.pantheon.io%2Fauth%2Fcallback&scope=login%20openid%20pantheon&connection='>تسجيل الدخول</a>"
        bot.send_message(chat_id=call.message.chat.id,text=f'''
=================================================
彡 𝗘𝗠𝗔𝗜𝗟 ❥ <code>{rand}@emailnax.com</code>
彡 𝗣𝗔𝗦𝗦𝗪𝗢𝗥𝗗 ❥ <code>FN#kC_GdkecH6ja</code>
彡 𝗪𝗘𝗕𝗦𝗜𝗧𝗘 ❥ {weblogin}
=================================================
اضغط للنسخ

''',parse_mode='html')
    elif call.data == "ptmail":
        bot.edit_message_text(chat_id=(call.message.chat.id),message_id=(call.message.id),text="قم برسال الايميل")
        @bot.message_handler(func=(lambda message:True))
        def prmessage(message):
            if message.text:
                pthead = {
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',
                    'Cache-Control': 'no-cache',
                    'Connection': 'keep-alive',
                    'Content-Length': '199',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Cookie': '_ga=GA1.2.1442978344.1631760627; _gid=GA1.2.801729137.1631760627; __utmc=97458314; __utmz=97458314.1631760627.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _mkto_trk=id:316-GSV-089&token:_mch-dashboard.pantheon.io-1631760627584-29222; ajs_anonymous_id=%22fcf4b685-5a66-43f6-b3d5-6278cba8fcdf%22; pantheon_tracking=%7B%22utm_source%22%3A%22No%20UTM%22%2C%22utm_medium%22%3A%22No%20UTM%22%2C%22utm_device%22%3A%22No%20UTM%22%2C%22utm_content%22%3A%22No%20UTM%22%2C%22utm_campaign%22%3A%22No%20UTM%22%2C%22utm_term%22%3A%22No%20UTM%22%2C%22utm_ad_group_name%22%3A%22No%20UTM%22%2C%22dtl%22%3A%22%22%2C%22referrer_url%22%3A%22%22%7D; pantheon_tracking=%7B%22utm_source%22%3A%22No%20UTM%22%2C%22utm_medium%22%3A%22No%20UTM%22%2C%22utm_device%22%3A%22No%20UTM%22%2C%22utm_content%22%3A%22No%20UTM%22%2C%22utm_campaign%22%3A%22No%20UTM%22%2C%22utm_term%22%3A%22No%20UTM%22%2C%22utm_ad_group_name%22%3A%22No%20UTM%22%2C%22dtl%22%3A%22%22%2C%22referrer_url%22%3A%22%22%7D; __utma=97458314.1442978344.1631760627.1631760627.1631763283.2; OptanonAlertBoxClosed=2021-09-16T03:35:41.701Z; _vwo_uuid_v2=D85586077E6C3CC18432718487186C7FF|db298eece003160e44d7fe53c2338d53; _vis_opt_s=1%7C; _vis_opt_test_cookie=1; _vwo_uuid=D85586077E6C3CC18432718487186C7FF; _vwo_ds=3%241631763524%3A1.13392115%3A%3A; _mkto_trk=id:316-GSV-089&token:_mch-pantheon.io-1631763528037-90938; _biz_sid=2a927e; _fbp=fb.1.1631763533718.266134017; _biz_uid=07537b0f05734e6795dddd255832c1b5; intercom-id-xkegk7cr=86cffc78-56ca-4239-9750-aefa9bb43ff3; intercom-session-xkegk7cr=; OptanonAlertBoxClosed=2021-09-16T03:39:16.803Z; _biz_flagsA=%7B%22Version%22%3A1%2C%22Mkto%22%3A%221%22%2C%22ViewThrough%22%3A%221%22%2C%22XDomain%22%3A%221%22%2C%22Frm%22%3A%221%22%7D; _vis_opt_exp_135_combi=1; _vis_opt_exp_141_combi=2; _vis_opt_exp_116_combi=2; _vis_opt_exp_116_goal_210=1; _biz_ABTestA=%5B1054094750%5D; _vis_opt_exp_141_goal_200=1; _vis_opt_exp_135_goal_200=1; _vis_opt_exp_116_goal_200=1; _vis_opt_exp_141_goal_212=1; _vis_opt_exp_135_goal_212=1; _vis_opt_exp_116_goal_212=1; _vis_opt_exp_141_goal_213=1; _vis_opt_exp_135_goal_213=1; _vis_opt_exp_116_goal_213=1; _csrf=eOFR7mv0u3d1sWGlWFzFQ1nK; __utmt=1; __utmb=97458314.4.10.1631763283; OptanonConsent=isIABGlobal=false&datestamp=Thu+Sep+16+2021+07%3A05%3A05+GMT%2B0300+(%D8%A7%D9%84%D8%AA%D9%88%D9%82%D9%8A%D8%AA+%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A+%D8%A7%D9%84%D8%B1%D8%B3%D9%85%D9%8A)&version=6.0.0&landingPath=NotLandingPage&groups=0_224028%3A1%2C1%3A1%2C2%3A1%2C0_224029%3A1%2C3%3A1%2C0_224030%3A1%2C0_224031%3A1%2C4%3A1%2C0_224032%3A1%2C0_224034%3A1%2C0_224036%3A1%2C0_224037%3A1%2C0_224039%3A1%2C0_224040%3A1%2C0_224041%3A1%2C0_224042%3A1%2C0_224043%3A1%2C0_224044%3A1%2C0_224045%3A1%2C0_224046%3A1%2C0_224047%3A1%2C0_263828%3A1%2C0_263832%3A1%2C0_224048%3A1%2C0_263836%3A1%2C0_263840%3A1%2C0_264785%3A1%2C0_263827%3A1%2C0_263831%3A1%2C0_224035%3A1%2C0_268794%3A1%2C0_263835%3A1%2C0_263839%3A1%2C0_263843%3A1%2C0_268773%3A1%2C0_268777%3A1%2C0_224038%3A1%2C0_263826%3A1%2C0_263830%3A1%2C0_263834%3A1%2C0_263838%3A1%2C0_268772%3A1%2C0_263842%3A1%2C0_263829%3A1%2C0_263833%3A1%2C0_263837%3A1%2C0_263292%3A1%2C0_263841%3A1%2C0_268771%3A1&consentId=61e45c1e-77a9-414d-8432-fd89a4b20575&AwaitingReconsent=false; OptanonConsent=isIABGlobal=false&datestamp=Thu+Sep+16+2021+07%3A05%3A41+GMT%2B0300+(%D8%A7%D9%84%D8%AA%D9%88%D9%82%D9%8A%D8%AA+%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A+%D8%A7%D9%84%D8%B1%D8%B3%D9%85%D9%8A)&version=6.7.0&landingPath=NotLandingPage&groups=0_224028%3A1%2C1%3A1%2C2%3A1%2C0_224029%3A1%2C3%3A1%2C0_224030%3A1%2C0_224031%3A1%2C4%3A1%2C0_224032%3A1%2C0_224034%3A1%2C0_224036%3A1%2C0_224037%3A1%2C0_224039%3A1%2C0_224040%3A1%2C0_224041%3A1%2C0_224042%3A1%2C0_224043%3A1%2C0_224044%3A1%2C0_224045%3A1%2C0_224046%3A1%2C0_224047%3A1%2C0_263828%3A1%2C0_263832%3A1%2C0_224048%3A1%2C0_263836%3A1%2C0_263840%3A1%2C0_264785%3A1%2C0_263827%3A1%2C0_263831%3A1%2C0_224035%3A1%2C0_268794%3A1%2C0_263835%3A1%2C0_263839%3A1%2C0_263843%3A1%2C0_268773%3A1%2C0_268777%3A1%2C0_224038%3A1%2C0_263826%3A1%2C0_263830%3A1%2C0_263834%3A1%2C0_263838%3A1%2C0_268772%3A1%2C0_263842%3A1%2C0_263829%3A1%2C0_263833%3A1%2C0_263837%3A1%2C0_263292%3A1%2C0_263841%3A1%2C0_268771%3A1&consentId=61e45c1e-77a9-414d-8432-fd89a4b20575&AwaitingReconsent=false; _vwo_sn=0%3A6%3A%3A%3A1; _uetsid=9baee920169f11ecb2033115ddab655c; _uetvid=9bb06660169f11ec8868995204769a69; _gat=1; _biz_nA=50; _biz_pendingA=%5B%22m%2Fblr%3Fe%3DsqGQFYB9WwcHq%252FX6lLc9F7AgGHBLcTdZFq0ehN6ILEhw%252FFqnXDRUFCmcfTujd%252FtIC%252B18sZmtvN%252F%252BYiXuesSkt6t%252BGq%252BfXT9iXAyNwZ1Bl5dmxt6XNCI2or7cn0y9veS2zq5ioPF95Gbu3Mk2exWd0J9fLtRjcNs6YTIvap4ECOA%253D%26frm_c%3D-1955448038%26eMail%3Ddsfdfdsfdfdsf%2540gmail.com%26eventSource%3DonClick-Button%26rnd%3Dba40548024594471bb0e7f2e71fcb67c%26_biz_u%3D07537b0f05734e6795dddd255832c1b5%26_biz_s%3D2a927e%26_biz_l%3Dhttps%253A%252F%252Fpantheon.io%252Fregister%26_biz_t%3D1631765171511%26_biz_i%3DRegister%2520%257C%2520Pantheon%26_biz_n%3D47%22%2C%22m%2Ffrm%3Fe%3DsqGQFYB9WwcHq%252FX6lLc9F7AgGHBLcTdZFq0ehN6ILEhw%252FFqnXDRUFCmcfTujd%252FtIC%252B18sZmtvN%252F%252BYiXuesSkt6t%252BGq%252BfXT9iXAyNwZ1Bl5dmxt6XNCI2or7cn0y9veS2zq5ioPF95Gbu3Mk2exWd0J9fLtRjcNs6YTIvap4ECOA%253D%26eMail%3Ddsfdfdsfdfdsf%2540gmail.com%26eventSource%3DAjaxIntercept%26rnd%3Dba40548024594471bb0e7f2e71fcb67c%26_biz_u%3D07537b0f05734e6795dddd255832c1b5%26_biz_s%3D2a927e%26_biz_l%3Dhttps%253A%252F%252Fpantheon.io%252Fregister%26_biz_t%3D1631765171652%26_biz_i%3DRegister%2520%257C%2520Pantheon%26_biz_n%3D48%22%2C%22m%2Ffrm%3Fe%3DsqGQFYB9WwcHq%252FX6lLc9F7AgGHBLcTdZFq0ehN6ILEhw%252FFqnXDRUFCmcfTujd%252FtIC%252B18sZmtvN%252F%252BYiXuesSkt6t%252BGq%252BfXT9iXAyNwZ1Bl5dmxt6XNCI2or7cn0y9veS2zq5ioPF95Gbu3Mk2exWd0J9fLtRjcNs6YTIvap4ECOA%253D%26frm_c%3D-1955448038%26eMail%3Ddsfdfdsfdfdsf%2540gmail.com%26eventSource%3DsubmitJQ%26rnd%3Dba40548024594471bb0e7f2e71fcb67c%26_biz_u%3D07537b0f05734e6795dddd255832c1b5%26_biz_s%3D2a927e%26_biz_l%3Dhttps%253A%252F%252Fpantheon.io%252Fregister%26_biz_t%3D1631765171842%26_biz_i%3DRegister%2520%257C%2520Pantheon%26_biz_n%3D49%22%5D',
                    'Host': 'dashboard.pantheon.io',
                    'Origin': 'https://pantheon.io',
                    'Pragma': 'no-cache',
                    'Referer': 'https://pantheon.io/',
                    'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': "Windows",
                    'Sec-Fetch-Dest': 'document',
                    'Sec-Fetch-Mode': 'navigate',
                    'Sec-Fetch-Site': 'same-site',
                    'Sec-Fetch-User': '?1',
                    'Upgrade-Insecure-Requests': '1',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',             
                }

                ptdata = {
                    'pda_campaign':'{}',
                    'firstname': 'Ibrahem',
                    'lastname': 'ALkabby',
                    'company': 'raple',
                    'title': '{}',
                    'email':f'{message.text}',
                    'password': 'FN#kC_GdkecH6ja',
                    'agency': 'agency',
                    'edu': 'edu',
                    'tos': 'tos',
                    '_csrf': 'bl25T4Su-VrvpiI0Pjme3ObuIig4Q08ZrdNs',
                }
                pturl = 'https://dashboard.pantheon.io/register'
                R = requests.post(pturl,headers=pthead,data=ptdata)
                weblogin = "<a href='https://pantheon.auth0.com/login?state=hKFo2SBKblczb3JaS3V6RHBTdnRUME5SbWdaMXFkRnVQaVljUKFupWxvZ2luo3RpZNkgU3M4S3B6YTJlUGRQaU1GRUNlaTJ3aDlfR1VDbU1mV06jY2lk2SBxOWZXajl4blB4NE9BQVk5SU5ZZGNmaVlJVGtHdmFIcg&client=q9fWj9xnPx4OAAY9INYdcfiYITkGvaHr&protocol=oauth2&response_type=code&redirect_uri=https%3A%2F%2Fdashboard.pantheon.io%2Fauth%2Fcallback&scope=login%20openid%20pantheon&connection='>تسجيل الدخول</a>"
                bot.send_message(chat_id=message.chat.id,text=f'''
=================================================
彡 𝗘𝗠𝗔𝗜𝗟 ❥ <code>{message.text}</code>
彡 𝗣𝗔𝗦𝗦𝗪𝗢𝗥𝗗 ❥ <code>FN#kC_GdkecH6ja</code>
彡 𝗪𝗘𝗕𝗦𝗜𝗧𝗘 ❥ {weblogin}
=================================================
اضغط للنسخ

''',parse_mode='html')
if __name__ == "__main__":
    bot.polling(none_stop=True)
