import tkinter as tk
from tkinter import font, messagebox
import pygame

class MenuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Game Menu")
        self.bg_color = "#0c0c0c"  # Dark background to simulate an old computer screen
        self.settings_bg_color = "#2e2e2e"  # Dark grey background for the settings page
        self.brightness_factor = 50  # Initial brightness factor
        self.is_fullscreen = True
        self.music_volume = 50  # Initial music volume

        # Initialize pygame for music control
        pygame.mixer.init()
        pygame.mixer.music.load('C:/Users/hussa/Downloads/background_music.mp3')  # Load your music file
        pygame.mixer.music.set_volume(self.music_volume / 100)  # Set the initial volume
        pygame.mixer.music.play(-1)  # Play the music indefinitely

        # Initialize screen stack
        self.screen_stack = []

        # Configure the main window
        self.root.configure(bg=self.bg_color)
        self.root.attributes('-fullscreen', self.is_fullscreen)

        # Fonts for buttons and logo
        self.button_font = font.Font(family='Arial', size=16, weight='bold')
        self.large_button_font = font.Font(family='Arial', size=24, weight='bold')
        self.logo_font = font.Font(family='hint-retrò_free-version', size=150, weight='bold')
        self.section_font = font.Font(family='hint-retrò_free-version', size=36, weight='bold')
        self.settings_font = font.Font(family='hint-retrò_free-version', size=15, weight='bold')

        # Create and configure the main menu
        self.create_main_menu()

    def create_main_menu(self):
        # Create main frame for center alignment
        self.main_frame = tk.Frame(self.root, bg=self.bg_color)
        self.main_frame.pack(fill="both", expand=True)

        # Centered ESC Logo at the top
        self.esc_logo = tk.Label(self.main_frame, text=">-ESC.", font=self.logo_font, bg=self.bg_color, fg="#c83d3d")
        self.esc_logo.pack(pady=(30, 80))

        # Define button texts and dimensions
        buttons = [
            ("Play", 200),
            ("Credits", 200),
            ("Settings", 200),
            ("Exit", 200)
        ]

        # Create buttons
        for text, width in buttons:
            button = self.create_boxy_button(self.main_frame, text, "#444444", "#ffffff", width, self.handle_button_click)
            button.pack(pady=15)

        # Push the main menu frame onto the stack
        self.screen_stack.append(self.main_frame)

    def create_boxy_button(self, parent, text, bg, fg, width, command):
        button_frame = tk.Frame(parent, bg=self.bg_color)
        button_frame.pack()

        button = tk.Button(button_frame, text=text, font=self.button_font, bg=bg, fg=fg, width=width // 10, height=2,
                           relief='raised', bd=2, command=lambda: command(text))
        button.pack(padx=5, pady=5)

        # Bind events
        button.bind("<Enter>", lambda e: self.on_hover(button))
        button.bind("<Leave>", lambda e: self.on_leave(button))

        return button_frame

    def on_hover(self, button):
        button_frame = button.master
        button_frame.config(width=int(button_frame.winfo_width() * 1.05), height=int(button_frame.winfo_height() * 1.05))
        button.config(font=self.button_font.copy().configure(size=18, weight='bold'))

    def on_leave(self, button):
        button_frame = button.master
        button_frame.config(width=int(button_frame.winfo_width() / 1.05), height=int(button_frame.winfo_height() / 1.05))
        button.config(font=self.button_font)

    def handle_button_click(self, text):
        if text == "Play":
            self.show_game_mode_options()
        elif text == "Credits":
            self.show_credits()
        elif text == "Settings":
            self.show_settings()
        elif text == "Exit":
            self.root.quit()

    def show_game_mode_options(self):
        self.hide_frames()
        
        # Create the game mode frame
        self.game_mode_frame = tk.Frame(self.root, bg=self.bg_color)
        self.game_mode_frame.pack(fill="both", expand=True)
        
        # Add title label
        tk.Label(self.game_mode_frame, text="Select Game Mode", font=self.section_font, bg=self.bg_color, fg="#c83d3d").pack(pady=(20, 40))  # Increase padding to push title down

        # Create a frame to center buttons
        button_frame = tk.Frame(self.game_mode_frame, bg=self.bg_color)
        button_frame.pack(expand=True)  # Center buttons vertically and horizontally

        # Create centered buttons
        self.create_centered_button(button_frame, "Single Player", self.show_levels)
        self.create_centered_button(button_frame, "Multiplayer", self.show_multiplayer_message)

        # Create return button at the bottom left
        self.create_return_button(self.game_mode_frame)

        self.screen_stack.append(self.game_mode_frame)

    def create_centered_button(self, parent, text, command):
        button_frame = tk.Frame(parent, bg=self.bg_color)
        button_frame.pack(pady=10)  # Space between buttons
        
        button = tk.Button(button_frame, text=text, font=self.button_font, bg="#444444", fg="#ffffff", command=command)
        button.pack(padx=20, pady=10)  # Add padding around the button

    def show_multiplayer_message(self):
        self.game_mode_frame.pack_forget()
        self.multiplayer_frame = tk.Frame(self.root, bg=self.bg_color)
        self.multiplayer_frame.pack(fill="both", expand=True)
        tk.Label(self.multiplayer_frame, text="Multiplayer is not out yet.", font=self.button_font, bg=self.bg_color, fg="#c0392b").pack(pady=20)

        self.create_return_button(self.multiplayer_frame)

        self.screen_stack.append(self.multiplayer_frame)

    def show_levels(self):
        self.hide_frames()

        # Create the levels frame
        self.levels_frame = tk.Frame(self.root, bg=self.bg_color)
        self.levels_frame.pack(fill="both", expand=True)

        # Add title label
        tk.Label(self.levels_frame, text="Select Level", font=self.section_font, bg=self.bg_color, fg="#c83d3d").pack(pady=(20, 40))

        # Create level buttons
        level_frame = tk.Frame(self.levels_frame, bg=self.bg_color)
        level_frame.pack(pady=20)

        # Create buttons for levels 0 to 10 in rows
        for row in range(0, 11, 5):  # Adjust number of buttons per row as needed
            row_frame = tk.Frame(level_frame, bg=self.bg_color)
            row_frame.pack(pady=5)
            for level in range(row, min(row + 5, 11)):  # Create up to 5 buttons per row
                if level == 0:
                    self.create_level_button(row_frame, level, "Level 0", self.start_level_0)
                else:
                    self.create_level_button(row_frame, level, f"Level {level} (Locked)", None)

        # Create return button
        self.create_return_button(self.levels_frame)

        # Update current screen
        self.screen_stack.append(self.levels_frame)
        self.current_screen = self.levels_frame

    def create_level_button(self, parent, level, text, command):
        button_frame = tk.Frame(parent, bg=self.bg_color)
        button_frame.pack(pady=5)
        
        if command:
            button = tk.Button(button_frame, text=text, font=self.button_font, bg="#444444", fg="#ffffff", command=command)
        else:
            button = tk.Button(button_frame, text=text, font=self.button_font, bg="#555555", fg="#888888", state="disabled")

        button.pack(padx=10, pady=5, fill="x")

    def start_level_0(self):
        self.levels_frame.pack_forget()
        self.welcome_frame = tk.Frame(self.root, bg=self.bg_color)
        self.welcome_frame.pack(fill="both", expand=True)
        tk.Label(self.welcome_frame, text="Welcome to Level 0", font=self.button_font, bg=self.bg_color, fg="#c83d3d").pack(pady=20)
        
        # Return button
        self.create_return_button(self.welcome_frame)

        self.screen_stack.append(self.welcome_frame)

    def show_settings(self):
        self.hide_frames()
        
        # Create the settings frame
        self.settings_frame = tk.Frame(self.root, bg=self.settings_bg_color, bd=2, relief='solid')
        self.settings_frame.place(relx=0.5, rely=0.5, anchor='center', width=600, height=800)
        
        # Prevent frame from resizing based on its contents
        self.settings_frame.pack_propagate(False)
        
        # Close button
        self.close_button = tk.Button(self.settings_frame, text="X", font=self.large_button_font, bg="#c83d3d", fg="#ffffff", command=self.close_settings)
        self.close_button.pack(side=tk.TOP, anchor='ne', padx=10, pady=10)
        
        tk.Label(self.settings_frame, text="Settings", font=self.large_button_font, bg=self.settings_bg_color, fg="#ffffff").pack(pady=40)

        # Brightness Slider
        tk.Label(self.settings_frame, text="Brightness:", font=self.settings_font, bg=self.settings_bg_color, fg="#ffffff").pack(pady=5)
        self.brightness_slider = tk.Scale(self.settings_frame, from_=0, to=100, orient="horizontal", command=self.update_brightness, length=250)
        self.brightness_slider.set(self.brightness_factor)
        self.brightness_slider.pack(pady=10)

        # Music Volume Slider
        tk.Label(self.settings_frame, text="Music Volume:", font=self.settings_font, bg=self.settings_bg_color, fg="#ffffff").pack(pady=5)
        self.volume_slider = tk.Scale(self.settings_frame, from_=0, to=100, orient="horizontal", command=self.update_volume, length=250)
        self.volume_slider.set(self.music_volume)
        self.volume_slider.pack(pady=10)

        # Fullscreen, Windowed Fullscreen, and Windowed Buttons
        self.create_mode_buttons()

        # Create a frame to contain the button
        button_frame = tk.Frame(self.settings_frame, bg=self.settings_bg_color)
        button_frame.pack(side=tk.BOTTOM, pady=(0, 100), fill='x')  # Adjust frame padding as needed

        self.apply_button = tk.Button(
            button_frame,
            text="Apply",
            font=('Arial', 18, 'bold'),  # Increase font size
            bg="#27ae60",
            fg="#ffffff",
            command=self.apply_settings,
            width=7,  # Increase width
            height=1    # Increase height
        )
        self.apply_button.pack(pady=10)  # Adjust padding within the frame as needed



        self.screen_stack.append(self.settings_frame)

    def create_mode_buttons(self):
        mode_frame = tk.Frame(self.settings_frame, bg=self.settings_bg_color)
        mode_frame.pack(pady=20)

        tk.Label(mode_frame, text="Display Mode:", font=self.settings_font, bg=self.settings_bg_color, fg="#ffffff").pack(pady=10)

        modes = [
            ("Fullscreen", self.set_fullscreen),
            ("Windowed", self.set_windowed_fullscreen),
        ]

        for mode_text, mode_command in modes:
            mode_button = tk.Button(
                mode_frame,
                text=mode_text,
                font=self.settings_font,
                bg="#444444",
                fg="#ffffff",
                width=20,
                height=2,
                relief='raised',
                bd=4,
                command=mode_command
            )
            mode_button.pack(side=tk.LEFT, padx=15, pady=10)


    def update_brightness(self, value):
        self.brightness_factor = int(value)
        # Placeholder: Implement brightness adjustment here

    def update_volume(self, value):
        self.music_volume = int(value)
        pygame.mixer.music.set_volume(self.music_volume / 100)

    def apply_settings(self):
        # Apply settings (e.g., brightness, volume, fullscreen)
        self.close_settings()

    def close_settings(self):
        self.settings_frame.pack_forget()
        self.show_main_menu()
    

    def hide_frames(self):
        if hasattr(self, 'main_frame'):
            self.main_frame.pack_forget()
        if hasattr(self, 'game_mode_frame'):
            self.game_mode_frame.pack_forget()
        if hasattr(self, 'multiplayer_frame'):
            self.multiplayer_frame.pack_forget()
        if hasattr(self, 'levels_frame'):
            self.levels_frame.pack_forget()
        if hasattr(self, 'welcome_frame'):
            self.welcome_frame.pack_forget()
        if hasattr(self, 'settings_frame'):
            self.settings_frame.pack_forget()

    def create_return_button(self, parent_frame):
        return_button = tk.Button(parent_frame, text="⮌", font=self.button_font, bg="#c83d3d", fg="#ffffff", command=self.go_back)
        return_button.pack(side=tk.BOTTOM, anchor=tk.SW, padx=20, pady=20)  # Adjust padding as needed


    def hide_frames(self):
        # Hide the current frame only
        if self.screen_stack:
            self.screen_stack[-1].pack_forget()

    def show_some_screen(self):
        # Hide the current frame if needed
        self.hide_frames()
        
        # Create and display the new frame
        self.some_frame = tk.Frame(self.root, bg=self.bg_color)
        self.some_frame.pack(fill="both", expand=True)
        
        # Push the new frame to the stack
        self.screen_stack.append(self.some_frame)

    def go_back(self):
        if len(self.screen_stack) > 1:
            # Pop the current screen
            current_frame = self.screen_stack.pop()
            current_frame.pack_forget()
            
            # Show the previous screen
            previous_frame = self.screen_stack[-1]
            previous_frame.pack(fill="both", expand=True)
        else:
            # If there's no previous frame, just ensure the root stays open
            self.root.deiconify()

        # Debug print to see what's in the screen stack
        print("Screen stack:", [type(frame) for frame in self.screen_stack])

    def show_main_menu(self):
        self.hide_frames()
        self.create_main_menu()

    def set_fullscreen(self):
        self.root.attributes('-fullscreen', True)
        self.is_fullscreen = True

    def set_windowed_fullscreen(self):
        self.root.attributes('-fullscreen', False)
        self.root.attributes('-topmost', False)
        self.is_fullscreen = True


if __name__ == "__main__":
    root = tk.Tk()
    app = MenuApp(root)
    root.mainloop()
