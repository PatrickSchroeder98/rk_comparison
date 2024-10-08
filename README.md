# RK and FRK comparison

This is a project created to compare the Runge-Kutta and Runge-Kutta-Fehlberg methods while solving the nuclear decay problem. 

## Features

User can choose which methods to use, set the input data and make calculations using the PyQt6 interface. Various plots with output data can be displayed. Saving to .csv file writes the current output data to spreadsheet.

## Project Structure

* analytical_module: Contains classes for equations and numerical methods.
* controller: Class that acts as the controller, similar to the MVC model.
* data: Classes used to hold data structures.
* exceptions: Classes that define custom exceptions and validations required for the application to function properly.
* plotting_module: Contains classes with methods for creating various plots.
* saving_module: Class responsible for saving data to files.
* interface: Classes that build the GUI using PyQt6 libraries.
* tests: Contains classes with tests for methods from all modules.

## Tests  
The project includes a comprehensive set of unit tests written using the unittest library to ensure that the all modules are working correctly and are handling edge cases properly.  

## Documentation  
The full documentation can be found on the [Software Documentation Website](https://patrickschroeder98.github.io/software_documentation/rk_comparison_docs/index.html).  
Or in the website [repository](https://github.com/PatrickSchroeder98/software_documentation/tree/main/rk_comparison_docs).  
The documentation also includes a [full code documentation](https://patrickschroeder98.github.io/software_documentation/rk_comparison_docs/sphinx_docs/index.html) generated by Sphinx. 
