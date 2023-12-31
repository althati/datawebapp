import streamlit as st
import os

def save_files():
    files =st.session_state.file_upload_widget
    print('inside save_files: ', files)
    doc_dir = 'data'
    if len(files) > 0:
        for file in files:
            with open(os.path.join(doc_dir, file.name), 'wb') as f:
                f.write(file.getbuffer())



def main():
    col1, col2 = st.columns(2)

    st.sidebar.title('Upload Robinhood Monthly Brokarage Account Statement')
    with st.sidebar.form(key='sidebar_form'):
        # Allow the user to upload a files
        uploaded_files = st.file_uploader('Upload files',
                                          type=['pdf'],
                                          key='file_upload_widget',
                                          accept_multiple_files=True,
                                          disabled=False)

        # If a files was uploaded, display its contents
        submit_btn = st.form_submit_button('Upload Files',
                                           on_click=save_files,
                                           disabled=False)
        if submit_btn:
            st.sidebar.write('No more upload possible')

main()