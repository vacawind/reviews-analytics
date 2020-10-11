

data = []
count = 0
string = 0
with open('reviews.txt','r') as f:
	for line in f: #每次讀取一行，故取名為line
		data.append(line)
		string = string + len(line)
		count = count + 1
		if count % 10000 == 0:
			print(count) #每讀1000行後印讀取進度

average_len = string / len(data) #每筆留言平均長度

print("檔案讀取結束，共有",len(data),"筆資料。")

print("每筆留言平均長度為",average_len)


# new = []
# for line in data:
# 	if len(line) < 100:
# 		new.append(line)

new = [line for line in data if len(line) < 100] #清單快寫法
print("留言長度小於100個字共有",len(new),"筆資料。")


# good = []
# for line in data:
# 	if "good" in line:
# 		good.append(line)
good = [line for line in data if "good" in line ] #清單快寫法
print("留言中有提到good的字眼共有",len(good),"筆資料。")

bad = ["bad" in line for line in data] #清單快寫法(進階)
# bad = []
# for line in data:
# 	bad.appned("bad" in line)
