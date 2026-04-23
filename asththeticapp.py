import streamlit as st

st.set_page_config(page_title="Cute Aesthetic Stationery", layout="wide")

# 🎀 Custom styling
st.markdown("""
    <style>
    body {
        background-color: #ffeef8;
    }
    .title {
        text-align: center;
        color: #ff69b4;
        font-size: 42px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .card {
        background-color: white;
        padding: 15px;
        border-radius: 20px;
        box-shadow: 0px 6px 15px rgba(0,0,0,0.1);
        text-align: center;
    }
    .price {
        color: #ff1493;
        font-weight: bold;
        font-size: 18px;
    }
    </style>
""", unsafe_allow_html=True)

# 🌸 Title
st.markdown('<div class="title">🌸 Cute Aesthetic Stationery 🌸</div>', unsafe_allow_html=True)

# 💖 Real aesthetic product images (Pinterest-style via Unsplash)
products = [
    {
        "name": "Pastel Notebook",
        "price": "₹199",
        "image": "https://images.unsplash.com/photo-1588072432836-e10032774350"
    },
    {
        "name": "Cute Gel Pens",
        "price": "₹99",
        "image": "https://images.unsplash.com/photo-1585386959984-a41552231658"
    },
    {
        "name": "Aesthetic Stickers",
        "price": "₹149",
        "image": "https://images.unsplash.com/photo-1606813902911-df3b8bbaae63"
    },
    {
        "name": "Mini Diary",
        "price": "₹179",
        "image": "https://images.unsplash.com/photo-1519681393784-d120267933ba"
    },
]

# 🧁 Layout
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
