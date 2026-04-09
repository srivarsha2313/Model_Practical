def add_one(num_list):
    num = int("".join(map(str, num_list)))  # convert list to number
    num += 1
    return list(map(int, str(num)))  # convert back to list

# Example
input_list = [1, 2, 3]
output = add_one(input_list)

print("Output:", output)