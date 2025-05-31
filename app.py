import streamlit as st
from llm import Model
from extractor import PDFHandler

# Initialize PDF handler and model
pdf_handler = PDFHandler()
model = Model()

# Streamlit interface
st.title('Legal Document Analyzer⚖️')

st.markdown("""
    <style>
    .justified-text {
        text-align: justify;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar Section

for _ in range(3):
        st.sidebar.write("") 

# Menu options
menu = ["Summarize Document", "Highlight Key Points", "Identify Issues", "Generate Legal Advice"]
choice = st.sidebar.selectbox("Choose an option", menu)

st.sidebar.subheader("Features")
st.sidebar.write("Video Summarization") 
st.sidebar.markdown(
    '<a href="https://your-video-summarizer-link.com" target="_blank">'
    '<button style="width:100%;padding:8px 0;background-color:#4CAF50;color:white;border:none;border-radius:4px;">Go to Video Summarizer</button>'
    '</a>',
    unsafe_allow_html=True
)  
for _ in range(7):
        st.sidebar.write("") 
st.sidebar.subheader("Build By:")
st.sidebar.write("[Gourav Chahar](https://gourav-chahar.netlify.app/)")
st.sidebar.write("contact: [Email](mailto:gouravchahar130405@gamil.com)")

if choice == "Summarize Document":
    st.subheader("Summarize Document")
    uploaded_file = st.file_uploader("Upload a legal document (PDF)", type=["pdf"])
    if uploaded_file is not None:
        st.write("Document Uploaded Successfully!")
        if st.button("Summarize"):
            text = pdf_handler.read_pdf(uploaded_file)
            prompt = f"Summarize the uploaded legal document: {text}"
            with st.spinner("Summarizing..."):
                response = model.get_response(prompt)
            st.write("Summary:")
            st.write(response)

elif choice == "Highlight Key Points":
    st.subheader("Highlight Key Points")
    uploaded_file = st.file_uploader("Upload a legal document (PDF)", type=["pdf"])
    if uploaded_file is not None:
        st.write("Document Uploaded Successfully!")
        if st.button("Highlight Points"):
            text = pdf_handler.read_pdf(uploaded_file)
            prompt = f"Highlight the key points in the uploaded legal document: {text}"
            with st.spinner("Highlighting key points..."):
                response = model.get_response(prompt)
            st.write("Highlighted Points:")
            st.write(response)

elif choice == "Identify Issues":
    st.subheader("Identify Issues")
    uploaded_file = st.file_uploader("Upload a legal document (PDF)", type=["pdf"])
    if uploaded_file is not None:
        st.write("Document Uploaded Successfully!")
        if st.button("Identify Issues"):
            text = pdf_handler.read_pdf(uploaded_file)
            prompt = f"Identify potential issues in the uploaded legal document: {text}"
            with st.spinner("Identifying issues..."):
                response = model.get_response(prompt)
            st.write("Issues Identified:")
            st.write(response)

elif choice == "Generate Legal Advice":
    st.subheader("Generate Legal Advice")
    user_input = st.text_area("Enter your legal question or issue")
    if st.button("Get Legal Advice"):
        prompt = f"Provide legal advice on: {user_input}"
        with st.spinner("Generating legal advice..."):
            response = model.get_response(prompt)
        st.write("Legal Advice:")
        st.write(response)