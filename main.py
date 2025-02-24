import customtkinter as ctk

root = ctk.CTk()
root.geometry("500x500")
root.title("Calculator")
root.resizable(False, False)
ctk.set_appearance_mode("dark")

equation_text =""
equation_label= ctk.StringVar()

def button_click(number):
    global equation_text
    equation_text += str(number)
    equation_label.set(equation_text)

def button_clear():
    global equation_text    
    equation_text = ""
    equation_label.set(equation_text)

def button_equal():
    global equation_text

    if "^" in equation_text:
        equation_text = equation_text.replace("^", "**")
    elif "%" in equation_text:
        equation_text = equation_text.replace("%", "/100")
    result = str(eval(equation_text))
    equation_label.set(result)
    equation_text = result




#put label text to right of the window
label = ctk.CTkLabel(root, 
                      font=("Rupee",40), 
                      width=500, height=80, 
                      fg_color="transparent",
                      corner_radius=4,
                      padx=10, pady=10,
                      anchor="e",
                      textvariable=equation_label
                      )
label.pack()

buttonframe = ctk.CTkFrame(root, width=500, height=500, fg_color="transparent")

buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)
buttonframe.columnconfigure(3, weight=1)
buttonframe.columnconfigure(4, weight=1)

#button width & height
btheight= 60
btwidth= 100

#first row
btn1 = ctk.CTkButton(buttonframe, height=btheight, width=btwidth, font=("Rupee",20), text="AC", fg_color="#893900", command=button_clear, corner_radius=400)
btn1.grid(row=0, column=0, padx=8, pady=8, sticky="nsew")

btn2 = ctk.CTkButton(buttonframe, height=btheight, width=btwidth,corner_radius=400, font=("Rupee",20), text="^", fg_color="#893900", command=lambda:button_click("^"))
btn2.grid(row=0, column=1, padx=8, pady=8, sticky="nsew")

btn3 = ctk.CTkButton(buttonframe, height=btheight, width=btwidth,corner_radius=400, font=("Rupee",20), text="%", fg_color="#893900", command=lambda:button_click("%"))
btn3.grid(row=0, column=2, padx=8, pady=8, sticky="nsew")

btn4 = ctk.CTkButton(buttonframe, height=btheight, width=btwidth,corner_radius=400, font=("Rupee",20), text="/", fg_color="#893900", command=lambda:button_click("/"))
btn4.grid(row=0, column=3, padx=8, pady=8, sticky="nsew")

#second row
btn5 = ctk.CTkButton(buttonframe, height=btheight, width=btwidth,corner_radius=400, font=("Rupee",20), text="7", command=lambda:button_click("7"))
btn5.grid(row=1, column=0, padx=8, pady=8, sticky="nsew")

btn6 = ctk.CTkButton(buttonframe, height=btheight, width=btwidth,corner_radius=400, font=("Rupee",20), text="8", command=lambda:button_click("8"))
btn6.grid(row=1, column=1, padx=8, pady=8, sticky="nsew")

btn7 = ctk.CTkButton(buttonframe, height=btheight, width=btwidth,corner_radius=400, font=("Rupee",20), text="9", command=lambda:button_click("9"))
btn7.grid(row=1, column=2, padx=8, pady=8, sticky="nsew")

btn8 = ctk.CTkButton(buttonframe, height=btheight, width=btwidth,corner_radius=400, font=("Rupee",20), text="*",fg_color="#893900", command=lambda:button_click("*"))
btn8.grid(row=1, column=3, padx=8, pady=8, sticky="nsew")

#third row
btn9 = ctk.CTkButton(buttonframe, height=btheight, width=btwidth,corner_radius=400, font=("Rupee",20), text="4", command=lambda:button_click("4"))
btn9.grid(row=2, column=0, padx=8, pady=8, sticky="nsew")

btn10 = ctk.CTkButton(buttonframe, height=btheight, width=btwidth,corner_radius=400, font=("Rupee",20), text="5", command=lambda:button_click("5"))
btn10.grid(row=2, column=1, padx=8, pady=8, sticky="nsew")

btn11 = ctk.CTkButton(buttonframe, height=btheight, width=btwidth,corner_radius=400, font=("Rupee",20), text="6", command=lambda:button_click("6"))
btn11.grid(row=2, column=2, padx=8, pady=8, sticky="nsew")

btn12 = ctk.CTkButton(buttonframe, height=btheight, width=btwidth,corner_radius=400, font=("Rupee",20), text="-", fg_color="#893900", command=lambda:button_click("-"))
btn12.grid(row=2, column=3, padx=8, pady=8, sticky="nsew")

#fourth row
btn13 = ctk.CTkButton(buttonframe, height=btheight, width=btwidth,corner_radius=400, font=("Rupee",20), text="1", command=lambda:button_click("1"))
btn13.grid(row=3, column=0, padx=8, pady=8, sticky="nsew")

btn14 = ctk.CTkButton(buttonframe, height=btheight, width=btwidth,corner_radius=400, font=("Rupee",20), text="2", command=lambda:button_click("2"))
btn14.grid(row=3, column=1, padx=8, pady=8, sticky="nsew")

btn15 = ctk.CTkButton(buttonframe, height=btheight, width=btwidth,corner_radius=400, font=("Rupee",20), text="3", command=lambda:button_click("3"))
btn15.grid(row=3, column=2, padx=8, pady=8, sticky="nsew")

btn16 = ctk.CTkButton(buttonframe, height=btheight, width=btwidth,corner_radius=400, font=("Rupee",20), text="+", fg_color="#893900", command=lambda:button_click("+"))
btn16.grid(row=3, column=3, padx=8, pady=8, sticky="nsew")

#fifth row
btn17 = ctk.CTkButton(buttonframe, height=btheight, width=btwidth,corner_radius=400, font=("Rupee",20), text="0", command=lambda:button_click("0"))
btn17.grid(row=4, columnspan=2, padx=8, pady=8, sticky="nsew")

btn18 = ctk.CTkButton(buttonframe, height=btheight, width=btwidth,corner_radius=400, font=("Rupee",20), text=".", command=lambda:button_click("."))
btn18.grid(row=4, column=2, padx=8, pady=8, sticky="nsew")

btn19 = ctk.CTkButton(buttonframe, height=btheight, width=btwidth,corner_radius=400, font=("Rupee",20), text="=", fg_color="#893900", command=button_equal)
btn19.grid(row=4, column=3, padx=8, pady=8, sticky="nsew")



buttonframe.pack(padx=16,pady=8,fill="both",expand=True)

root.mainloop()