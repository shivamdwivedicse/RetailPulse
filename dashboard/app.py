import streamlit as st 
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
import pickle 


#page configuration
st.set_page_config(
    page_title = "RetailPulse",
    page_icon = "🛒",
    layout = "wide"
)


#sidebar Navigation 
st.sidebar.title("🛒 RetailPulse")
st.sidebar.markdown("----")

page = st.sidebar.selectbox(
    "Navigation",
    ["🏠 Home",
     "👥 Customer Segmentation",
     "📉 Churn Prediction",
     "📈 Demand Forecasting",
     "📦 Inventory Optimization"]
)
#---------------------------Home page 

if page == "🏠 Home":
    st.title("🛒 RetailPulse")
    st.subheader("AI-Powered Customer Analytics and Demand Forecasting Platform")
    st.markdown("---")

    st.header("📊 Key Metrics")

#Key metricdone s :- 
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("👥 Total Customers", "4,989")
    with col2:
        st.metric("🎯 AUC-ROC Score", "0.99")
    with col3:
        st.metric("📈 MAPE Score", "7.41%")
    with col4:
        st.metric("📦 Stock Reduction", "35%")

    st.markdown("---")

#Project overview:-

    st.header("🎯 Project Overview")
    st.write("""RetailPulse is an end-to-end Data Science solution for retail businesses using Machine Learning and Advanced Analytics.""")

#4 tasks cards:-

    st.header("✅ Project Tasks")
    col1 , col2 = st.columns(2)

    with col1:
         
        st.success("👥 Customer Segmentation — K-Means (6 Clusters)")
        st.success("📉 Churn Prediction — XGBoost + SHAP")

    with col2:
        st.success("📈 Demand Forecasting — Prophet (MAPE 7.41%)")
        st.success("📦 Inventory Optimization — 35% Reduction")


    st.markdown("---")

# Dataset Info
    st.header("📂 Datasets Used")

    col1, col2 = st.columns(2)

    with col1:
        st.info("🛒 Online Retail II — 1M+ Transactions")
    with col2:
        st.info("🏪 Store Sales Forecasting Dataset")



# ------------SEGMENTATION PAGE------




elif page == "👥 Customer Segmentation":
    
    st.title("👥 Customer Segmentation")
    st.markdown("---")
    
    # Load data
    rfm = pd.read_csv('rfm_segments.csv')
    
    # Metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Customers", len(rfm))
    with col2:
        st.metric("Total Segments", "6")
    with col3:
        st.metric("Algorithm", "K-Means")
    
    st.markdown("---")
    
    # Segment Distribution
    st.header("📊 Segment Distribution")
    
    fig, ax = plt.subplots(figsize=(10,4))
    rfm['Segment'].value_counts().plot(
        kind='bar', color='Green', ax=ax)
    ax.set_title('Customers per Segment')
    ax.set_xlabel('Segment')
    ax.set_ylabel('Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig)
    
    st.markdown("---")
    
    # Segment Filter
    st.header("🔍 Explore Segments")
    
    selected_segment = st.selectbox(
        "Select Segment:",
        rfm['Segment'].unique()
    )
    
    filtered = rfm[rfm['Segment'] == selected_segment]
    st.write(f"Total Customers: {len(filtered)}")
    st.dataframe(filtered[['Customer ID', 'Recency', 'Frequency', 'Monetary', 'Segment']])




# ---------------- CHURN PAGE ----------



elif page == "📉 Churn Prediction":
    
    st.title("📉 Churn Prediction")
    st.markdown("---")
    
    # Load data
    rfm = pd.read_csv('rfm_segments.csv')
    
    # Metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("AUC-ROC Score", "0.99")
    with col2:
        st.metric("Precision@top20%", "0.43")
    with col3:
        at_risk = len(rfm[rfm['Segment'] == 'At risk'])
        st.metric("At Risk Customers", at_risk)
    
    st.markdown("---")
    
    # At Risk customers table
    st.header("⚠️ At Risk Customers")
    at_risk_df = rfm[rfm['Segment'] == 'At risk']
    st.dataframe(at_risk_df[['Customer ID', 'Recency',
                              'Frequency', 'Monetary']])
    
    st.markdown("---")
    
    # What-if Analysis
    st.header("🔮 What-if Analysis")
    st.write("Enter the value of customer and Predict")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        recency = st.slider("Recency (days)", 0, 738, 100)
    with col2:
        frequency = st.slider("Frequency", 1, 50, 5)
    with col3:
        monetary = st.slider("Monetary (₹)", 0, 5000, 1000)
    
    # Load model
    model = pickle.load(open('churn_model.pkl', 'rb'))
    
    # Predict
    input_data = np.array([[recency, frequency, monetary]])
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]
    
    if st.button("🔮 Predict"):
        if prediction == 1:
            st.error(f"⚠️ At Risk! Probability: {probability:.2%}")
        else:
            st.success(f"✅ Active! Probability: {1-probability:.2%}")




