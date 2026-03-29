def print_help():
    print("\n--- ТУСЛАМЖ ---")
    print("Боломжит үйлдлүүд:")
    print("- Урагшаа: Чиглэлийн дагуу явах")
    print("- Зүүн: Зүүн тийш эргэх")
    print("- Баруун: Баруун тийш эргэх")
    print("- Буцах: Өмнөх өрөө рүү орох (Зөвхөн хонгилд)")
    print("- Хайх: Өрөөг нэгжих (Авдар нээх эсвэл буу хайх)")
    print("- Тулалдах: Мангастай нүүр тулах")
    print("- !help: Тусламж харах")
    print("----------------\n")

def start_game():
    inventory = {"key": False, "gun": False}
    current_floor = 6
    monster_attempts = 0
    
    print("Та хөдөө орон нутагт орших хаягдсан 6 давхар нууц лабораторид сэрлээ.")
    print("Хүмүүс дээр туршилт хийдэг байсан аймшигт газар бололтой. Та эндээс амьд гарах ёстой!")
    print("Тусламж авах бол !help гэж бичээрэй.")

    while True:
        # User input logic
        move = input(f"\n[{current_floor}-р давхар] Таны үйлдэл: ").strip().lower()

        if move == "!help":
            print_help()
            continue
        elif not move:
            print("Ямар нэгэн тушаал оруулна уу. Хэрэв мэдэхгүй байвал !help гэж бичээрэй.")
            continue

        # --- FLOOR 6: START ---
        if current_floor == 6:
            if move == "урагшаа":
                print("Та шатаар доошоо 5-р давхар руу буулаа.")
                current_floor = 5
            else:
                print("Энд өөр зам байхгүй. Урагшаа явж шат руу оч.")

        # --- FLOOR 5: SEARCH FOR GUN ---
        elif current_floor == 5:
            if move == "хайх":
                print("Та нэгэн шүүгээн дотроос БУУ оллоо! Одоо та аюулгүй байж магадгүй.")
                inventory["gun"] = True
            elif move == "урагшаа":
                print("Та 4-р давхар руу буулаа.")
                current_floor = 4
            else:
                print("Буруу тушаал.")

        # --- FLOOR 4: SEARCH FOR KEY (AVDAR) ---
        elif current_floor == 4:
            if move == "хайх":
                print("Та өрөөний буланд нэгэн 'Авдар' оллоо. Нээж үзэх үү?")
                choice = input("Нээх үү? (тийм/үгүй): ").strip().lower()
                if choice == "тийм":
                    print("Авдар дотор хуучин ТҮЛХҮҮР байна. Та түлхүүрийг авлаа.")
                    inventory["key"] = True
            elif move == "урагшаа":
                print("Та 3-р давхар руу орлоо. Гэтэл...")
                current_floor = 3
            else:
                print("Буруу тушаал.")

        # --- FLOOR 3: THE MONSTER ---
        elif current_floor == 3:
            print("АЙМШИГТАЙ! Таны өмнө мутацид орсон мангас байна!")
            choice = input("Тулалдах уу эсвэл Зугтах уу? (тулалдах/зугтах): ").strip().lower()
            
            if choice == "тулалдах":
                if inventory["gun"]:
                    print("Та буугаараа мангасыг буудаж унагаалаа! Зам чөлөөтэй боллоо.")
                    current_floor = 2
                else:
                    print("Та нүцгэн гараараа тулалдахыг оролдсон боловч мангаст бариулж ҮХЛЭЭ.")
                    break
            elif choice == "зугтах":
                print("Та сандран гүйж байна! Зүүн эсвэл Баруун хаалганы аль нь вэ?")
                direction = input("Чиглэл: ").strip().lower()
                if direction == "зүүн" or direction == "баруун":
                    print("Та арай гэж мангасаас мултарч 2-р давхар руу орлоо.")
                    current_floor = 2
                else:
                    monster_attempts += 1
                    if monster_attempts >= 2:
                        print("Та хэтэрхий их хугацаа алдлаа. Мангас таныг барьж идэв. ТОГЛООМ ДУУСЛАА.")
                        break
                    print("Буруу хаалга! Мангас ойртож байна, дахин оролд!")

        # --- FLOOR 2 & 1: FINDING THE EXIT ---
        elif current_floor == 2:
            print("2-р давхар нам гүм байна. Гэхдээ эндээс гарах хаалга алга.")
            if move == "урагшаа":
                current_floor = 1
            else:
                print("Доошоо 1-р давхар руу яв.")

        elif current_floor == 1:
            print("Та 1-р давхарт ирлээ. Гарах хаалга ТҮГЖЭЭТЭЙ байна!")
            if inventory["key"]:
                print("Танд түлхүүр байгаа тул хаалгыг нээж амьд гарлаа! БАЯР ХҮРГЭЕ!")
                break
            else:
                print("Танд түлхүүр байхгүй байна. Магадгүй Хонгилд (Basement) байгаа болов уу?")
                current_floor = 0 # Basement logic

        # --- BASEMENT: BACK COMMAND ENABLED ---
        elif current_floor == 0:
            print("Та харанхуй Хонгилд (Basement) байна.")
            if move == "хайх":
                print("Та хог доороос хаалганы ТҮЛХҮҮР оллоо!")
                inventory["key"] = True
            elif move == "буцах":
                print("Та 1-р давхар руу буцлаа.")
                current_floor = 1
            else:
                print("Энд зөвхөн 'хайх' эсвэл 'буцах' гэсэн үйлдлүүд боломжтой.")

start_game()