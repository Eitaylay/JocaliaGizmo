from replit import clear
from getkey import getkey
from prettytable import PrettyTable
import math
import time


going_back = False


def gold_weight_converter(back):
    """Take input of weight of 15 or 14 pal 2 pyar and change its weight to pure gold weight."""
    s_price = int(input("Input 100% gold price: "))
    while not back:
        print("Gold weight converter")
        print("Choose a method!\n 1. 15pal to 100%\n 2. 14pal 2pyar to 100%\n 3. 14pal to 100% \n 0. back")
        gwc_choice = getkey()
        clear()
        if gwc_choice == '0':
            back = True


        def gwc_method(gwc_choice, back):
            """whereas s is မီးလင်း , a is 15ပဲရည် b is ဒင်္ဂါးရွှေ"""

            def q_round(x):
                return round(x*4)/4

            def a_to_s(s_price, weight):
                formula = 16 / 17
                gold_quality = "15 pal"
                a_price = math.trunc(s_price * formula)
                gwc_calculation(a_price, weight, gold_quality, formula)

            def b_to_s(s_price, weight):
                formula = 16 / 17.5
                gold_quality = "14 pal 2 pyar"
                b_price = math.trunc(s_price * formula)
                gwc_calculation(b_price, weight, gold_quality, formula)

            def c_to_s(c_price, weight):
                formula = 16 / 18
                gold_quality = "14 pal"
                c_price = math.trunc(s_price * formula)
                gwc_calculation(c_price, weight, gold_quality, formula)
            
            def gwc_calculation(price, weight, quality, formula):

                t = PrettyTable()
                x = [0, 1.5, 2]
                yway_weight = float(kyat * 128 + pal * 8 + yway)
                
                t.field_names = ["Quality", quality, "➟", "100%", "Value"]
                t.add_row(["Price", price, " ", s_price, ""])
                for sote in x:
                    
                    soated_yway = ((128 - sote) / 128) * yway_weight
                    soated_kpy = soated_yway
                    so_pal, so_kyat = math.modf(soated_kpy / 128)
                    so_kyat = int(so_kyat)
                    so_yway, so_pal = math.modf(so_pal * 16)
                    so_pal = int(so_pal)
                    so_yway = q_round(so_yway * 8)
                    if so_yway >= 8:
                        so_yway = so_yway - 8
                        so_pal += 1
                    soated_weight = [so_kyat, so_pal, so_yway]
                    converted_weight = soated_yway * formula
                    s_pal, s_kyat = math.modf(converted_weight / 128)
                    s_kyat = int(s_kyat)
                    s_yway, s_pal = math.modf(s_pal * 16)
                    s_pal = int(s_pal)
                    s_yway = q_round(s_yway * 8)
                    if s_yway >= 8:
                        s_yway = s_yway - 8
                        s_pal += 1
                    s_weight = [s_kyat, s_pal, s_yway]
                    value = math.trunc(soated_yway / 128 * price)
                    t.add_row(["Weight", soated_weight, sote, s_weight, value])
                print(t)


            while not back:
                time.sleep(0.4)
                print("gram or kyat, pal, yway? g or any: ")
                gram_or_kpy = getkey()
                # kpy = kyat pal yway
                clear()
                time.sleep(0.4)
                
                if gram_or_kpy.lower() == 'g' or gram_or_kpy.lower() == 'ါ':
                    gram = float(input("Input weight in gram: "))
                    pal, kyat = math.modf(gram / 16.6)
                    kyat = int(kyat)
                    yway, pal = math.modf(pal * 16)
                    pal = int(pal)
                    yway = q_round(yway * 8)

                else:
                    print("Input weight in (kyat pal yway)")
                    
                    kyat = int(input("Kyat: "))
                    pal = int(input("Pal: "))
                    yway = float(input("Yway: "))

                weight = [kyat, pal, yway]

                if gwc_choice == '1':
                    a_to_s(s_price, weight)
                elif gwc_choice == '2':
                    b_to_s(s_price, weight)
                elif gwc_choice == '3':
                    c_to_s(s_price, weight)
                else:
                    print("Invalid input")

                print("\n'any keys' = again (or) '0' = return")
                return_or_again = getkey()
                clear()
                if return_or_again == '0':
                    back = True

        gwc_method(gwc_choice, back)
        

def burmese_smith_length_converter(back):
    """It is used to measure the bracelet's inside and outside of radius."""

    while not back:
        cm = float(input("Please type the length in centimeter!\n"))
        pal, inch = math.modf(cm / 2.54)
        inch = math.trunc(inch)
        pal = round(pal * 16, 2)
        print(f"{inch} inches & {pal} pal")
        print("\n'any keys' = again (or) '0' = return")
        return_or_again = getkey()
        clear()
        if return_or_again == '0':
            back = True

def profited_based_value(back):
    """We use this program when we want to know the base value of a profited item."""

    while not back:
        value = int(input("What is the price?"))
        percentage = float(input("what is the percentage?"))
        act_value = 100 * value / (percentage + 100)
        print(f"Main Value is {act_value}.")
        print("\n'any keys' = again (or) '0' = return")
        return_or_again = getkey()
        clear()
        if return_or_again == '0':
            back = True


def diamond_Ratisize_calculation(back):
    """Traditional diamond size calculation"""

    while not back:
        ct_weight = float(input("Please input the Carat Weight: "))
        count_diamond= int(input("Please input the Diamond's count: "))
        diamond_size = (11 * count_diamond) / (10 * ct_weight)
        print(diamond_size)
        print("\n'any keys' = again (or) '0' = return")
        return_or_again = getkey()
        clear()
        if return_or_again == '0':
            back = True


while True:
    print("Hi, I'm Jocalia Gizmo. What can I help you?")

    print("Choose a service! \n 1. Gold weight converter \n 2. Burmese smith length converter \n 3. Profited based value \n 4. Diamond Rati-size calculation \n ")

    main_input = getkey()
    clear()

    if main_input == '1':
        gold_weight_converter(going_back)
    elif main_input == '2':
        burmese_smith_length_converter(going_back)
    elif main_input == '3':
        profited_based_value(going_back)
    elif main_input == '4':
        diamond_Ratisize_calculation(going_back)
    else:
        print("wrong input!")