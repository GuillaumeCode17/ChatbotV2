import threading
from time import sleep
from tkinter import *
from chat import get_response, bot_name
from utils.variables import *

CD = Default_Color


class ChatApplication:
    def __init__(self) -> None:
        self.window = Tk()
        self._setup_main_window()

    def run(self):
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title("Chat")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=570, height=670, bg=CD.BG_COLOR)

        # head label
        head_label = Label(self.window, bg=CD.BG_COLOR, fg=CD.TEXT_COLOR,
                           text="Welcome, Write 'Quit' to exit", font=CD.FONT_BOLD, pady=10)
        head_label.place(relwidth=1)

        # head_instructions = Label
        #     self.window, bg="black", fg="White", text="Instructions")
        # head_instructions.grid(row=1, column=1)

        # tiny divider
        line = Label(self.window, width=450, bg=CD.BG_GRAY)
        line.place(relwidth=1, rely=0.07, relheight=0.012)

        # text widget
        self.text_widget = Text(self.window, width=20, height=2,
                                bg="black", fg=CD.TEXT_COLOR, font=CD.FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        # scrool bar
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)

        # bottom label widget
        bottom_label = Label(self.window, bg=CD.BG_GRAY, height=80)
        bottom_label.place(relwidth=1, rely=0.825)

        # message entry box
        self.msg_entry = Entry(bottom_label, borderwidth=10, bg="black",
                               fg=CD.TEXT_COLOR, font=("Times", 20), insertbackground="white")
        self.msg_entry.place(relwidth=0.74, relheight=0.06,
                             rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

        # send button
        send_button = Button(bottom_label, text="Send", font=CD.FONT_BOLD,
                             width=20, bg=CD.BG_GRAY, command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)

    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "You")

    def _insert_message(self, msg, sender):
        if not msg:
            return

        def User_text():
            self.msg_entry.delete(0, END)
            msgp1 = f"{sender}"
            msg1 = f": {msg}\n\n"
            self.text_widget.tag_config('user', foreground=CD.ORANGE)
            self.text_widget.configure(state=NORMAL)
            self.text_widget.insert(END, msgp1, 'user')
            self.text_widget.insert(END, msg1)
            self.text_widget.configure(state=DISABLED)

        def SkyNet_text():
            sleep(0.370)
            msgp2 = f"{bot_name}"
            msg2 = f": {get_response(msg)}\n\n"
            quitting = ": Okay Boss, I'm Closing the app..."
            clearing = ": Okay Boss, I'm cleaning the ChatBox"
            self.text_widget.tag_config('SkyNet', foreground=CD.GREEN)
            print(msg)
            if msg.lower() == "quit" or msg.lower() == "exit":
                self.text_widget.configure(state=NORMAL)
                self.text_widget.insert(END, msgp2, 'SkyNet')
                self.text_widget.insert(END, quitting)
                self.text_widget.configure(state=DISABLED)
                self.text_widget.see(END)
                sleep(2)
                self.window.quit()
            elif msg.lower() == "clear" or msg.lower() == "cls":
                self.text_widget.configure(state=NORMAL)
                self.text_widget.insert(END, msgp2, 'SkyNet')
                self.text_widget.insert(END, clearing)
                sleep(1)
                self.text_widget.delete('1.0', END)
                self.text_widget.configure(state=DISABLED)
                self.text_widget.see(END)
            else:
                self.text_widget.configure(state=NORMAL)
                self.text_widget.insert(END, msgp2, 'SkyNet')
                self.text_widget.insert(END, msg2)
                self.text_widget.configure(state=DISABLED)
                self.text_widget.see(END)

        User_text()
        threading.Thread(target=SkyNet_text).start()


if __name__ == "__main__":
    app = ChatApplication()
    app.run()
