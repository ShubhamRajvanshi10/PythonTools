import os
def FindMergeRecord(File_Path):
    with open(File_Path, 'r') as RF:
        for line in RF:
            if line.startswith("4,"):
                eventID,FPID,Status,Category,five,six,seven,SQB = line.split(",")
		print("event ID {0} and FPID {1}".format(eventID,FPID))
	    if line.startswith("3,"):
	        Event,FPID,SQB = line.split(",")
	        print("event ID {0} and FPID {1}".format(Event,FPID))
    return

def main():
    File_Path = raw_input("Please provide the Full Path of file")
    FindMergeRecord(File_Path)

main()	
