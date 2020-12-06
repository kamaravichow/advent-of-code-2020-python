input_file = open('./input.txt', 'r')
input_passport_list_text = input_file.read()

input_passport_list = input_passport_list_text.split('\n\n')
clean_input_passport_list = []
input_file.close()

for line in input_passport_list:
    clean_input_passport_list.append(line.replace('\n', ' '))

#byr:1985 eyr:2021 iyr:2011 hgt:175cm pid:163069444 hcl:#18171d

valid_passports = 0

must_fields = ['byr', 'iyr', 'eyr', 'hgt', 'ecl', 'pid']

for each_passport in clean_input_passport_list:
    items = each_passport.split(":")
    cleaned_items = []

    
    # for item in items:
    #     keys = []
    #     keys.append(item[0])
    #     print(keys)
    print(each_passport)
    

    # for item_field in item_fields:
    #     for i in range (0,len(item_field)):
    #         if item_field[i].split(':')[i] in must_fields:
    #             valid_passports += 1

# print(valid_passports)