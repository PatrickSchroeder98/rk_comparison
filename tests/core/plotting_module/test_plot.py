import unittest
from unittest import mock

from rk_comparison.core.plotting_module.plot import Plot


class TestPlot(unittest.TestCase):
    """Tests for the Plot class."""

    @mock.patch("rk_comparison.core.plotting_module.plot.plt")
    def test_plot(self, mock_plt):
        """Tests the standard plot method."""
        pl = Plot()
        x = [0.0, 1.0, 2.0]
        y = [[1.0, 2.0, 3.0]]
        legend = "Test Legend"
        title = "Test Title"
        x_label = "Test X"
        y_label = "Test Y"
        pl.plot(x, y, x_label, y_label, legend, title)
        mock_plt.plot.assert_called_once_with([0.0, 1.0, 2.0], [1.0, 2.0, 3.0])
        mock_plt.title.assert_called_once_with("Test Title")
        mock_plt.xlabel.assert_called_once_with("Test X")
        mock_plt.ylabel.assert_called_once_with("Test Y")
        mock_plt.legend.assert_called_once_with("Test Legend")
        mock_plt.show.assert_called_once()

    @mock.patch("rk_comparison.core.plotting_module.plot.plt")
    def test_plot_bar(self, mock_plt):
        """Tests the standard plot method."""
        pl = Plot()
        x = [3.0, 2.0, 1.0]
        y = ["RK1", "RK2", "RK3"]
        title = "Test Title"
        x_label = "Test X"
        y_label = "Test Y"
        pl.plot_bar(x, y, x_label, y_label, title)
        mock_plt.bar.assert_called_once_with([3.0, 2.0, 1.0], ["RK1", "RK2", "RK3"])
        mock_plt.title.assert_called_once_with("Test Title")
        mock_plt.xlabel.assert_called_once_with("Test X")
        mock_plt.ylabel.assert_called_once_with("Test Y")
        mock_plt.show.assert_called_once()


if __name__ == "__main__":
    unittest.main()
