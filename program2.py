import tkinter as tk
from tkinter import messagebox, PhotoImage

def compute_number_apples(money, apple_price):
    max_apples = money // apple_price
    remaining_money = money % apple_price
    return max_apples, remaining_money

def show_result():
    try:
        money = int(money_input.get())
        apple_price = float(apple_price_input.get())

        price_of_apples, remaining_money = compute_number_apples(money, apple_price)

        result_window = tk.Toplevel(root)
        result_window.title("Result")
        result_window.geometry("200x200")
      
        result_label = tk.Label(result_window, text=f'Number of Apples: {price_of_apples: .2f} pcs \nChange: {remaining_money: .2f} pesos')
        result_label.place(relx=0.5, rely=0.5, anchor="center")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid amounts.")

def on_closing():
    if messagebox.askokcancel("Exit", "Do you want to exit?"):
        root.destroy()

# Main Window
root = tk.Tk()
root.title("Via Corporation")
root.geometry("860x790")

image_path=PhotoImage(file=r"C:\Users\RACHELL\OneDrive\Avah\Files\fruitas2.png")
bg_image=tk.Label(root,image=image_path)
bg_image.place(relheight=1,relwidth=1)

# Labels and Widgets
label_description = tk.Label(root, text="Enter the right values in the following:", font=('Helvetica',15), bd=4, relief="sunken")
label_description.place(relx=0.5, rely=0.3, anchor="center")

money_label = tk.Label(root, text="Amount of money you have:", font=('Helvetica',13), bd=4, relief="sunken")
money_label.place(x=340, y=290, anchor="center")

money_input = tk.Entry(root, font=('Helvetica',13), bd=4, relief="sunken")
money_input.place(x=560, y=290, anchor="center")

apple_price_label = tk.Label(root, text="Price of apples:", font=('Helvetica',13), bd=4, relief="sunken")
apple_price_label.place(x=340, y=330, anchor="center")

apple_price_input = tk.Entry(root, font=('Helvetica',13), bd=4, relief="sunken")
apple_price_input.place(x=560, y=330, anchor="center")

# Compute Button
compute_button = tk.Button(root, text="Add to cart", command=show_result, font=('Helvetica',15), bd=4, bg='#FF5733', fg='white')
compute_button.place(relx=0.5, rely=0.5, anchor="center")

# Window Close 
root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()