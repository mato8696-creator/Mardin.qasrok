import streamlit as st
import urllib.parse

MY_WHATSAPP = "9647504909929" 

st.set_page_config(page_title="Mardin Food Pro", page_icon="🍕")

# دیزاینا سایتێ
st.markdown("""
<style>
    .stApp { background-color: #ffffff; }
    h1, h2, h3, p, label { color: #1a1a1a !important; text-align: right; direction: rtl; }
    .food-card {
        background-color: #f9f9f9;
        padding: 20px;
        border-radius: 20px;
        border: 2px solid #eeeeee;
        margin-bottom: 20px;
    }
    .stNumberInput, .stSelectbox { direction: rtl !important; }
</style>
""", unsafe_allow_html=True)

st.title("🍴 مینیویا پێشکەفتییا ماردین قەسرۆک")

# پشکا زانیاریێن گشتی
with st.expander("👤 زانیاریێن کڕیار و جهی (لێرە پڕ بکە)"):
    name = st.text_input("ناڤێ تە:", placeholder="ناڤێ خۆ بنڤیسە")
    map_link = st.text_input("لینکێ خەریتەیێ (Location):", placeholder="لینکێ لێرە دانێ")
    user_note = st.text_area("تێبینییەکا دی هەیە؟", placeholder="بۆ نموونە: بێ پیاز...")

st.divider()

# لیستا خوارنان دگەل فەراخی (Options)
menu_data = [
    {
        "id": "pizza",
        "name": "پیتزا ایطالي 🍕",
        "price": 5000,
        "options": ["گۆشت 🥩", "مریشک 🍗", "نیڤ ب نیڤ 🌗", "سەوزە 🥦"],
        "img": "https://images.unsplash.com/photo-1513104890138-7c749659a591?w=400"
    },
    {
        "id": "lafa",
        "name": "لەفا سوری 🌯",
        "price": 2000,
        "options": ["فەلافل 🧆", "پەتاتە 🍟", "تێکەڵاو ✨"],
        "img": "https://images.unsplash.com/photo-1529006557810-274b9b2fc783?w=400"
    },
    {
        "id": "chicken",
        "name": "لەفا مریشکی 🍗",
        "price": 1000,
        "options": ["بێ سۆس ❌", "سۆس زێدە 🧴", "تیژ (حار) 🔥"],
        "img": "https://images.unsplash.com/photo-1626082927389-6cd097cdc6ec?w=400"
    }
]

if "cart" not in st.session_state:
    st.session_state.cart = []

st.subheader("🍕 خوارنەکێ هەلبژێره و جۆرێ وێ دیار بکە")

for food in menu_data:
    with st.container():
        st.markdown(f'<div class="food-card">', unsafe_allow_html=True)
        col_img, col_txt = st.columns([1, 2])
        
        with col_img:
            st.image(food['img'], use_container_width=True)
        
        with col_txt:
            st.markdown(f"### {food['name']}")
            st.markdown(f"**بها: {food['price']} دینار**")
            
            # فەراخا جۆرێ خوارنێ
            selected_type = st.selectbox(f"جۆرێ {food['name']}:", food['options'], key=f"type_{food['id']}")
            
            # فەراخا ژمارەیێ
            quantity = st.number_input(f"چەند دانە؟", min_value=1, max_value=20, value=1, key=f"qty_{food['id']}")
            
            if st.button(f"🛒 زێدە بکە", key=f"btn_{food['id']}"):
                item_total = food['price'] * quantity
                st.session_state.cart.append({
                    "name": food['name'],
                    "type": selected_type,
                    "qty": quantity,
                    "total_price": item_total
                })
                st.toast(f"✅ {quantity} {food['name']} ({selected_type}) زێدە بوو")
        st.markdown('</div>', unsafe_allow_html=True)

# پیشاندانا سەبەتەی و کۆمێ گشتی
if st.session_state.cart:
    st.divider()
    st.header("🛒 سەبەتەیا کڕینێ")
    grand_total = 0
    order_details = ""
    
    for item in st.session_state.cart:
        line_price = item['total_price']
        grand_total += line_price
        st.write(f"🔹 {item['qty']} دانە {item['name']} - جۆر: {item['type']} = **{line_price} د.ع**")
        order_details += f"- {item['qty']}x {item['name']} ({item['type']})\n"

    st.markdown(f"## 💰 کۆمێ گشتی: {grand_total} دینار")
    
    if st.button("🚀 فرێکرنا تەڵەبێ بۆ واتس ئەپێ"):
        if name and map_link:
            msg = f"📦 تەڵەبەکا نوو هات!\n\n👤 کڕیار: {name}\n📍 جهـ: {map_link}\n📝 تێبینی: {user_note}\n\n🍴 خوارنێن داواکری:\n{order_details}\n💵 کۆمێ گشتی: {grand_total} دینار"
            url = f"https://wa.me/{MY_WHATSAPP}?text={urllib.parse.quote(msg)}"
            st.markdown(f'<a href="{url}" target="_blank" style="background:#25d366; color:white; padding:15px; border-radius:10px; text-decoration:none; display:block; text-align:center; font-weight:bold;">تەمامکرن د واتس ئەپێ دا</a>', unsafe_allow_html=True)
        else:
            st.warning("⚠️ تکایە ناڤ و جهێ خۆ (Location) دیار بکە.")

if st.button("🗑️ پاکژکرنا سەبەتەی"):
    st.session_state.cart = []
    st.rerun()
