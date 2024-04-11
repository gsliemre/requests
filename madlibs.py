import tkinter as tk

def generate_mad_libs():
    # Kullanıcıdan alınan kelimeleri işleyin ve hikayeyi oluşturun
    name = entry_name.get()
    adjective = entry_adjective.get()
    verb = entry_verb.get()

    mad_libs_result = f"{name} çok {adjective} bir şekilde {verb}."

    # Sonucu ekranda gösterin
    result_label.config(text=mad_libs_result)

# Tkinter penceresi oluşturun
root = tk.Tk()
root.title("Mad Libs Oluşturucu")

# Giriş alanları ve düğme ekleyin
entry_name = tk.Entry(root)
entry_adjective = tk.Entry(root)
entry_verb = tk.Entry(root)
generate_button = tk.Button(root, text="Hikaye Oluştur", command=generate_mad_libs)
result_label = tk.Label(root, text="")

# Arayüzdeki bileşenleri düzenleyin
entry_name.place(x=10, y=10)
entry_adjective.place(x=150, y=10)
entry_verb.place(x=320, y=10)
generate_button.place(x=470, y=9)
result_label.place(x=60, y=38)

# Pencerenin boyutunu ayarlayın
root.geometry("550x100")

# Pencereyi görünür hale getirin

entry_adjective.pack()
entry_verb.pack()
generate_button.pack()
result_label.pack()

root.mainloop()
