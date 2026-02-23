import streamlit as st
from database import (
    create_table,
    add_product,
    view_product,
    update_name,
    update_quantity,
    update_price,
    update_all,
    delete_product,
    get_low_stock
)

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Inventory Dashboard",
    page_icon="📦",
    layout="wide"
)

create_table()

# ---------------- SIDEBAR ----------------
st.sidebar.title("📦 Inventory System")

page = st.sidebar.radio(
    "Navigation",
    ["🏠 Home", "➕ Add Product", "📋 Inventory", "✏️ Update Product", "🗑️ Delete Product"]
)

# Load products once
products = view_product()

# ---------------- HOME PAGE ----------------
if page == "🏠 Home":

    st.title("📦 Inventory Management Dashboard")
    st.markdown("### Welcome to your inventory system")

    total_products = len(products) if products else 0
    total_quantity = sum(p[2] for p in products) if products else 0
    total_value = sum(p[2] * p[3] for p in products) if products else 0

    low_stock_items = get_low_stock()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Products", total_products)
    col2.metric("Total Quantity", total_quantity)
    col3.metric("Inventory Value", f"₹ {total_value:.2f}")
    col4.metric("Low Stock Items", len(low_stock_items))
    low_stock = get_low_stock()

    if low_stock:
        st.warning("⚠️ Low Stock Alert!")

        for item in low_stock:
            st.write(f"Product: {item[1]} | Quantity Left: {item[2]}")

    st.divider()

    st.subheader("Recent Inventory Overview")

    if products:
        st.dataframe(products, use_container_width=True)
    else:
        st.info("No products available yet.")

# ---------------- ADD PRODUCT ----------------
elif page == "➕ Add Product":

    st.title("Add New Product")

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Product Name")

    with col2:
        quantity = st.number_input("Quantity", min_value=0, step=1)

    price = st.number_input("Price (₹)", min_value=0.0, step=1.0)

    if st.button("Add Product", use_container_width=True):
        if name:
            add_product(name, quantity, price)
            st.success("✅ Product added successfully!")
            st.rerun()
        else:
            st.warning("Product name required.")

# ---------------- VIEW INVENTORY ----------------
elif page == "📋 Inventory":

    st.title("Inventory List")

    search = st.text_input("🔎 Search Product")

    if products:
        if search:
            filtered = [
                p for p in products
                if search.lower() in p[1].lower()
            ]
            st.dataframe(filtered, use_container_width=True)
        else:
            st.dataframe(products, use_container_width=True)
    else:
        st.warning("Inventory is empty.")
        
# ---------------- UPDATE PRODUCT ----------------
elif page == "✏️ Update Product":

    st.title("Update Product")

    if not products:
        st.warning("No products available.")
    else:
        st.dataframe(products, use_container_width=True)

        product_id = st.number_input("Product ID", min_value=1, step=1)

        option = st.selectbox(
            "Select what to update",
            ["Name", "Quantity", "Price", "Everything"]
        )

        if option == "Name":
            new_name = st.text_input("New Name")
            if st.button("Update"):
                update_name(product_id, new_name)
                st.success("Updated successfully!")
                st.rerun()

        elif option == "Quantity":
            new_qty = st.number_input("New Quantity", min_value=0)
            if st.button("Update"):
                update_quantity(product_id, new_qty)
                st.success("Updated successfully!")
                st.rerun()

        elif option == "Price":
            new_price = st.number_input("New Price", min_value=0.0)
            if st.button("Update"):
                update_price(product_id, new_price)
                st.success("Updated successfully!")
                st.rerun()

        elif option == "Everything":
            new_name = st.text_input("New Name")
            new_qty = st.number_input("New Quantity", min_value=0)
            new_price = st.number_input("New Price", min_value=0.0)

            if st.button("Update Product"):
                update_all(product_id, new_name, new_qty, new_price)
                st.success("Product updated!")
                st.rerun()

# ---------------- DELETE PRODUCT ----------------
elif page == "🗑️ Delete Product":

    st.title("Delete Product")

    if not products:
        st.warning("No products available.")
    else:
        st.dataframe(products, use_container_width=True)

        product_id = st.number_input("Enter Product ID", min_value=1, step=1)

        confirm = st.checkbox("I confirm deletion")

        if st.button("Delete Product", use_container_width=True):
            if confirm:
                delete_product(product_id)
                st.success("Product deleted successfully!")
                st.rerun()
            else:
                st.warning("Please confirm deletion.")