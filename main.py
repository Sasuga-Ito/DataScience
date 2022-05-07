import streamlit as st
from streamlit_option_menu import option_menu
from fileset import file_select


def space(num):
    for _ in range(num):
        st.write("")


if __name__ == "__main__":
    st.set_page_config(page_title="Welcome to Data Science Project!",
                       page_icon=":bar_chart:",
                       layout="wide")

    header = st.container()

    with header:
        st.title(":bar_chart: Welcome to Data Science Project!")
        selected = option_menu(
            menu_title="Main menu",
            menu_icon="cast",
            options=["Make file", "Filtering"],
            icons=["file-bar-graph", "filter-square"],
            default_index=0,
            orientation="horizontal"
        )

    if selected == "Make file":
        file_list = []
        with st.sidebar:
            st.header("File settings")
            num_f = st.number_input(
                label="Input a number of files",
                min_value=1,
                max_value=100,
                value=1,
                key="num_files"
            )
            st.markdown("""___""")

            for i in range(num_f):
                if "file" + str(i) not in st.session_state:
                    st.session_state["file" + str(i)] = "File name"

                cols1, cols2 = st.columns(2)
                with cols1:
                    st.write("File" + str(i+1) + " name")
                with cols2:
                    key = "fp" + str(i)
                    if st.button("Browse file" + str(i+1), key=key):
                        st.session_state["file"+str(i)] = file_select()
                file_list.append(st.session_state["file" + str(i)])
                st.code(file_list[i])

                key = "coe" + str(i)
                coe = st.number_input(
                    label="Coefficient",
                    min_value=0.0,
                    max_value=1e20,
                    value=1.0,
                    key=key,
                )
                space(4)