# -----------FORECASTING PAGE----------------


elif page == "📈 Demand Forecasting":
    st.title("📈 Demand Forecasting")
    st.markdown("---")

    #Metrics 
    col1,col2,col3 = st.columns(3)
    with col1:
        st.metric("MAPE Score :", "7.41")
    with col2:
        st.metric("Target MAPE :" , "<=12%")
    with col3:
        st.metric("Forecaste Days :", "30")
    
    st.markdown("---")

    #Load forecaste data future:-

    forecast_df = pd.read_csv("Future_sales_forecast.csv")
    forecast_df['ds'] = pd.to_datetime(forecast_df['ds'])

    #30 days Forecast Chart 
    st.header("📊 30 Days Sales Forecast")
    fig , ax = plt.subplots(figsize = (12,5))
    ax.plot(forecast_df['ds'] , forecast_df['yhat'],color = 'blue' , marker = 'o',markersize = 3 ,label = 'Predicted sales')
    ax.fill_between(forecast_df['ds'] , forecast_df['yhat'],forecast_df['yhat_lower'] , forecast_df['yhat_upper'],alpha=0.3,color='blue',label = 'Uncertanity Range')

    ax.set_title("30 days Sales Forecast")
    ax.set_xlabel("Date")
    ax.set_ylabel("Sales (₹)")
    ax.legend()
    plt.xticks(rotation =45)
    plt.tight_layout()
    st.pyplot(fig)

    st.markdown("---")

    #Forecaste table

    st.header("📋 Forecast Data")
    forecast_df['yhat'] = forecast_df['yhat'].round(2)
    st.dataframe(forecast_df[['ds' , 'yhat' , 'yhat_lower','yhat_upper']])

    st.download_button(label = "📥 Download Forecast CSV",data = forecast_df.to_csv(index=False), file_name = 'Sales_forecast.csv',mime='text/csv')


# ----------inventory optimization page---------


elif page == "📦 Inventory Optimization":
    st.title("📦 Inventory Optimization")
    st.markdown("----")

    #metrics
    col1,col2,col3 = st.columns(3)
    with col1:
        st.metric("Reorder Point:","₹4,021")
    with col2:
        st.metric("Safety Stock:","₹862")
    with col3:
        st.metric("Reorder Quantity:", "₹18,092")

    st.markdown("---")

    #Stock Reduction
    st.header("📊 Stock Reduction Achievement")
    col1,col2 = st.columns(2)
    with col1:
        st.metric("Overstock Reduction", "35%", "-35%")
    with col2:
        st.metric("Understock Reduction", "35%", "-35%")
    
    st.markdown('---')

    #bar chart 
    st.header("📈 Before vs After Optimization")

    fig,ax = plt.subplots(figsize = (10,5))

    categories = ['Overstock','Understock']
    before = [3581,832]
    after = [2327,541]
    x = range(len(categories))
    ax.bar([p - 0.2 for p in x], before , width = 0.4,color='red',label = 'Before')
    ax.bar([p + 0.2 for p in x], after , width = 0.4,color='orange',label = 'After(35% Reduced)')

    ax.set_title("Overstock and Understock Reduction")
    ax.set_xticks(x)
    ax.set_xticklabels(categories)
    ax.set_ylabel('Value (₹)')
    ax.legend()
    ax.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    st.pyplot(fig)

    st.markdown("---")

    #Alert system 
    st.header("🚨 Reorder Alert System")
    
    current_stock = st.number_input(
        "Current Stock Value (₹)", 
        value=5000
    )
    
    if current_stock <= 4021:
        st.error(f"🚨 ALERT: Stock Low! Place order of ₹18,092 as soon as possible!")
    elif current_stock <= 5000:
        st.warning(f"⚠️ Do monitor! Stock is decresing")
    else:
        st.success(f"✅ Stock Sufficient!")