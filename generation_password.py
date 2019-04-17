import string
import random

def generate_password(symbols='ads', number = 8):
	s = []
	# Наполнение списка необходимыми наборами символов
	if 'u' in symbols:
		s.append(string.ascii_uppercase)
	if 'l' in symbols:
		s.append(string.ascii_lowercase)
	if 'a' in symbols:
		s.append(string.ascii_letters)
	if 'd' in symbols:
		s.append(string.digits)
	if 's' in symbols:
		s.append(string.punctuation)
	# Объединение их в одну строку и затем разбивка на отдельные символы
	separate_symbols = list(''.join(s))
	# Выбор из полученного списка случайных символов в количестве равном требуемой длине пароля
	random_symbols = [random.choice(separate_symbols) for x in range(number)]
	# Полученная строка с паролем
	return ''.join(random_symbols)

def print_password(symbols, number):
	# Вывод в терминал
	print(generate_password(symbols, number))

if __name__ == '__main__':
	print_password()