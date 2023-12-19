import streamlit as st
from src.pipeline.predict_pipeline import CustomData, PredictionPipeline

def home_page():
    st.title('Diamond Price Predictor')
    st.write('Welcome to the Diamond Price Predictor. Please fill in the details below to get the predicted price.')

    carat = st.number_input('Carat', min_value=0.0, step=0.1)
    depth = st.number_input('Depth', min_value=0.0, step=0.1)
    table = st.number_input('Table', min_value=0.0, step=0.1)
    x = st.number_input('x', min_value=0.0, step=0.1)
    y = st.number_input('y', min_value=0.0, step=0.1)
    z = st.number_input('z', min_value=0.0, step=0.1)
    cut = st.selectbox('Cut', ['Ideal', 'Premium', 'Very Good', 'Good', 'Fair'])
    color = st.selectbox('Color', ['D', 'E', 'F', 'G', 'H', 'I', 'J'])
    clarity = st.selectbox('Clarity', ['IF', 'VVS1', 'VVS2', 'VS1', 'VS2', 'SI1', 'SI2', 'I1'])

    if st.button('Predict'):
        data = CustomData(
            carat=carat,
            depth=depth,
            table=table,
            x=x,
            y=y,
            z=z,
            cut=cut,
            color=color,
            clarity=clarity
        )
        final_new_data = data.get_data_as_dataframe()
        predict_pipeline = PredictionPipeline()
        pred = predict_pipeline.predict(final_new_data)

        results = round(pred[0], 2)
        st.write(f"The predicted price is: ${results}")

def main():
    st.set_page_config(page_title='Diamond Price Predictor')
    home_page()

if __name__ == "__main__":
    main()
