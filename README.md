![image](https://github.com/user-attachments/assets/3051cbf3-dde5-45c8-ac1a-64c4776ef226)Blueprint Generator: Room Layout Visualization Tool
Overview
The Blueprint Generator is a desktop application developed using Tkinter and Matplotlib, designed to create and visualize customizable room layouts for houses. Users can input room specifications such as plot dimensions, room types, and additional features (garage, garden) to generate multiple layout variations. The generated blueprints are displayed in a visual format for easy viewing and comparison.

This application is perfect for real estate professionals, architects, or anyone interested in visualizing different house layouts.

Features
Customizable Plot Dimensions: Enter the plot width and length to fit your desired layout.
Room Count Selection: Choose the number of bedrooms and bathrooms for your blueprint.
Additional Features: Toggle the inclusion of a garden and garage in the layout.
Multiple Layout Variations: Generate three different blueprint variations with a base layout and two design variations.
Room Visualization: Visual representation of rooms with color-coding for different room types (e.g., living room, kitchen, bedroom).
Navigation: Use "Previous" and "Next" buttons to easily browse through generated layouts.
Screenshots


![Screenshot 2025-01-20 181143](https://github.com/user-attachments/assets/7a9b4ecc-aebd-4f83-b1b3-2907a3c23454)


Main Interface

Blueprint Visualization

Prerequisites
To run the application, you need Python 3.x and the following Python libraries:

Tkinter (for building the GUI)
Matplotlib (for generating the graphical blueprint layout)
You can install the required dependencies using pip:

bash
Copy
Edit
pip install matplotlib
How to Run the Application
Download the Project:

Clone or download the repository files to your local machine.
Navigate to the Project Folder:

Use the terminal or command prompt to go to the folder where the Python file (blueprint_generator.py) is located.
Run the Script:

Execute the script using the following command:
bash
Copy
Edit
python blueprint_generator.py
Interact with the Application:

The GUI will open, allowing you to input room and plot specifications.
Click the "Generate Blueprints" button to generate layouts based on your input.
Navigate between layouts using the "Previous" and "Next" buttons.
Application Structure
Room Class:

Represents an individual room with attributes such as ID, name, position (x, y), size (width, length), and type (e.g., living room, bedroom).
Blueprint Class:

Represents the entire blueprint, including plot dimensions and a list of rooms.
BlueprintGenerator Class:

Manages the GUI, handles user input, and displays the blueprints. It contains methods for generating layouts and visualizing the designs.
Functions and Methods:

generate_id(): Generates unique IDs for each room.
generate_layouts(): Creates room layouts based on user specifications, including variations.
create_input_form(): Sets up the user input form for room specifications.
create_display_area(): Prepares the display area for visualizing the blueprint.
generate_blueprints(): Generates the blueprint layouts.
display_current_blueprint(): Displays the currently selected blueprint layout.
show_previous() and show_next(): Methods to navigate between different layouts.
Usage Instructions
Set Plot Dimensions:

Input the width and length of the plot (in feet).
Select Room Counts:

Choose the number of bedrooms (from 1 to 5) and bathrooms (from 1 to 4).
Toggle Additional Features:

Check the boxes to include a garden and/or garage in your layout.
Generate Blueprints:

Click the "Generate Blueprints" button to create and view three different layout options.
Browse Through Layouts:

Use the "Previous" and "Next" buttons to navigate through the generated blueprints.
License
This project is open-source and licensed under the MIT License. Feel free to modify, distribute, and use it as per your needs.

Contributing
Contributions are welcome! If you have any suggestions or improvements, feel free to fork the repository and submit a pull request.

Fork the repository.
Create a new branch for your feature or bugfix.
Make the necessary changes.
Submit a pull request with a detailed description of your changes.
Acknowledgments
Matplotlib for generating visual representations of the blueprints.
Tkinter for creating the graphical user interface.
UUID for generating unique identifiers for rooms.
