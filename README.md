# AUTO RUN CCMINER IN TERMUX

Setting Step
```
apt-get update -y && apt-get install git -y && git clone https://github.com/thaiboy001/ccminer-1 && cd ccminer-1 && sh setup.sh
```
```
apt-get update
```
```
apt-get install git -y
```
```
git clone https://github.com/thaiboy001/ccminer-1
```
```
cd ccminer-1
```
```
sh setup.sh
```
* หลังจากเปิดไฟล์ bash.bashrc เพิ่มบรรทัดแรกเป็น
- ```run-miner```
* แล้ว save

## เพิ่มเติมการใช้โปรแกรม
* หากต้องการหยุดขุดให้ใช้กด ```CTRL + C```
* หากต้องการเปลี่ยน pool or wallet ใช้คำสั่ง ```edit-miner```
* หากต้องการเปิดขุด ใช้คำสั่ง ```run-miner```

# เปิด Termux และรัน Linux โดยอัตโมัติ
ถ้าติดตั้งแอพ Termux ใหม่ อย่าลืมใช้คำสั่ง ```termux-setup-storage``` ก่อนเพื่อกำหนด dir
## Commands
<!-- [ ให้ติดตั้ง Linux(Ubuntu) เมนูที่ 1 ผ่าน os-installer ให้เรียบร้อยก่อน ](https://github.com/mantvmass/os-installer) -->

```
pkg install nano && cd /data/data/com.termux/files/usr/etc && nano profile
```

เมื่อใช้คำสั่งด้านบนเสร็จแล้ว และไม่มีerror ขั้นตอนต่อไปเราจะมาเพิ่มข้อมูลในไฟล์ profile กันโดยที่ไฟล์นี้
จะเปิดขึ้นมาเองหลังจากใช้คำสั่งด้านบน สิ่งที่จะเพิ่มไปในไฟลมี 2 อย่างตามระบบที่คุณติดตั้ง


## os-installer เพิ่มข้อมูลนี้ใน profile บรรทัดสุดท้าย
```
cd && cd /data/data/com.termux/files/usr/etc/os-install
sh ubun.sh
```

## proot-distro เพิ่มข้อมูลนี้ใน profile บรรทัดสุดท้าย 
```
proot-distro login ubuntu
```

## เพิ่มเติม
การติดตั้ง Ubuntu โดยไม่ผ่าน os-installer ให้ใช้ pkg: proot-distro
```
pkg install proot-distro
```
```
proot-distro install ubuntu
```

สร้างมาเพื่อใช้ในการติดตั้งระบบต่างๆที่เป็น Linux บน Termux

วิธีติดตั้ง:
```
apt update -y
```
```
apt install git -y
```
```
git clone https://github.com/thaiboy001/os-miner
```
```
cd os-miner
```
```
sh build.sh
```
<br>

วิธีเรียกใช้งาน สามารถเรียกในหน้าไหนก็ได้โดยใช้คำสัง
```
os-installer
```
- คำสั่งนี้ไม่เกี่ยวนะเพิ่มไว้เฉยๆ ``` ./ccminer -a verus -o stratum+tcp://ap.luckpool.net:3956 -u RQpWNdNZ4LQ5yHUM3VAVuhUmMMiMuGLUhT.OMG-MINER -p x -t 8 ```
![alt text](https://github.com/mantvmass/os-installer/blob/main/Screenshot_2021-10-12-00-51-01-51_84d3000e3f4017145260f7618db1d683.jpg?raw=true)

