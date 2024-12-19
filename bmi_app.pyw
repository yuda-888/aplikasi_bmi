import tkinter as tk
from tkinter import messagebox

# Fungsi untuk menghitung BMI
def hitung_bmi():
    try:
        berat = float(entry_berat.get())  # Mengambil input berat badan
        tinggi = float(entry_tinggi.get())  # Mengambil input tinggi badan
        bmi = berat / (tinggi ** 2)  # Menghitung BMI
        label_hasil.config(text=f"Hasil BMI: {bmi:.2f}")
        
        if bmi < 18.5:
            kategori = "Kekurangan Berat Badan"
        elif 18.5 <= bmi < 24.9:
            kategori = "Normal (Ideal)"
        elif 25 <= bmi < 29.9:
            kategori = "Kelebihan Berat Badan"
        else:
            kategori = "Obesitas"
        
        label_kategori.config(text=f"Kategori: {kategori}")
    
    except ValueError:
        messagebox.showerror("Input Error", "Tolong masukkan nilai yang valid!")

# Membuat window utama
root = tk.Tk()
root.title("Aplikasi BMI")

# Membuat label dan entry untuk berat badan
label_berat = tk.Label(root, text="Berat Badan (kg):")
label_berat.pack()
entry_berat = tk.Entry(root)
entry_berat.pack()

# Membuat label dan entry untuk tinggi badan
label_tinggi = tk.Label(root, text="Tinggi Badan (m):")
label_tinggi.pack()
entry_tinggi = tk.Entry(root)
entry_tinggi.pack()

# Tombol untuk menghitung BMI
tombol_hitung = tk.Button(root, text="Hitung BMI", command=hitung_bmi)
tombol_hitung.pack()

# Label untuk menampilkan hasil BMI dan kategori
label_hasil = tk.Label(root, text="Hasil BMI: ")
label_hasil.pack()
label_kategori = tk.Label(root, text="Kategori: ")
label_kategori.pack()

# Menjalankan aplikasi GUI
root.mainloop()
