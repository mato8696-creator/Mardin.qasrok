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
        border: none;
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
    {"id": "lb", "name": "لەحم بعجین 🌮", "price": 2500, "opts": ["سادە", "دگەل پەنێری"]}
]

if "cart" not in st.session_state:
    st.session_state.cart = []

# نیشاندانا خوارنان
for food in menu_data:
    with st.container():
        st.markdown(f'<div class="food-card">', unsafe_allow_html=True)
        st.markdown(f"### {food['name']}")
        st.write(f"بها: {food['price']} دینار")
        f_type = st.selectbox(f"جۆر:", food['opts'], key=f"t_{food['id']}")
        f_qty = st.number_input(f"ژمارە:", min_value=1, max_value=20, value=1, key=f"q_{food['id']}")
        f_note = st.text_input(f"تێبینی:", placeholder="بۆ نموونە: بێ بیبەر...", key=f"n_{food['id']}")
        
        if st.button(f"🛒 زێدە بکە", key=f"b_{food['id']}"):
            st.session_state.cart.append({
                "name": food['name'], "type": f_type, "qty": f_qty, "note": f_note, "price_val": food['price'] * f_qty
            })
            st.toast(f"✅ زێدە بوو")
        st.markdown('</div>', unsafe_allow_html=True)

# پشکا سەبەتەی و زانیاریێن گەهاندنێ
if st.session_state.cart:
    st.divider()
    st.header("🛒 سەبەتەیا تە")
    grand_total = 0
    details = ""
    for item in st.session_state.cart:
        grand_total += item['price_val']
        details += f"- {item['qty']} {item['name']} ({item['type']})"
        if item['note']: details += f" [{item['note']}]"
        details += "\n"
        st.write(f"🔹 {item['qty']} {item['name']} ({item['type']})")

    st.subheader(f"💰 کۆمێ گشتی: {grand_total} دینار")
    
    # --- بۆشاییێن نوو بۆ جهـ و مۆبایلێ ---
    st.markdown("### 📞 زانیاریێن گەهاندنێ")
    user_address = st.text_input("📍 جهێ تە (ناڤ و نیشان):", placeholder="بۆ نموونە: قەسرۆک - نێزیک مزگەفتێ")
    user_phone = st.text_input("📱 ژمارەیا مۆبایلێ:", placeholder="0750 XXX XX XX")
    extra_req = st.text_area("✍️ تە چ داخازییێن دیتر هەنە؟", placeholder="هەر تشتەکێ دی لێرە بنڤیسە...")

    # ئامادەکردنا نامەیێ
    if st.button("🚀 تەمامکرنا داخازیێ"):
        if user_address and user_phone:
            msg = f"📦 تەڵەبەکا نوو!\n\n🍴 خوارن:\n{details}\n📍 جهـ: {user_address}\n📞 مۆبایل: {user_phone}\n📝 تێبینی: {extra_req}\n💰 کۆم: {grand_total} دینار"
            url = f"https://wa.me/{MY_WHATSAPP}?text={urllib.parse.quote(msg)}"
            
            st.markdown(f'<a href="{url}" target="_blank" style="background:#25d366; color:white; padding:15px; border-radius:10px; text-decoration:none; display:block; text-align:center; font-weight:bold;">✅ کلیک بکە بۆ ناردنێ بۆ واتس ئەپ</a>', unsafe_allow_html=True)
            st.info("تەڵەب ب کێمتر ژ ١ سەعەت دێ گەهیت. دگەل ڕێز و سلاڤان.")
        else:
            st.warning("⚠️ تکایە جهـ و ژمارەیا مۆبایلێ بنڤیسە بەری ناردنێ!")

if st.button("🗑️ پاکژکرنا سەبەتەی"):
    st.session_state.cart = []
    st.rerun()
