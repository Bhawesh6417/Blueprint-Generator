import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
import string
import uuid

class Room:
    def __init__(self, id, name, x, y, width, length, room_type):
        self.id = id
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.length = length
        self.type = room_type

class Blueprint:
    def __init__(self, id, width, length, rooms):
        self.id = id
        self.width = width
        self.length = length
        self.rooms = rooms

def generate_id():
    return str(uuid.uuid4())[:8]

def generate_layouts(specs):
    blueprints = []
    
    for i in range(3):
        rooms = []
        current_x = 0
        current_y = 0
        
        # Calculate base layout width
        base_width = 35  # Living room (20) + Kitchen (15)
        total_width = base_width + 20 if specs['has_garage'] else base_width
        
        # Living room
        rooms.append(Room(
            generate_id(),
            'Living Room',
            current_x,
            current_y,
            20,
            20,
            'living'
        ))
        
        # Kitchen
        rooms.append(Room(
            generate_id(),
            'Kitchen',
            current_x + 20,
            current_y,
            15,
            15,
            'kitchen'
        ))
        
        # Garage
        if specs['has_garage']:
            rooms.append(Room(
                generate_id(),
                'Garage',
                base_width,
                current_y,
                20,
                22,
                'garage'
            ))
        
        # Bedrooms
        bedroom_start_x = current_x
        for b in range(specs['bedrooms']):
            rooms.append(Room(
                generate_id(),
                f'Bedroom {b + 1}',
                bedroom_start_x + (b * 15),
                current_y + 20,
                15,
                12,
                'bedroom'
            ))
        
        # Bathrooms
        bathroom_start_x = current_x
        for b in range(specs['bathrooms']):
            rooms.append(Room(
                generate_id(),
                f'Bathroom {b + 1}',
                bathroom_start_x + (b * 10),
                current_y + 32,
                8,
                10,
                'bathroom'
            ))
        
        # Garden
        if specs['has_garden']:
            rooms.append(Room(
                generate_id(),
                'Garden',
                current_x,
                current_y + 42,
                total_width,
                15,
                'garden'
            ))
        
        # Create layout variations
        if i > 0:
            for room in rooms:
                if i == 1:
                    # Second layout: shift rooms slightly right and compress vertically
                    room.x += 3
                    room.y = room.y * 0.9
                else:
                    # Third layout: mirror the layout horizontally
                    room.x = total_width - (room.x + room.width)
        
        blueprints.append(Blueprint(
            generate_id(),
            max(specs['plot_width'], total_width + 5),
            specs['plot_length'],
            rooms
        ))
    
    return blueprints

