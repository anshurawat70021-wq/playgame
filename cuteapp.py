import streamlit as st

# Page settings
st.set_page_config(page_title="Cute Aesthetic Stationery", layout="wide")

# Custom CSS for aesthetic look
st.markdown("""
    <style>
    body {
        background-color: #ffeef8;
    }
    .title {
        text-align: center;
        color: #ff69b4;
        font-size: 40px;
        font-weight: bold;
    }
    .card {
        background-color: white;
        padding: 15px;
        border-radius: 15px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
        text-align: center;
    }
    .price {
        color: #ff1493;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">🌸 Cute Aesthetic Stationery 🌸</div>', unsafe_allow_html=True)

# Products data
products = [
    {"name": "Pastel Notebook", "price": "₹199", "image": "https://via.placeholder.com/200"},
    {"name": "Cute Gel Pens", "price": "₹99", "image": "https://via.placeholder.com/200"},
    {"name": "Aesthetic Stickers", "price": "₹149", "image": "https://via.placeholder.com/200"},
    {"name": "Mini Diary", "price": "₹179", "image": "https://via.placeholder.com/200"},
]

# Layout in columns
cols = st.columns(4)

for i, product in enumerate(products):
    with cols[i % 4]:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.image(product["image"])
        st.subheader(product["name"])
        st.markdown(f'<p class="price">{product["price"]}</p>', unsafe_allow_html=True)

        if st.button(f"Buy {product['name']}", key=i):
            st.success("🛍️ Added to cart!")

        st.markdown('</div>', unsafe_allow_html=True)
