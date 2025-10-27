
import math

ad = float(input("Angle of Attack in Degrees: "))
ar = math.radians(ad)
sv = math.sin(ar)
cv = math.cos(ar)
v = float(input("Velocity in m/s: "))

Vx = v*cv                   #Velocity Component along X-axis
Vy = v*sv                   #Velocity Component along Y-axis

Ls = -1*sv                  #Negative operator for Lift Vector

print(f"X Component for Velocity = {Vx:.4f}")
print(f"Y Component for Velocity = {Vy:.4f}")
print("\nForce Vector for Drag: ")
print(f"X = {cv:.4f}     Y = {sv:.4f}")
print("\nForce Vector for Lift: ")
print(f"X = {Ls:.4f}     Y = {cv:.4f}")

