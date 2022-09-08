from tkinter import *
from textblob import TextBlob


def clear_all():
    word1_field.delete(0, END)
    word2_field.delete(0, END)


def correction():
    word2_field.delete(0, END)
    input_word = word1_field.get()

    # Textblob Documentation: https://textblob.readthedocs.io/en/dev/
    blob_obj = TextBlob(input_word)

    corrected_word = str(blob_obj.correct())
    word2_field.insert(10, corrected_word)


if __name__ == "__main__":
    # Tkinter documentation:  https://docs.python.org/3/library/tk.html
    root = Tk()  # Create a GUI window
    root.configure(background='#293A4A')  # Set the background colour of GUI window
    root.geometry("380x100")  # Set the configuration of GUI window (WidthxHeight)

    # Set the name of tkinter GUI window
    root.title("GUI example with spell corrector")
    head_label = Label(root, text='Spell Corrector', fg='white', bg="#293A4A")
    lbl_input = Label(root, text="Input Word", fg='white', bg='#293A4A')
    lbl_corrected = Label(root, text="Corrected Word", fg='white', bg='#293A4A')

    # Grid method
    head_label.grid(row=0, column=1)
    lbl_input.grid(row=1, column=0)
    lbl_corrected.grid(row=3, column=0, padx=10)

    # Create a text entry box
    word1_field = Entry()
    word2_field = Entry()

    # (padx - pady) Keyword argument used to set padding along x-axis and x-axis
    word1_field.grid(row=1, column=1, padx=10, pady=5)
    word2_field.grid(row=3, column=1, padx=10, pady=5)

    btn_correction = Button(root, text="Correction", bg="#179bd7", fg="white", command=correction, height=1, width=10)
    btn_correction.grid(row=1, column=2)

    btn_clear_all = Button(root, text="Clear", bg="#f2b138", fg="black", command=clear_all, height=1, width=10)
    btn_clear_all.grid(row=3, column=2)

    root.mainloop()  # Start the GUI
