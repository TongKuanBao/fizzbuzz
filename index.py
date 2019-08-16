'''
Write a function that takes a number and returns “fizz” if it’s divisible by 3, returns
“buzz” if it’s divisible by 5 and returns “fizzbuzz” if it’s divisible by 3 and 5.
'''

def fizzy(input_number):
    answer_both = 'fizz buzz'
    answer_three = 'fizz'
    answer_five = 'buzz'

    if input_number % 3 == 0 and input_number % 5 == 0:
        return answer_both
    elif input_number % 3 == 0:
        return answer_three
    elif input_number % 5 == 0:
        return answer_five
