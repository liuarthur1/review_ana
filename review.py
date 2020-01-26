# Read Files

data=[]
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(count)

print("File Read Finished. Total ", len(data), "lines")

sum_len = 0
for d in data:
	sum_len += len(d)
print("Average length is ", sum_len/len(data))


new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print("Over length 100: ", len(new))
print(new[0])


good = []
for d in data:
	if 'good' in d:
		good.append(d)
print("Total ", len(good), "lines contains good")
print(good[0])