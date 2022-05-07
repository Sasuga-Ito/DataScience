import os
import streamlit as st
import tkinter as tk
from tkinter import filedialog, messagebox


def file_select():
    if "filedir" not in st.session_state:
        st.session_state["filedir"] = "C:\\"

    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()

    filetype = [('All', '*')]
    file = filedialog.askopenfilename(
        initialdir=st.session_state["filedir"],
        filetypes=filetype
    )
    root.destroy()

    if file == "":
        caution(
            title="Caution",
            message="Please choose a file"
        )
        file = file_select()

    st.session_state["filedir"] = os.path.dirname(file)

    return file


def caution(title, message):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showwarning(
        title=title,
        message=message
    )
    root.destroy()


if __name__ == "__main__":
    file_select()
