# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.17 (default, Dec  5 2019, 10:47:43) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
from urllib2 import *
from os import system
import requests, sys
from socket import gethostbyname as wongedan
i = '\x1b[92m'
n = '\x1b[0m'

def one():
    zx = raw_input('\x1b[96mmasukan site > \x1b[92m')
    print '\x1b[94mplease wait proses...\x1b[0m'
    trans = wongedan(zx)
    api = 'http://api.hackertarget.com/dnslookup/?q=' + trans
    yopie = urlopen(api).read()
    print '\n\x1b[92mresult\x1b[0m :\n'
    print '=' * 50
    print i + yopie + n
    print '=' * 50


def two():
    zx = raw_input('\x1b[96mmasukan site > \x1b[92m')
    print '\x1b[94mplease wait proses...\x1b[0m'
    trans = wongedan(zx)
    api = 'http://api.hackertarget.com/whois/?q=' + trans
    yopie = urlopen(api).read()
    print '\n\x1b[92mresult\x1b[0m :\n'
    print '=' * 50
    print i + yopie + n
    print '=' * 50


def tiga():
    zx = raw_input('\x1b[96mmasukan site > \x1b[92m')
    print '\x1b[94mplease wait proses...\x1b[0m'
    trans = wongedan(zx)
    api = 'http://api.hackertarget.com/reverseiplookup/?q=' + trans
    yopie = urlopen(api).read()
    print '\n\x1b[92mresult\x1b[0m :\n'
    print '=' * 50
    print i + yopie + n
    print '=' * 50


def four():
    zx = raw_input('\x1b[96mmasukan site > \x1b[92m')
    print '\x1b[94mplease wait proses...\x1b[0m'
    trans = wongedan(zx)
    api = 'http://api.hackertarget.com/geoip/?q=' + trans
    yopie = urlopen(api).read()
    print '\n\x1b[92mresult\x1b[0m :\n'
    print '=' * 50
    print i + yopie + n
    print '=' * 50


def five():
    zx = raw_input('\x1b[96mmasukan site > \x1b[92m')
    print '\x1b[94mplease wait proses...\x1b[0m'
    trans = wongedan(zx)
    api = 'http://api.hackertarget.com/subnetcalc/?q=' + trans
    yopie = urlopen(api).read()
    print '\n\x1b[92mresult\x1b[0m :\n'
    print '=' * 50
    print i + yopie + n
    print '=' * 50


def six():
    zx = raw_input('\x1b[96mmasukan site > \x1b[92m')
    print '\x1b[94mplease wait proses...\x1b[0m'
    trans = wongedan(zx)
    api = 'http://api.hackertarget.com/pagelinks/?q=' + trans
    yopie = urlopen(api).read()
    print '\n\x1b[92mresult\x1b[0m :\n'
    print '=' * 50
    print i + yopie + n
    print '=' * 50


def seven():
    zx = raw_input('\x1b[96mmasukan site > \x1b[92m')
    print '\x1b[94mplease wait proses...\x1b[0m'
    trans = wongedan(zx)
    api = 'http://api.hackertarget.com/nmap/?q=' + trans
    yopie = urlopen(api).read()
    print '\n\x1b[92mresult\x1b[0m :\n'
    print '=' * 50
    print i + yopie + n
    print '=' * 50


def lapan():
    zx = raw_input('\x1b[96mmasukan site > \x1b[92m')
    print '\x1b[94mplease wait proses...\x1b[0m'
    trans = wongedan(zx)
    api = 'http://api.hackertarget.com/zonetransfer/?q=' + trans
    yopie = urlopen(api).read()
    print '\n\x1b[92mresult\x1b[0m :\n'
    print '=' * 50
    print i + yopie + n
    print '=' * 50


def nine():
    zx = raw_input('\x1b[96mmasukan site > \x1b[92m')
    print '\x1b[94mplease wait proses...\x1b[0m'
    trans = wongedan(zx)
    api = 'http://api.hackertarget.com/hostsearch/?q=' + trans
    yopie = urlopen(api).read()
    print '\n\x1b[92mresult\x1b[0m :\n'
    print '=' * 50
    print i + yopie + n
    print '=' * 50


def ten():
    zx = raw_input('\x1b[96mmasukan site > \x1b[92m')
    print '\x1b[94mplease wait proses...\x1b[0m'
    trans = wongedan(zx)
    api = 'http://api.hackertarget.com/mtr/?q=' + trans
    yopie = urlopen(api).read()
    print '\n\x1b[92mresult\x1b[0m :\n'
    print '=' * 50
    print i + yopie + n
    print '=' * 50


