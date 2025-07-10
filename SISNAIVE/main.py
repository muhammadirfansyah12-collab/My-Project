import tkinter as tk
from tkinter import filedialog
from model import train_model, predict
from preprocessing import *

model = None

def prediksi():
    global model
    try:
        nilai = kategorikan_nilai(int(entry_nilai.get()))
        kehadiran = kategorikan_kehadiran(int(entry_kehadiran.get()))
        partisipasi = kategorikan_nilai(int(entry_partisipasi.get()))
        result = predict(model, [nilai, kehadiran, partisipasi])
        label_hasil.config(text=f"Hasil: {result}")
    except Exception as e:
        label_hasil.config(text="Error: " + str(e))

def load_csv():
    global model
    path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    model = train_model(path)
    label_hasil.config(text="Model siap digunakan!")

root = tk.Tk()
root.title("SISNAIVE - Naive Bayes Siswa")

tk.Label(root, text="Nilai Matematika").pack()
entry_nilai = tk.Entry(root)
entry_nilai.pack()

tk.Label(root, text="Kehadiran (%)").pack()
entry_kehadiran = tk.Entry(root)
entry_kehadiran.pack()

tk.Label(root, text="Partisipasi (%)").pack()
entry_partisipasi = tk.Entry(root)
entry_partisipasi.pack()

tk.Button(root, text="Upload Dataset CSV", command=load_csv).pack(pady=5)
tk.Button(root, text="Prediksi Karakteristik", command=prediksi).pack(pady=5)

label_hasil = tk.Label(root, text="")
label_hasil.pack()

root.mainloop()
