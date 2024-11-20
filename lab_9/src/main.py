from lab_1.src.main import main as lab1_main
from lab_2.src.BLL.main import main as lab2_main
from lab_3.src.main import main as lab3_main
from lab_4.src.main import main as lab4_main
from lab_5.src.main import main as lab5_main
from lab_7.src.main import main as lab7_main
from lab_8.src.main import main as lab8_main

from shared.constants.global_variables import labs_menu


def main():
    while True:
        print(labs_menu)
        choice = input("Введіть номер лабораторної роботи (або 0 для виходу): ")

        match choice:
            case "1":
                print("\nЗапуск лабораторної №1...")
                lab1_main()
            case "2":
                print("\nЗапуск лабораторної №2...")
                lab2_main()
            case "3":
                print("\nЗапуск лабораторної №3...")
                lab3_main()
            case "4":
                print("\nЗапуск лабораторної №4...")
                lab4_main()
            case "5":
                print("\nЗапуск лабораторної №5...")
                lab5_main()
            case "7":
                print("\nЗапуск лабораторної №7...")
                lab7_main()
            case "8":
                print("\nЗапуск лабораторної №8...")
                lab8_main()
            case "0":
                print("До побачення!")
                break
            case _:
                print("Некоректний вибір. Спробуйте ще раз.")
