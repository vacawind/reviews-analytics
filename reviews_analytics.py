

data = []
count = 0
with open('reviews.txt','r') as f:
	for line in f: #每次讀取一行，故取名為line
		data.append(line)
		count = count + 1
		if count % 1000 == 0:
			print(count) #每讀1000行後印讀取進度

print("檔案讀取結束，共有",len(data),"筆資料。")

