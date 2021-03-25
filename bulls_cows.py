import random
import time
import os


def get_number() -> int:
    """
    function returns 4 unique digits number
    """
    number = random.randint(1234, 9876)
    freq = 0
    while freq != 1:
        for digit in str(number):
            if str(number).count(digit) > freq:
                freq = str(number).count(digit)
        if freq > 1:
            number = random.randint(1234, 9876)
            freq = 0
    return number


def get_guess() -> int:
    """
    function returns guess-number with lenght = 4 and all its digits are unique
    """
    guess = 0
    freq = 0
    while len(str(guess)) != 4 or freq != 1:
        global attempts
        try:
            guess = int(input(f"Guess: "))
        except ValueError:
            print("NOOOOoooo! This is not an integer. This game is not ready for it!... Again!!!")
            guess = 0
        for digit in str(guess):
            if str(guess).count(digit) > freq:
                freq = str(guess).count(digit)
        if freq > 1:
            freq = 0
            print("Only unique digits in a number.")
        if len(str(guess)) != 4:
            print("You can play only with 4-digit number. Try it again.")
        attempts += 1
    return guess


def comparison(number, guess) -> None:
    """
    prints the result of comparison
    """
    number = str(number)
    guess = str(guess)
    cows = 0
    bulls = 0
    for i, num in enumerate(guess):
        if guess[i] == number[i]:
            bulls += 1
        elif num in number:
            cows += 1
    if bulls == 1:
        name_bull = "bull"
    else:
        name_bull = "bulls"
    if cows == 1:
        name_cow = "cow"
    else:
        name_cow = "cows"
    print(f"{bulls} {name_bull}, {cows} {name_cow}")
    print(underlining)


def result_file(nr_of_guesses, times) -> None:
    """
    result: Nr. of attempts, Name, time table
    :return: Nothing, only printing table with results + inserting last game
    also save the results to txt file
    """
    name = input('Enter your name to the scoreboard: ')
    header = ['Guesses', 'Name', 'Time']
    result = [nr_of_guesses, name, times]
    result_print = ''
    # if the .txt file doesn't exist it is created in the same folder as .py file
    if not os.path.exists('result.txt'):
        f = open('result.txt', 'w')
        f.close()
    # .txt file is saved to list, if the file is empty list is empty
    with open('result.txt', 'r') as file:
        result_string = file.read()
        result_list = result_string.split()
    # if the file is empty it creates 'header'
    if not result_list:
        result_list.extend(header)
    list_size = len(result_list) - 1

    if list_size < 3:
        result_list.extend(result)
    else:
        for index in range(3, list_size + 1):
            if index % 3 == 0:
                if (int(result_list[index]) > result[0] or int(result_list[index]) == result[0]
                        and float(result_list[index + 2]) > float(result[2])):
                    result_list[index:index] = result
                    break
            elif index == list_size:
                result_list.extend(result)
    # from list -> string
    for word in result_list:
        result_print += str(word) + ' '
    print(underlining)
    print("Let's see the scoreboard!")
    print(underlining)
    # print table with results
    for i, word in enumerate(result_list):
        if i % 3 == 0:
            print(f'{word: ^{len(result_list[0])}}', end=' ')
        elif i % 3 == 1:
            print(f'|{word: ^15}|', end=' ')
        else:
            print(f'{word: >7}s')
    # save string to .txt file
    with open('result.txt', 'w') as file:
        file.write(result_print)


# Main program
attempts = 0
underlining = 100 * '='
print(underlining)
print("Yo. Let's play a game!".center(100))
print(underlining)
print(f"I've generated a random 4 digit number for ya. Do you dare to guess it?\n"
      f"All digits in this random number are non-recurring (each digit is in number only once).\n"
      f"Are you ready to rumble???? \n"
      f"Let's play BULLS & COWS!!!")
print(underlining)

random_number = get_number()
returned_guess = 0
start = time.time()
while random_number != returned_guess:
    returned_guess = get_guess()
    comparison(random_number, returned_guess)
end = time.time()

final_time = round(end - start, 2)
if attempts == 1:
    print(f"WOOOOOW. You've guessed it in 1 guess! GOOD JOB!!")
else:
    print(f"You've made it in {attempts} guesses.")
print(f"You've guessed it in {final_time}s.")
print(underlining)
result_file(attempts, final_time)
