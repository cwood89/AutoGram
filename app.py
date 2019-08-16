import tkinter as tk
import screenShot
import postToGram
HEIGHT = 600
WIDTH = 400
BACKGROUND_COLOR = "#292929"
BACKGROUND_ALT = "#4a4a4a"
TEXT_COLOR = "#65f752"


def submit_post():
    user = user_field.get()
    pswd = password_field.get()
    title = post_field.get()
    descript = description_field.get("1.0", "end-1c")
    screenShot.shot(title=title, cs=codesample_field.get('1.0', "end"))
    file = open("output.txt", "w")
    file.write(str(codesample_field.get('1.0', "end")))
    file.close()
    s = " "
    print(user + s + pswd +
          s + title + s + descript)


root = tk.Tk()
root.title("AutoGram")
root.iconbitmap(r"images/autogramicon.ico")

canvas = tk.Canvas(root, bg=BACKGROUND_COLOR, height=HEIGHT,
                   width=WIDTH, highlightthickness=0)
canvas.pack()

background_image = tk.PhotoImage(
    file="images/matrix.png", width=WIDTH, height=HEIGHT)
background_label = tk.Label(
    canvas, bg=BACKGROUND_COLOR, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

container = tk.Frame(root, bg=BACKGROUND_ALT)
container.place(relx=0.1, rely=0.11, relwidth=0.8, relheight=0.8)

title = tk.Label(canvas, text="AutoGram", bg=BACKGROUND_ALT,
                 fg=TEXT_COLOR, font=("Arial", 40))
title.place(relx=0.1, rely=0.02, relwidth=0.8)

frame = tk.Frame(container, bg=BACKGROUND_ALT)
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)


username = tk.Label(frame, text="username: ",
                    bg=BACKGROUND_ALT, fg=TEXT_COLOR, font=("Arial", 12), pady=7)
username.grid(row=0, column=0)
user_field = tk.Entry(frame, bg="white")
user_field.grid(row=0, column=1)

password = tk.Label(frame, text="password: ",
                    bg=BACKGROUND_ALT, fg=TEXT_COLOR, font=("Arial", 12), pady=7)
password.grid(row=1, column=0)
password_field = tk.Entry(frame, bg="white", show="\u2022")
password_field.grid(row=1, column=1)

post = tk.Label(frame, text="title: ",
                bg=BACKGROUND_ALT, fg=TEXT_COLOR, font=("Arial", 12), pady=7)
post.grid(row=2, column=0)
post_field = tk.Entry(frame, bg="white")
post_field.grid(row=2, column=1)

codesample = tk.Label(frame, text="code sample: ",
                      bg=BACKGROUND_ALT, fg=TEXT_COLOR, font=("Arial", 12), pady=7)
codesample.grid(row=3, column=0)
codesample_field = tk.Text(frame, width=15, height=5, bg="white")
codesample_field.grid(row=3, column=1, pady=7)

description = tk.Label(frame, text="description: ",
                       bg=BACKGROUND_ALT, fg=TEXT_COLOR, font=("Arial", 12), pady=7)
description.grid(row=4, column=0)
description_field = tk.Text(frame, width=15, height=5, bg="white")
description_field.grid(row=4, column=1, pady=7)

button = tk.Button(frame, text="Post", fg=BACKGROUND_COLOR,
                   bg=TEXT_COLOR, command=submit_post)
button.place(relx=0.35, rely=0.9, relheight=0.05, relwidth=0.30)

root.mainloop()
