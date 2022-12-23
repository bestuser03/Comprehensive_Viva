# reverse read

f1 = open("merge.txt", "w")

with open("test.txt", "r") as myfile:
	data = myfile.read()

data_1 = data[::-1]

f1.write(data_1)

f1.close()
