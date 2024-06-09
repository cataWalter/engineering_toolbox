import cmath as cmath
import math as math
import numpy as numpy
from engineering_notation import EngNumber

ROUNDED = 5


def parallel(impedances):
    res = 0
    for impedance in impedances:
        res += 1 / impedance
    res = 1 / res
    return res


def millman(currents, impedances):
    res = sum(currents) * parallel(impedances)
    return res


def complex_power(voltage, current):
    return 1 / 2 * voltage * numpy.conj(current)


def polar_rad_to_rect(mod, ph_rad):
    return cmath.rect(mod, ph_rad)


def polar_deg_to_rect(mod, ph_deg):
    return cmath.rect(mod, math.radians(ph_deg))


def rect_to_polar_rad(z):
    return cmath.polar(z)


def rect_to_polar_deg(z):
    return cmath.polar(z)[0], math.degrees(cmath.polar(z)[1])


def print_complex(z):
    mod = cmath.polar(z)[0]
    phase = cmath.polar(z)[1]
    print("mod = " + str(round(mod, ROUNDED)))
    print("phase = " + str(round(phase, ROUNDED)) + " rad")
    print("phase = " + str(round(math.degrees(phase), ROUNDED)) + " deg")


def print_voltage_capacitor(vc_0, vc_inf, Req, C):
    print("tau (time constant) = " + EngNumber(Req * C) + "s")
    print("vc(t) = " + str(vc_inf) + "(" + str(vc_0 - vc_inf) + ")exp(-t/tau)")


d0 = 5e-2
D0 = 5.32e-2
t0 = 20
alp1 = 24e-6
alp2 = 29e-6

tf1 = t0 + (D0 - d0) / (d0 * alp1)
tf2 = t0 + ((D0 - d0) / (d0 * alp1 - D0 * alp2))
tf3 = -9314
print()
"""
v0 = 2e-3
h = 10
t0 = 277
p0 = 2e5
p1 = 1e5
t1 = 22 + 273
R = 8.314

n = p0 * v0 / R / t0
v1 = n * R * t1 / p1*1e3





m1 = 0.1
t1 = 20
m2 = 0.055
t2 = 40
tf1 = 25
c1 = 4186
c2 = m1 * c1 * (tf1 - t1) / (m2 * (t2 - tf1))
Q = 76.5e3
tf2 = 78
y2 = (Q - m1 * c1 * (tf2 - tf1) - m2 * c2 * (tf2 - tf1)) / m2
z2 = y2*1e-3
"""
