def is_isogram(x):
	l = []
	is_gram = True;
	for c in x:
		if c in 'abcdefghijklmnopqrstvuwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
			if c in l:
				is_gram = False
				break
			else:
				l.append(c)
	return is_gram

print(is_isogram(input('enter word:')))
