import os
def CheckMethodMonitor(File_Path):
    with open(File_Path, "r") as File:
        for Line in File:
            if Line.startswith('61,'):
                lastField = Line.split(">")[3]
                Method_name, data = lastField.split('|')
                one,two,three,four,five,six = data.split(' ')
		print("==============checking for {0}=============".format(Method_name))
		if (int(one) != int(six)):
                    print("{0} not equal to {1}".format(one,six))
		if (float(four) > float(five)):
                    print("Min Duartion {0} is greater then max duration {1}".format(four,five))
		print("=================Done=====================\n")
    return

def main():
    File_Path = str(raw_input("Please provide the absolute path for agg raw data file"))
    if not os.path.exists(File_Path):
        print("=============Not Valid File or path=========")
    else:
	CheckMethodMonitor(File_Path)

main()
