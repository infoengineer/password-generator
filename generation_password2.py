import string
import random
import click

def generate_password(symbols, symbols):
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


@click.command()
@click.argument('path', default='', type=click.Path())
@click.option('-u', '--user', default='unknown', show_default=True, help='User name or login.')
@click.option('-s', '--symbols', default='ads', help='Symbol set for password (like ads or \'ads\'): \n u-uppercase, \n l-lowcase, \n a-all, \n d-digits, \n s-special.')
@click.option('-n', '--number', default=8, show_default=True, type=int, help='Password length.')
def print_password(path, user, symbols, number):
	# Вывод в терминал
	print('u: {} p: {}'.format(user, generate_password(symbols, number)))

if __name__ == '__main__':
	print_password()