import os
import optparse
def Generate_MM(Controller_Name, TestRun_Number, Instr_Path):
	Instr_File = open(Instr_Path, 'r')
	Instr_Prof = Instr_File.readlines()
	Instr_File.close()
	print("Getting data from database")
	cmd="/home/netstorm/{0}/bin/ndi_get_entity_time_ex --testrun {1} --status -2 --entity 0".format(Controller_Name,TestRun_Number)
	output = os.popen(cmd).read()
	if output == "":
		print("{} <- QUERY NOT GIVING OUTPUT".format(cmd))
		return
	print("got data from database")
	with open('MethodMonitor_WithOneMS.txt','w+') as IP:
		MM_Count = 0
		for TRL in output.splitlines():
        		#one,two,FQM,four,five,six,seven,Avg,nine,ten,elevan,twalve,thirteen=TRL.split('|')
			splittedValues = TRL.split('|')
			FQM = splittedValues[2]
			Avg = splittedValues[4]
			#print FQM
			#print Avg
			if Avg == "total_self_time_in_ms":
				pass
			else:
				Avg = float(Avg)
				if Avg >= 1:
					if FQM == "Entity Name":
						pass
					else:
						FQC,Method = FQM.rsplit('.', 1)
						Method_Line = "{0}|{1}|".format(FQC,Method)
						for IPL in Instr_Prof:
							if Method_Line in IPL:
								if FQC.startswith('System.') or FQC.startswith('mscorlib.'):
									pass
								else:
									#IP.write(IPL)
									PackageName = IPL.split("|" , 1)[0]
									IP.write(PackageName + "|" + Method + "_" + str(MM_Count) + "|" + FQC + "." + Method + "||||| \n")
									MM_Count = MM_Count + 1

	return

def main():
	parser = optparse.OptionParser("Usage %prog" + " -C <Controller Name>" + " -T <Test run number>" + " -I <InstrumentationProfilePath>")
	parser.add_option("-C", dest="Controller_Name", type="string", help="Provide exact controller name")
	parser.add_option("-T", dest="TestRun_Number", type="string", help="Provide TestRun Number")
	parser.add_option("-I", dest="Instr_Path", type="string", help="Instr Profile Path")
	(options, args) = parser.parse_args()
	Controller_Name=str(options.Controller_Name)
	TestRun_Number=str(options.TestRun_Number)
	Instr_Path=str(options.Instr_Path)
	Des_Path = ''
	if (Controller_Name == "None") or (TestRun_Number == "None") or (Instr_Path == "None"):
		print("Usage-> python Gen_MethodMonitor.py -C <Controller Name> -T <TestRun number> -I <InstrumentationProfilePath>")
	else:
		Des_Path = os.path.join("/home/netstorm/" + Controller_Name + "/logs/TR" + TestRun_Number)
		if not os.path.exists(Des_Path):
			print("Test Run path is not valid = {0} ".format(Des_Path))
		else:
			if os.path.exists(Instr_Path) and os.path.getsize(Instr_Path) > 0:
				#print "AllFine"
				Generate_MM(Controller_Name, TestRun_Number, Instr_Path)
			else:
				print ("Not a valid path or file is empty==> {}".format(Instr_Path))
	return

if __name__ == '__main__':
	main()		
