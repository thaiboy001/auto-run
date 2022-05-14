# 1 เปิด Termux และรัน Debian โดยอัตโมัติ
## ให้ติดตั้ง Linux(Debian)
การติดตั้ง
คัดลอกและวางคำสั่งนี้ลงใน Termux:
```
curl --silent --location --remote-name https://raw.githubusercontent.com/trungtai33/debian-bullseye-in-termux/master/install.sh; bash install.sh; rm install.sh
```
# 2 รัน Debian โดยอัตโมัติ
```
pkg install nano && cd /data/data/com.termux/files/usr/etc && nano profile
```
เมื่อใช้คำสั่งด้านบนเสร็จแล้ว และไม่มีerror ขั้นตอนต่อไปเราจะมาเพิ่มข้อมูลในไฟล์ profile กันโดยที่ไฟล์นี้
จะเปิดขึ้นมาเองหลังจากใช้คำสั่งด้านบน สิ่งที่จะเพิ่มไปตามระบบที่คุณติดตั้ง
Linux(Debian) เพิ่มข้อมูลนี้ใน profile บรรทัดสุดท้าย
```
start-debian-bullseye
```
จบขั้นตอน เปิด Termux และรัน Debian โดยอัตโมัติ
# 3 AUTO รัน CCMINER ใน TERMUX -- mantvmass --
แบบเร็ว
```
apt-get update -y && apt-get install git -y && git clone https://github.com/thaiboy001/ccminer-1 && cd ccminer-1 && sh setup.sh
```
แบบทีล่ะคําสั่ง
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
หลังจากเปิดไฟล์ bash.bashrc เพิ่มบรรทัดแรกเป็น
```
run-miner
```
## pool
```
luckpool
```
stratum+tcp://ap.luckpool.net:3956
```
zergpool
```
stratum+tcp://verushash.asia.mine.zergpool.com:3300
```
zpool
```
stratum+tcp://heavyhash.sea.mine.zpool.ca:5138
```
แล้ว save
```
## เพิ่มเติมการใช้โปรแกรม
* หากต้องการหยุดขุดให้ใช้กด ```CTRL + C```
* หากต้องการเปลี่ยน pool or wallet ใช้คำสั่ง ```edit-miner```
* หากต้องการเปิดขุด ใช้คำสั่ง ```run-miner```
```
