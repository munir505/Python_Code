import hashlib
import string

password = "2Yh4s"
hash_object = hashlib.md5(password.encode())
hashed_password = hash_object.hexdigest()

password_guessed = False
alpha = [' ']

lower_letters = list(string.ascii_lowercase)
upper_letters = list(string.ascii_uppercase)
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def fill_alpha(letter_list):
    for x in letter_list:
        alpha.append(x)


def hash_password():
    predicted_password = ""
    i_range = 0
    j_range = 0
    k_range = 0
    l_range = 0
    for i in range(i_range, len(alpha)):
        for j in range(j_range, len(alpha)):
            for k in range(k_range, len(alpha)):
                for l in range(l_range, len(alpha)):
                    for m in range(1, len(alpha)):
                        possible = ""
                        possible += alpha[m]
                        possible += alpha[l]
                        possible += alpha[k]
                        possible += alpha[j]
                        possible += alpha[i]
                        print(possible)
                        hash_object2 = hashlib.md5(possible.encode())
                        hashed_password2 = hash_object2.hexdigest()
                        if hashed_password2 == hashed_password:
                            predicted_password = possible
                    l_range = 1
                k_range = 1
            j_range = 1
        i_range = 1
    print(i_range)
    return predicted_password


# Attempt to make a single for loop simulate as multiple
# Using array as index list and while loop
def hash_password_one_loop():
    password_length = 1
    index_array = []
    wh_val = 5
    while password_length < wh_val:
        index_array.append(0)
        for x in range(pow(len(alpha), password_length)):
            print(1)
        print(index_array)
        print(pow(len(alpha), password_length))
        password_length += 1


def main():
    fill_alpha(lower_letters)
    fill_alpha(upper_letters)
    fill_alpha(numbers)
    print(alpha)
    print("Password: ", hash_password())


main()
