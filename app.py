import streamlit as st
import urllib.parse

# ژمارەی واتس ئەپەکەت
MY_WHATSAPP = "9647504909929" 

st.set_page_config(page_title="Mardin Food", page_icon="🍕")

# دیزاینا سایتێ (CSS)
st.markdown("""
<style>
    .stApp { background-color: #f8f9fa; }
    h1, h2, h3, p, label { color: #1a1a1a !important; text-align: right; direction: rtl; }
    .food-card {
        background-color: white;
        padding: 15px;
        border-radius: 15px;
        border: 1px solid #e0e0e0;
        margin-bottom: 15px;
        text-align: center;
    }
    .price { color: #2ecc71; font-size: 20px; font-weight: bold; }
    input, textarea { text-align: right !important; direction: rtl !important; }
    .stButton>button {
        width: 100%;
        background-color: #27ae60 !important;
        color: white !important;
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)

st.title("🍴 خارنگەها ماردین قەسرۆک")

# --- پشکا زانیارییان (ئەوێن تە دڤێت هەر حازر بن) ---
st.subheader("📋 زانیاریێن کڕیاری")
col1, col2 = st.columns(2)
with col1:
    address = st.text_input("📍 ناڤ و نیشان:", placeholder="جهێ خۆ بنڤیسە")
with col2:
    name = st.text_input("👤 ناڤێ تە:", placeholder="ناڤێ خۆ بنڤیسە")

user_note = st.text_area("📝 تێبینی (چ تە دڤێت؟):", placeholder="بۆ نموونە: بێ بیبەر بیت...")

st.divider()

# --- لیستا خوارنان ---
st.subheader("🍕 مینیویا خوارنێ")
menu = [
    {"name": "پیتزا ایطالي 🍕", "price": 5000, "img": "https://images.unsplash.com/photo-1513104890138-7c749659a591?w=400"},
    {"name": "لەفا سوری 🌯", "price": 2000, "img": "https://images.unsplash.com/photo-1529006557810-274b9b2fc783?w=400"},
    {"name": "لەفا مریشکی 🍗", "price": 1000, "img": "https://images.unsplash.com/photo-1626082927389-6cd097cdc6ec?w=400"},
    {"name": "لەحم بعجین 🌮", "price": 2500, "img": "https://images.unsplash.com/photo-1593560708920-61dd98c46a4e?w=400"}
]

if "cart" not in st.session_state:
    st.session_state.cart = []

for food in menu:
    with st.container():
        st.markdown(f'<div class="food-card">', unsafe_allow_html=True)
        st.image(food['img'], use_container_width=True)
        st.markdown(f'<div style="font-size: 22px; font-weight: bold; color:black;">{food["name"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="price">بها: {food["price"]} دینار</div>', unsafe_allow_html=True)
        if st.button(f"➕ زێدە بکە بۆ سەبەتەی", key=food['name']):
            st.session_state.cart.append(food)
            st.toast(f"✅ {food['name']} زێدە بوو")
        st.markdown('</div>', unsafe_allow_html=True)

# --- پشکا سەبەتەی و ناردنێ ---
if st.session_state.cart:
    st.divider()
    st.subheader("🛒 سەبەتەیا تە")
    total = sum(item['price'] for item in st.session_state.cart)
    summary = "\n".join([f"- {i['name']}" for i in st.session_state.cart])
    
    st.write(f"کۆمێ گشتی: **{total} دینار**")
    
    if st.button("🚀 ناردنا تەڵەبێ بۆ واتس ئەپ"):
        if name and address:
            msg = f"📦 تەڵەبەکا نوو!\n👤 کڕیار: {name}\n📍 جهـ: {address}\n📝 تێبینی: {user_note}\n\n🍴 خوارن:\n{summary}\n💰 کۆم: {total} دینار"
            url = f"https://wa.me/{MY_WHATSAPP}?text={urllib.parse.quote(msg)}"
            st.markdown(f'<a href="{url}" target="_blank" style="background:#25d366; color:white; padding:15px; border-radius:10px; text-decoration:none; display:block; text-align:center; font-weight:bold;">تەمامکرنا تەڵەبێ ل واتس ئەپێ</a>', unsafe_allow_html=True)
        else:
            st.error("⚠️ تکایە ناڤ و جهێ خۆ بنڤیسە!")
