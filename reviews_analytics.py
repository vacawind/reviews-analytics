

data = []
count = 0
string = 0
with open('reviews.txt','r') as f:
	for line in f: #每次讀取一行，故取名為line
		data.append(line)
		string = string + len(line)
		count = count + 1
		if count % 1000 == 0:
			print(count) #每讀1000行後印讀取進度

average_len = string / len(data) #每筆留言平均長度

print("檔案讀取結束，共有",len(data),"筆資料。")

print("每筆留言平均長度為",average_len)

