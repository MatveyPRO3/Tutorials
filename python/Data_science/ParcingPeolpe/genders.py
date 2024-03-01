import requests, json

def getGenders(names,incomes):
	url = ""
	cnt = 0
	if not isinstance(names,list):
		names = [names,]
	
	for name in names:
		if url == "":
			url = "name[0]=" + name
		else:
			cnt += 1
			url = url + "&name[" + str(cnt) + "]=" + name
		

	req = requests.get("https://api.genderize.io?" + url)
	results = json.loads(req.text)
	
	retrn = []
	for result,income in zip(results,incomes):
		if result["gender"] is not None:
			retrn.append((result["name"],result["gender"],income))
		else:
			retrn.append((u'None',u'0.0',0.0))
	return retrn

if __name__ == '__main__':
	print(getGenders(["Brian","Apple","Jessica","Zaeem","NotAName"],[1,2,3,4,5]))