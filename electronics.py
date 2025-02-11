import cmath as cmath
import math as math
import types

import numpy as numpy

from engineering_notation import EngNumber

ROUNDED = 3


def parallel(*impedances):
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


def impedance_capacitor(w_rads, capacitance):
    return 1 / (1j * w_rads * capacitance)


def impedance_inductor(w_rads, inductance):
    return 1j * w_rads * inductance


vg = 48
ig = 10j
w = 1000
l1 = 9e-3
l2 = 8e-3
c1 = c2 = 1e-3
r1 = 10
r2 = 4
r3 = 1
r4 = 12
r5 = 12
r6 = 12
zc1 = impedance_capacitor(w, c1)
zc2 = impedance_capacitor(w, c2)
zl1 = impedance_inductor(w, l1)
zl2 = impedance_inductor(w, l2)
v1 = vg
z1 = r1 + zc1 + zl1
z2 = r2 + zl2
z3 = r3 + zc2
iv2 = (v1 / z3 - ig)
zv2 = parallel(z3, r5, r6, r4)
v2 = (v1 / z3 - ig) * parallel(z3, r5, r6, r4)
v3 = v1 + ig * parallel(z1, z2)
vc1 = (v3 - v1) / z1 * zc1
vc1t = rect_to_polar_rad(vc1)
i1 = (v1 - v3) / parallel(z1, z2) + (v1 - v2) / z3
svg = 1 / 2 * vg * i1.conjugate()
vth = v3 - v1
zth = z2
vz1 = vth * z1 / (z1 + zth)
sz1 = vz1 * vz1 / (2 * z1.conjugate())
print()
