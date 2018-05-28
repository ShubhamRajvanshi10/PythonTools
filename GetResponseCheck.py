import os

def main():
  GetResponseID = 18
  cmd = "grep '^2,' DotNet_ISP9922E_nzperf_K* | grep -o '[0-9]*:[0-9]*:[0-9]*' | cut -d ':' -f2"
  #print(cmd)
  ParentFps = os.popen(cmd).read()
  #print(ParentFps)
  for FP in ParentFps.splitlines():
    #print(FP)
    FindSQB="grep '{0}' * | grep -o '_T[0-9]*:[0-9]*:[0-9]*:[1]:[0-9]*'".format(FP)
    FpDetails=os.popen(FindSQB).read()
    if FpDetails == "":
      print FP
    #print(FpDetails)
    #for Fpline in FpDetails:
      #print Fpline
      #FPID, SQB = Fpline.split(",")
      #print(FPID)'''
  return


main()
