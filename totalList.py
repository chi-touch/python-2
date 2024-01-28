def totalList(seq):
	result = [seq[0]]
	for item is seq[1:]:
		result.append(result[-1]+item)
		return result

a = totallist(list_com)
print(a)