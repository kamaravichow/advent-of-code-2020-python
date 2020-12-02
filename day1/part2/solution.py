

def subsum_finder_helper(num_list,target):
    # Solve the subset sum problem for two target numbers    
    for item in num_list:
        sub_target = target - item
        if sub_target in num_list:
            return item*sub_target
    return None

def subsum_finder(num_list,target,num_nums):
    if num_nums==2:
        return subsum_finder_helper(num_list,target)
    else:
        for i,val in enumerate(num_list):
            sub_target = target - val
            sub_solution = subsum_finder(num_list[i:],sub_target,num_nums-1)
            if sub_solution is None:
                continue
            else:
                return val * sub_solution


# opens the inputs file and extracts to a list
list_of_inputs = open("./input.txt").readlines()
cleaned_list = []

# strips each line without a line break
for item in list_of_inputs:
	cleaned_list.append(item.strip())

# Inputs are in string type we convert them to integers
for i in range(0, len(cleaned_list)): 
    cleaned_list[i] = int(cleaned_list[i]) 

print(cleaned_list)


result = str(subsum_finder(cleaned_list,2020,3)) # use num_nums = 2 for the first and num_nums = 3 for the second

print("Solution is : " + result)