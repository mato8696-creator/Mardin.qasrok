import streamlit as st
import urllib.parse

# ١. ژمارەیا تە یا واتس ئەپێ (ب ڤی شێوەی بنڤیسە)
MY_WHATSAPP = "7504909929" 

st.set_page_config(page_title="Matin Food", page_icon="🍕", layout="centered")

# ستایلێ سایتێ
st.markdown("""
<style>
    .stApp { background-color: #fcfcfc; }
    .food-item { background: white; padding: 15px; border-radius: 12px; border-bottom: 3px solid #25d366; margin-bottom: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    .price-tag { color: #25d366; font-weight: bold; font-size: 1.2rem; }
</style>
""", unsafe_allow_html=True)

st.title("🍕 مینیویا چێشتخانەیا مەتین")
st.write("بخێر بێی! خوارنا خۆ هەلبژێره و ب ڕێکا واتس ئەپێ تەڵەب بکە.")

# ٢. لیستەیا خوارنان (تو دشێی ئەڤان بگوهۆڕی)
menu = {
    "پیتزا شاهانە": 8500,
    "بەرگرێ گۆشتی": 5500,
    "کەنتاکی (٣ پارچە)": 7500,
    "لۆفەیا مریشکێ": 4500,
    "کۆکا کۆلا": 500,
    "ئاڤ": 250
}

# دروستکرنا سەبەتەی
if "cart" not in st.session_state:
    st.session_state.cart = []

# ٣. نیشاندانا مینیوێ
st.subheader("🍴 لیستا خوارنان")
for item, price in menu.items():
    with st.container():
        st.markdown(f'<div class="food-item"><b>{item}</b> - <span class="price-tag">{price} د.ع</span></div>', unsafe_allow_html=True)
        if st.button(f"🛒 زێدە بکە بۆ سەبەتەی ({item})", key=item):
            st.session_state.cart.append({"item": item, "price": price})
            st.toast(f"✅ {item} زێدە بوو")

# ٤. سەبەتە و ناردنا تەڵەبێ
st.divider()
if st.session_state.cart:
    st.subheader("🛒 سەبەتەیا تە")
    total = 0
    items_summary = ""
    for i, order in enumerate(st.session_state.cart):
        st.write(f"{i+1}. {order['item']} - {order['price']} د.ع")
        total += order['price']
        items_summary += f"- {order['item']} ({order['price']} IQD)\n"
    
    st.markdown(f"### **کۆمێ گشتی: {total} دینار**")
    
    if st.button("🗑️ پاکژکرنا سەبەتەی"):
        st.session_state.cart = []
        st.rerun()

    st.divider()
    st.subheader("📋 زانیاریێن گەهاندنێ")
    name = st.text_input("ناڤێ تە:")
    address = st.text_input("ناڤ و نیشان (جهێ تە):")

    if st.button("✅ فڕێکرنا تەڵەبێ بۆ واتس ئەپ"):
        if name and address:
            # ئامادەکردنا پەیامێ
            message = f"📦 تەڵەبەکا نوو هات!\n\n👤 کڕیار: {name}\n📍 جهـ: {address}\n\n🍴 خوارنێن داواکری:\n{items_summary}\n💰 کۆمێ گشتی: {total} دینار"
            
            # دروستکرنا لینکێ واتس ئەپێ
            whatsapp_url = f"https://wa.me/{MY_WHATSAPP}?text={urllib.parse.quote(message)}"
            
            st.markdown(f'<a href="{whatsapp_url}" target="_blank" style="background:#25d366; color:white; padding:15px; border-radius:10px; text-decoration:none; display:block; text-align:center; font-weight:bold;">کلیک لێرە بکە بۆ واتس ئەپ</a>', unsafe_allow_html=True)
        else:
            st.warning("⚠️ تکایە ناڤ و نیشانێن خۆ بنڤیسە.")
else:
    st.info("سەبەتەیا تە بەتالە، خوارنەکێ هەلبژێرە.")

st.write("---")
st.caption("Matin Food Delivery System 2026")

