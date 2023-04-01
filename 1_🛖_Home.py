import streamlit as st

st.set_page_config(
    page_title = "PDF CHAT",
    page_icon = "",
)

st.title("PDF CHAT")
my_text = """
***If you're a student***, ChatPDF can make your learning experience more efficient and effective. With ChatPDF, you can easily understand textbooks, handouts, presentations, and research papers without wasting hours flipping through them. By supporting your academic growth, ChatPDF can help you succeed in your studies responsibly.

***For professionals***, ChatPDF can help you analyze financial reports, sales reports, project proposals, business proposals, training manuals, legal contracts, and other documents quickly and efficiently. Your data is secure in ChatPDF's cloud storage and can be deleted at any time.

***If you're a curious person***, ChatPDF can unlock a wealth of knowledge from historical documents, poetry, literature, and more. ChatPDF understands any language and can reply in your preferred one, making it easy to satisfy your curiosity and expand your horizons. With ChatPDF, you can get answers to any question from any PDF.
"""
st.video('https://youtu.be/qrKwtJN2yfo')
st.markdown(my_text)