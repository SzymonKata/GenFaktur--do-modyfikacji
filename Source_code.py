import os
import tkinter as tk
from tkinter import *
from reportlab.pdfgen import canvas
from tkinter import filedialog

# ==== creating main class
class InvoiceGenerator:
    def __init__(self,root):
        self.root = root
        self.root.title("Faktura")
        self.root.geometry("750x800")

        # creating frame in window

        self.frame=Frame(self.root,bg="white")
        self.frame.place(x=80,y=20, width=600, height=700)

        Label(self.frame,text="Wprowadź szczegóły firmy. ",font=("times new roman",30,"bold"),bg="white",fg="green",bd=0).place(x=50,y=10)

        Label(self.frame, text="Nazwa firmy", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(
            x=50, y=80)
        self.company_name=Entry(self.frame,font=("times new roman",15),bg="light grey")
        self.company_name.place(x=270,y=80,width=300,height=35)

        Label(self.frame, text="Adres firmy", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(
            x=50, y=140)
        self.address= Entry(self.frame, font=("times new roman", 15), bg="light grey")
        self.address.place(x=270, y=140, width=300,height=35)

        Label(self.frame, text="Miasto", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(
            x=50, y=200)
        self.city = Entry(self.frame, font=("times new roman", 15), bg="light grey")
        self.city.place(x=270, y=200, width=300, height=35)

        Label(self.frame, text="Numer telefonu", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(
            x=50, y=260)
        self.gst = Entry(self.frame, font=("times new roman", 15), bg="light grey")
        self.gst.place(x=270, y=260, width=300, height=35)

        Label(self.frame, text="Data", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(
            x=50, y=320)
        self.date = Entry(self.frame, font=("times new roman", 15), bg="light grey")
        self.date.place(x=270, y=320, width=300, height=35)

        Label(self.frame, text="Adres mailowy", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(
            x=50, y=380)
        self.contact = Entry(self.frame, font=("times new roman", 15), bg="light grey")
        self.contact.place(x=270, y=380, width=300, height=35)

        Label(self.frame, text="Dane klienta", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(
            x=50, y=440)
        self.c_name = Entry(self.frame, font=("times new roman", 15), bg="light grey")
        self.c_name.place(x=270, y=440, width=300, height=35)

        Label(self.frame, text="Podpis firmy", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(
            x=50, y=500)
        self.aus = Entry(self.frame, font=("times new roman", 15), bg="light grey")
        self.aus.place(x=270, y=500, width=300, height=35)

        Label(self.frame, text="Logo firmy", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(
            x=50, y=560)

        # ==== Browse File
        Button(self.frame, text="Przeszukaj pliki", font=("times new roman", 14), command=self.browse).place(x=270, y=560)

        # ====submit details
        Button(self.frame, text = "Wygenerej fakturę",command = self.generate_invoice, font = ("times new roman", 14),fg = "white",cursor = "hand2", bg = "#B00857").place(x = 50, y = 640, width = 180, height = 40)

    # ==== Browse Function
    def browse(self):
        self.file_name = filedialog.askopenfilename(title="Wybierz plik")
        Label(self.frame, text=os.path.basename(self.file_name), font=("times new roman", 15)).place(x=270, y=600)

    # ==== Invoice Generation Function
    def generate_invoice(self):
        c = canvas.Canvas("Faktura.pdf", pagesize=(200, 250), bottomup=0)
        c.setFillColorRGB(0.8, 0.5, 0.7)

        c.line(70, 22, 180, 22)
        c.line(5, 45, 195, 45)
        c.line(15, 120, 185, 120)
        c.line(35, 108, 35, 220)
        c.line(115, 108, 115, 220)
        c.line(135, 108, 135, 220)
        c.line(160, 108, 160, 220)
        c.line(15, 220, 185, 220)

        c.translate(10, 40)
        c.scale(1, -1)
        c.drawImage(self.file_name, 0, 0, width=50, height=30)

        c.scale(1, -1)
        c.translate(-10, -40)

        c.setFont("Times-Bold", 10)
        c.drawCentredString(125, 20, self.company_name.get())

        c.setFont("Times-Bold", 5)
        c.drawCentredString(125, 30, self.address.get())
        c.drawCentredString(125, 35, self.city.get() + ", Polska")
        c.setFont("Times-Bold", 6)
        c.drawCentredString(125, 42, "Numer Telefonu :"+self.gst.get())

        c.setFont("Times-Bold", 8)
        c.drawCentredString(100, 55, "Faktura VAT")

        c.setFont("Times-Bold", 5)

        c.drawRightString(70, 70, "Numer faktury :")
        c.drawRightString(100, 70, "1/2022")

        c.drawRightString(70, 80, "Data :")
        c.drawRightString(100, 80, self.date.get())

        c.drawRightString(70, 90, "Dane klienta :")
        c.drawRightString(100, 90, self.c_name.get())

        c.drawRightString(70, 100, "Adres mailowy :")
        c.drawRightString(150, 150, self.contact.get())

        c.roundRect(15, 108, 170, 130, 10, stroke=1, fill=0)

        c.drawCentredString(25, 118, "Numer:")
        c.drawCentredString(75, 118, "Zamówienia")
        c.drawCentredString(125, 118, "Cena")
        c.drawCentredString(148, 118, "Ilosc")
        c.drawCentredString(173, 118, "Razem")

        c.drawString(30, 230, "Faktura wygenerowana przez Source.code.py")

        c.drawRightString(180, 228, self.aus.get())
        c.drawRightString(180, 235, "Podpis")

        c.showPage()
        c.save()

# ==== creating main function
def main():
    # ==== create tkinter window
    root = Tk()
    # === creating object for class InvoiceGenerator
    obj = InvoiceGenerator(root)
    # ==== start the gui
    root.mainloop()

if __name__ == "__main__":
    # ==== calling main function
    main()
