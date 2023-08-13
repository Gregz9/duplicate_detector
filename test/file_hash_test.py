import hashlib

data_file = open("test_files/random_data1.txt", "r")

print(data_file.name)

data = data_file.read()

file_hash = hashlib.sha256(data.encode("utf-8")).hexdigest()
print(file_hash)
data_file.close()

data2 = open("test_files/random_data1.txt", "rb")

file_hash = hashlib.file_digest(data2, "sha256")
print(file_hash.hexdigest())

data2.close()

data2.close()
