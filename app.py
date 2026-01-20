import streamlit as st
import urllib.parse

# ژمارەیا تە یا واتس ئەپێ
MY_WHATSAPP = "9647504909929" 

st.set_page_config(page_title="Mardin Qasrok", page_icon="🍴")

# دیزاینا سایتێ (ڕەنگی ڕەش و وێنەیێ پاشبنەمایێ)
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(rgba(0,0,0,0.75), rgba(0,0,0,0.75)), 
        url("https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1000");
        background-size: cover;
        color: white;
    }
    h1, h2, h3, p, label { color: white !important; text-align: right; direction: rtl; }
    .food-card {
        background-color: rgba(30, 30, 30, 0.9);
        padding: 20px;
        border-radius: 20px;
        border: 1px solid #444;
        margin-bottom: 20px;
        text-align: center;
    }
    input, textarea { background-color: #222 !important; color: white !important; text-align: right !important; }
</style>
""", unsafe_allow_html=True)

st.title("🍴 خارنگەها ماردین قەسرۆک")
st.write("ب خێرهاتی بۆ مینیویا ماردین قەسرۆک")

# --- پشکا زانیارییان (تەنێ ناڤ و تێبینی) ---
st.subheader("📋 زانیاریێن کڕیاری")
name = st.text_input("👤 ناڤێ تە:", placeholder="ناڤێ خۆ لێرە بنووسە")
user_note = st.text_area("📝 تێبینی یان ناڤ و نیشان:", placeholder="لێرە بنڤیسە کا چ تە دڤێت...")

st.divider()

# لیستا خوارنان
menu_data = [
    {"id": "piz", "name": "پیتزا ایطالي 🍕", "price": 5000, "opts": ["مریشک 🍗", "گۆشت 🥩", "نیڤ ب نیڤ 🌗", "سەوزە 🥦"]},
    {"id": "laf_s", "name": "لەفا سوری 🌯", "price": 2000, "opts": ["فەلافل", "پەتاتە", "تێکەڵاو"]},
    {"id": "laf_m", "name": "لەفا مریشکی 🍗", "price": 1000, "opts": ["ئاسایی", "تیژ 🔥", "بێ سۆس"]},
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
        
        # هەڵبژارتنا جۆر و ژمارەیێ
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
        if name:
            msg = f"📦 تەڵەبەکا نوو!\n👤 کڕیار: {name}\n📝 تێبینی: {user_note}\n\n🍴 خوارن:\n{details}\n💰 کۆم: {grand_total} دینار"
            url = f"https://wa.me/{MY_WHATSAPP}?text={urllib.parse.quote(msg)}"
            st.markdown(f'<a href="{url}" target="_blank" style="background:#25d366; color:white; padding:15px; border-radius:10px; text-decoration:none; display:block; text-align:center; font-weight:bold;">تەمامکرنا تەڵەبێ د واتس ئەپێ دا</a>', unsafe_allow_html=True)
        else:
            st.error("⚠️ تکایە ناڤێ خۆ بنڤیسە!")

if st.button("🗑️ پاکژکرنا سەبەتەی"):
    st.session_state.cart = []
    st.rerun()
