import random as ran

f = open("questions.txt")
info_raw = f.read()
f.close

info_list = info_raw.split("\n")
info_size = len(info_list)

print("****************************************")
print("*                                      *")
print("*      Randomized Auto Questioner      *")
print("*                                      *")
print("****************************************")
print(" ")
print("--- Please, input any value to get the next question. ---")
print(" ")

for i in range(1, len(info_list)+1):
    choice = ran.randint(0, len(info_list)-1)
    message = "-> Question {0} / {1} :\t {2}"
    print(message.format(i, info_size, info_list.pop(choice)))
    input()

print("\n--- Please, input any value to finish the program. ---")
input()