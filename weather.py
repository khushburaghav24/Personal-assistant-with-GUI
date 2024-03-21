# https://search.yahoo.com/search?fr=weather+patna
# user agent : Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36
# id = <div class="imperial-metric fz-50 lh-40 pr-2" data-metric="31" data-imperial="88">88</div>


from requests_html import HTMLSession
import  speech_to_text

def weather():
    s = HTMLSession()
    query = "patan"
    url = f'https://search.yahoo.com/search?fr=weather+patna'
    r = s.get(url, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'})
    temp  = r.html.find('span#wob_tm' , first= True).text
    unit = r.html.find('div.vk_bk.wob-unit span.wob_t' , first= True).text
    desc  = r.html.find('span#wob_dc' , first= True).text
    return temp+" " + unit+" "+ desc
