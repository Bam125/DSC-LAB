#--------------------------------------------------------------------------
# LE. 1.1
# ME 144L - Spring 2024

#--------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression 

#LE Question 1 - Linear Regression
#--------------------------------------------------------------------------
# Data Values np.array([148,482,831]).reshape((-1,1))
Angle = np.array([-1.57,-1.26,-0.94,-0.63,-0.31,0.0,0.31,0.65,0.96,1.23,1.52]).reshape((-1,1)) 
#In Radians, is the "y" variable.

Voltage = np.array([1.176,1.648,1.874,2.175,2.438,2.503,2.925,3.067,3.450,3.686,4.014]).reshape((-1,1))
#In Volts, is the "x" variable.

# Linear Regression
model    = LinearRegression().fit(Voltage,Angle)
Rsquared = model.score(Voltage,Angle)
slope, intercept = model.coef_, model.intercept_
print("LE 1.1, Q1 Requested Values:")
print("\n")
print('Intercept =', intercept, 'Radians')
print('Slope =', slope, 'Radians/Volt')
print('Coefficient of Determination [R\u00b2 value]] =', Rsquared)
print("\n")
print("\n")



# Plot the raw data and regression using a scatter plot
plt.figure(1)
plt.scatter(Voltage,Angle, c="r", marker='.')
plt.plot(Voltage,slope*Voltage + intercept)
plt.xlabel('Voltage [Volts]')
plt.ylabel('Angle [Rads]')
plt.legend(['Raw Data','Lin. Reg.'])
plt.title('LE 1.1 Question 1 - Angle vs. Voltage Linear Regression')
plt.grid()
plt.show()

#LE Question 2 - Measure the force-deflection curve for a bungee cord.

# Raw Data arrays (do not adjust)
Mass     = np.array([0,50,100,200,300,400,500,700,900,1000,1133]).reshape(-1, 1) # [g]
L_bungee = np.array([8.75,8.875,8.925,8.95,8.975,9,9.375,11.125,13.25,14,15.5]).reshape(-1, 1) #[in]

#-------------------------------------------------------------------------------------------------------
# Begin code updates here
# All code required can be found in the Lab1_Python_Basics.py file from Lab Work
#-------------------------------------------------------------------------------------------------------

# Convert bungee data from [in] to [mm]
L_mm = L_bungee*25.4

# Solve for Force --> convert mass from [g] to [kg] and multiply by gravity, 9.81 [m/s^2]
Force  = (Mass/1000)*9.81

# Solve for Delta Length by subtracting equilibrium length from all L_mm values
DeltaL = L_mm-(8.75*25.4)

# Plot data to see where change in K1 and K2 occurs
plt.figure(2)
plt.scatter(DeltaL,Force)
plt.xlabel('Length [mm]')
plt.ylabel('Force [N]')
plt.title('Force vs Length')
plt.grid()
plt.show()

# Looking at plot, it seems the K1 to K2 change occurs at the ___ data point

# Set this equal to the value at which K1 & K2 change
its =  6


# Separate K1 and K2 data sets
X_k1, Y_k1 = DeltaL[0:its], Force[0:its]
X_k2, Y_k2 = DeltaL[its-1:], Force[its-1:] # its-1 allows for some overlap

# Apply linear regression to K1 Subset
# Linear Regression: For K1, use X_k1 and Y_k1 data (data does not require reshaping)
# Solve for slope_k1, int_k1, and Rs_k1 (Rs is the R^2 value)

model    = LinearRegression().fit(X_k1,Y_k1)
Rs_k1 = model.score(X_k1,Y_k1)
slope_k1, int_k1 = model.coef_, model.intercept_

print("LE 1.1, Q2 Requested Values:")
print("\n")
print('k1 intercept [N] =', int_k1)
print('k1 slope [N/mm] =', slope_k1)
print('k1 R\u00b2 =', Rs_k1)
print("\n")


# Apply linear regression to K2 Subset
# Linear Regression: For K2, use X_k2 and Y_k2 data (data does not require reshaping)
# Solve for slope_k2, int_k2, and Rs_k2 (Rs is the R^2 value)

model    = LinearRegression().fit(X_k2,Y_k2)
Rs_k2 = model.score(X_k2,Y_k2)
slope_k2, int_k2 = model.coef_, model.intercept_

print('k2 intercept [N] =', int_k2)
print('k2 slope [N/mm] =', slope_k2)
print('k2 R\u00b2 =', Rs_k2)


#-------------------------------------------------------------------------------------------------------
# End of code updates
#-------------------------------------------------------------------------------------------------------
# Plot the raw data and regression using a scatter plot
# Plot can be updated as desired
plt.figure()
plt.scatter(DeltaL,Force, c="r", marker='x')
plt.plot(X_k1,slope_k1*X_k1 + int_k1)
plt.plot(X_k2,slope_k2*X_k2 + int_k2)
plt.xlabel('Length [mm]')
plt.ylabel('Force [N]')
plt.legend(['Raw Data','K1 Reg.','K2 Reg.'])
plt.title('LE 1.1 Question 2 - Regressions of Bungee Data')
plt.grid()
plt.show()









