import streamlit as st
import urllib.parse

# ژمارەیا تە یا واتس ئەپێ (پێدڤییە ب 964 دەسپێ بکەت)
MY_WHATSAPP = "9647504909929" 

st.set_page_config(page_title="Mardin Food", page_icon="🍔")

# دیزاینا سایتێ (CSS)
st.markdown("""
<style>
    .stApp { background-color: #ffffff; }
    h1, h2, h3, p { color: #1a1a1a !important; text-align: right; direction: rtl; }
    .food-card {
        background: #f9f9f9;
        padding: 15px;
        border-radius: 15px;
        border: 1px solid #eeeeee;
        margin-bottom: 20px;
        text-align: center;
    }
    .price { color: #25d366; font-size: 22px; font-weight: bold; margin-top: 10px; }
    .stButton>button {
        width: 100%;
        background-color: #25d366 !important;
        color: white !important;
        border-radius: 10px;
        font-weight: bold;
    }
    img { border-radius: 10px; object-fit: cover; }
</style>
""", unsafe_allow_html=True)

st.title("🍴 خارنگەها ماردین قەسرۆک")
st.write("ب خێرهاتی بۆ باشترین خوارنێن قەسرۆکێ")

# لیستەیا خوارنان دگەل وێنەیان
menu = [
    {
        "name": "پیتزا ایطالي 🍕", 
        "price": 5000, 
        "img": "https://images.unsplash.com/photo-1513104890138-7c749659a591?w=400"
    },
    {
        "name": "لەفا سوری 🌯", 
        "price": 2000, 
        "img": "https://images.unsplash.com/photo-1529006557810-274b9b2fc783?w=400"
    },
    {
        "name": "لەفا مریشکی 🍗", 
        "price": 1000, 
        "img": "https://images.unsplash.com/photo-1626082927389-6cd097cdc6ec?w=400"
    },
    {
        "name": "لەحم بعجین 🌮", 
        "price": 2500, 
        "img": "https://images.unsplash.com/photo-1593560708920-61dd98c46a4e?w=400"
    },
    {
        "name": "کۆکا کۆلا 🥤", 
        "price": 500, 
        "img": "https://images.unsplash.com/photo-1622483767028-3f66f32aef97?w=400"
    },
    {
        "name": "ئاڤ 💧", 
        "price": 250, 
        "img": "https://images.unsplash.com/photo-1548839140-29a749e1cf4d?w=400"
    }
]

if "cart" not in st.session_state:
    st.session_state.cart = []

# نیشاندانا خوارنان
for food in menu:
    with st.container():
        st.markdown(f'<div class="food-card">', unsafe_allow_html=True)
        st.image(food['img'], use_container_width=True)
        st.markdown(f'<div style="font-size: 24px; font-weight: bold;">{food["name"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="price">بها: {food["price"]} دینار</div>', unsafe_allow_html=True)
        if st.button(f"کڕینا {food['name']}", key=food['name']):
            st.session_state.cart.append(food)
            st.toast(f"✅ {food['name']} زێدە بوو")
        st.markdown('</div>', unsafe_allow_html=True)

# پشکا سەبەتەی
if st.session_state.cart:
    st.divider()
    st.header("🛒 سەبەتەیا تە")
    total = sum(item['price'] for item in st.session_state.cart)
    
    for item in st.session_state.cart:
        st.write(f"✅ {item['name']} - {item['price']} د.ع")
    
    st.markdown(f"### کۆمێ گشتی: {total} دینار")
    
    name = st.text_input("ناڤێ تە:", placeholder="ناڤێ خۆ لێرە بنووسە")
    address = st.text_input("ناڤ و نیشان:", placeholder="ناونیشانی خۆ لێرە بنووسە")

    if st.button("✅ ناردنا تەڵەبێ بۆ واتس ئەپ"):
        if name and address:
            summary = "\n".join([f"- {i['name']}" for i in st.session_state.cart])
            msg = f"📦 تەڵەبەکا نوو!\n👤 کڕیار: {name}\n📍 جهـ: {address}\n\n🍴 خوارن:\n{summary}\n💰 کۆم: {total} دینار"
            url = f"https://wa.me/{MY_WHATSAPP}?text={urllib.parse.quote(msg)}"
            st.markdown(f'<a href="{url}" target="_blank" style="background:#25d366; color:white; padding:15px; border-radius:10px; text-decoration:none; display:block; text-align:center; font-weight:bold;">کلیک بکە بۆ تەمامکرنێ د واتس ئەپێ دا</a>', unsafe_allow_html=True)
