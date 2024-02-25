print("Calculate velocity(v)")
s = float(input("Distance(km unit & at least 1 km) : "))
if s < 1 :
    s = 1
t = float(input("Time(hr unit & at least 1 hr) : "))
if t < 1 :
    t = 1
v = s/t
print("Velocity =",v,"km/hr")
