# Mini Quiz Game – Starter Version
# Хичээлийн зорилго:
# 1. Python function ашиглаж сурах
# 2. if / elif / else нөхцөл ашиглах
# 3. Кодыг хөгжүүлж сайжруулах

# 1. Хэрэглэгчийг угтах функц
def greet_user():
    name = input("Таны нэрийг хэн гэдэг вэ?: ")
    print(f"Сайн байна уу, {name}! Mini Quiz тоглоомд тавтай морил!")
    return name  # Нэрийг буцаана, дараа ашиглаж болно


# 2. Асуулт асуух функц
def ask_question(question, answer):
    user_answer = input(question + " ")
    if user_answer.lower() == answer.lower():
        print(" Зөв!")
        return 1  # Оноо 1 нэмнэ
    else:
        print(" Буруу!")
        return 0  # Оноо нэмэхгүй


# 3. Оноог харуулах функц
def show_score(score):
    print(f"Таны авсан оноо: {score} / 3")
    if score == 3:
        print(" Маш сайн!")
    elif score == 2:
        print(" Сайн байна!")
    else:
        print("Дараагийн удаа илүү сайн хийнэ гэж найдая!")


#  4. Гол тоглоомын функц
def run_quiz():
    score = 0  # Эхний оноо 0
    print("Тоглоом эхэлж байна...")

    # 📝 Энд байгаа асуултуудыг сурагчид өөрчилж болно
    score += ask_question("Монгол улсын нийслэл аль хот вэ?", "Улаанбаатар")
    score += ask_question("2 + 2 хэд вэ?", "4")
    score += ask_question("Python гэдэг нь ямар төрлийн хэл вэ? (programming / human / animal)", "programming")

    # Оноог харуулах
    show_score(score)


# 5. Програм ажиллуулах хэсэг
def main():
    greet_user()
    run_quiz()


#  Програм эхлүүлэх
if __name__ == "__main__":
    main()
