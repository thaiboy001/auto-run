import os, json, time
from progress.spinner import MoonSpinner



# install miner function 
def install():
    # os.system("git clone --single-branch -b ARM https://github.com/monkins1010/ccminer")
    os.system("git clone --single-branch -b ARM https://github.com/thaiboy001/ccminer")

# run miner function
def run():
    with open("set-miner/miner.json", encoding="utf-8") as set:
        load = set.read()
        loads = json.loads(load)
        pool = loads['Pool']
        wallet = loads['Wallet']
        password = loads['Pass']
        cpu = loads['Cpu']
    if pool == "" or wallet == "":
        print("pool หรือ wallet กรุณาตั้งค่าใหม่")
        time.sleep(3)
        set_miner()
    # print(pool, wallet, password, cpu)
    
    os.system(f"cd ccminer && ./ccminer -a verus -o {pool} -u {wallet} -p {password} -t {cpu}")

def set_miner():
    pool = None
    wallet = None
    password = None
    cpu = None
    try:
        print("ตัวอย่าง: \033[93mstratum+tcp://ap.luckpool.net:3956\033[00m")
        pool = input("Pool[-o]: ")

        print("ตัวอย่าง: \033[93mRQpWNdNZ4LQ5yHUM3VAVuhUmMMiMuGLUhT.OMG-MINER\033[00m")
        wallet = input("Wallet[-u]: ")

        print("ตัวอย่าง: \033[93mx หรือ ( hybrid เฉพาะ luckpool )\033[00m")
        password = input("Password[-p]: ")

        print("\033[93m 0 ขึ้นไป หรือ เท่ากับจำนวณเธรด CPU เช็ค 'lscpu'\033[00m")
        cpu = int(input("CPU[-t]: "))

        if pool == "" or wallet == "":
            raise Exception()
        if password == "":
            password = "x"
        if cpu == "":
            cpu = 1
    except:
        print("\nเกิดข้อผิดพลาด มีบางอย่างไม่ถุูกต้อง!")
        time.sleep(2)
        set_miner()
    puts = {
        'Pool': pool,
        'Wallet': wallet,
        'Pass': password,
        'Cpu': cpu
    }
    with open("set-miner/miner.json", "w") as set:
        json.dump(puts, set, indent=4)

while True:
    os.system("clear")
    with MoonSpinner("กำลังเรียกใช้ ไม'เนอะ ขุดเหรียญ...") as bar:
        for i in range(100):
            time.sleep(0.05)
            bar.next()
	os.system("clear")
    if os.path.exists("ccminer") == False:
        install()
        break
    if os.path.exists("set-miner") == True:
        if os.path.isfile("set-miner/miner.json") == True:
            run()
            break
        else:
            set_miner()
    else:
        os.system("mkdir set-miner")


    
    
