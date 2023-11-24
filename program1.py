import tkinter as tk
from tkinter import messagebox, PhotoImage

def shopping_cart(apple_quantity, orange_quantity):
    apple_price = 20
    orange_price = 25
    total_cost = (apple_quantity * apple_price) + (orange_quantity * orange_price)
    return total_cost

def generate_receipt(apple_quantity, orange_quantity, total_cost):
    receipt_text = f"Receipt\n\n"
    receipt_text += f"Apples: {apple_quantity} x 20 = {apple_quantity * 20} \n"
    receipt_text += f"Oranges: {orange_quantity} x 25 = {orange_quantity * 25} \n"
    receipt_text += f"Total Amount: ₱{total_cost} \n\n"
    receipt_text += f"Do you want to check out?\n"
    return receipt_text

def cart_items():
    try:
        apple_quantity = int(apple_input.get())
        orange_quantity = int(orange_input.get())
        total_cost = shopping_cart(apple_quantity, orange_quantity)

        receipt_text = generate_receipt(apple_quantity, orange_quantity, total_cost)
        messagebox.showinfo("Receipt", receipt_text)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid number.")
        
def on_exit():
    if messagebox.askokcancel("Exit", "Do you want to exit?"):
        root.destroy()

# Main Window
root = tk.Tk()
root.title("Via Corporation")
root.geometry("860x790")

image_path=PhotoImage(file=r"C:\Users\RACHELL\OneDrive\Avah\Files\fruitas.png")
bg_image=tk.Label(root,image=image_path)
bg_image.place(relheight=1,relwidth=1)

# Labels and Widgets
label_description = tk.Label(root, text="Enter Number of Fruits You Want to Buy", font=('Helvetica',15), bd=4, relief="sunken")
label_description.place(relx=0.5, rely=0.3, anchor="center")

label_apple = tk.Label(root, text="Quantity of apples:", font=('Helvetica',13), bd=4, relief="sunken")
label_apple.place(x=320, y=290, anchor="center")

apple_input = tk.Entry(root, font=('Helvetica',13), bd=4, relief="sunken")
apple_input.place(x=520, y=290, anchor="center")

label_orange = tk.Label(root, text="Quantity of oranges:", font=('Helvetica',13), bd=4, relief="sunken")
label_orange.place(x=320, y=330, anchor="center")

orange_input = tk.Entry(root, font=('Helvetica',13), bd=4, relief="sunken")
orange_input.place(x=520, y=330, anchor="center")

# Cart Button
cart_button = tk.Button(root, text="Add to cart", command=cart_items, font=('Helvetica',15), bd=4, bg='#FF5733', fg='white')
cart_button.place(relx=0.5, rely=0.5, anchor="center")

# Window Close 
root.protocol("WM_DELETE_WINDOW", on_exit)

root.mainloop()