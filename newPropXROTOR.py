import subprocess

# Path to the XROTOR executable
xrotor_executable = "xrotor.exe"

# Input variables
name = "APC4_2x2"
numBlades = 2
velo = 1.0 #meters/second
tipRadius = 0.05334 #meters
hubRadius = 0.00635 #meters
numRadialStations = 18

radStationData = """
0.15  0.2140  35.780
0.20  0.1994  36.563
0.25  0.1907  34.738
0.30  0.1851  30.893
0.35  0.1831  27.687
0.40  0.1848  25.230
0.45  0.1887  23.071
0.50  0.1921  21.292
0.55  0.1926  19.791
0.60  0.1904  18.511
0.65  0.1850  17.392
0.70  0.1767  16.467
0.75  0.1654  15.593
0.80  0.1515  14.841
0.85  0.1345  14.136
0.90  0.1141  13.437
0.95  0.0817  11.919
1.00  0.0032   7.128
"""


dataDat = "%s.dat" % (name)

# Input commands to XROTOR
xrotor_input = """
arbi
%d
%f
%f
%f
%d
%s
\n
\n
n
save %s
""" % (numBlades,velo,tipRadius,hubRadius,numRadialStations,radStationData,dataDat)

# Run XROTOR and communicate with it
process = subprocess.Popen(xrotor_executable, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
process.communicate(xrotor_input)
