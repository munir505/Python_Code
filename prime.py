user_input = input("Enter Range ")
input_range = int(user_input)
for x in range(2, input_range):
    num = x
    num_prime = "true"
    for y in range(2, input_range):
        if x % y == 0:
            if x != y:
                num_prime = "false"
    if num_prime == "true":
        print(x, "Is a Prime")
