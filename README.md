# xrotor-python-terminal-control
Use Python scripts to run simulations in the XROTOR terminal

There are two main modes here: Velocity Sweeps or RPM Sweeps

Velocity Sweeps:
Run a series of velocities at a single rpm to determine Ct and Cp at each velocity/advance ratio

Files Required-
* newPropXROTOR.py
* initializeDataCSV_Vel_Sweep.py
* runXROTOR_Case_Vel_Sweep.py
* getDataXROTOR_Vel_Sweep.py

Steps-
1. Change all the inputs in newPropXROTOR.py and run
  #Path to the XROTOR executable
  xrotor_executable
  #Name of the propeller
  name
  #Number of blades
  numBlades
  #Velocity to create the propeller (1 is suggested)
  velo [meters/second]
  #Tip radius
  tipRadius [meters]
  #Hub radius
  hubRadius [meters]
  #Number of radial stations in the geometry data
  numRadialStations
  #All of the radial station data in format """ r/R   c/R   beta """  
  radStationData
2. Change all the inputs in initializeDataCSV_Vel_Sweep.py and run
  #Name of the propeller (same as step 1)
  name
  #File path to the csv outputted from step 1
  csv_file_path
3. Change all the inputs in runXROTOR_Case_Vel_Sweep.py and run
  #Path to the XROTOR executable (same as step 1)
  xrotor_executable
  #Name of the propeller (same as step 1)
  name
  #All of the velocities to run at in format [###,###,...]  
  velo [meters/second]
  #RPM to run at
  rpm
4. Change all the inputs in getDataXROTOR_Vel_Sweep.py and run
  #Name of the propeller (same as step 1)
  name
  #Path to the folder with all the files outputted from step 3
  folder_path
  #File path to the outputted csv from step 2
  csv_file_path


RPM Sweeps:
Run a series of RPMs at a single advance ratio (.001 for hover) to determine Ct and Cp at each RPM

Files Required-
* newPropXROTOR.py
* initializeDataCSV_RPM_Sweep.py
* runXROTOR_Case_RPM_Sweep.py
* getDataXROTOR_RPM_Sweep.py

Steps-
1. Change all the inputs in newPropXROTOR.py and run
  #Path to the XROTOR executable
  xrotor_executable
  #Name of the propeller
  name
  #Number of blades
  numBlades
  #Velocity to create the propeller (1 is suggested)
  velo [meters/second]
  #Tip radius
  tipRadius [meters]
  #Hub radius
  hubRadius [meters]
  #Number of radial stations in the geometry data
  numRadialStations
  #All of the radial station data in format """ r/R   c/R   beta """  
  radStationData
2. Change all the inputs in initializeDataCSV_RPM_Sweep.py and run
  #Name of the propeller (same as step 1)
  name
  #File path to the csv outputted from step 1
  csv_file_path
3. Change all the inputs in runXROTOR_Case_RPM_Sweep.py and run
  #Path to the XROTOR executable (same as step 1)
  xrotor_executable
  #Name of the propeller (same as step 1)
  name
  #All of the RPMs to run at in format [###,###,...]  
  rpms
  #Propeller diameter
  diam [meters]
  #Advance ratio to run at (.001 for hover)
  adv_ratio_J
4. Change all the inputs in getDataXROTOR_RPM_Sweep.py and run
  #Name of the propeller (same as step 1)
  name
  #Path to the folder with all the files outputted from step 3
  folder_path
  #File path to the outputted csv from step 2
  csv_file_path
