# AUTO รัน CCMINER ใน TERMUX

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
```
run-miner
```
* แล้ว save

## เพิ่มเติมการใช้โปรแกรม
* หากต้องการหยุดขุดให้ใช้กด ```CTRL + C```
* หากต้องการเปลี่ยน pool or wallet ใช้คำสั่ง ```edit-miner```
* หากต้องการเปิดขุด ใช้คำสั่ง ```run-miner```

# เปิด Termux และรัน (Debian โดยอัตโมัติ

## 1.ให้ติดตั้ง Linux(Debian)
## การติดตั้ง
4
คัดลอกและวางคำสั่งนี้ลงใน Termux:
5
```
6
curl --silent --location --remote-name https://raw.githubusercontent.com/trungtai33/debian-bullseye-in-termux/master/install.sh; ทุบตี install.sh; rm install.sh
7
```
8
วิธีเรียกใช้```start-debian-bullseye```เพื่อเข้าสู่ระบบ
9
## ถอนการติดตั้ง
10
ใช้ความระมัดระวังเมื่อใช้คำสั่งนี้เนื่องจากจะไม่ขอคำยืนยัน
11
```
12
curl --silent --location --remote-name https://raw.githubusercontent.com/trungtai33/debian-bullseye-in-termux/master/uninstall.sh; bash uninstall.sh; rm ถอนการติดตั้ง.sh
13
```
# รัน Debian โดยอัตโมัติ

```
pkg install nano && cd /data/data/com.termux/files/usr/etc && nano profile
```

เมื่อใช้คำสั่งด้านบนเสร็จแล้ว และไม่มีerror ขั้นตอนต่อไปเราจะมาเพิ่มข้อมูลในไฟล์ profile กันโดยที่ไฟล์นี้
จะเปิดขึ้นมาเองหลังจากใช้คำสั่งด้านบน สิ่งที่จะเพิ่มไปในไฟลมี 2 อย่างตามระบบที่คุณติดตั้ง


## Linux(Debian) เพิ่มข้อมูลนี้ใน profile บรรทัดสุดท้าย
```
start-debian-bullseye
```
จบขั้นตอน เปิด Termux และรัน (Debian โดยอัตโมัติ
```
```
