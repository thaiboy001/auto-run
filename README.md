## 1 เปิด Termux และรัน ubuntu โดยอัตโมัติ แก้ลงไม่ผ่าน 31/05/65
### ให้ติดตั้ง Linux (ubuntu) หรือ (debian) *เลือกลงอย่างใดอย่างหนึ่ง
การติดตั้ง
ถ้าติดตั้งแอพ Termux ใหม่ อย่าลืมใช้คำสั่ง ```termux-setup-storage``` ก่อนเพื่อกำหนด dir
```
termux-setup-storage
```
คัดลอกและวางคำสั่งนี้ลงใน Termux:
* แบบเร็ว รวมคําสั่ง
* Linux (ubuntu) อูบุนตู (22.04)
```
pkg install proot-distro -y && proot-distro install ubuntu && pkg install nano && cd /data/data/com.termux/files/usr/etc && nano profile
```
* หรือ Linux (debian) เดเบียน (เสถียร)
```
pkg install proot-distro -y && proot-distro install debian && pkg install nano && cd /data/data/com.termux/files/usr/etc && nano profile
```
* แบบทีละคําสั่ง
```
pkg install proot-distro -y
```
* Linux (ubuntu) อูบุนตู (22.04)
```
proot-distro install ubuntu
```
* หรือ Linux (debian) เดเบียน (เสถียร)
```
proot-distro install debian
```
## 2 รัน (Debian) (ubuntu) โดยอัตโมัติ
```
pkg install nano && cd /data/data/com.termux/files/usr/etc && nano profile
```
เมื่อใช้คำสั่งด้านบนเสร็จแล้ว และไม่มี error ขั้นตอนต่อไปเราจะมาเพิ่มข้อมูลในไฟล์ profile กันโดยที่ไฟล์นี้
จะเปิดขึ้นมาเองหลังจากใช้คำสั่งด้านบน สิ่งที่จะเพิ่มไปตามระบบที่คุณติดตั้ง
Linux (Debian) (ubuntu) เพิ่มข้อมูลนี้ใน profile บรรทัดสุดท้าย

* Linux (ubuntu) อูบุนตู (22.04)
```
proot-distro login ubuntu
```
* หรือ Linux (debian) เดเบียน (เสถียร)
```
proot-distro login debian
```
ออกจาก ubuntu จากเทอร์มินัล
```
exit
```
จบขั้นตอน เปิด Termux และรัน (Debian) (ubuntu) โดยอัตโมัติ
## 3 Auto รัน CCminer V.1 ใน Termux Created By [mantvmass](https://github.com/mantvmass)
* แบบเร็ว รวมคําสั่ง
```
apt-get update -y && apt-get install git -y && git clone https://github.com/thaiboy001/auto-run && cd auto-run && sh setup.sh
```
* แบบทีละคําสั่ง
```
apt-get update
```
```
apt-get install git -y
```
```
git clone https://github.com/thaiboy001/auto-run
```
```
cd auto-run
```
```
sh setup.sh
```
หลังจากเปิดไฟล์ bash.bashrc เพิ่มบรรทัดแรกเป็น
```
run-miner
```
แล้ว save
## pool
* luckpool
```
stratum+tcp://ap.luckpool.net:3956
```
* zergpool
```
stratum+tcp://verushash.asia.mine.zergpool.com:3300
```
* zpool
```
stratum+tcp://heavyhash.sea.mine.zpool.ca:5138
```
## wallet
```
```
## เพิ่มเติมการใช้โปรแกรม
* หากต้องการหยุดขุดให้ใช้กด ```CTRL + C```
* หากต้องการเปลี่ยน pool or wallet ใช้คำสั่ง 
```
edit-miner
```
* หากต้องการเปิดขุด ใช้คำสั่ง 
```
run-miner
```
* ออกจากเทอร์มินัล
```
exit
```
### CCminer V.1 แก้และเรียบเรียง ใหม่ By.* [Facebook](https://github.com/thaiboy001)


### สนับสนุนนักพัฒนา
- ชื่อ ```ภูมินท์ มะลิวรรณ```
- กสิกรไทย ```0608905863```
- พร้อมเพย์ ```0639723211```

### ติดต่อ
* [Facebook](https://www.facebook.com/PhuminMaliwan)
* YouTube
   * [MANTVMASS](https://www.youtube.com/channel/UCYJk0E1wwY3zX-i8tn95mhw)
   * [MOBILE MINING](https://www.youtube.com/channel/UCevNnlKLgRTg-cku5JQ2Ahw) 
