list_of_inputs = open("./input.txt").readlines()
cleaned_list = []

for item in list_of_inputs:
	cleaned_list.append(item.strip())

correct_passwords_count = 0

for item in cleaned_list:
    pCurrent = item.split(" ")
    pInfo = pCurrent[0]
    pTimesMin, pTimesMax = pInfo.split ("-")
    pLetter = pCurrent[1].strip(":")
    pCheckString = pCurrent[2].strip()

    # 1 letter should be atleast ptimesmin
    # 2 letter count should not exceed ptimesmax
    pCurrentLetterCount = pCheckString.count(pLetter)
    if(pCurrentLetterCount >= int(pTimesMin) and pCurrentLetterCount <= int(pTimesMax)):
        correct_passwords_count = correct_passwords_count + 1


print(correct_passwords_count)