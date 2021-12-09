def uniquedict(dict_list):
	return list(map(dict, set(tuple(sorted(d.items())) for d in dict_list)))


dict_list = [{'name': 'affirm', 'confidence': 0.9448149204254}, {'name': 'affirm', 'confidence': 0.944814920425415}, {'name': 'inform', 'confidence': 0.9842240810394287}, {'name': 'inform', 'confidence': 0.9842240810394287}]  # Assign list of dictionaries here
print(uniquedict(dict_list))

