import os
import optparse

def WriteServer(TierID,S_ServerValue,S_InstanceValue):
  with open('Server.conf', 'a') as S:
    for ServerID in range(2,(S_ServerValue + 2)):
      S.write('10.10.30.6' + str(ServerID) + '|Server' + str(ServerID) + '|' + str(ServerID) + '|' + str(TierID) + '|1|NA|root|abeona|/apps/java|/opt/cavisson/monitors|N|Windows|0|01/06/18 12:00:59|1527010943434|1517483514189|1' + '\n')
      WriteInstance(TierID,ServerID,S_InstanceValue)
  return


def WriteInstance(I_TierID,I_ServerID,I_InstanceCount):
  with open('Instance.conf', 'a') as I:
    for InstanceID in range(1,(I_InstanceCount + 1)):
      I.write('Instance' + str(InstanceID) + '|Trade' + str(InstanceID) + '|appinstance|DotNet|' + str(InstanceID)  + '|' + str(I_ServerID) + '|' + str(I_TierID)  + '|netstorm|xxxx|app1|0|0|1.6|1|pattern|filename|01/06/18 12:00:59|1527010943434|1519311942845|1|1' + '\n')
  return

def WriteTier(TierValue,ServerValue,InstanceCount):
  with open('Tier.conf', 'a') as T:
    T.write("#TierName|Tier Id|Tier Description|NA|NA" + "\n" + "Cavisson|0|Cavisson tier|NA|NA " + "\n" + "Default|999|Default|0|NA" + "\n")
    for i in range(1,(TierValue + 1 )):
      T.write("Tier" + str(i) + "|" + str(i) + "|Tier Description|NA|NA" + "\n")
      WriteServer(i,ServerValue,InstanceCount)
  return



def main():
  parser = optparse.OptionParser("Usage %prog" + " -T <Tier Count>" + " -S <Server Count>" + " -I <Instance Count>")
  parser.add_option("-T", dest="TierCount", type="int", help="Provide the total Tier count")
  parser.add_option("-S", dest="ServerCount", type="int", help="Provide the total Server count")
  parser.add_option("-I", dest="InstanceCount", type="int", help="Provide the total Instance count")
  (options, args) = parser.parse_args()
  TierValue=int(options.TierCount)
  ServerValue=int(options.ServerCount)
  InstanceValue=int(options.InstanceCount)
  if (TierValue == "None") or (ServerValue == "None") or (InstanceValue == "None"):
    print('Usage-> python GenTopology.py -T <Tier Count> -S <Server Count> -I <Instance Count>')
  else:
    Server = ServerValue/TierValue
    Instance = InstanceValue/ServerValue
    WriteTier(TierValue,Server,Instance)
  return

main()

