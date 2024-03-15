import json,re,time,random
import requests
import ddddocr
from datetime import datetime
from beepy import beep
from wakepy import keep

class KVR():

    @staticmethod
    def get_frame_url():
        return 'https://terminvereinbarung.muenchen.de/abh/termin/'
    
    @staticmethod
    def get_capchaimg_url():
        return 'https://terminvereinbarung.muenchen.de/abh/securimage/securimage_show.php'


def get_termins(buro):

    # Session is required to keep cookies between requests
    s = requests.Session()
    
    # First request to get and save cookies
    first_page = s.get(buro.get_frame_url())
    try:
        token = re.search('FRM_CASETYPES_token" value="(.*?)"', first_page.text).group(1)
    except AttributeError:
        token = None
    # print(token)

    # image OCR
    captcha_response = s.get(buro.get_capchaimg_url(), verify=False)
    ocr = ddddocr.DdddOcr(show_ad=False)    
    code = ocr.classification(captcha_response.content)
    # print(code)
    
    termin_data = {
        'CASETYPES[Notfalltermin UA 35]': 1,
        'step': 'WEB_APPOINT_SEARCH_BY_CASETYPES',
        'FRM_CASETYPES_token': token,
        'captcha_code': code
    }
    response = s.post(buro.get_frame_url(), termin_data)
    txt = response.text
    json_str = re.search('jsonAppoints = \'(.*?)\'', txt).group(1)
    appointments = json.loads(json_str)

    return appointments

def now():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


if __name__ == '__main__':    
    
    print('Sound test, please adjust your computer volume')
    try:
        beep(sound='ping')
    except Exception as e:
        print(e)
    print('Start monitoring...')

    available_last_time = False

    with keep.running() as k:
        while True:
            #try captcha, gap 1-2 second
            while True:
                try:  
                    appointment_data = get_termins(KVR)
                except AttributeError:
                    # print('Fail to identify the captcha, automatically proceed to another try')
                    #Caution with time setting!
                    time.sleep(random.randint(1,2))
                    continue
                break
            
            available = False
            appointments = appointment_data['LOADBALANCER']['appoints']
            # print(appointments)
            
            for day in appointments:
                if len(appointments[day]):
                    try:
                        beep(sound='ping')
                    except Exception as e:
                        print(e)
                    print(f'\n{now()} | Termin available on {day}!', end='')
                    with open('log.txt', 'a') as f:
                        f.write(f'{now()}\n')

                    #Bool available kept for further application
                    available = True
                    break
            
            if not available:
                if available_last_time:
                    print(f'\n\r{now()} | No Termin available...', end='')
                else:
                    print(f'\r{now()} | No Termin available...', end='')
                
                available_last_time = False
            else:
                available_last_time = True

            #Caution with time setting!
            time.sleep(random.randint(1,2))        

