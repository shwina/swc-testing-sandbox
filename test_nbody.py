from numpy.testing import *
from nbody import *

class TestNBody:
    def setup(self):
        offset_momentum(BODIES['sun'])

    def test_momentum_conservation(self):
        P1 = report_momentum()
        advance(0.01, 10)
        P2 = report_momentum()
        assert_allclose(P1, P2, rtol=0.01)

    def test_energy_conservation(self):
        E1 = report_energy()
        advance(0.01, 10)
        E2 = report_energy()
        assert_allclose(E1, E2, rtol=0.01)
