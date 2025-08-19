import random
#1.“Онооны систем” нэмэх (цөөхөн оролдлого хийвэл өндөр оноо авах).
#2.“Түвшин” нэмэх (1–20 → 1–50 → 1–100 хүртэл).
#3. show_score гэсэн функц нэмж оруулах

def guess_number():
    secret = random.randint(1, 20)
    attempts = 0

    while True:
        guess = int(input("Та 1-20 хооронд тоо оруулна уу: "))
        attempts += 1

        if guess == secret:
            print("🎉 Зөв таалаа! Та", attempts, "оролдлого хийлээ.")
            break
        elif guess < secret:
            print("🔼 Илүү том тоо оруулна уу.")
        else:
            print("🔽 Илүү бага тоо оруулна уу.")

# Функцийг ажиллуулах
guess_number()
