#!/usr/bin/env python3


def ad_feture(output, output2):     # print output in beatiful way
    return ("/-" + "-"*len(output) + "---" + "-"*len(output2) + "-\\" +
            "\n"+"| " + output + " | " + output2 + " |"+"\n"+"\-" +
            "-"*len(output) + "---" + "-"*len(output2) + "-/")


while True:     # to protect program from users and human error
    a = input()
    number = a.split(" ")
    try:    # test did we give 2 numbers
        float(number[0])
        int(number[1])
    except (ValueError, IndexError):        # message on error
        print("Invalid number!")
    else:       # test if we put as second number 2 or 10
        if number[1] != "2" and number[1] != "10":
            print("Invalid number!")
        elif number[1] == "2":      # if second number is 2 test if we have only 0 and 1 in first number
            test = list(number[0])
            if "-" in test:     # cut off "-" for test
                test.pop(0)
            if "." in test:     # cut out "." for test
                g = test.index(".")
                test.pop(g)
            for q in range(0, len(test)):       # test only digits in our input
                test[q] = int(test[q])
                if test[q] > 1:
                    print("Invalid number!")
            else:
                break
        else:
            break

number[0] = str(number[0])
number[1] = int(number[1])

helper = 0      # do we have "-" variable

if "." in number[0]:        # if number is .decimal thn is splited to two part before and after "."
    number_to_change = number[0].split(".")
    number_to_change_to_dot = list(number_to_change[0])
    number_to_change_after_dot = list(number_to_change[1])

else:
    number_to_change_to_dot = list(number[0])       # if it is note to not have an error
    number_to_change_after_dot = None       # here we can have a problem


if "-" in number_to_change_to_dot:      # if we have "-" we cut it off for now
    number_to_change_to_dot.pop(0)
    helper = 1      # tells program that we had "-"

if number[1] == 2:
    n = "10"
    power_of_two = 0
    dec_number = 0
    if number_to_change_after_dot is not None:      # for .dec change from binary
        dot_dec_number = 0
        dot_power_of_two = -1
        for i in range(len(number_to_change_to_dot) - 1, -1, -1):       # before dot part
            number_to_change_to_dot[i] = int(number_to_change_to_dot[i])
            c = number_to_change_to_dot[i]*pow(2, power_of_two)
            dec_number += c
            power_of_two += 1
        for z in range(0, len(number_to_change_after_dot)):         # after dot part
            number_to_change_after_dot[z] = int(number_to_change_after_dot[z])
            d = number_to_change_after_dot[z]*pow(2, dot_power_of_two)
            dot_power_of_two -= 1
            dot_dec_number += d
        if helper != 0:        # if we had "-"
            dec_number = dec_number + dot_dec_number
            dec_number = dec_number*(-1)
        else:
            dec_number = dec_number + dot_dec_number
    else:       # if we don't have .dec
        for i in range(len(number_to_change_to_dot) - 1, -1, -1):
            number_to_change_to_dot[i] = int(number_to_change_to_dot[i])
            c = number_to_change_to_dot[i]*pow(2, power_of_two)
            dec_number += c
            power_of_two += 1
            if helper != 0:
                dec_number = dec_number*(-1)
    dec_number = str(dec_number)
    answer = ad_feture(dec_number, n)
    print(answer)

if number[1] == 10:     # if we want to change form dec to bin
    n = "2"
    if number_to_change_after_dot is not None:
        number_to_change_to_dot = "".join(number_to_change_to_dot)      # change before float part into number form list
        number_to_change_to_dot = float(number_to_change_to_dot)
        number_to_change_after_dot.insert(0, ".")       # add 0. to float part of number (still as list)
        number_to_change_after_dot.insert(0, "0")
        number_to_change_after_dot = "".join(number_to_change_after_dot)        # change float part to number
        number_to_change_after_dot = float(number_to_change_after_dot)
        binary_number_to_dot = []
        binary_number_after_dot = []

        if number_to_change_to_dot == 0:        # add before . 0 to float part in print
            binary_number_to_dot.insert(0, "0")

        while number_to_change_to_dot > 0:      # convert dec part to binar
            x = int(number_to_change_to_dot % 2)        # set modulo as int (0 or 1) from our number to .
            number_to_change_to_dot = (number_to_change_to_dot - x)/2       # have to look at this
            binary_number_to_dot.append(x)      # add binery number to print
        binary_number_to_dot.reverse()  # revers list
        for v in range(0, len(binary_number_to_dot)):       # change number to format better to print
            binary_number_to_dot[v] = str(binary_number_to_dot[v])

        if helper != 0:     # add to before . part - if our input was -
            binary_number_to_dot.insert(0, "-")
        binary_number_to_dot = "".join(binary_number_to_dot)

        x = 0       # set float part to starting value to convert
        number_to_change_after_dot = (number_to_change_after_dot)*2
        while number_to_change_after_dot > 0:
            x = int(number_to_change_after_dot % 2)     # set modulo as int (0 or 1) from our number to .
            number_to_change_after_dot = (number_to_change_after_dot - x)*2     # * rest of our input float
            binary_number_after_dot.append(x)       # after minus modulo, hve to look at this

        for v in range(0, len(binary_number_after_dot)):        # connect and print before and after . 
            binary_number_after_dot[v] = str(binary_number_after_dot[v])        # parts of now binary number
        binary_number_after_dot = "".join(binary_number_after_dot)
        binary_output = binary_number_to_dot + "." + binary_number_after_dot
        answer = ad_feture(binary_output, n)
        print(answer)

    else:       # variant for non .dec number in input
        number_to_change_to_dot = "".join(number_to_change_to_dot)      # change before float part into number form list
        number_to_change_to_dot = float(number_to_change_to_dot)
        binary_number = []
        while number_to_change_to_dot > 0:
            x = int(number_to_change_to_dot % 2)        # set modulo as int (0 or 1) from our number to .
            number_to_change_to_dot = (number_to_change_to_dot - x)/2
            binary_number.append(x)
        binary_number.reverse()
        for v in range(0, len(binary_number)):
            binary_number[v] = str(binary_number[v])
        if helper != 0:     # add to before . part - if our input was -
            binary_number.insert(0, "-")
        binary_output = "".join(binary_number)
        answer = ad_feture(binary_output, n)
        print(answer)