class BlueprintGenerator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Blueprint Generator")
        self.root.geometry("1200x800")
        
        self.create_input_form()
        self.create_display_area()
        self.blueprints = []
        self.current_blueprint_index = 0
        
    def create_input_form(self):
        input_frame = ttk.Frame(self.root, padding="10")
        input_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Plot dimensions
        ttk.Label(input_frame, text="Plot Width (ft):").grid(row=0, column=0, sticky=tk.W)
        self.plot_width = ttk.Entry(input_frame)
        self.plot_width.insert(0, "40")
        self.plot_width.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(input_frame, text="Plot Length (ft):").grid(row=1, column=0, sticky=tk.W)
        self.plot_length = ttk.Entry(input_frame)
        self.plot_length.insert(0, "60")
        self.plot_length.grid(row=1, column=1, padx=5, pady=5)
        
        # Room counts
        ttk.Label(input_frame, text="Number of Bedrooms:").grid(row=2, column=0, sticky=tk.W)
        self.bedrooms = ttk.Spinbox(input_frame, from_=1, to=5, width=5)
        self.bedrooms.set(2)
        self.bedrooms.grid(row=2, column=1, padx=5, pady=5)
        
        ttk.Label(input_frame, text="Number of Bathrooms:").grid(row=3, column=0, sticky=tk.W)
        self.bathrooms = ttk.Spinbox(input_frame, from_=1, to=4, width=5)
        self.bathrooms.set(2)
        self.bathrooms.grid(row=3, column=1, padx=5, pady=5)
        
        # Additional features
        self.has_garden = tk.BooleanVar(value=True)
        ttk.Checkbutton(input_frame, text="Include Garden", variable=self.has_garden).grid(row=4, column=0, columnspan=2, pady=5)
        
        self.has_garage = tk.BooleanVar(value=True)
        ttk.Checkbutton(input_frame, text="Include Garage", variable=self.has_garage).grid(row=5, column=0, columnspan=2, pady=5)
        
        # Generate button
        ttk.Button(input_frame, text="Generate Blueprints", command=self.generate_blueprints).grid(row=6, column=0, columnspan=2, pady=20)
        
        # Navigation buttons
        self.nav_frame = ttk.Frame(input_frame)
        self.nav_frame.grid(row=7, column=0, columnspan=2, pady=10)
        ttk.Button(self.nav_frame, text="Previous", command=self.show_previous).pack(side=tk.LEFT, padx=5)
        ttk.Button(self.nav_frame, text="Next", command=self.show_next).pack(side=tk.LEFT, padx=5)
        
    def create_display_area(self):
        self.display_frame = ttk.Frame(self.root, padding="10")
        self.display_frame.grid(row=0, column=1, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        self.figure, self.ax = plt.subplots(figsize=(10, 8))
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.display_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
    def generate_blueprints(self):
        specs = {
            'plot_width': int(self.plot_width.get()),
            'plot_length': int(self.plot_length.get()),
            'bedrooms': int(self.bedrooms.get()),
            'bathrooms': int(self.bathrooms.get()),
            'has_garden': self.has_garden.get(),
            'has_garage': self.has_garage.get()
        }
        
        self.blueprints = generate_layouts(specs)
        self.current_blueprint_index = 0
        self.display_current_blueprint()
        
    def display_current_blueprint(self):
        if not self.blueprints:
            return
            
        self.ax.clear()
        blueprint = self.blueprints[self.current_blueprint_index]
        
        # Plot outline
        self.ax.add_patch(plt.Rectangle((0, 0), blueprint.width, blueprint.length,
                                      fill=False, color='black', linewidth=2))
        
        # Room colors
        colors = {
            'living': 'lightblue',
            'kitchen': 'lightgreen',
            'bedroom': 'lightpink',
            'bathroom': 'lavender',
            'garage': 'lightgray',
            'garden': 'palegreen'
        }
        
        # Draw rooms
        for room in blueprint.rooms:
            self.ax.add_patch(plt.Rectangle((room.x, room.y), room.width, room.length,
                                          fill=True, color=colors.get(room.type, 'white')))
            self.ax.add_patch(plt.Rectangle((room.x, room.y), room.width, room.length,
                                          fill=False, color='black'))
            
            # Add room labels
            self.ax.text(room.x + room.width/2, room.y + room.length/2,
                        f'{room.name}\n{room.width}\'x{room.length}\'',
                        ha='center', va='center', wrap=True)
        
        self.ax.set_xlim(-5, blueprint.width + 5)
        self.ax.set_ylim(-5, blueprint.length + 5)
        self.ax.set_aspect('equal')
        self.ax.set_title(f'Blueprint {self.current_blueprint_index + 1}/3')
        self.canvas.draw()
        
    def show_previous(self):
        if self.blueprints:
            self.current_blueprint_index = (self.current_blueprint_index - 1) % len(self.blueprints)
            self.display_current_blueprint()
            
    def show_next(self):
        if self.blueprints:
            self.current_blueprint_index = (self.current_blueprint_index + 1) % len(self.blueprints)
            self.display_current_blueprint()
            
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = BlueprintGenerator()
    app.run()
