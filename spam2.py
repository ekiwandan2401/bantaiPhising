import customtkinter as ctk
import requests
import random
import string
from threading import Thread
import time

class FacebookLoginGUI:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title("Facebook Login Tool")
        self.window.geometry("800x600")
        self.platforms = ['Google', 'Facebook']
        # Set default theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        # Variables
        self.is_running = False
        self.current_line = 0
        self.credentials = []
        
        self.create_widgets()
        self.load_credentials()
        
    def create_widgets(self):
        # Main frame
        self.main_frame = ctk.CTkFrame(self.window)
        self.main_frame.pack(padx=20, pady=20, fill="both", expand=True)
        
        # Title
        self.title_label = ctk.CTkLabel(
            self.main_frame, 
            text="Facebook Login Tool", 
            font=("Helvetica", 24, "bold")
        )
        self.title_label.pack(pady=10)
        
        # File input frame
        self.file_frame = ctk.CTkFrame(self.main_frame)
        self.file_frame.pack(fill="x", padx=10, pady=5)
        
        self.file_label = ctk.CTkLabel(
            self.file_frame,
            text="Credentials File:",
            font=("Helvetica", 12)
        )
        self.file_label.pack(side="left", padx=5)
        
        self.file_path = ctk.CTkEntry(
            self.file_frame,
            placeholder_text="Enter file path...",
            width=400
        )
        self.file_path.pack(side="left", padx=5)
        self.file_path.insert(0, "file.txt")
        
        self.load_button = ctk.CTkButton(
            self.file_frame,
            text="Load File",
            command=self.load_credentials
        )
        self.load_button.pack(side="left", padx=5)
        
        # Status frame
        self.status_frame = ctk.CTkFrame(self.main_frame)
        self.status_frame.pack(fill="x", padx=10, pady=5)
        
        self.status_label = ctk.CTkLabel(
            self.status_frame,
            text="Status: Idle",
            font=("Helvetica", 12)
        )
        self.status_label.pack(side="left", padx=5)
        
        # Progress frame
        self.progress_frame = ctk.CTkFrame(self.main_frame)
        self.progress_frame.pack(fill="x", padx=10, pady=5)
        
        self.progress_bar = ctk.CTkProgressBar(self.progress_frame)
        self.progress_bar.pack(fill="x", padx=5, pady=5)
        self.progress_bar.set(0)
        
        # Log frame
        self.log_frame = ctk.CTkFrame(self.main_frame)
        self.log_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        self.log_text = ctk.CTkTextbox(
            self.log_frame,
            height=300,
            font=("Courier", 12)
        )
        self.log_text.pack(fill="both", expand=True, padx=5, pady=5)
        
        # Control buttons frame
        self.control_frame = ctk.CTkFrame(self.main_frame)
        self.control_frame.pack(fill="x", padx=10, pady=5)
        
        self.start_button = ctk.CTkButton(
            self.control_frame,
            text="Start",
            command=self.start_process
        )
        self.start_button.pack(side="left", padx=5)
        
        self.stop_button = ctk.CTkButton(
            self.control_frame,
            text="Stop",
            command=self.stop_process,
            state="disabled"
        )
        self.stop_button.pack(side="left", padx=5)
        
    def load_credentials(self):
        try:
            with open(self.file_path.get(), 'r') as file:
                self.credentials = [line.strip() for line in file.readlines()]
            self.log_message(f"Loaded {len(self.credentials)} credentials from file")
            self.progress_bar.set(0)
        except Exception as e:
            self.log_message(f"Error loading file: {str(e)}")
            
    def log_message(self, message):
        self.log_text.insert("end", f"{time.strftime('%H:%M:%S')} - {message}\n")
        self.log_text.see("end")
        
    def start_process(self):
        if not self.credentials:
            self.log_message("No credentials loaded!")
            return
            
        self.is_running = True
        self.start_button.configure(state="disabled")
        self.stop_button.configure(state="normal")
        self.status_label.configure(text="Status: Running")
        
        # Start process in separate thread
        Thread(target=self.process_loop, daemon=True).start()
        
    def stop_process(self):
        self.is_running = False
        self.start_button.configure(state="normal")
        self.stop_button.configure(state="disabled")
        self.status_label.configure(text="Status: Stopped")
        
    def process_loop(self):
        sess = requests.Session()
        
        # Headers configuration
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9,id;q=0.8',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded',
            'dnt': '1',
            'origin': 'https://akkxks.fungames.works',
            'referer': 'https://akkxks.fungames.works/verify.php',
            'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        }
        
        try:
            # Initial connection
            ress = sess.get('https://akkxks.fungames.works', headers=headers)
            if ress.status_code == 200:
                self.log_message("Initial connection successful")
                
            # Verify token
            data_verification = {'azcodeToken': 'zgpd9'}
            response = sess.post('https://akkxks.fungames.works/verify.php', headers=headers, data=data_verification)
            if response.status_code == 200:
                self.log_message("Token verification successful")
                
            # Login with gToken
            params = {'gToken': 'verified'}
            data_login = {'sessionToken': 'azf'}
            response2 = sess.post('https://akkxks.fungames.works/index.php', headers=headers, params=params, data=data_login)
            if response2.status_code == 200:
                self.log_message("Session initialization successful")
            
            # Process credentials
            total_credentials = len(self.credentials)

            while self.is_running and self.current_line < total_credentials:
                try:
                    line = self.credentials[self.current_line]
                    email, password = line.split(':')
                    choice = random.choice(self.platforms)
                    self.log_message(f"Trying: {email}")
                    
                    data_credentials = {
                        'email': email.strip(),
                        'password': password.strip(),
                        'login': choice,
                    }
                    
                    response = sess.post('https://akkxks.fungames.works/fgnDate.php', headers=headers, data=data_credentials)
                    
                    if response.status_code == 200:
                        self.log_message(f"Success - Email: {email} |Platform : {choice} | Status Code : {response.url}")
                    else:
                        self.log_message(f"Failed - Status Code: {response.status_code}")
                        
                    # Update progress
                    progress = (self.current_line + 1) / total_credentials
                    self.progress_bar.set(progress)
                    
                    self.current_line += 1
                    time.sleep(0.5)  # Add delay to prevent overwhelming the server
                    
                except Exception as e:
                    self.log_message(f"Error processing line {self.current_line}: {str(e)}")
                    self.current_line += 1
                    
        except Exception as e:
            self.log_message(f"Connection error: {str(e)}")
            
        finally:
            if self.current_line >= total_credentials:
                self.log_message("Process completed!")
            else:
                self.log_message("Process stopped!")
                
            self.stop_process()
            
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = FacebookLoginGUI()
    app.run()