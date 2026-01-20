import streamlit as st
import urllib.parse

MY_WHATSAPP = "9647504909929" 

st.set_page_config(page_title="Mardin Qasrok", page_icon="📍")

# دیزاینا سایتێ (ڕەنگی ڕەش و وێنەیێ پاشبنەمایێ)
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), 
        url("https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1000"); /* وێنەیێ خارنگەهەکا جوان */
        background-size: cover;
        color: white;
    }
    h1, h2, h3, p, label { color: white !important; text-align: right; direction: rtl; }
    .food-card {
        background-color: rgba(30, 30, 30, 0.85); /* ڕەشەکێ ڕوون */
        padding: 20px;
        border-radius: 20px;
        border: 1px solid #444;
        margin-bottom: 20px;
        text-align: center;
    }
    .stSelectbox, .stNumberInput { direction: rtl !important; }
    .map-btn {
        background-color: #4285F4 !important;
        color: white !important;
        padding: 12px;
        border-radius: 10px;
        text-align: center;
        display: block;
        text-decoration: none;
        font-weight: bold;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

st.title("🍴 خارنگەها ماردین قەسرۆک")
st.write("بخێر بێی بۆ جوانترین خارنگەها قەسرۆکێ")

# --- پشکا زانیارییان و خەریتەیێ (هەر حازرە) ---
st.subheader("📋 زانیاریێن گەهاندنێ")
name = st.text_input("👤 ناڤێ تە:", placeholder="ناڤێ خۆ لێرە بنووسە")

st.markdown('<a href="https://www.google.com/maps" target="_blank" class="map-btn">📍 ڤەکرنا Google Maps بۆ دیارکرنا جهی</a>', unsafe_allow_html=True)
map_link = st.text_input("🔗 لینکێ جهێ خۆ (Location) لێرە دانێ:", placeholder="لینکێ لێرە 'Paste' بکە...")

user_note = st.text_area("📝 تێبینییەکا دی هەیە؟", placeholder="بۆ نموونە: بێ بیبەر بیت...")

st.divider()

# لیستا خوارنان
menu_data = [
    {"id": "piz", "name": "پیتزا ایطالي 🍕", "price": 5000, "opts": ["گۆشت 🥩", "مریشک 🍗", "سەوزە 🥦"]},
    {"id": "laf_s", "name": "لەفا سوری 🌯", "price": 2000, "opts": ["فەلافل", "پەتاتە", "تێکەڵاو"]},
    {"id": "laf_m", "name": "لەفا مریشکی 🍗", "price": 1000, "opts": ["ئاسایی", "تیژ 🔥"]},
    {"id": "lb", "name": "لەحم بعجین 🌮", "price": 2500, "opts": ["سادە", "دگەل پەنێری"]}
]

if "cart" not in st.session_state:
    st.session_state.cart = []

st.subheader("🍕 مینیویا خوارنێ")

for food in menu_data:
    with st.container():
        st.markdown(f'<div class="food-card">', unsafe_allow_html=True)
        st.markdown(f"### {food['name']}")
        st.write(f"بها: {food['price']} دینار")
        
        f_type = st.selectbox(f"جۆرێ {food['name']}:", food['opts'], key=f"t_{food['id']}")
        f_qty = st.number_input(f"چەند دانە؟", min_value=1, max_value=20, value=1, key=f"q_{food['id']}")
        
        if st.button(f"🛒 زێدە بکە بۆ سەبەتەی", key=f"b_{food['id']}"):
            st.session_state.cart.append({
                "name": food['name'],
                "type": f_type,
                "qty": f_qty,
                "price": food['price'] * f_qty
            })
            st.toast(f"✅ {f_qty} {food['name']} زێدە بوو")
        st.markdown('</div>', unsafe_allow_html=True)

# پشکا سەبەتەی و ناردنێ
if st.session_state.cart:
    st.divider()
    st.header("🛒 سەبەتەیا کڕینێ")
    grand_total = 0
    details = ""
    for item in st.session_state.cart:
        grand_total += item['price']
        st.write(f"🔹 {item['qty']}x {item['name']} ({item['type']}) = {item['price']} د.ع")
        details += f"- {item['qty']}x {item['name']} ({item['type']})\n"
    
    st.subheader(f"💰 کۆمێ گشتی: {grand_total} دینار")
    
    if st.button("🚀 فرێکرنا تەڵەبێ بۆ واتس ئەپ"):
        if name and map_link:
            msg = f"📦 تەڵەبەکا نوو!\n👤 کڕیار: {name}\n📍 جهـ: {map_link}\n📝 تێبینی: {user_note}\n\n🍴 خوارن:\n{details}\n💰 کۆم: {grand_total} دینار"
            st.markdown(f'<a href="https://wa.me/{MY_WHATSAPP}?text={urllib.parse.quote(msg)}" target="_blank" style="background:#25d366; color:white; padding:15px; border-radius:10px; text-decoration:none; display:block; text-align:center; font-weight:bold;">تەمامکرنا تەڵەبێ د واتس ئەپێ دا</a>', unsafe_allow_html=True)
        else:
            st.error("⚠️ تکایە ناڤ و لینکێ جهێ خۆ (Location) بنڤیسە!")

if st.button("🗑️ پاکژکرنا سەبەتەی"):
    st.session_state.cart = []
    st.rerun()
