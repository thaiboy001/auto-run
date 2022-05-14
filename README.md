# 1 เปิด Termux และรัน (Debian โดยอัตโมัติ
36
34
37
•
38
35
39
## ให้ติดตั้ง Linux(Debian)
40
36
41
## การติดตั้ง
42
37
43
```
44
38
45
คัดลอกและวางคำสั่งนี้ลงใน Termux:
46
39
47
```
48
40
49
```curl --silent --location --remote-name https://raw.githubusercontent.com/trungtai33/debian-bullseye-in-termux/master/install.sh; bash install.sh; rm install.sh
50
41
51
```
52
42
53
## วิธีถอนการติดตั้ง debian
54
43
55
ใช้ความระมัดระวังเมื่อใช้คำสั่งนี้เนื่องจากจะไม่ขอคำยืนยัน
56
44
57
```
58
45
59
curl --silent --location --remote-name https://raw.githubusercontent.com/trungtai33/debian-bullseye-in-termux/master/uninstall.sh; bash uninstall.sh; rm uninstall.sh
60
46
61
```
62
47
63
# 2 รัน Debian โดยอัตโมัติ
64
48
65
•
66
49
67
```
68
50
69
pkg install nano && cd /data/data/com.termux/files/usr/etc && nano profile
70
51
71
```
72
52
73
•
74
53
75
เมื่อใช้คำสั่งด้านบนเสร็จแล้ว และไม่มีerror ขั้นตอนต่อไปเราจะมาเพิ่มข้อมูลในไฟล์ profile กันโดยที่ไฟล์นี้
76
54
77
จะเปิดขึ้นมาเองหลังจากใช้คำสั่งด้านบน สิ่งที่จะเพิ่มไปในไฟลมี 2 อย่างตามระบบที่คุณติดตั้ง
78
55
79
•
80
56
81
•
82
57
83
## Linux(Debian) เพิ่มข้อมูลนี้ใน profile บรรทัดสุดท้าย
84
58
85
```
86
59
87
start-debian-bullseye
88
60
89
```
90
61
91
จบขั้นตอน เปิด Termux และรัน (Debian โดยอัตโมัติ
92
62
93
```
94
63
95
```
96
64
97
•

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

