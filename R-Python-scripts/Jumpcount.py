#JumpExtractor.py: Extracts Markov jump counts from a full jump history log file.
#for other use, this script needs to update the source of discrete trait state, the input of the log file, and the count of steps in the log file. Here it is 6880.

def main():
    source = ['AF','EAP','ECA','LAC','MENA','NA','SAS','USA']

#    for clock in range(7):
    infile = open("H1N1-pdasub-trait_geo_compjumpHistory-comb.log", "r")
    count = {}
    for line in infile:
        jumps = line.split("},{")
        for i in jumps:
            packet = i.split(",")
            if packet[2]+" "+packet[3] in count:
                count[packet[2]+" "+packet[3]] += 1/6880
            else:
                count[packet[2]+" "+ packet[3]] = 1/6880
        for x in source:
            for y in source:
                if x != y:
                    if x+" "+y not in count:
                        count[x+" "+y] = 0
    report = list(count.items())
    report.sort()
    for item in report:
        locations, average = item
        print(locations,average)
    infile.close()

main()
