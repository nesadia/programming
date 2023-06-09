from num2words import num2words

def convert_number_to_words(num):
    try:
        num = int(num)
        words = num2words(num, lang='uk')
        return words
    except ValueError:
        return "Помилка: введіть ціле число."
