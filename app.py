import streamlit as st
import urllib.parse

# ژمارەیا تە یا واتس ئەپێ
MY_WHATSAPP = "9647504909929" 

st.set_page_config(page_title="Mardin Qasrok", page_icon="🍕")

# دیزاینا سایتێ
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
    .stButton>button {
        background-color: #e74c3c !important;
        color: white !important;
        border-radius: 10px;
        width: 100%;
    }
    .wa-button {
        background-color: #25d366 !important;
        color: white !important;
        padding: 15px;
        border-radius: 10px;
        text-decoration: none;
        display: block;
        text-align: center;
        font-weight: bold;
        font-size: 18px;
        margin-top: 10px;
    }
    input, textarea { background-color: #222 !important; color: white !important; text-align: right !important; direction: rtl !important; }
</style>
""", unsafe_allow_html=True)

st.title("🍴 خارنگەها ماردین قەسرۆک")

# مینیویا خوارنێ
menu_data = [
    {"id": "piz", "name": "پیتزا ایطالي 🍕", "price": 5000, "opts": ["مریشک 🍗", "گۆشت 🥩", "نیڤ ب نیڤ 🌗"]},
    {"id": "laf_s", "name": "لەفا سوری 🌯", "price": 2000, "opts": ["فەلافل", "پەتاتە", "تێکەڵاو"]},
    {"id": "laf_m", "name": "لەفا مریشکی 🍗", "price": 1000, "opts": ["ئاسایی", "تیژ 🔥"]},
    {"id": "lb", "name": "لەحم بعجین 🌮", "price": 2500, "id_alt": "lb1", "opts": ["سادە", "دگەل پەنێری"]}
]

if "cart" not in st.session_state:
    st.session_state.cart = []

for food in menu_data:
    with st.container():
        st.markdown(f'<div class="food-card">', unsafe_allow_html=True)
        st.markdown(f"### {food['name']}")
        st.write(f"بها: {food['price']} دینار")
        f_type = st.selectbox(f"جۆر:", food['opts'], key=f"t_{food['id']}")
        f_qty = st.number_input(f"ژمارە:", min_value=1, max_value=20, value=1, key=f"q_{food['id']}")
        f_note = st.text_input(f"تێبینی:", placeholder="بۆ نموونە: بێ بیبەر...", key=f"n_{food['id']}")
        
        if st.button(f"🛒 زێدە بکە بۆ سەبەتەی", key=f"b_{food['id']}"):
            st.session_state.cart.append({
                "name": food['name'], "type": f_type, "qty": f_qty, "note": f_note, "price_val": food['price'] * f_qty
            })
            st.toast(f"✅ زێدە بوو")
        st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# --- پشکا ناردنێ و پەیوەندییا بەردەوام ---
st.header("📲 تەمامکرنا داخازیێ یان پەیوەندی")

# نیشاندانا سەبەتەی ئەگەر تشتەک تێدا بیت
grand_total = 0
details = ""
if st.session_state.cart:
    st.subheader("🛒 سەبەتەیا تە:")
    for item in st.session_state.cart:
        grand_total += item['price_val']
        details += f"- {item['qty']} {item['name']} ({item['type']})"
        if item['note']: details += f" [{item['note']}]"
        details += "\n"
        st.write(f"🔹 {item['qty']} {item['name']} ({item['type']})")
    st.write(f"💰 کۆمێ گشتی: **{grand_total} دینار**")
else:
    st.write("سەبەتەیا تە یا ڤالایە، بەس تو دشێی هەر نامەیێ بنێری.")

# بۆشاییێن زانیارییان (هەردەم یێن دیارن)
user_address = st.text_input("📍 جهێ تە (ناڤ و نیشان):")
user_phone = st.text_input("📱 ژمارەیا مۆبایلێ:")
extra_req = st.text_area("✍️ تە چ داخازییێن دیتر هەنە؟", placeholder="ئەگەر خوارن نەڤێت، لێرە بنڤیسە...")

# ئامادەکردنا لینکی
msg = f"📦 تەڵەب/پەیوەندی!\n\n🍴 خوارن:\n{details if details else 'چ خوارن نەهاتییە هەلبژارتن'}\n📍 جهـ: {user_address}\n📞 مۆبایل: {user_phone}\n📝 تێبینی: {extra_req}\n💰 کۆم: {grand_total} دینار"
url = f"https://wa.me/{MY_WHATSAPP}?text={urllib.parse.quote(msg)}"

# دوکما واتس ئەپێ یا بەردەوام
st.markdown(f'<a href="{url}" target="_blank" class="wa-button">✅ کلیک بکە بۆ واتس ئەپێ</a>', unsafe_allow_html=True)

st.markdown("""
<div style="text-align: center; margin-top: 20px; opacity: 0.8;">
    <p>تەڵەب ب کێمتر ژ ١ سەعەت دێ گەهیت.</p>
    <p><b>سوپاس دا خزمەتا تە بکەین</b></p>
</div>
""", unsafe_allow_html=True)

if st.button("🗑️ پاکژکرنا سەبەتەی"):
    st.session_state.cart = []
    st.rerun()
