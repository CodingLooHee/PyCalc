from pycalc.general import rad2deg, deg2rad
from math import isclose


class TestAngleConverion:
    def test_rad2deg(self):
        assert isclose(rad2deg(1), 57.2957795, rel_tol=1e-06)

    def test_deg2rad(self):
        assert isclose(deg2rad(1), 0.0174532925, rel_tol=1e-06)
