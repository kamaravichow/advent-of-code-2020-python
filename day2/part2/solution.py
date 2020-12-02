
list_of_inputs = open("./input.txt").readlines()
cleaned_list = []

for item in list_of_inputs:
	cleaned_list.append(item.strip())

correct_passwords_count = 0

for item in cleaned_list:
    chCorrect = 0
    pCurrent = item.split(" ")

    pInfo = pCurrent[0]

    pTimesMin, pTimesMax = pInfo.split ("-")

    pLetter = pCurrent[1].strip(":")

    pCheckString = pCurrent[2].strip()

    pCurrentLetterCount = pCheckString.count(pLetter)

    if int(pTimesMin) <= int(pTimesMax) <= len(pCheckString):
        
        if pCheckString[int(pTimesMin)-1] == pLetter:
            chCorrect += 1

        if pCheckString[int(pTimesMax)-1] == pLetter:
            chCorrect += 1
            
        if chCorrect == 1:
            correct_passwords_count += 1

print(correct_passwords_count)



