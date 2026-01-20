import streamlit as st
import urllib.parse

# ژمارەیا واتس ئەپا تە
MY_WHATSAPP = "9647504909929" 

st.set_page_config(page_title="Mardin Qasrok", page_icon="🍴")

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
    input, textarea { background-color: #222 !important; color: white !important; text-align: right !important; }
    .success-msg {
        background-color: rgba(37, 211, 102, 0.2);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #25d366;
        text-align: center;
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

st.title("🍴 خارنگەها ماردین قەسرۆک")

# پشکا زانیارییان
st.subheader("📋 زانیاریێن گەهاندنێ")
address = st.text_input("📍 جهێ تە (ناڤ و نیشان):", placeholder="بۆ نموونە: قەسرۆک - نێزیک قوتابخانێ")
user_note = st.text_area("📝 تێبینییەکا دی هەیە؟", placeholder="بۆ نموونە: بێ بیبەر بیت...")

st.divider()

# لیستا خوارنان
menu_data = [
    {"id": "piz", "name": "پیتزا ایطالي 🍕", "price": 5000, "opts": ["مریشک 🍗", "گۆشت 🥩", "سەوزە 🥦"]},
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
                "price_val": food['price'] * f_qty
            })
            st.toast(f"✅ زێدە بوو")
        st.markdown('</div>', unsafe_allow_html=True)

# پشکا ناردنێ و پەیاما سەرکەفتنێ
if st.session_state.cart:
    st.divider()
    st.header("🛒 سەبەتەیا کڕینێ")
    grand_total = 0
    details = ""
    for item in st.session_state.cart:
        price = item.get('price_val', 0)
        qty = item.get('qty', 1)
        name_item = item.get('name', 'خوارن')
        type_item = item.get('type', 'ئاسایی')
        
        grand_total += price
        st.write(f"🔹 {qty}x {name_item} ({type_item}) = {price} د.ع")
        details += f"- {qty}x {name_item} ({type_item})\n"
    
    st.subheader(f"💰 کۆمێ گشتی: {grand_total} دینار")
    
    if st.button("🚀 تەمامکرنا داخازیێ و ناردن بۆ واتس ئەپ"):
        if address:
            msg = f"📦 تەڵەبەکا نوو هات!\n📍 جهێ کڕیاری: {address}\n📝 تێبینی: {user_note}\n\n🍴 خوارنێن داواکری:\n{details}\n💵 کۆمێ گشتی: {grand_total} دینار"
            url = f"https://wa.me/{MY_WHATSAPP}?text={urllib.parse.quote(msg)}"
            
            # نیشاندانا لینکێ واتس ئەپێ
            st.markdown(f'<a href="{url}" target="_blank" style="background:#25d366; color:white; padding:15px; border-radius:10px; text-decoration:none; display:block; text-align:center; font-weight:bold; margin-bottom: 20px;">✅ کلیک بکە بۆ تەمامکرنێ د واتس ئەپێ دا</a>', unsafe_allow_html=True)
            
            # --- پەیاما ڕێزگرتنێ کو ل سەر سایتێ تە دێ دیار بیت ---
            st.markdown(f"""
            <div class="success-msg">
                <h3>🙏 سوپاس بۆ کڕینا تە</h3>
                <p>داخازیا تە هاتە وەرگرتن. ب کێمتر ژ <b>١ سەعەت</b> دێ گەهیتە دەستێ تە.</p>
                <p><small>ئەگەر هندەک گیرۆ بوو، ببورە ژبەر خەپسەیا ڕێگایە. مە دڤێت باشترین خزمەت پێشکێشی تە بکەین.</small></p>
                <p><b>دگەل ڕێز و سلاڤان، خارنگەها ماردین</b></p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.error("⚠️ تکایە جهێ خۆ بنڤیسە دا خوارن بگەهیتە دەف تە!")

if st.button("🗑️ پاکژکرنا سەبەتەی"):
    st.session_state.cart = []
    st.rerun()
