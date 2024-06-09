import cmath as cmath
import math as math
import types

import numpy as numpy

from engineering_notation import EngNumber


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


def get_main_variables():
    # Get the dictionary of current local variables
    current_vars = locals().copy()

    # We do not want to print the function itself
    exclude_keys = ['get_main_variables']

    # Filter out the function and other internal attributes
    main_vars = {k: v for k, v in current_vars.items() if
                 k not in exclude_keys and not k.startswith('__')}

    return main_vars


def format_value(value):
    if isinstance(value, float):
        # Check if the number is in engineering notation
        if 'e' in f"{value}":
            return f"{value:.3e}"
        return f"{value:.3f}"
    elif isinstance(value, complex):
        real_part = f"{value.real:.3e}" if 'e' in f"{value.real}" else (fvalue.real:.3f}")
        imag_part = f"{value.imag:.3e}" if 'e' in f"{value.imag}" \
            else f"{value.imag:.3f}"
        return f"{real_part} + {imag_part}j"
    elif isinstance(value, (list, tuple)):
        return [format_value(v) for v in value]
    elif isinstance(value, dict):
        return {k: format_value(v) for k, v in value.items()}
    else:
        return value


q = 1
eps0 = 8.85e-12
eps1 = eps0 * 10
eps2 = eps0 * 2
L = 1
Z = 1 + 2j
Z1 = parallel([Z, Z, Z])

global_vars = globals().copy()
exclude_keys = list(__builtins__.__dict__.keys()) + ['get_global_variables',
                                                     'main', '__builtins__']
filtered_globals = {k: format_value(v) for k, v in global_vars.items()
                    if k not in exclude_keys and not k.startswith('__') and
                    not isinstance(v, (
                        types.ModuleType, types.FunctionType, type))}
for name, value in filtered_globals.items():
    print(f"{name} = {value}")
