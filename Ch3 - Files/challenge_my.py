# Solution to programming challenge for Learning Python course
# LinkedIn Learning Python course by Joe Marini
#
import os
from os import path

# create dir and open file
results_dir = "results"
os.makedirs(results_dir, exist_ok=True)
src = path.join(results_dir, "results.txt")

# get the size and list of files
files = ""
total_size = 0
list_files = os.listdir()
for i in list_files:
	if path.isfile(i):
		total_size = total_size + os.stat(i).st_size
		files = files + "\n" + i


# open file and append results
def write_results():
	my_file = open(src, "w+")
	my_file.write("Total size in bytes: " + str(total_size) + "\n" +
	              "Files list:\n" +
	              "-------------")
	my_file.write(files)
	my_file.close()


write_results()
