import customtkinter as ctk
import tkinter as tk
import FileOrganizer as fo  

class App(ctk.CTk):
    ctk.set_appearance_mode("System") 
    ctk.set_default_color_theme("blue") 

    def __init__(self):
        super().__init__()  
        self.geometry("500x500") 
        self.title("File Organizer") 

        # Title Label
        self.main_title_label = ctk.CTkLabel(
            master=self, 
            text="File Organizer", 
            text_color="#0DAADE", 
            font=("Arial", 20, "bold"), 
            corner_radius=25, 
            fg_color="black"
        )
        self.main_title_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        # Main Frame
        self.main_frame = ctk.CTkFrame(master=self, corner_radius=25, height=350, width=390)
        self.main_frame.place(relx=0.5, rely=0.55, anchor=tk.CENTER)

        # Path Entry
        self.main_entry_path = ctk.CTkEntry(
            master=self.main_frame, 
            placeholder_text="Enter path of the folder...", 
            width=280, 
            fg_color="gray25", 
            corner_radius=25
        )
        self.main_entry_path.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

        # Start Button
        self.start_button = ctk.CTkButton(
            master=self.main_frame, 
            text="Start Organizing", 
            fg_color="#1DDBC8", 
            text_color="black", 
            corner_radius=25, 
            command=self.clickbutton 
        )
        self.start_button.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        # Result Label (Changed from Entry to Label for better text display)
        self.result_label = ctk.CTkLabel(
            master=self.main_frame,
            text="Ready to organize!",
            text_color="white",
            wraplength=350,  # Wraps long text so it doesn't get cut off
            font=("Arial", 14)
        )
        self.result_label.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

    def clickbutton(self):
        path_str = self.main_entry_path.get().strip()
        
        if not path_str:
            self.result_label.configure(text="Please enter a path first!", text_color="red")
            return

        # 2. Call the function from the other file
        try:
            # We pass the path to the function, and it returns the result string
            result_message = fo.organize_folder(path_str)
            
            # 3. Update the label with the result
            self.result_label.configure(text=result_message, text_color="white")
            
        except Exception as e:
            self.result_label.configure(text=f"Error: {str(e)}", text_color="red")

if __name__== '__main__' : 
    app = App()
    app.mainloop()