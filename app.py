import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load pickled objects
with open('label_encoders.pkl', 'rb') as file:
    encoder = pickle.load(file)

with open('scaler1.pkl', 'rb') as file:
    scaler = pickle.load(file)

with open('carprice.pkl', 'rb') as file:
    model = pickle.load(file)

# Set page configuration
st.set_page_config(
    page_title="Car Price Prediction",
    page_icon=r"img/carlogo.png"
)

# Apply CSS styling
st.markdown("""
<style>
h1 {
    color: red; /* Change to your desired color */
}
</style>
""", unsafe_allow_html=True)

def main():
    option = st.sidebar.radio("Options", ["Home", "App Page"])
    if option == "Home":
        st.title("About Car Dekho")
        st.write("""
        CarDekho.com is India's leading car search venture that helps users buy cars that are right for them. 
        Its website and app carry rich automotive content such as expert reviews, detailed specs and prices, 
        comparisons as well as videos and pictures of all car brands and models available in India. 
        The company has tie-ups with many auto manufacturers, more than 4000 car dealers, and numerous financial institutions to 
        facilitate the purchase of vehicles.
        """)
        # st.image(r"C:\Users\shank\Desktop\car_dheko\CarDekho-FY22-social.jpg")
        st.write("""
        CarDekho.com has launched many innovative features to ensure that users get an immersive experience of the car 
                 model before visiting a dealer showroom. These include a Feel The Car tool that gives 360-degree interior/exterior 
                 views with sounds of the car and explanations of features with videos; search and comparison by make, model, price, 
                 features; and live offers and promotions in all cities. The platform also has used car classifieds wherein users can 
                 upload their cars for sale, and find used cars for buying from individuals and used car dealers.
        """)
    
    else:
        st.title("Car Dekho Price Prediction")
        
        
        bt = st.selectbox("Body Type",["Select bodytype"]+['Hatchback' ,'SUV', 'Sedan', 'MUV',  'Minivans', 'Wagon'])
        km =st.slider("Kilo Meter", min_value=700, max_value=150000)
        trans = st.selectbox("Transmission",["Select Transmission"]+['Manual','Automatic'])
        owners = st.selectbox("No of Owners",["Select no.of.owner"]+[0,1,2,3,4,5])
        brand = st.selectbox("Brand",["Select Brand"]+['Maruti', 'Ford', 'Tata', 'Hyundai', 'Datsun', 'Honda' ,'Renault', 'Volkswagen',
                                            'Mahindra', 'Skoda', 'MG', 'Kia', 'Toyota', 'Nissan' ,'Fiat', 'Chevrolet',
                                                        'Citroen' ,'Mini', 'Hindustan Motors'])

        model_year =st.slider("Model Year", min_value=1985, max_value=2023)
        # insurance = st.selectbox("Insurance Validity",["Select Insurance Validity"]+['Third Party', 'Comprehensive', 'Zero Dep', 'Not Available'])
        fueltype = st.selectbox("Fuel Type",["Select Fuel Type"]+['Petrol', 'Diesel', 'LPG', 'CNG'])
        mileage = st.slider("Mileage", min_value=10.0, max_value=28.0)
        engine =st.slider("Engine CC", min_value=700, max_value=2000)
        seat = st.slider("No of Seats", min_value = 4, max_value = 8)
        # color = st.selectbox("Color",["Select Color"]+['white', 'red', 'others', 'gray', 'maroon', 'orange', 'silver', 'blue', 'brown',
        #                                                 'yellow', 'black', 'gold', 'green', 'purple'])
        # gears = st.selectbox("Gear Box",["Select Gears"]+[5, 7, 4, 6, 0, 8])
        steering_type = st.selectbox("Steering Type",["Select Steering type"]+['EPAS', 'Electronic', 'Manual', 'Power']) 
        front_brake = st.selectbox("Front Brake",["Select Front Brake type"]+['Disc', 'others']) 
        rear_brake = st.selectbox("Rear Brake",["Select Rear brake type"]+['Disc', 'Drum']) 
        tyre_type = st.selectbox("Tyre Type",["Select Tyre type"]+['Radial', 'Tubeless']) 

        city = st.selectbox("City",["Select City"]+['Bangalore', 'Chennai', 'Delhi', 'Hyderabad', 'Jaipur', 'Kolkata'])

        details1 = []
        
        
        if bt != "Select bodytype":
            encoded_value = encoder["bt"].transform([bt])[0]
            details1.append(int(encoded_value))
        else:
            st.warning("Please choose correct any option in body type box")
        if km:
            details1.append(km)

        if trans != "Select Transmission":
            encoded_value = encoder["transmission"].transform([trans])[0]
            details1.append(int(encoded_value))
        else:
            st.warning("Please choose correct any option in transmission box")
        
        if owners != "Select no.of.owner":
            details1.append(owners)
        else:
            st.warning("Please choose correct any option in owners box")
            
        
        if brand != "Select Brand":
            encoded_value = encoder["oem"].transform([brand])[0]
            details1.append(int(encoded_value))
        else:
            st.warning("Please choose correct any option in brand box")

        if model_year:
            details1.append(float(model_year))
      
        # if insurance != "Select Insurance Validity":
        #     encoded_value = encoder["Insurance Validity"].transform([insurance])[0]
        #     details1.append(int(encoded_value))
        # else:
        #     st.warning("Please choose correct any option in insurance box")

        if fueltype != "Select Fuel Type":
            encoded_value = encoder["Fuel Type"].transform([fueltype])[0]
            details1.append(int(encoded_value))
        else:
            st.warning("Please choose correct any option in fueltype")
        
        if mileage:
            details1.append(mileage)

        if engine:
            details1.append(engine)

        # Add mean values
        max_power_mean = 83.284
        details1.append(max_power_mean)

        torque_mean = 127.384
        details1.append(torque_mean)

        # if color != "Select Color":
        #     encoded_value = encoder["Color"].transform([color])[0]
        #     details1.append(int(encoded_value))
        # else:
        #     st.warning("Please choose correct any option in color box")

        if seat:
            details1.append(seat)
        
        Length_mean = 3880.395
        details1.append(Length_mean)

        Width_mean = 1690.101
        details1.append(Width_mean)

        Height_mean = 1542.333
        details1.append(Height_mean)

        wheelbase_mean = 2465.064
        details1.append(wheelbase_mean)

        if steering_type != "Select Steering type":
            # city = city.lower()
            encoded_value = encoder["Steering Type"].transform([steering_type])[0]
            details1.append(int(encoded_value))
            print(encoded_value)
        else:
            st.warning("Please choose correct any option in city box")

        if front_brake != "Select Front Brake type":
            # city = city.lower()
            encoded_value = encoder["Front Brake Type"].transform([front_brake])[0]
            details1.append(int(encoded_value))
            print(encoded_value)
        else:
            st.warning("Please choose correct any option in city box")

        if rear_brake != "Select Rear Brake type":
            # city = city.lower()
            encoded_value = encoder["Rear Brake Type"].transform([rear_brake])[0]
            details1.append(int(encoded_value))
            print(encoded_value)
        else:
            st.warning("Please choose correct any option in city box")

        if tyre_type != "Select Tyre type":
            # city = city.lower()
            encoded_value = encoder["Tyre Type"].transform([tyre_type])[0]
            details1.append(int(encoded_value))
            print(encoded_value)
        else:
            st.warning("Please choose correct any option in city box")
        

        # if gears != "Select Gears":
        #     details1.append(gears)
        # else:
        #     st.warning("Please choose correct any option in gears box")
        if city != "Select City":
            # city = city.lower()
            encoded_value = encoder["City"].transform([city])[0]
            details1.append(int(encoded_value))
            print(encoded_value)
        else:
            st.warning("Please choose correct any option in city box")
        # Convert to DataFrame and scale
        details = [details1]
        if len(details1) == 18:
            values_scaled = scaler.transform(details)
        
        #st.write(f"Scaled Input Data: {values_scaled}")
    

        if st.button("Estimate Price"):
            car_price_pred = model.predict(values_scaled)
            st.success(f"Estimated Price: ₹{round(car_price_pred[0], 2)}")
    
        

if __name__ == "__main__":
    main()