def IG():
    zx = raw_input('\x1b[96mmasukan ig target > \x1b[92m')
    print '\x1b[94mplease wait proses...\x1b[0m'
    api = 'https://indosec.web.id/api/ig.php?action=info&username=' + zx
    yopie = requests.get(api)
    print '\n\x1b[92mresult\x1b[0m :\n'
    print '=' * 50
    print i + yopie.content + n
    print '\n\x1b[93mNOTE \x1b[0m: \x1b[92mJIKA INGIN MENYALIN LINK HAPUS TANDA \\ AGAR BISA DIAKSES :)'
    print '=' * 50


def has():
    zx = raw_input('\x1b[96mmasukan text string > \x1b[92m')
    print '\x1b[94mplease wait proses...\x1b[0m'
    api = 'https://indosec.web.id/api/ultra_hash.php?action=enc&value=' + zx
    yopie = requests.get(api)
    print '\n\x1b[92mresult\x1b[0m :\n'
    print '=' * 50
    print i + yopie.content + n
    print '=' * 50


def nasa():
    print '\x1b[94mplease wait proses...\x1b[0m'
    api = 'https://api.nasa.gov/planetary/apod?api_key=NNKOjkoul8n1CH18TWA9gwngW1s1SmjESPjNoUFo'
    yopie = requests.get(api)
    print '\n\x1b[92mresult\x1b[0m :\n'
    print '=' * 50
    print i + yopie.content + n
    print '=' * 50


def shell():
    zx = raw_input('\x1b[96mmasukan url web login > \x1b[92m')
    print '\x1b[94mplease wait proses...\x1b[0m'
    api = 'https://indosec.web.id/api/brute.php?type=shell&url=' + zx
    yopie = requests.get(api)
    print '\n\x1b[92mresult\x1b[0m :\n'
    print '=' * 50
    print i + yopie.content + n
    print '=' * 50


def sock():
    zx = raw_input('\x1b[96mmasukan jumlah socks > \x1b[92m')
    print '\x1b[94mplease wait proses...\x1b[0m'
    api = 'https://indosec.web.id/api/socks.php?type=get&jumlah=' + zx
    yopie = requests.get(api)
    print '\n\x1b[92mresult\x1b[0m :\n'
    print '=' * 50
    print i + yopie.content + n
    print '=' * 50


def laz():
    zx = raw_input('\x1b[96mmasukan email lazada > \x1b[92m')
    print '\x1b[94mplease wait proses...\x1b[0m'
    api = 'https://indosec.web.id/api/checker.php?type=lazada&email=' + zx
    yopie = requests.get(api)
    print '\n\x1b[92mresult\x1b[0m :\n'
    print '=' * 50
    print i + yopie.content + n
    print '=' * 50


def ebay():
    zx = raw_input('\x1b[96mmasukan email ebay > \x1b[92m')
    print '\x1b[94mplease wait proses...\x1b[0m'
    api = 'https://indosec.web.id/api/checker.php?type=ebay&email=' + zx
    yopie = requests.get(api)
    print '\n\x1b[92mresult\x1b[0m :\n'
    print '=' * 50
    print i + yopie.content + n
    print '=' * 50


menu = '\n                        \x1b[93msubtool & IGET\n                        Zone-xploiter\x1b[95m\n                     >coded by Mr.ZOMBY<\x1b[0m\n\n[01].\x1b[94mDNS Lookup\x1b[0m\n[02].\x1b[94mWhois Lookup\x1b[0m\n[03].\x1b[94mReverse IP Lookup\x1b[0m\n[04].\x1b[94mGeoIP Lookup\x1b[0m\n[05].\x1b[94mSubnet Lookup\x1b[0m\n[06].\x1b[94mExtract Link\x1b[0m\n[07].\x1b[94mport scanner\x1b[0m\n[08].\x1b[94mzone transfer\x1b[0m\n[09].\x1b[94mHost finder\x1b[0m\n[10].\x1b[94mMtr Traceroute\x1b[0m\n[11].\x1b[94mchecker profile IG\x1b[0m\n[12].\x1b[94mUltra hash pass\x1b[0m\n[13].\x1b[94minformation from NASA\x1b[0m\n[14].\x1b[94mBrute shell login\x1b[0m\n[15].\x1b[94mGet socks\x1b[0m\n[16].\x1b[94mLazada email checker\x1b[0m\n[17].\x1b[94mebay email checker\x1b[0m\n'