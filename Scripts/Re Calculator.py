
def main():
    a = float(input("Density of Fluid: "))
    b = float(input("Characteristic Length in meter (Chord Length for Airfoil): "))
    d = float(input("Dynamic Viscosity: "))

    print("1. Re to Flow Velocity\n2. Flow Velocity to Re")

    choice = input("\nChoose Mode of Operation: ")

    if choice == "1":
        Re = float(input("\nRe: "))
        v = (Re*d)/a*b
        print(f"Flow Velocity for Reynold's Number {Re: .1e} is {v: .2f} m/s")

    elif choice == "2":
        v = float(input("\nFlow Velocity: "))
        Re = (a*b*v)/d
        print(f"The Reynolds Number for a flow velocity of {v} m/s is {Re: .1e}")

main()