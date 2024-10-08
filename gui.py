import tkinter as tk
from tkinter import filedialog, messagebox
from bb8_strings import StringExtractor 

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("BB8-Strings")
        self.extractor = StringExtractor()
        
        self.label = tk.Label(root, text="Select a binary file to extract strings:")
        self.label.pack(pady=10)
        
        self.browse_button = tk.Button(root, text="Browse", command=self.browse_file)
        self.browse_button.pack(pady=5)
        
        self.extract_button = tk.Button(root, text="Extract Strings", command=self.extract_strings)
        self.extract_button.pack(pady=5)
        
        self.result_text = tk.Text(root, height=15, width=50)
        self.result_text.pack(pady=10)

    def browse_file(self):
        file_path = filedialog.askopenfilename(title="Select a binary file",
                                               filetypes=(("Binary files", "*.bin;*.exe;*.dll"), ("All files", "*.*")))
        if file_path:
            self.selected_file = file_path
            self.label.config(text=f"Selected file: {os.path.basename(file_path)}")

    def extract_strings(self):
        if hasattr(self, 'selected_file'):
            extracted = self.extractor.extract_strings(self.selected_file)
            self.result_text.delete(1.0, tk.END)  # Clear previous results
            self.result_text.insert(tk.END, "\n".join(extracted) if extracted else "No strings found.")
        else:
            messagebox.showwarning("Warning", "Please select a binary file first.")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
