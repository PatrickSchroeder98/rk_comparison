import unittest
from math import e
from rk_comparison.core.analytical_module.nuclear_decay import NuclearDecay


class TestNuclearDecay(unittest.TestCase):
    """Tests for the NuclearDecay class."""

    def test_init(self):
        """Test to check constructor while creating the object."""
        nd = NuclearDecay()
        self.assertEqual(1.0, nd.tau)
        self.assertEqual(100.0, nd.nuclei)
        del nd

    def test_set_tau(self):
        """Test of setting tau value."""
        nd = NuclearDecay()
        nd.set_tau(5.0)
        self.assertEqual(5.0, nd.tau)
        del nd

    def test_get_tau(self):
        """Test of getting tau value."""
        nd = NuclearDecay()
        self.assertEqual(1.0, nd.get_tau())
        del nd

    def test_set_nuclei(self):
        """Test of setting nuclei value."""
        nd = NuclearDecay()
        nd.set_nuclei(500.0)
        self.assertEqual(500.0, nd.nuclei)
        del nd

    def test_get_nuclei(self):
        """Test of getting nuclei value."""
        nd = NuclearDecay()
        self.assertEqual(100.0, nd.get_nuclei())
        del nd

    def test_equation(self):
        """Test of nuclear decay differential equation."""
        nd = NuclearDecay()
        result = nd.equation(0.0, 100.0)
        self.assertEqual(-100.0, result)
        del nd

    def test_equation_analytical(self):
        """Test of nuclear decay analytical solution."""
        nd = NuclearDecay()
        result = nd.equation_analytical(1.0, -1.0)
        self.assertEqual(e, result)
        del nd


if __name__ == '__main__':
    unittest.main()
