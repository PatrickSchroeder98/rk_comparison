import unittest
from unittest.mock import MagicMock, mock_open, patch
from rk_comparison.core.saving_module.save_data import SaveData
from rk_comparison.core.controller.controller import Controller

class TestSaveData(unittest.TestCase):
    """Tests for the SaveData class."""

    @patch('builtins.open', new_callable=mock_open)
    @patch('rk_comparison.core.saving_module.save_data.writer')
    def test_save(self, mock_writer, mock_open):
        """Tests the save method to ensure data is written correctly to the file."""
        mock_file = MagicMock()
        mock_open.return_value = mock_file
        mock_csv_writer = MagicMock()
        mock_writer.return_value = mock_csv_writer

        controller = Controller()
        save_data = SaveData()
        controller.rs.time = [0.0, 1.0, 2.0]
        controller.rs.resultAnalytical = [100.0, 80.0, 60.0]
        controller.rs.resultRK4 = [100.1, 80.1, 60.1]
        controller.cd.compareRK4 = [0.1, 0.1, 0.1]
        controller.cd.min_values = [0.0]
        controller.cd.max_values = [100.0]
        controller.cd.mean_values = [50.0]
        controller.id.truth_table = [
            False,
            False,
            False,
            True,
            False,
            False,
            False,
            False,
            False,
            False
        ]

        expected_result = [
            ["Time [s]", 0.0, 1.0, 2.0],
            ["Analytical [nuclei]", 100.0, 80.0, 60.0],
            ["", "", "", ""],
            ["RK4 [nuclei]", 100.1, 80.1, 60.1],
            ["", "", "", ""],
            ['Comparison RK4 [nuclei]', 0.1, 0.1, 0.1],
            ["", "", "", ""],
            ["Method", "RK4", "", ""],
            ["Minimal values", 0.0, "", ""],
            ["Maximal values", 100.0, "", ""],
            ["Mean values", 50.0, "", ""],
            ["", "", "", ""]
        ]
        save_data.prepare_data = MagicMock(return_value=expected_result)

        with open('test.csv', 'w', newline='') as file:
            save_data.save(file, controller)

        save_data.prepare_data.assert_called_once_with(controller)
        mock_csv_writer.writerow.assert_called_with([2.0, 60.0, '', 60.1, '', 0.1, '', '', '', '', '', ''])
        del save_data, controller

    def test_prepare_data(self):
        """Tests the prepare_data method to ensure it returns the correct list structure."""
        controller = Controller()
        save_data = SaveData()
        controller.rs.time = [0.0, 1.0, 2.0]
        controller.rs.resultAnalytical = [100.0, 80.0, 60.0]
        controller.rs.resultRK4 = [100.1, 80.1, 60.1]
        controller.cd.compareRK4 = [0.1, 0.1, 0.1]
        controller.cd.min_values = [0.0]
        controller.cd.max_values = [100.0]
        controller.cd.mean_values = [50.0]
        controller.id.truth_table = [
            False,
            False,
            False,
            True,
            False,
            False,
            False,
            False,
            False,
            False
        ]

        expected_result = [
            ["Time [s]", 0.0, 1.0, 2.0],
            ["Analytical [nuclei]", 100.0, 80.0, 60.0],
            ["", "", "", ""],
            ["RK4 [nuclei]", 100.1, 80.1, 60.1],
            ["", "", "", ""],
            ['Comparison RK4 [nuclei]', 0.1, 0.1, 0.1],
            ["", "", "", ""],
            ["Method", "RK4", "", ""],
            ["Minimal values", 0.0, "", ""],
            ["Maximal values", 100.0, "", ""],
            ["Mean values", 50.0, "", ""],
            ["", "", "", ""]
        ]
        result = save_data.prepare_data(controller)
        self.assertEqual(expected_result, result)
        del save_data, controller

    def test_add_results(self):
        """Tests the add_results method to ensure results are added correctly."""
        controller = Controller()
        save_data = SaveData()
        results = []
        controller.id.truth_table = [
            False,
            False,
            False,
            True,
            False,
            False,
            False,
            False,
            False,
            False
        ]
        controller.rs.resultRK4 = [100.0, 80.5, 61.0]

        save_data.add_results(controller, results, False)
        expected_results = [["RK4 [nuclei]", 100.0, 80.5, 61.0]]
        self.assertEqual(expected_results, results)
        del save_data, controller

    def test_add_results_comparison(self):
        """Tests the add_results method to ensure comparison results are added correctly."""
        controller = Controller()
        save_data = SaveData()
        results = []
        controller.id.truth_table = [
            False,
            False,
            False,
            True,
            False,
            False,
            False,
            False,
            False,
            False
        ]
        controller.cd.compareRK4 = [100.0, 80.5, 61.0]

        save_data.add_results(controller, results, True)
        expected_results = [["Comparison RK4 [nuclei]", 100.0, 80.5, 61.0]]
        self.assertEqual(expected_results, results)
        del save_data, controller

    def test_add_space(self):
        """Tests the add_space method to ensure space is added correctly."""
        save_data = SaveData()
        results = [["Data", 1.0, 2.0]]
        whitespaces_count = 3

        save_data.add_space(results, whitespaces_count)
        expected_results = [["Data", 1.0, 2.0], ["", "", ""]]
        self.assertEqual(results, expected_results)
        del save_data

    def test_add_statistics_descriptions(self):
        """Tests the add_statistics_descriptions method to ensure descriptions are added correctly."""
        controller = Controller()
        save_data = SaveData()
        results = []
        controller.id.truth_table = [
            False,
            False,
            False,
            True,
            False,
            False,
            False,
            False,
            False,
            False
        ]

        save_data.add_statistics_descriptions(controller, results, 3)
        expected_results = [["Method", "RK4", ""]]
        self.assertEqual(expected_results, results)
        del save_data, controller

    def test_add_statistics(self):
        """Tests the add_statistics method to ensure statistics are added correctly."""
        save_data = SaveData()
        results = []
        statistics_result = [0.0, 1.0, 2.0]
        name = "Test Statistics"
        whitespaces_count = 5

        save_data.add_statistics(results, statistics_result, name, whitespaces_count)
        expected_results = [["Test Statistics", 0.0, 1.0, 2.0, ""]]
        self.assertEqual(expected_results, results)
        del save_data


if __name__ == '__main__':
    unittest.main()
