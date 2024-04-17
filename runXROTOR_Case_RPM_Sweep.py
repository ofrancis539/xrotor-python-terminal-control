import subprocess

# Path to the XROTOR executable
xrotor_executable = "xrotor.exe"

# Input variables
name = "APC9x6"
propDat = "%s.dat" % (name)
rpms = [2500,
2750,
3000,
3250,
3500,
3750,
4000,
4250,
4500,
4750,
5000,
5250,
5500,
5750,
6000,
6250,
6500,
6750,
7000
]
diam = 9/39.37 #(meters)
adv_ratio_J = .001


for ind,rpm in enumerate(rpms):
    velo = rpm*diam*adv_ratio_J/60
    dataDat = "%s_%d_RPM_Sweep.dat" % (name,rpm)

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
    """ % (propDat,velo,rpm,dataDat)

    # Run XROTOR and communicate with it
    process = subprocess.Popen(xrotor_executable, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    process.communicate(xrotor_input)

