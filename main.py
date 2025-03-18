import streamlit as st
import json

st.set_page_config(page_title="Personal Library by urooj shakeel" , page_icon="📚" , layout="centered")
# load & save library data
def load_library():
    try:
        with open("library.json", "r")as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_libray():
    with open("library.json", "w")as file:
        json.dump(library,file,indent=4)

# initialize laibrary
library = load_library()

st.title("Personal Library Manager")
menu = st.sidebar.radio("Select an Option",["View Library","Add Book","Remove Book","Search Book","Save and Exit"])
if menu == "View Library":
    st.sidebar.title("Your Library")
    if library:
        st.table(library)
    else:
        st.write("No book in your library. Add some books!")

#Add book
elif menu == "Add Book": 
    st.title("Add a new book")
    title = st.text_input("Title")
    author = st.text_input("Author")
    year = st.number_input("Year",min_value=2010, max_value=2100,step=1)
    genre = st.text_input("Genre")
    read_status = st.checkbox("Mark as Read")
    
    if st.button("Add Book"):
        library.append({"title":title, "author":author,"year":year,"genre":genre,"read_status":read_status})
        save_libray()
        st.success("Book added successfully!")
        st.rerun()

# remove book
elif menu == "Remove Book":
    st.title("Remove a book")
    book_titles = [book["title"] for book in library]

    if book_titles:
        selected_book = st.selectbox("Select a book to Remove", book_titles)
        if st.button("Remove Book"):
            library = [book for book in library if book["title"] != selected_book]
            save_libray()
            st.success("Book removed successfully!")
            st.rerun()
        else:
            st.warning("No book in your library.add some books!.")

#search book 
elif menu == "Search Book":
    st.sidebar.title("search a book...")
    search_term = st.text_input("Enter Title or author name:")

    if st.button("Search"):
        results = [book for book in library if search_term.lower()in book["title"].lower() or search_term.lower() in book["author"].lower()]
        if results:
            st.table(results)
        else:
            st.warning("No book found!")
            
    
# save and exit
elif menu == "Save and Exit":
    save_libray()
    st.success("Library saved successfully!")

         
