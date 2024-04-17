import subprocess

# Path to the XROTOR executable
xrotor_executable = "xrotor.exe"

# Input variables
name = "APC4_2x2"
propDat = "%s.dat" % (name)
velo = [10.33217929,
10.92995406,
11.54934481,
12.20189618,
12.81860837,
13.3933475,
14.00880077,
14.61554872,
15.30530531,
15.83306245,
16.47039958,
17.04489763
    ]
rpm = 15065

for ind,vel in enumerate(velo):
    dataDat = "%s_%d_%d_Vel_Sweep.dat" % (name,rpm,ind)

    # Input commands to XROTOR
    xrotor_input = """
    load %s
    oper
    velo
    %f
    rpm
    %d
    writ
    %s
    """ % (propDat,vel,rpm,dataDat)

    # Run XROTOR and communicate with it
    process = subprocess.Popen(xrotor_executable, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    process.communicate(xrotor_input)


