import os

def main():
  FinishPipeLineID=19
  cmd = "grep '^4,' Store* | cut -d ',' -f2 "
  FPIDS = os.popen(cmd).read()
  for FP in FPIDS.splitlines():
    #print("Checking for FP - " + FP)
    cmdCheck = "grep '{0}' Store* | grep -o '_{1}:[0-9]*_0_[0-9]*' ".format(FP, FinishPipeLineID)
    status = os.popen(cmdCheck).read()
    if status == "":
      print(FP)
  return

main()
