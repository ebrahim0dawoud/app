import tkinter as tk
from tkinter import messagebox
from pytube import YouTube


# وظائف الأزرار
def download_high_quality():
    try:
        link = link_entry.get()
        yt = YouTube(link)
        stream = yt.streams.get_highest_resolution()
        stream.download()
        messagebox.showinfo("نجاح", "تم تنزيل الفيديو بجودة عالية!")
    except Exception as e:
        messagebox.showerror("خطأ", f"حدث خطأ أثناء التنزيل: {e}")


def download_low_quality():
    try:
        link = link_entry.get()
        yt = YouTube(link)
        stream = yt.streams.get_lowest_resolution()
        stream.download()
        messagebox.showinfo("نجاح", "تم تنزيل الفيديو بجودة منخفضة!")
    except Exception as e:
        messagebox.showerror("خطأ", f"حدث خطأ أثناء التنزيل: {e}")


def download_audio():
    try:
        link = link_entry.get()
        yt = YouTube(link)
        stream = yt.streams.filter(only_audio=True).first()
        stream.download()
        messagebox.showinfo("نجاح", "تم تنزيل الصوت فقط!")
    except Exception as e:
        messagebox.showerror("خطأ", f"حدث خطأ أثناء التنزيل: {e}")


#دخل الرابط عشان الزراير تظهر
def show_buttons():
    link = link_entry.get()
    if link:
        button_high.pack(pady=5)
        button_low.pack(pady=5)
        button_audio.pack(pady=5)
    else:
        messagebox.showwarning("تحذير", "يرجى إدخال رابط الفيديو!")


# إنشاء النافذة الرئيسية
root = tk.Tk()
root.title("برنامج تنزيل الفيديو")
root.geometry("400x300")

#ازاي ادخل الرابط
link_label = tk.Label(root, text="أدخل رابط الفيديو:", font=("Arial", 12))
link_label.pack(pady=10)

link_entry = tk.Entry(root, width=40, font=("Arial", 12))
link_entry.pack(pady=5)

# الزراير تظهر
submit_button = tk.Button(root, text="عرض خيارات التنزيل", font=("Arial", 12), command=show_buttons)
submit_button.pack(pady=10)

# الأزرار (مخفية في البداية)
button_high = tk.Button(root, text="تنزيل بجودة عالية", font=("Arial", 12), command=download_high_quality)
button_low = tk.Button(root, text="تنزيل بجودة منخفضة", font=("Arial", 12), command=download_low_quality)
button_audio = tk.Button(root, text="تنزيل الصوت فقط", font=("Arial", 12), command=download_audio)

# تثبيت الواجهه
root.mainloop()