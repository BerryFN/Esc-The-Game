import tkinter as tk
from tkinter import font
import pygame

class MenuApp:
    def __init__(self, root):
        self.root = root
        self.bg_color = "black"
        self.button_font = ("Arial", 20)
        self.hacker_font = ("Arial", 40, "bold")  # Example font for the welcome message
        self.player_name = ""
        self.text_speed = 50  # Default animation speed in milliseconds
        self.text_speed_fast = 10  # Speed when space is held
        self.animating_text = False

        self.root = root
        self.bg_color = "#000000"  # Example background color
        self.button_font = ("Arial", 16)
        self.hacker_font = ("VT323", 24)  # Define the hacker font here
        self.player_name = ""
        self.screen_stack = []

        self.root = root
        self.root.configure(bg="black")
        self.bg_color = "#1a1a1a"
        self.button_font = ("Arial", 20)
        self.screen_stack = []


        self.root = root
        self.root.title("Game Menu")
        self.bg_color = "#0c0c0c"
        self.settings_bg_color = "#2e2e2e"
        self.brightness_factor = 50
        self.is_fullscreen = True
        self.music_volume = 50

        # Initialize pygame for music control
        pygame.mixer.init()
        pygame.mixer.music.load('C:/Users/hussa/Downloads/background_music.mp3')
        pygame.mixer.music.set_volume(self.music_volume / 100)
        pygame.mixer.music.play(-1)

        # Initialize screen stack
        self.screen_stack = []

        # Configure the main window
        self.root.configure(bg=self.bg_color)
        self.root.attributes('-fullscreen', self.is_fullscreen)

        # Fonts for buttons and logo
        self.button_font = font.Font(family='Arial', size=16, weight='bold')
        self.large_button_font = font.Font(family='Arial', size=24, weight='bold')
        self.logo_font = font.Font(family='Arial', size=150, weight='bold')
        self.section_font = font.Font(family='Arial', size=36, weight='bold')
        self.settings_font = font.Font(family='Arial', size=15, weight='bold')

        # Create and configure the main menu
        self.create_main_menu()

    def create_stone_button(self, parent, text, width, command):
        button_frame = tk.Frame(parent, bg=self.bg_color)
        button_frame.pack()

        # Create the button with stone-like styling
        button = tk.Button(button_frame, text=text, font=self.button_font, bg="#6d6e70", fg="#000000", relief='raised', borderwidth=4, command=lambda: command(text))
        button.config(width=width // 10, height=2)
        button.pack(padx=5, pady=5)

        # Bind events for hover effect
        button.bind("<Enter>", lambda e: self.on_hover(button))
        button.bind("<Leave>", lambda e: self.on_leave(button))

        return button_frame

    def on_hover(self, button):
        button.config(relief='sunken')

    def on_leave(self, button):
        button.config(relief='raised')

    def create_main_menu(self):
        self.main_frame = tk.Frame(self.root, bg=self.bg_color)
        self.main_frame.pack(fill="both", expand=True)

        self.esc_logo = tk.Label(self.main_frame, text=">-ESC.", font=self.logo_font, bg=self.bg_color, fg="#c83d3d")
        self.esc_logo.pack(pady=(30, 80))

        buttons = [
            ("Play", 200),
            ("Credits", 200),
            ("Settings", 200),
            ("Exit", 200)
        ]

        for text, width in buttons:
            button = self.create_stone_button(self.main_frame, text, width, self.handle_button_click)
            button.pack(pady=15)

        self.screen_stack.append(self.main_frame)

    def handle_button_click(self, button_text):
        if button_text == "Play":
            self.show_game_mode_options()
        elif button_text == "Credits":
            self.show_credits()
        elif button_text == "Settings":
            self.show_settings()
        elif button_text == "Exit":
            self.root.quit()

    def show_game_mode_options(self):
        self.hide_frames()

        self.game_mode_frame = tk.Frame(self.root, bg=self.bg_color)
        self.game_mode_frame.pack(fill="both", expand=True)

        tk.Label(self.game_mode_frame, text="Select Game Mode", font=self.section_font, bg=self.bg_color, fg="#c83d3d").pack(pady=(20, 40))

        button_frame = tk.Frame(self.game_mode_frame, bg=self.bg_color)
        button_frame.pack(expand=True)

        self.create_centered_button(button_frame, "Single Player", self.show_levels)
        self.create_centered_button(button_frame, "Multiplayer", self.show_multiplayer_message)

        self.create_return_button(self.game_mode_frame)

        self.screen_stack.append(self.game_mode_frame)

    def show_credits(self):
        self.hide_frames()

        # Create credits frame
        self.credits_frame = tk.Frame(self.root, bg=self.bg_color)
        self.credits_frame.pack(fill="both", expand=True)

        # Credits text with specific formatting
        credits_text = (
            "Esc.\n\n"
            "Managed By King.Farooq & B3rry\n\n"
            "Developers: King.Farooq | B3rry\n\n"
            "Graphic Designers: King.Farooq | Ghxsttttt\n\n"
            "Advertisment: King.Farooq | ZaxyMb | B3rry | Ghxsttttt\n\n"
            "Instagram - insta goes here\n\n"
            "Tiktok - tiktok goes here\n\n"
            "X (Formally known as Twitter) - X (Formally known as Twitter) goes here\n\n"
            "Youtube - Youtube goes here\n\n"
            "Website - website goes here\n\n"
        )

        # Create a Label to display the credits
        self.credits_label = tk.Label(
            self.credits_frame,
            text=credits_text,
            font=self.settings_font,
            bg=self.bg_color,
            fg="#ffffff",
            wraplength=600,  # Ensure text fits within the frame
            justify="center",
            padx=20,
            pady=20
        )
        self.credits_label.pack(pady=20, padx=20)

        # Apply custom formatting using HTML-like tags
        self.credits_label.configure(
            text=self.format_credits_text(credits_text)
        )

        # Create return button
        self.create_return_button(self.credits_frame)

        # Update screen stack
        self.screen_stack.append(self.credits_frame)

    def format_credits_text(self, text):
        # Helper function to format the text with HTML-like tags
        # Note: This is a simplified example; actual implementation may vary
        formatted_text = text.replace("<b>", "<b>").replace("</b>", "</b>")
        return formatted_text

    def create_return_button(self, parent):
        # Create return button with hover effects
        return_button = tk.Button(
            parent,
            text="⮌",
            font=('Arial', 18, 'bold'),  # Increased font size and bold for better visibility
            bg="#c83d3d",
            fg="#ffffff",
            command=self.show_main_menu,
            width=20,  # Increased width
            height=2,  # Increased height
            relief='raised',  # Added raised relief for better visibility
            bd=4  # Added border width for a better look
        )

        # Bind hover effects
        return_button.bind("<Enter>", lambda e: return_button.config(bg="#d9534f"))
        return_button.bind("<Leave>", lambda e: return_button.config(bg="#c83d3d"))

        return_button.pack(side=tk.BOTTOM, anchor='sw', padx=20, pady=20)

    def show_main_menu(self):
        # Clear the credits frame and show the main menu
        self.credits_frame.pack_forget()
        self.create_main_menu()

        def create_centered_button(self, parent, text, command):
            button_frame = tk.Frame(parent, bg=self.bg_color)
            button_frame.pack(pady=10)

            button = self.create_stone_button(button_frame, text, 200, command)
            button.pack(padx=20, pady=10)

    def create_return_button(self, parent):
        return_button = tk.Button(parent, text="⮌", font=self.button_font, bg="#c83d3d", fg="#ffffff", command=self.show_main_menu)
        return_button.pack(side=tk.BOTTOM, pady=20)

    def show_main_menu(self):
        for screen in self.screen_stack:
            screen.pack_forget()
        self.create_main_menu()

    def hide_frames(self):
        for screen in self.screen_stack:
            screen.pack_forget()

    # Methods for settings and game mode options...

    def update_brightness(self, value):
        self.brightness_factor = int(value)
        # Placeholder: Implement brightness adjustment here

    def update_volume(self, value):
        self.music_volume = int(value)
        pygame.mixer.music.set_volume(self.music_volume / 100)

    def apply_settings(self):
        self.close_settings()

    def close_settings(self):
        self.settings_frame.pack_forget()
        self.show_main_menu()

    def set_fullscreen(self):
        self.is_fullscreen = True
        self.root.attributes('-fullscreen', True)

    def set_windowed_fullscreen(self):
        self.is_fullscreen = False
        self.root.attributes('-fullscreen', False)

    def create_centered_button(self, parent, text, command):
        button_frame = tk.Frame(parent, bg=self.bg_color)
        button_frame.pack(pady=10)  # Space between buttons

        button = tk.Button(button_frame, text=text, font=self.button_font, bg="#6d6e70", fg="#000000", relief='raised', borderwidth=4, command=command)
        button.config(width=20, height=2)  # Adjust width and height as needed
        button.pack(padx=20, pady=10)  # Add padding around the button

        # Bind events for hover effect
        button.bind("<Enter>", lambda e: self.on_hover(button))
        button.bind("<Leave>", lambda e: self.on_leave(button))

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

        # Create level buttons frame
        level_frame = tk.Frame(self.levels_frame, bg=self.bg_color)
        level_frame.pack(pady=20)

        # Create buttons for levels 0 to 10 in a grid layout
        for level in range(11):
            row = level // 5
            col = level % 5
            if level == 0:
                self.create_level_button(level_frame, row, col, level, "Level 0", self.start_level_0)
            else:
                self.create_level_button(level_frame, row, col, level, f"Level {level} (Locked)", None)

        # Create return button at the bottom
        self.create_return_button(self.levels_frame)

        # Update current screen
        self.screen_stack.append(self.levels_frame)
        self.current_screen = self.levels_frame

    def create_level_button(self, parent, row, col, level, text, command):
        button_frame = tk.Frame(parent, bg=self.bg_color)
        button_frame.grid(row=row, column=col, padx=10, pady=10)
        
        if command:
            button = tk.Button(button_frame, text=text, font=self.button_font, bg="#6d6e70", fg="#000000", relief='raised', borderwidth=4, command=command)
        else:
            button = tk.Button(button_frame, text=text, font=self.button_font, bg="#555555", fg="#888888", relief='raised', borderwidth=4, state="disabled")

        button.config(width=20, height=2)  # Adjust width and height as needed
        button.pack(padx=10, pady=5, fill="x")
        
        # Bind events for hover effect
        button.bind("<Enter>", lambda e: self.on_hover(button))
        button.bind("<Leave>", lambda e: self.on_leave(button))

    def create_return_button(self, parent):
        return_button = tk.Button(parent, text="⮌", font=self.button_font, bg="#c83d3d", fg="#ffffff", command=self.show_main_menu)
        return_button.config(width=10, height=2)  # Adjust size as needed
        return_button.pack(side=tk.BOTTOM, pady=20)

        # Bind events for hover effect
        return_button.bind("<Enter>", lambda e: self.on_hover(return_button))
        return_button.bind("<Leave>", lambda e: self.on_leave(return_button))

    def on_hover(self, button):
        button.config(font=self.button_font_hover, relief='raised')

    def on_leave(self, button):
        button.config(font=self.button_font, relief='raised')
    

    def start_level_0(self):
        self.clear_screen()  # Clear any existing screens or frames
        self.start_name_screen()  # Show the name entry screen

    def start_name_screen(self):
        self.clear_screen()  # Clear previous screen content

        # Create the frame for the name entry screen
        self.name_screen = tk.Frame(self.root, bg=self.bg_color)
        self.name_screen.pack(fill="both", expand=True)

        # Prompt label
        self.prompt_label = tk.Label(
            self.name_screen, 
            text="What's your name?", 
            font=self.button_font, 
            bg=self.bg_color, 
            fg="white"
        )
        self.prompt_label.pack(pady=20)

        # Text entry box
        self.hidden_name_entry = tk.Entry(
            self.name_screen, 
            font=("Arial", 24), 
            bg=self.bg_color, 
            fg="white", 
            insertbackground="white"
        )
        self.hidden_name_entry.pack(pady=(20, 10))
        self.hidden_name_entry.focus()
        self.hidden_name_entry.bind("<Return>", self.on_name_entered)

        # Enter to continue label
        self.enter_label = tk.Label(
            self.name_screen, 
            text="Press Enter to continue", 
            font=("Arial", 16), 
            bg=self.bg_color, 
            fg="white"
        )
        self.enter_label.pack(pady=10)
        self.blinking_animation()  # Start blinking animation

    def on_name_entered(self, event):
        self.player_name = self.hidden_name_entry.get()
        self.hidden_name_entry.pack_forget()  # Hide the entry widget
        self.prompt_label.pack_forget()  # Hide the prompt label
        self.enter_label.pack_forget()  # Hide the enter label

        self.display_welcome_message()  # Display welcome message

    def display_welcome_message(self):
        self.welcome_frame = tk.Frame(self.root, bg=self.bg_color)
        self.welcome_frame.pack(fill="both", expand=True)

        # Welcome message
        welcome_text = f"Welcome to Esc {self.player_name}"
        self.welcome_label = tk.Label(
            self.welcome_frame,
            text=welcome_text,
            font=self.hacker_font,
            bg=self.bg_color,
            fg="white",
            justify="center"
        )
        self.welcome_label.pack(pady=20)

        # Enter to continue label
        self.enter_label = tk.Label(
            self.welcome_frame,
            text="Press Enter to continue",
            font=("Arial", 16),
            bg=self.bg_color,
            fg="white"
        )
        self.enter_label.pack(pady=10)
        self.blinking_animation()  # Start blinking animation

        self.root.bind("<Return>", self.start_option_screen)  # Bind Enter key to continue to the options screen

    def start_option_screen(self, event=None):
        self.root.unbind("<Return>")  # Unbind Enter key to prevent multiple calls

        self.clear_screen()  # Clear the welcome message screen

        # Create the options screen
        self.option_screen = tk.Frame(self.root, bg=self.bg_color)
        self.option_screen.pack(fill="both", expand=True)

        self.text_frame = tk.Frame(self.option_screen, bg=self.bg_color, bd=2, relief="solid")
        self.text_frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.text_box = tk.Text(
            self.text_frame, 
            font=("Arial", 16), 
            bg=self.bg_color, 
            fg="white", 
            wrap="word", 
            bd=0, 
            highlightthickness=2, 
            highlightbackground="#00ff00"
        )
        self.text_box.pack(padx=10, pady=10)
        self.text_box.config(state="disabled")

        self.button_frame = tk.Frame(self.option_screen, bg=self.bg_color)
        self.button_frame.pack(pady=(5, 20))

        self.create_option_button("Option 1", self.option1_action, 0)
        self.create_option_button("Option 2", self.option2_action, 1)

        self.animating_text = True
        self.animate_text()  # Start text animation after setting up the screen

        self.root.bind("<space>", self.speed_up_text_animation)  # Bind space key to speed up animation
        self.root.bind("<KeyRelease-space>", self.reset_text_animation)  # Bind space key release to reset animation speed

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.pack_forget()

    def create_option_button(self, text, command, column):
        button = tk.Button(
            self.button_frame, 
            text=text, 
            font=("Arial", 24), 
            command=command, 
            bg=self.bg_color, 
            fg="white", 
            width=15, 
            height=2
        )
        button.grid(row=0, column=column, padx=10, pady=10)
        button.bind("<Enter>", self.on_hover)
        button.bind("<Leave>", self.on_leave)
        return button

    def on_hover(self, event):
        event.widget.config(bg="#555555")

    def on_leave(self, event):
        event.widget.config(bg=self.bg_color)

    def option1_action(self):
        print("Option 1 selected")

    def option2_action(self):
        print("Option 2 selected")

    def animate_text(self):
        if not self.animating_text:
            return

        # Example animation logic - you can adjust this to your needs
        text = "This is the introductory text for Level 0. You can choose Option 1 or Option 2 below."
        self.text_box.config(state="normal")
        self.text_box.delete("1.0", "end")

        # Add text one character at a time
        self.animate_text_recursively(text, 0)
        
    def animate_text_recursively(self, text, index):
        if index < len(text):
            self.text_box.insert("end", text[index])
            self.text_box.update()
            self.root.after(self.text_speed, self.animate_text_recursively, text, index + 1)
        else:
            self.text_box.config(state="disabled")  # Disable editing after animation

    def speed_up_text_animation(self, event):
        self.text_speed = self.text_speed_fast  # Speed up text animation

    def reset_text_animation(self, event):
        self.text_speed = 50  # Reset to default speed

    def blinking_animation(self):
        if self.enter_label:
            current_color = self.enter_label.cget("fg")
            new_color = "black" if current_color == "white" else "white"
            self.enter_label.config(fg=new_color)
            self.root.after(500, self.blinking_animation)  # Blink every 500ms
    
    def show_settings(self):
        self.hide_frames()
        
        # Create the settings frame
        self.settings_frame = tk.Frame(self.root, bg=self.settings_bg_color, bd=2, relief='solid')
        self.settings_frame.place(relx=0.5, rely=0.5, anchor='center', width=600, height=800)
        
        # Prevent frame from resizing based on its contents
        self.settings_frame.pack_propagate(False)
        
        # Close button
        self.close_button = tk.Button(
            self.settings_frame,
            text="X",
            font=self.large_button_font,
            bg="#c83d3d",
            fg="#ffffff",
            relief='raised',
            borderwidth=4,
            command=self.close_settings
        )
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
            font=self.button_font,  # Use retro style font
            bg="#27ae60",
            fg="#ffffff",
            relief='raised',
            borderwidth=4,
            command=self.apply_settings,
            width=15,  # Adjust width
            height=2    # Adjust height
        )
        self.apply_button.pack(pady=10)  # Adjust padding within the frame as needed

        self.screen_stack.append(self.settings_frame)


    def create_mode_buttons(self):
        mode_frame = tk.Frame(self.settings_frame, bg=self.settings_bg_color)
        mode_frame.pack(pady=20)

        tk.Label(mode_frame, text="Display Mode:", font=self.settings_font, bg=self.settings_bg_color, fg="#ffffff").pack(pady=10)

        modes = [
            ("Fullscreen", self.set_fullscreen),
            ("Windowed Fullscreen", self.set_windowed_fullscreen),
            ("Windowed", self.set_windowed),
        ]

        for mode_text, mode_command in modes:
            mode_button = tk.Button(
                mode_frame,
                text=mode_text,
                font=self.settings_font,
                bg="#6d6e70",  # Retro stone color
                fg="#000000",  # Dark text color for contrast
                relief='raised',
                borderwidth=4,
                width=20,
                height=2,
                command=mode_command
            )
            mode_button.pack(side=tk.LEFT, padx=15, pady=10)

            # Bind events for hover effect
            mode_button.bind("<Enter>", lambda e, b=mode_button: self.on_hover(b))
            mode_button.bind("<Leave>", lambda e, b=mode_button: self.on_leave(b))


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
    
    def on_hover(self, button):
        button.config(relief='sunken')  # Change button relief to sunken on hover

    def on_leave(self, button):
        button.config(relief='raised')  # Change button relief back to raised on leave

    def set_fullscreen(self):
        self.is_fullscreen = True
        self.root.attributes('-fullscreen', True)
        self.root.attributes('-topmost', True)  # Keep the window on top

    def set_windowed_fullscreen(self):
        self.is_fullscreen = False
        self.root.attributes('-fullscreen', False)
        self.root.attributes('-topmost', False)  # Allow other windows to be on top

    def set_windowed(self):
        self.is_fullscreen = False
        self.root.attributes('-fullscreen', False)
        self.root.attributes('-topmost', False)  # Allow other windows to be on top
        self.root.geometry('800x600')  # Set a default window size for windowed mode


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

    def create_return_button(self, parent):
        button_frame = tk.Frame(parent, bg=self.bg_color)
        button_frame.pack(side="bottom", anchor="w", padx=20, pady=20)  # Place at the bottom left

        return_button = tk.Button(button_frame, text="⮌", font=self.button_font, bg="#c83d3d", fg="#ffffff", relief='raised', borderwidth=4, command=self.go_back)
        return_button.config(width=15, height=2)  # Adjust size as needed
        return_button.pack(padx=5, pady=5)

        # Bind events for hover effect
        return_button.bind("<Enter>", lambda e: self.on_hover(return_button))
        return_button.bind("<Leave>", lambda e: self.on_leave(return_button))



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
