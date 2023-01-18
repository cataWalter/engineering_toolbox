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


x = (parallel([1 + 2j, 14j, 3 + 2j, 1 + 6j]))
print_complex(x)
print(cmath.rect(10, 1))
