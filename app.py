import streamlit as st
import urllib.parse

# ژمارەیا تە یا واتس ئەپێ (ڕاست بکە)
MY_WHATSAPP = "7504909929" 

st.set_page_config(page_title="Matin Food", page_icon="🍔")

# دیزاینا سایتێ (CSS)
st.markdown("""
<style>
    .stApp { background-color: #ffffff; }
    h1, h2, h3, p { color: #1a1a1a !important; text-align: right; direction: rtl; }
    .food-card {
        background: #f9f9f9;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #eeeeee;
        margin-bottom: 15px;
        text-align: right;
    }
    .price { color: #25d366; font-size: 20px; font-weight: bold; }
    .stButton>button {
        width: 100%;
        background-color: #25d366 !important;
        color: white !important;
        border-radius: 10px;
        border: none;
        padding: 10px;
    }
</style>
""", unsafe_allow_html=True)

st.title("🍴 خارنگە ها ماردین قەسرۆک")
st.write("بخێر بێی! باشترین خوارن ل دەف مە پەیدا دبن.")

# لیستەیا خوارنان ب وێنە (Emoji)
menu = [
    {"name": "پیتزا ایطالي 🍕", "price": 5000 "هزار},
    {"name": "لەفا سوری", "price": 2000 "هزار},
    {"name": "لە فا مریشکی", "price": 1000 " هزار},
    {"name": "لەحم معجین ", "price": 1500 2500 3000},
    {"name": "کۆکا کۆلا 🥤", "price": 500},
    {"name": "ئاڤ 💧", "price": 250}
]

if "cart" not in st.session_state:
    st.session_state.cart = []

# نیشاندانا خوارنان ب شێوازێ کارت
for food in menu:
    st.markdown(f"""
    <div class="food-card">
        <div style="font-size: 22px; font-weight: bold;">{food['name']}</div>
        <div class="price">بها: {food['price']} دینار</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button(f"کڕینا {food['name']}", key=food['name']):
        st.session_state.cart.append(food)
        st.toast(f"{food['name']} زێدە بوو")

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
            msg = f"📦 تەڵەبەکا نوو!\n👤 کڕیار: {name}\n📍 ناڤ و نیشان: {address}\n\n🍴 خوارن:\n{summary}\n💰 کۆم: {total} دینار"
            url = f"https://wa.me/{MY_WHATSAPP}?text={urllib.parse.quote(msg)}"
            st.markdown(f'<a href="{url}" target="_blank" style="background:#25d366; color:white; padding:15px; border-radius:10px; text-decoration:none; display:block; text-align:center; font-weight:bold;">کلیک بکە بۆ تەمامکرنێ د واتس ئەپێ دا</a>', unsafe_allow_html=True)
