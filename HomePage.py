import streamlit as st

# Page configuration
st.set_page_config(
    page_title="MonsoonSIM - Retail Module Tools",
    page_icon="🏪",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap');
    
    body {
        color: #E0E0E0;
        background-color: #1E1E1E;
    }
    .stApp {
        background-color: #1E1E1E;
    }
    .main-header {
        font-size: 2.8rem;
        color: #61DAFB;
        text-align: center;
        margin-bottom: 1.5rem;
        font-weight: 700;
    }
    .sub-header {
        font-size: 2rem;
        color: #BB86FC;
        margin-top: 2rem;
        margin-bottom: 1rem;
        font-weight: 500;
    }
    .feature-header {
        font-size: 1.4rem;
        color: #03DAC6;
        margin-top: 1.5rem;
        margin-bottom: 0.5rem;
        font-weight: 500;
    }
    .info-box {
        background-color: #2C2C2C;
        padding: 1.5rem;
        border-radius: 10px;
        margin-top: 2rem;
        border: 1px solid #424242;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .start-button {
        text-align: center;
        margin-top: 2rem;
    }
    .custom-button {
        background-color: #03DAC6;
        color: #121212;
        padding: 0.75rem 1.5rem;
        font-size: 1.1rem;
        font-weight: 600;
        border: none;
        border-radius: 30px;
        cursor: pointer;
        transition: all 0.3s ease;
        text-decoration: none;
        display: inline-block;
    }
    .custom-button:hover {
        background-color: #018786;
        box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
        transform: translateY(-2px);
    }
    .stExpander {
        border: 1px solid #424242;
        border-radius: 10px;
        margin-bottom: 1rem;
        background-color: #2C2C2C;
    }
    a {
        color: #BB86FC;
        text-decoration: none;
    }
    a:hover {
        text-decoration: underline;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Main content
st.markdown(
    "<h1 class='main-header'>MonsoonSIM - Retail Module Tools</h1>",
    unsafe_allow_html=True,
)

st.markdown(
    "<div style='text-align: center; padding: 10px; background-color: #2C2C2C; border-radius: 10px; margin-bottom: 20px;'>"
    "<p style='margin: 0; font-size: 1.1rem;'>Created by Muhammad Raihan | University of Al Azhar Indonesia</p>"
    "<p style='margin: 10px 0;'>Connect with me: "
    "<a href='https://www.linkedin.com/in/muhammad-raihan-0ba3872ab' target='_blank'>LinkedIn</a> | "
    "<a href='https://www.instagram.com/muhandrai/' target='_blank'>Instagram</a>"
    "</p>"
    "</div>",
    unsafe_allow_html=True,
)

# Display a retail-related image
st.image(
    "https://images.unsplash.com/photo-1556740738-b6a63e27c4df?auto=format&fit=crop&w=1000&q=80",
    caption="Innovative Retail Solutions",
    use_column_width=True,
)

st.markdown(
    """
    ## MonsoonSIM - Experiential Learning through Business Simulations and Gamification

    MonsoonSIM is revolutionizing business education by offering gamified learning experiences 
    that bridge theory and practice. With over 120,371 users across more than 200 academic 
    institutions worldwide, it provides real-world scenarios for hands-on learning.
    """
)

st.markdown(
    """
    <h3 class='sub-header'>Tool Overview</h3>

    This advanced tool, developed by **Muhammad Raihan** from the University of Al Azhar Indonesia, 
    is designed to enhance the MonsoonSIM learning experience for retail business scenarios.
    """,
    unsafe_allow_html=True,
)

with st.expander("Features"):
    st.markdown(
        """
    1. Multi-Location Management:
        - Manage multiple retail locations
        - Input location-specific details like rental size, rental cost, and overflow fee
        - Apply product categories to all locations
    
    2. Retail Information Tracking:
        - Record store rental size, rental costs, and overflow fees
        - Track product details like costs, initial prices, shelf life, and product dimensions
        - Store and retrieve location-specific information using session state

    3. Capacity Planning:
        - Calculate stock percentage based on product dimensions and rental size
        - Provide feedback on whether the selected product quantities exceed the available rental space

    4. Price Strategy:
        - Calculate the average minimum price per unit to cover all costs
        - Consider rental costs, overflow fees, and product costs in the calculation

    5. Sales Velocity:
        - Input daily sales data for each product
        - Calculate average sales per day for each product

    6. Marketing Evaluation:
        - Compare before and after sales data for each product
        - Calculate the change in sales and percentage change

    7. Session State Management:
        - Store and retrieve location-specific information using Streamlit's session state
        - Display the session state for the selected rental location in the sidebar as JSON
    """
    )

st.markdown(
    """
    ### How to Use This Tool:

    1. Use the sidebar to input your store locations and select a product category.
    2. Select a store location to view and edit its specific details.
    3. Use the "Retail Information" expander to input rental details and edit product information.
    4. Utilize the various tools in each tab to analyze different aspects of your retail operations:
       - Capacity Planning: Check if your stock fits within the rental space
       - Price Strategy: Calculate minimum prices to cover costs
       - Sales Velocity: Track and analyze daily sales
       - Marketing Evaluation: Compare sales before and after marketing efforts
    5. View your session data in the sidebar for a quick overview of your inputs.
    """
)
