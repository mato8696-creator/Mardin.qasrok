import streamlit as st
import urllib.parse

MY_WHATSAPP = "9647504909929" 

st.set_page_config(page_title="Mardin Food Pro", page_icon="🍕")

# ستایلێ سایتێ
st.markdown("""
<style>
    .stApp { background-color: #ffffff; }
    h1, h2, h3, p, label { color: #1a1a1a !important; text-align: right; direction: rtl; }
    .food-card { background-color: #f9f9f9; padding: 20px; border-radius: 20px; border: 2px solid #eeeeee; margin-bottom: 20px; }
</style>
""", unsafe_allow_html=True)

st.title("🍴 مینیویا پێشکەفتییا ماردین قەسرۆک")

# زانیاریێن کڕیاری (هەر حازرن)
st.subheader("📋 زانیاریێن گەهاندنێ")
name = st.text_input("👤 ناڤێ تە:", placeholder="ناڤێ خۆ بنڤیسە")
map_link = st.text_input("📍 لینکێ خەریتەیێ (Location):", placeholder="لینکێ لێرە دانێ")
user_note = st.text_area("📝 تێبینی (چ تە دڤێت؟):", placeholder="بۆ نموونە: بێ بیبەر بیت...")

st.divider()

# لیستا خوارنان
menu_data = [
    {"id": "piz", "name": "پیتزا ایطالي 🍕", "price": 5000, "opts": ["گۆشت 🥩", "مریشک 🍗", "سەوزە 🥦"]},
    {"id": "laf_s", "name": "لەفا سوری 🌯", "price": 2000, "opts": ["فەلافل", "پەتاتە", "تێکەڵاو"]},
    {"name": "لەفا مریشکی 🍗", "price": 1000, "id": "laf_m", "opts": ["ئاسایی", "تیژ 🔥"]},
    {"name": "لەحم بعجین 🌮", "price": 2500, "id": "l_b", "opts": ["سادە", "دگەل پەنێری"]}
]

if "cart" not in st.session_state:
    st.session_state.cart = []

for food in menu_data:
    with st.container():
        st.markdown(f'<div class="food-card">', unsafe_allow_html=True)
        st.markdown(f"### {food['name']}")
        st.write(f"بها: {food['price']} دینار")
        
        # فەراخێن تە دڤیان
        f_type = st.selectbox(f"جۆرێ خوارنێ:", food['opts'], key=f"t_{food['id']}")
        f_qty = st.number_input(f"چەند دانە؟", min_value=1, max_value=10, value=1, key=f"q_{food['id']}")
        
        if st.button(f"🛒 زێدە بکە", key=f"b_{food['id']}"):
            st.session_state.cart.append({
                "name": food['name'],
                "type": f_type,
                "qty": f_qty,
                "price": food['price'] * f_qty
            })
            st.toast("زێدە بوو!")
        st.markdown('</div>', unsafe_allow_html=True)

# پشکا سەبەتەی
if st.session_state.cart:
    st.divider()
    st.header("🛒 سەبەتەیا کڕینێ")
    grand_total = 0
    details = ""
    for item in st.session_state.cart:
        grand_total += item['price']
        st.write(f"🔹 {item['qty']}x {item['name']} ({item['type']}) = {item['price']} د.ع")
        details += f"- {item['qty']}x {item['name']} ({item['type']})\n"
    
    st.subheader(f"کۆم: {grand_total} دینار")
    
    if st.button("🚀 ناردن بۆ واتس ئەپ"):
        if name and map_link:
            msg = f"📦 تەڵەبەکا نوو!\n👤 کڕیار: {name}\n📍 جهـ: {map_link}\n📝 تێبینی: {user_note}\n\n🍴 خوارن:\n{details}\n💰 کۆم: {grand_total} دینار"
            st.markdown(f'<a href="https://wa.me/{MY_WHATSAPP}?text={urllib.parse.quote(msg)}" target="_blank" style="background:#25d366; color:white; padding:15px; border-radius:10px; text-decoration:none; display:block; text-align:center;">تەمامکرن ل واتس ئەپێ</a>', unsafe_allow_html=True)
        else:
            st.error("تکایە ناڤ و جهێ خۆ بنڤیسە!")

if st.button("🗑️ پاکژکرنا سەبەتەی"):
    st.session_state.cart = []
    st.rerun()
