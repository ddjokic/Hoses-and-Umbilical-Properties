#!/bin/env python
import inout
print ("Hoses and Umbilical Properties")
print ("Use maker's data, if available, instead of this calculation")
print("1 - Hoses")
print("2 - Umbilcals")
opt1=inout.get_integer("Choose 1 or 2: ", 0)
if opt1==1:
	print ("Calculating Hoses Properties")
	IDmm=inout.get_float("Enter hose inner diameter in mm or '0' for default of 100mm: ", 100.0)
	ID=IDmm/1000
	#calculating Outer Diameter
	HPod = 1.40*IDmm      #high pressure hoses
	LPod = 1.28*IDmm	  #low pressure hoses
	FFod = 1.34*IDmm      #fold-flat hoses
	#calculating mass per meter
	HPmass = 0.73253*ID  #high pressure hoses
	LPmass = 0.3642*ID   #low pressure hoses
	FFmass = 0.1844*ID   #fold-flat hoses
	#calculating Axial Stiffness
	HPas = ID*2.8*10**6  #high pressure hoses
	LPas = ID*3.4*10**6  #low pressure hoses
	FFas = ID*6.56*10**6 #fold-flat hoses
	#calculating Bending Stiffness
	HPbs = 30000*ID**4   #high pressure hoses
	LPbs = 600*ID**3     #low pressure hoses
	FFbs = 100*ID**3     #fold-flat hoses
	#writing results to a file "hoses.txt"
	fname='hoses.txt'
	fn=open(fname, 'a')
	inout.write_file(fn, "Inner Diameter of Hose [mm] : ", IDmm)
	fn.write("\n")
	fn.write("\nHigh Pressure Hoses Properties:")
	inout.write_file(fn, "Outer Diameter [mm]: ", HPod)
	inout.write_file(fn, "Mass per meter [t/m]: ", HPmass)
	inout.write_file(fn, "Axial Stiffness [kN]: ", HPas)
	inout.write_file(fn, "Bending Stiffness [kN*sqm]: ", HPbs)
	fn.write("\n")
	fn.write("\nLow Pressure Hoses Properties:")
	inout.write_file(fn, "Outer Diameter [mm]: ", LPod)
	inout.write_file(fn, "Mass per meter [t/m]: ", LPmass)
	inout.write_file(fn, "Axial Stiffness [kN]: ", LPas)
	inout.write_file(fn, "Bending Stiffness [kN*sqm]: ", LPbs)
	fn.write("\n")
	fn.write("\nFold - Flat Hoses Properties:")
	inout.write_file(fn, "Outer Diameter [mm]: ", FFod)
	inout.write_file(fn, "Mass per meter [t/m]: ", FFmass)
	inout.write_file(fn, "Axial Stiffness [kN]: ", FFas)
	inout.write_file(fn, "Bending Stiffness [kN*sqm]: ", FFbs)
	fn.close()
elif opt1==2:
	print ("Calculating Umbilical Properties")
	ODmm=inout.get_float("Enter Outer Diameter of umbilical in mm or '0' for default of 150mm: ", 150.0)
	OD=ODmm/1000
	#calculating mass per meter
	Mass = 1.8*OD**2
	#calculating Axial Stiffness
	AS = OD*1.44*10**6
	#calculating Bending Stiffness
	BS = 3000*OD**3
	fname='umbilical.txt'
	fn=open(fname, 'a')
	inout.write_file(fn, "Outer Diameter of Umbilical [mm] : ", ODmm)
	fn.write("\n")
	fn.write("\nUmbilical Properties:")
	inout.write_file(fn, "Mass per meter [t/m]: ", Mass)
	inout.write_file(fn, "Axial Stiffness [kN]: ", AS)
	inout.write_file(fn, "Bending Stiffness [kN*sqm]: ", BS)
	fn.close()
else:
	print("Invalid Choice - exit now")