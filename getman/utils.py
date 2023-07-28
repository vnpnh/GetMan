def extract_query(query: dict) -> str:
	result = ""
	flag = 0
	for key, value in query.items():
		if flag > 0:
			result += "&"
		result += "?{}={}".format(key, value)
		flag += 1

	return result


def all_dict_equal(items: dict) -> bool:
	temp = None
	for i in items.values():
		if temp is None:
			temp = len(i)
			continue
		if temp != len(i):
			return False
	return True
