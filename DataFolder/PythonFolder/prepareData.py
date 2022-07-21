
import shutil
import sys
from unittest import suite
from link import removeFiles
import os

# -------- global parameters ------ #

filedate = open("../TextFolder/bigFiles/DayMonthYear.txt", "r",encoding="UTF-8")
DayMonthYear = filedate.readlines()
filedate.close()

# --------------------------------- #

def main():
    if len(sys.argv) == 1:
        print("please, choose type of data, use 1 for global or 2 for specific.")
    elif sys.argv[1] == "1":
        file = open("../TextFolder/bigFiles/globalFile.txt", "r", encoding="UTF-8")
        folder_destination = "../TextFolder/globalData"
    else:
        file = open("../TextFolder/bigFiles/specificFile.txt", "r", encoding="UTF-8")
        folder_destination = "../TextFolder/specificData"

    lines = file.readlines()
    file.close()

    removeFiles(folder_destination)

    i = 1
    startingDate = DayMonthYear.index("2022-05-23 02.22.10\n") #specify where to start for date
    j=0
    test = 0 # create file or not
    test2 = 0 # close or not
    test3 = 0 # writing beginning or not

    print(len(lines))

    for line in lines:
        j = j+1
        if j == len(lines):
            print("ok")
            fichier.close()
            shutil.move("data" + DayMonthYear[startingDate][0:19]  + ".txt", folder_destination) 
            test2 = 1
            test = 0
        if "nan" in line:
            if test2 == 0:
                fichier.close()
                shutil.move("data" + DayMonthYear[startingDate][0:19] + ".txt", folder_destination)
                test2 = 1
                test = 0
                i = i + 1 
                startingDate = startingDate + 1
            else:
                pass 
        else:
            if test == 0:
                fichier = open("data" + DayMonthYear[startingDate][0:19] + ".txt", "a", encoding="UTF-8")
                test = 1
                test2 = 0
                
                if test3 == 1:
                    if sys.argv[1] == "1":
                        fichier.write('[1:36];[1:37];[1:38]')
                        fichier.write('\n')
                        fichier.write('Presskraft_ton;Reglering_%;Stampelhast_mm_per_s')
                        fichier.write('\n')
                    else:
                        fichier.write('[0:0];[0:1];[0:2];[0:3];[0:4];[0:5];[0:6];[0:7];[0:8];[0:9];[0:10];[0:11];[0:12];[0:13];[0:14];[0:15];[0:16];[0:17];[0:18];[0:19];[0:20];[0:21];[0:22];[0:23];[0:24];[0:25];[0:26];[0:27];[0:28];[0:29];[0:30];[0:31];[0:32];[0:33];[0:34];[0:35];[0:36];[0:37];[0:38];[0:41];[0:45];[0:54];[0:67];[0:68];[0:88];[0:89];[0:90];[0:91];[0:102];[0:103];[0:104];[0:111];[0:112];[0:113];[0:114];[0:115];[0:116];[0:117];[0:118];[0.0];[0.1];[0.2];[0.3];[0.4];[0.5];[0.6];[0.7];[0.8];[0.9];[0.10];[0.11];[0.12];[0.13];[0.14];[0.15];[0.16];[0.17];[0.18];[0.20];[0.21];[0.22];[0.23];[0.24];[0.25];[0.26];[0.27];[0.28];[0.29];[0.30];[0.31];[0.32];[0.33];[0.34];[0.35];[0.36];[0.37];[0.38];[0.39];[0.40];[0.41];[0.42];[0.43];[0.44];[0.45];[0.46];[0.47];[0.48];[0.49];[0.50];[0.51];[0.52];[0.53];[0.54];[0.55];[0.56];[0.57];[0.58];[0.59];[0.60];[0.61];[0.62];[0.63];[0.64];[0.65];[0.66];[0.67];[0.68];[0.69];[0.70];[0.71];[0.72];[0.77];[0.79];[0.82];[0.84];[0.89];[0.90];[0.91];[0.92];[0.93];[0.94];[0.95];[0.96];[0.97];[0.98];[0.99];[0.100];[0.101];[0.102];[0.103];[0.120];[0.121];[0.122];[0.125];[0.126];[0.130];[0.131];[0.132];[0.136];[0.138];[0.139];[0.143];[0.146];[0.150];[0.151]')
                        fichier.write('\n')
                        fichier.write('Hcyl regl +U6051-K3.11_bv_promille V27(6530);Hcyl regl  +U6051-K3.11_äv_promille V27(6530);Hcyl grund +U6051-K3.12_bv_promille V28(6540);Hcyl grund +U6051-K3.12_äv_promille V28(6540);Ycyl regl +U6051-K3.13_bv_promille V32(6570);Ycyl regl +U6051-K3.13_äv_promille V32(6570);Ycyl grund +U6051-K3.14_bv_promille V33(6585);Ycyl grund +U6051-K3.14_äv_promille V33(6585);RCyl pref +U6051-K3.15_bv_promille V47(6615);RCyl pref +U6051-K3.15_äv_promille V47(6615);Rcyl pref/HT fram  +U6051-K3.16_bv_promille V48(6635);Rcyl pref/HT fram  +U6051-K3.16_äv_promille V48(6635);Rcyl avl/ht mottr +U6051-K3.17_bv_promille V49(6650);Rcyl avl/ht mottr +U6051-K3.17_äv_promille V49(6650);Först Rcyl;Dorn, dekomp 2:a steg (prop), ÄV ventilläge promille V5(6740);Dorn, fram hast.regl HT (prop), BV ventilläge promille V6(6750);Dorn, fram hast.regl HT (prop), ÄV ventilläge promille V6(6750);Dorn, fram h.regl avlopp / retur HT, BV promille V7(6770);Dorn, fram hast.regl avlopp / retur HT (prop), ÄV ventilläge promille V7(6770);Först Dorn;Stämpels position i mm;Stämpelhastighet;Extr. Hast;Uppmätt presskraft;Hcyl Aktuellt tryck;YCyl Aktuellt tryck;Rcyl Aktuellt tryck;Dorn Aktuellt tryck;Rcyl mottr Aktuellt tryck;Först Hcyl;Nivå Lågtrycksflaska;Dorn, dekomp 2:a steg (prop), BV ventilläge promille (mek 5) (bl.6777);Tryck i lågtrycksflaska;Tryck efter ventil lt flaska;Äc_Slutet Aktuellt tryck;Äc_öppet Aktuellt tryck;Ht flaska Aktuellt tryck;Förstärkning yttercylindrar;Styrtryck dorncylinder;ÄC Position i mm;Tryck dorn returcyl;IDB_Takttid\kyltid_vatten;IDB_Takttid\kyltid_luft;Sagmotorhast;Sagmotormoment;Sagmotorstrom;DB_Såg\saghast_kaphast;DB_HMI_paneler\styrtryck.stampelblock;DB_HMI_paneler\styrtryck.returcylinderblock;DB_HMI_paneler\styrtryck.amnescylinderblock;DB_diag_V49\AI_oppna;DB_diag_V49\AI_stang;DB_diag_V27\AI_oppna;DB_diag_V27\AI_stang;DB_diag_V32\AI_oppna;DB_diag_V32\AI_stang;DB_diag_V6\AI_oppna;DB_diag_V6\AI_stang;Huvudcyl., fram HT (on/off) (mek 21) (bl.6723);Huvudcyl., fram HT (on/off) (mek 23) (bl.6725);Huvudcyl., decomp ventil (on/off) öppna (mek 22) (bl.6722);Huvudcyl., prefillventil (on/off) öppna (mek 29) (bl.6721);Yttercyl., prefillventil öppna (nedre) (on/off) (mek 30) (bl.6736);Yttercyl., prefillventil öppna (övre) (on/off) (mek 31) (bl.6736);Yttercyl., fram HT (on/off) (mek 24) (bl.6738);Yttercyl., fram HT (on/off) (mek 26) (bl.6740);Yttercyl., dekompventil öppna (on/off) (mek 25) (bl.6737);Rcyl, prefillventil (on/off) (mek 41) (bl.6751);Rcyl, dekompventil (on/off) (mek 42) (bl.6753);Rcyl, prefillventil (on/off) (mek 43) (bl.6754);Rcyl, HT (on/off) (mek 44) (bl.6755);Rcyl, stä retur / mottryck HT (on/off) (mek 45) (bl.6757);Rcyl, stä fram avlopp (on/off) (mek 46) (bl.6758);Dorn, fram HT (on/off) (mek 1) (bl.6778);Dorn, dekomp 1:a steg (on/off) (mek 4) (bl.6776);Dorn, retur HT (on/off) (mek 2) (bl.6780);Dorn, fram avlopp (on/off) (mek 3) (bl.6781);Ämnescyl., avstängningsventil (on/off) (mek 137) (bl.6792);Ämnescyl., slut sakta HT (on/off) (mek 61) (bl.6792);Ämnescyl., öppna sakta avlopp (on/off) (mek 62) (bl.6792);Ämnescyl., öppna fort avlopp (on/off) (mek 63) (bl.6792);Ämnescyl., slut sakta avlopp (on/off) (mek 64) (bl.6792);Ämnescyl., öppna fort HT (on/off) (mek 65) (bl.6793);Ämnescyl., öppna sakta HT (on/off) (mek 66) (bl.6792);Lågtrycksflaska, dräneringsventil lågtryck press (bl.6682);Dorn, prefillventil öppna (mek 80) (bl.6774);Huvudcyl., decomp ventil öppen (bl.6722);Huvudcyl., decomp ventil stängd (bl.6722);Lågtrycksflaska, avtappning lt-flaska (bl.6680);Lågtrycksflaska, lågtrycksventil (bl.6681);Ämnescyl., avstängningsventil (on/off) öppen (bl.6792);Ämnescyl., avstängningsventil (on/off) stängd (bl.6792);Ämnescyl., sluter sakta ventil stängd (bl.6794);Ämnescyl., öppna fort ventil stängd (bl.6793);Ämnescyl., öppna sakta ventil stängd (bl.6793);Rcyl, stä fram avlopp (on/off) öppen (bl.6758);Rcyl, stä fram avlopp (on/off) stängd (bl.6758);Rcyl, stä retur / mottryck HT (on/off) öppen (bl.6757);Rcyl, stä retur / mottryck HT (on/off) stängd (bl.6757);Rcyl, HT (on/off) öppen (bl.6755);Rcyl, HT (on/off) stängd (bl.6755);Rcyl, prefillventil (on/off) öppen (bl.6754);Rcyl, prefillventil (on/off) stängd (bl.6754);Rcyl, dekompventil (on/off) öppen (bl.6753);Rcyl, dekompventil (on/off) stängd (bl.6753);Rcyl, prefillventil (on/off) öppen (bl.6751);Rcyl, prefillventil (on/off) stängd (bl.6751);Yttercyl., dekompventil öppen (bl.6737);Yttercyl., dekompventil stängd (bl.6737);Yttercyl., fram HT (on/off) öppen (bl.6740);Yttercyl., fram HT (on/off) stängd (bl.6740);Yttercyl., fram HT (on/off) öppen (bl.6738);Yttercyl., fram HT (on/off) stängd (bl.6738);Huvudcyl., fram HT (on/off) öppen (bl.6725);Huvudcyl., fram HT (on/off) stängd (bl.6725);Huvudcyl., fram HT (on/off) öppen (bl.6723);Huvudcyl., fram HT (on/off) stängd (bl.6723);Dorn, fram avlopp (on/off), öppen (bl.6781);Dorn, fram avlopp (on/off), stängd (bl.6781);Dorn, retur HT (on/off), öppen (bl.6780);Dorn, retur HT (on/off), stängd (bl.6780);Dorn, dekomp 1:a steg (on/off), öppen (bl.6776);Dorn, dekomp 1:a steg (on/off), stängd (bl.6776);Dorn, fram HT (on/off), öppen (bl.6778);Dorn, fram HT (on/off), stängd (bl.6778);Dorn, prefillventil öppen? (bl.6774);Lågtrycksflaska, lågtrycksventil stängd (bl.6681);Lågtrycksflaska, lågtrycksventil öppen (bl.6681);Lågtrycksflaska, dräneringsventil lågtryck press öppen (bl.6682);Lågtrycksflaska, dräneringsventil lågtryck press stängd (bl.6682);Ämnescylinder tätad;Ämnescylinder slutet läge;hast_reglering_till;indikering högtryck till;Högtr.avst., huvudtryck > 250 bar (bl.6692);Högtr.avst., huvudtryck < 10 bar (bl.6692);Högtr.avst., huvudventil öppen (bl.6693);Högtr.avst., huvudventil stängd (gränsläge) (bl.6693);Högtr.avst., huvudventil stängd (tryckvakt) (bl.6693);Högtr.avst., utjämning över huvudventil (bl.6692);Högtr.avst., dränering huvudtryck (bl.6692);Högtr.avst., huvudventil öppna (bl.6693);Högtr.avst., huvudventil stäng (bl.6693);Högtr.avst., styrtryck (bl.6691);Högtr.avst., dränering styrtryck (bl.6691);Högtr.avst., styrtrycksventil öppen (gränsläge) (bl.6691);Högtr.avst., styrtrycksventil stängd (gränsläge) (bl.6691);Högtr.avst., styrtryck > 250 bar (bl.6691);Högtr.avst., styrtryck <10 bar (bl.6691);Stämpel bakre läget;Dorn, i bakre läge (bl.6775);Dorn, i främre läge (bl.6775);hast_stiger;hast_sjunker_oppna_extr;Dorn, avsaktning bakre läge (bl.6775);Dorn, avsaktning främre läge (bl.6775);Revolver, stickerläge 2 (bl.6822);Stämpel tillåt högtryck;backning_klar;backning;Manuellt eller auto;Ämnescylinder borstläge;Ämnescylinder stopp fram vid stansning;Ämnescylinder slut sakta')
                        fichier.write('\n')
                        
                fichier.write(line)
                fichier.write('\n')
                test3 = 1
            else :
                fichier.write(line)
                fichier.write('\n')
        


if __name__ == "__main__":
    main()

    test=os.listdir("./")
    for item in test:
        if item.endswith(".txt"):
            os.remove(item)
            