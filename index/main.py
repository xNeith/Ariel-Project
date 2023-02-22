from tkinter import *
import tkinter.messagebox
import customtkinter
from PIL import Image, ImageTk
def main():
    customtkinter.set_appearance_mode("light")  
    root = customtkinter.CTk()
    root.geometry("500x530")
    root.resizable(width=False, height=False)
    root.title("Mrs. Freddy's Shop")


    empanada_normal = customtkinter.CTkImage(Image.open("empN.jpg"), size=(100, 100))
    empanada_arreglada = customtkinter.CTkImage(Image.open("empA.jpeg"), size=(100, 100))
    empanada_pobre = customtkinter.CTkImage(Image.open("pobre.jpeg"), size=(100, 100))


    frame = customtkinter.CTkFrame(master=root, corner_radius= 20, fg_color="#bd1f26")
    frame.grid(pady=15, padx=20)


    titulo = customtkinter.CTkLabel(master=frame, corner_radius=2, text="Welcome to the shopping menu!",
                                    font=("Roboto Black 900", 24, "bold"),
                                    text_color=("#ecd778"))
    titulo.grid(row=0, column=0)


    def change_frame():
        root.destroy()
    
        app = customtkinter.CTk()
        app.geometry("500x200")
        app.title("Mrs. Freddy's Shop")
        frame = customtkinter.CTkFrame(master=app, corner_radius= 8, fg_color="#bd1f26",)
        frame.grid(pady=15, padx=15)

        titulo = customtkinter.CTkLabel(master=frame, corner_radius=2, text="Let's finish your order!",
                                        font=("Roboto Black 900", 24, "bold"),
                                        text_color=("#260028"))
        titulo.grid(row=0,column=1)

        size = customtkinter.CTkLabel(master=frame, corner_radius=2, text="Size",
                                        font=("Roboto Black 900", 21, "bold"),
                                        text_color=("#ecd778"))
        size.grid(row=2,column=0)

        cb1 = customtkinter.CTkCheckBox(master=frame, text="Small",
                                    font=("Roboto Black900",12,"bold"),
                                    corner_radius=6,
                                    border_width=3,
                                    border_color="#260028",
                                    fg_color="#260028",
                                    hover_color="#eed77a",
                                    checkmark_color="#eed77a",
                                    text_color="#e8ca78",
                                    text_color_disabled=("gray60", "gray45"))
        cb1.grid(row=3,column=0)

        cb2 = customtkinter.CTkCheckBox(master=frame, text="Medium",
                                    font=("Roboto Black900",12,"bold"),
                                    corner_radius=6,
                                    border_width=3,
                                    border_color="#260028",
                                    fg_color="#260028",
                                    hover_color="#eed77a",
                                    checkmark_color="#eed77a",
                                    text_color="#e8ca78",
                                    text_color_disabled=("gray60", "gray45"))
        cb2.grid(row=4,column=0)

        cb3 = customtkinter.CTkCheckBox(master=frame, text="Large",
                                    font=("Roboto Black900",12,"bold"),
                                    corner_radius=6,
                                    border_width=3,
                                    border_color="#260028",
                                    fg_color="#260028",
                                    hover_color="#eed77a",
                                    checkmark_color="#eed77a",
                                    text_color="#e8ca78",
                                    text_color_disabled=("gray60", "gray45"))
        cb3.grid(row=5,column=0)


        flavor = customtkinter.CTkLabel(master=frame, corner_radius=2, text="Flavor",
                                        font=("Roboto Black 900", 21, "bold"),
                                        text_color=("#ecd778"))
        flavor.grid(row=2,column=1)

        cb4 = customtkinter.CTkCheckBox(master=frame, text="Chicken",
                                    font=("Roboto Black900",12,"bold"),
                                    corner_radius=6,
                                    border_width=3,
                                    border_color="#260028",
                                    fg_color="#260028",
                                    hover_color="#eed77a",
                                    checkmark_color="#eed77a",
                                    text_color="#e8ca78",
                                    text_color_disabled=("gray60", "gray45"))
        cb4.grid(row=3,column=1)

        cb5 = customtkinter.CTkCheckBox(master=frame, text="Mechada",
                                    font=("Roboto Black900",12,"bold"),
                                    corner_radius=6,
                                    border_width=3,
                                    border_color="#260028",
                                    fg_color="#260028",
                                    hover_color="#eed77a",
                                    checkmark_color="#eed77a",
                                    text_color="#e8ca78",
                                    text_color_disabled=("gray60", "gray45"))
        cb5.grid(row=4,column=1)

        cb6 = customtkinter.CTkCheckBox(master=frame, text="Meat",
                                    font=("Roboto Black900",12,"bold"),
                                    corner_radius=6,
                                    border_width=3,
                                    border_color="#260028",
                                    fg_color="#260028",
                                    hover_color="#eed77a",
                                    checkmark_color="#eed77a",
                                    text_color="#e8ca78",
                                    text_color_disabled=("gray60", "gray45"))
        cb6.grid(row=5,column=1)


        extras = customtkinter.CTkLabel(master=frame, corner_radius=2, text="Extras",
                                        font=("Roboto Black 900", 21, "bold"),
                                        text_color=("#ecd778"))
        extras.grid(row=2,column=2)

        cb7 = customtkinter.CTkCheckBox(master=frame, text="Tomato S.",
                                    font=("Roboto Black900",12,"bold"),
                                    corner_radius=6,
                                    border_width=3,
                                    border_color="#260028",
                                    fg_color="#260028",
                                    hover_color="#eed77a",
                                    checkmark_color="#eed77a",
                                    text_color="#e8ca78",
                                    text_color_disabled=("gray60", "gray45"))
        cb7.grid(row=3,column=2)

        cb8 = customtkinter.CTkCheckBox(master=frame, text="mayonnaise",
                                    font=("Roboto Black900",12,"bold"),
                                    corner_radius=6,
                                    border_width=3,
                                    border_color="#260028",
                                    fg_color="#260028",
                                    hover_color="#eed77a",
                                    checkmark_color="#eed77a",
                                    text_color="#e8ca78",
                                    text_color_disabled=("gray60", "gray45"))
        cb8.grid(row=4,column=2)

        cb9 = customtkinter.CTkCheckBox(master=frame, text="More",
                                    font=("Roboto Black900",12,"bold"),
                                    corner_radius=6,
                                    border_width=3,
                                    border_color="#260028",
                                    fg_color="#260028",
                                    hover_color="#eed77a",
                                    checkmark_color="#eed77a",
                                    text_color="#e8ca78",
                                    text_color_disabled=("gray60", "gray45"))
        cb9.grid(row=5,column=2)


        def messagebox():
            tkinter.messagebox.showinfo(title="Succesfull Purchase", message="Your purchase was succesfull")
            app.destroy()
            main()
        
        def cancel():
            app.destroy()
            main()

        buttom_1 = customtkinter.CTkButton(master=frame,  
                                        fg_color=("#ecd778"),
                                        text="COMPRAR",
                                        text_color="#870937",
                                        corner_radius=8,
                                        width=10,
                                        height=10,
                                        font=("Roboto Black 900",12, "bold"),
                                        border_spacing=10,
                                        command=messagebox)
        buttom_1.grid(column=0,row=8)

        buttom_2 = customtkinter.CTkButton(master=frame,  
                                        fg_color=("#ecd778"),
                                        text="CANCELAR",
                                        text_color="#870937",
                                        corner_radius=8,
                                        width=10,
                                        height=10,
                                        font=("Roboto Black 900",12, "bold"),
                                        border_spacing=10,
                                        command=cancel)
        buttom_2.grid(column=2,row=8)


        app.mainloop()

    buttom_1 = customtkinter.CTkButton(master=frame,
                                    image=empanada_normal,
                                    fg_color=("#ecd778"),
                                    text="Freddy's Empanadita",
                                    text_color="#870937",
                                    corner_radius=8,
                                    width=200,
                                    height=110,
                                    font=("Roboto Black 900",30, "bold"),
                                    border_spacing=10,
                                    command=change_frame)
    buttom_1.grid(column=0,row=1,pady = 10, padx=10)

    buttom_2 = customtkinter.CTkButton(master=frame,
                                    image=empanada_arreglada,
                                    fg_color=("#ecd778"),
                                    text="The Arreglada            ",
                                    text_color="#870937",
                                    corner_radius=8,
                                    width=200,
                                    height=110,
                                    font=("Roboto Black 900",30, "bold"),
                                    border_spacing=10,
                                    command=change_frame)
    buttom_2.grid(column=0, row=2, pady = 10,padx=10)

    buttom_3 = customtkinter.CTkButton(master=frame,
                                    image=empanada_pobre,
                                    fg_color=("#ecd778"),
                                    text="Empanada Pobre       ",
                                    text_color="#870937",
                                    corner_radius=8,
                                    width=200,
                                    height=110,
                                    font=("Roboto Black 900",30, "bold"),
                                    border_spacing=10, 
                                    command=change_frame)
    buttom_3.grid(column=0, row=3, pady = 10,padx=10)
        


    root.mainloop()
main()