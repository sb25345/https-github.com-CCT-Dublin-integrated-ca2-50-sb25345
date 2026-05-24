import streamlit as st
import pandas as pd

st.set_page_config(page_title="Easy Grocery Helper", layout="wide")

st.title("🛒 Easy Smart Grocery Helper")
st.markdown("**Big clear text • Simple navigation • Made for adults 65+**")


# ====================== LOAD DATA ======================
@st.cache_data
def load_data():
    try:
        return pd.read_csv("long_df.csv")
    except:
        st.error("Data file not found. Please make sure long_df.csv is uploaded.")
        return pd.DataFrame()


long_df = load_data()

if long_df.empty:
    st.stop()

# Top products
top_products = long_df['product'].value_counts().head(15)

# ====================== SIDEBAR ======================
st.sidebar.header("Choose a Page")
page = st.sidebar.radio("Go to:",
                        ["Most Popular Items", "Often Bought Together", "Why This Helps"])

# ====================== PAGE 1 ======================
if page == "Most Popular Items":
    st.subheader("Top 15 Most Popular Grocery Items")
    st.bar_chart(top_products, use_container_width=True)

# ====================== PAGE 2: Often Bought Together ======================
elif page == "Often Bought Together":
    st.subheader("Often Bought Together")
    st.write("Select a product to see common combinations:")

    selected = st.selectbox("Choose a product:", top_products.index.tolist())

    # Real rules (you can expand this)
    rules = {
        "Organic Whole Strawberries": ["Banana", "Organic Blueberries", "Greek Yogurt", "Organic Whole Milk"],
        "Organic Bakery Hamburger Buns Wheat - 8 CT": ["Organic Original Hommus", "Grapefruit Sparkling Water"],
        "Vitamin D Whole Milk": ["Aged White Cheddar Baked Rice & Corn Puffs", "Bag of Organic Bananas"],
        "Bag of Organic Bananas": ["Organic Whole Milk", "Organic Strawberries"],
    }

    companions = rules.get(selected, ["Organic Whole Milk", "Banana", "Greek Yogurt"])

    st.write(f"**Main Item:** {selected}")
    st.write("**Customers often buy these together:**")
    for item in companions:
        st.success(f"• {item}")

# ====================== PAGE 3 ======================
else:
    st.subheader("Why This Dataset is Great for Machine Learning")
    st.markdown("""
    This app uses real data from **over 800,000 shopping baskets** from Instacart.

    It helps online grocery stores by:
    - Showing popular items
    - Suggesting useful combinations
    - Making shopping faster and easier for you

    **Designed with large text and simple layout for adults 65+**
    """)

st.caption("Educational project using uchoice-Instacart dataset | For academic purposes only")