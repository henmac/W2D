import streamlit as st
import requests
from datetime import datetime, timedelta
from PIL import Image
from io import BytesIO

# Set the page layout
st.set_page_config(layout="wide", page_icon="🌤️", initial_sidebar_state="expanded")

# Define OpenWeatherMap API key and base URL
API_KEY = '7ebbdce7109e2488d0d3484091b681ef'
BASE_URL = 'http://api.openweathermap.org/data/2.5/forecast?'  # Forecast API for 3-hour intervals

# Function to get 3-hour interval weather forecast
def get_weather_forecast(city_name):
    complete_url = f"{BASE_URL}appid={API_KEY}&q={city_name}&units=metric"
    response = requests.get(complete_url)
    return response.json()

# Function to suggest clothing based on temperature and weather conditions
def clothing_suggestion(temp, weather_id):
    if temp < 0:
        suggestion = "Heavy jacket, gloves, scarf, and boots."
        image_urls = [
            "https://i.pinimg.com/564x/a2/a3/9c/a2a39c4c3be03220a5969f256fd6de8a.jpg",
            "https://product-images-cdn.liketoknow.it/.OkI6RB0lCjJNkJqbENuCDcKmBeBk5mmjwg61KTyBU7FMB9JJzA0SoJWM4howbmkOrLEvXj3NgxUlyDNmwH8vDXlhbkbhpN6CGZXMc2NYYdicF6Svp9ZAuPjlCGa0m8F_M6gVcA2cupvPTUUcbiY1kaT4w_Akw7Vkk6ddI.vARta.7cbNk9Xq5mgjsM-"
        ]
        message = "Brr! It's freezing outside. Stay warm!"
        
    elif 0 <= temp < 10:
        suggestion = "Warm coat, sweater, and insulated shoes."
        image_urls = [
            "https://product-images-cdn.liketoknow.it/GC9iCtdnc.y5rv1THsU4x1dStyCfud7nU1WfU1euy3eo24hx_kLVZOWsk6IVydfQxcdC4H8E2_Qwfn_JOOSu0AUwNxhkw5L3tPSeSeqlcfW9Q63tj1HfS.tCIfnJF1Mb3huWhL4Dsbm3eXlfOcZ.kp5P2YbmlPvLEbQlGScjvYW4pOLLso.JMrmNYp0-?v=0&auto=format&fm=webp&w=450&q=80&dpr=2",
            "https://product-images-cdn.liketoknow.it/fvMX246S7EvuH8F.jo.DN6WxaWAKff1xL49d7XZ8bMhJJk4K3KsrIZ709hUF3J8vrIh4.COV4uMrKf1.cRDeqo3pGDvzGMah17plrEuHuuI26p6u5Z1dfXgVHteJcdna1RkKA6LhwbMy5Whs_eivA54KCJi5eFCu1kHNd4Ia.ZPtd2RnGLIp6bf_J3Q-"
        ]
        message = "A bit chilly! Grab a warm coat."

    elif 10 <= temp < 20:
        suggestion = "Light jacket, long sleeves, and jeans."
        image_urls = [
            "https://product-images-cdn.liketoknow.it/Ij.L2RgQ1yGkX9gL2v5wGXOSyyzw20Tfb6NFr6jLdmdofpXoTysqq7cXYCuz6zQIDBMImYjSNafumHSu29cpa7xsjwsJ27wSHSTj0W7GjbZjXWyba3LQrEoyWkRhV3vk_7_xrPceqki3osW3peLhAUBZFOQOjP76lg1HspBQ7n9S5n1z023Qx5D_h3Q-?v=0&auto=format&fm=webp&w=450&q=80&dpr=2",
            "https://product-images-cdn.liketoknow.it/tZybnLgSh93JrPHPoRrG_rEhE7ec11gtCOv0kZ0.89NcTqItc_7rPZ6nTmUso4GXEf2k2F.8VbDmh3Qe.1shbXb_d7amiOSr25.6RMDjeX3T1gOZ1UkJviLOkcfePoCh6P7RC5QCq1YwfpVcy.bO18A9THnaUcuFQEOmNZvaOn_z4kUTryLnv3GO0Ec-"
        ]
        message = "Cool weather! A jacket should do."

    elif 20 <= temp < 25:
        suggestion = "T-shirt, shorts, or light pants."
        image_urls = [
            "https://product-images-cdn.liketoknow.it/CidDfV7bKWudI0zJMLHSPMrG4jAkShNYnZF2g6TSwToft7oW03ID_nNApqAncjyjGHuZB.h9PZJKXyh.60q8SkxzemwM9YR9eVzGNtqW3vwaGhvKVGKiqvzlX9VeTOAlq2Pb7vPt7ZYWHu0jqyCDrYEmPsU0QNb0kXYbrYhhdaGZn6TfoFnzciFb5ng-?v=0&auto=format&fm=webp&w=450&q=80&dpr=2",
            "https://product-images-cdn.liketoknow.it/PiRrCG8qkb78QVbCosrdUdMd7ZnmV74g5J4DjK0TbeSEaNITcgxxnTKRBO3JzpBiLlzmmZ7rCk7rx9Ik4IACjj_lBVv7nymIkDFHBwSgBhOcnnl30GAQW2QRZ7vt9KMTge8pWomAkSSsBwGqX18kypQZMlVM1EuXk6LPKRYU.WrYGh2JPkJHqtkFeOc-"
        ]
        message = "Nice weather! Dress comfortably."

    else:
        suggestion = "Tank top, shorts, and sunglasses."
        image_urls = [
            "https://product-images-cdn.liketoknow.it/dpq_l0m7gShgT.CE9o0fDO73zBG_LX8kyl9thI5PtENnCyDGqipHHAs6hWDMC2v6iFPF2gP6sIpK8KZfRXPb7pYnuZ1tZV46xN_sKImkib43EEQUOoqoJDEYNsIVIe0TuEMDa1F_igsYID77CcR9OSTIOBMuKazHyTXQwXo_kbYLZ2vPPtwMI8MOcLc-?v=0&auto=format&fm=webp&w=450&q=80&dpr=2",
            "https://product-images-cdn.liketoknow.it/RGSkHDH1_jNMlZgc3rygrkt5u4Hp770jnRz0ELDzvsSDAP45yyLG1FciBNB.5Za6MhMuByuAS9u6WcMB9IqWq3jDy.rCe2WwINP9EMWFLyVYpKREntE41JYJhLDPHI.b3ctEsTPJUcDUPAL.vV32XSJNJErlYPK8zTiE652z9UHwrOobHr5Qqc0A7LQ-"
        ]
     
        message = "It's hot! Stay cool and hydrated."

 # Modify suggestion based on weather condition using 'id'
    if 200 <= weather_id < 600:  # Rain or storm
        suggestion += " Consider waterproof clothes and an umbrella."
        image_urls = [
            "https://product-images-cdn.liketoknow.it/HgAAsHJ8.rnSwVWyugGqHrobtD7lMNL4nuoFoLrnEDIQOOfwhVfaO1wRfdJNxk8vurgqFYCHjiZo.vBL3Lil7YYVE1Mn7QAGy9n_IFg8j7Mcsuhn5VcIbryeNy50LLOM1J7r04CUg8fxhxpcuwPBWPmo91cjO7MUruW0_6MI_GgSAVq3wtMFPhUEpvA-?v=0&auto=format&fm=webp&w=450&q=80&dpr=2",
            "https://product-images-cdn.liketoknow.it/tZybnLgSh93JrPHPoRrG_rEhE7ec11gtCOv0kZ0.89NcTqItc_7rPZ6nTmUso4GXEf2k2F.8VbDmh3Qe.1shbXb_d7amiOSr25.6RMDjeX3T1gOZ1UkJviLOkcfePoCh6P7RC5QCq1YwfpVcy.bO18A9THnaUcuFQEOmNZvaOn_z4kUTryLnv3GO0Ec-?v=0&auto=format&fm=webp&w=450&q=80&dpr=2"
        ]
        message = "Rainy or stormy conditions! Don't forget your umbrella!"
       
    elif 600 <= weather_id < 700:  # Snow conditions
        suggestion += " Dress warmly with waterproof boots."
        image_urls = [
            "https://product-images-cdn.liketoknow.it/TcOF2FOhK2qUIikOSYmPRIu5.NIyN4V_8CyTL37.wch0GzJYgsOBpNuJQuSuEPyg0jEYn7i.Yhz2KmMGmp.fsN18BFzbaYhFdUeBpAT7FJmCBLhl9p72GTvWBGssM61s7_ducgaKcaj0F5NJryVa07RC7aHOilq4mwFDr8.puP63StSXefS_qGQnk1c-?v=0&auto=format&fm=webp&w=450&q=80&dpr=2",
            "https://product-images-cdn.liketoknow.it/tZybnLgSh93JrPHPoRrG_rEhE7ec11gtCOv0kZ0.89NcTqItc_7rPZ6nTmUso4GXEf2k2F.8VbDmh3Qe.1shbXb_d7amiOSr25.6RMDjeX3T1gOZ1UkJviLOkcfePoCh6P7RC5QCq1YwfpVcy.bO18A9THnaUcuFQEOmNZvaOn_z4kUTryLnv3GO0Ec-?v=0&auto=format&fm=webp&w=450&q=80&dpr=2"
        ]
        message = "It's snowing! Stay cozy and warm."

    elif 700 <= weather_id < 800:  # Fog or mist
        suggestion += " Wear something visible in low light."
        image_urls = [
            "https://product-images-cdn.liketoknow.it/OTpZKa.TuUpASY_5levGNYZF4EshzJusNDGwZ45BDJlAdj_1rtnmntLMHyuXRfP6DTr0fx3RHdsIHdv.5YlkLGyVZ_7fbLrayMod55bbu8Yjii04unqeurPV5t6oko4mchDJlUmKKR3yLX6fX6.BsvFWTTjwSHzDEwm7uxSzhD9u1cMuIQJjGdsPxRg-?v=0&auto=format&fm=webp&w=450&q=80&dpr=2",
            "https://product-images-cdn.liketoknow.it/PCGO6tUMHm5vytpjZoIcJwEs4EjmyvwW4sM6fABTs8JUyzR_FLmvtlngPFcdCDRT6Yi2H3KCejASOuBPYV7IQFcvSo5JWBLDd6B7tFWEiEoAkcRthPADbUasIWo3UhyQYKLwfw7jkjlioQBjBiItBZ27kci6DNe.xvKDW8LunJtA5aeMn8ruC55o.Bc-?v=0&auto=format&fm=webp&w=450&q=80&dpr=2"
        ]
        message = "It's foggy out there. Stay visible!"
    elif 800 < weather_id < 900:  # Cloudy, windy, or stormy
        suggestion += " Windbreaker or extra layers might help."
        image_urls = [
            "https://product-images-cdn.liketoknow.it/uF8E0IP_9dv.CMkE8xMqOp7d2SAjE0R_ulv4w6CHnDzCORGA.58mB_6fG3gyvVy.mTuejwZ_Y18df03PcokbYlblRG22YQw6zVQBsoF0f7zBAj1bfXN.7LTV6N56zoop5hClYJn.YSivU7.OWR_LCJ8sx1JJmV8EA86wmpghtb54b7hK7aTUtRmxIek-?v=0&auto=format&fm=webp&w=450&q=80&dpr=2",
            "https://product-images-cdn.liketoknow.it/pDTI6uUt9mF0fZT8TnGY69gTfw9Xi.ijOVwdKBuKcyFLOLeP1_xacCW6Zn_oRcHXhvj3FacAkm1eHRQwvl.7tebZENG_DGW6EqnfujPaJfcRmzXBGBznp1utK4DQQgHCm.0Ae4tKJAFo7JPUYdV.p2G3iV8IUvGeZ6.riG8SOfa_SBEZeYzkOB0PUJw-?v=0&auto=format&fm=webp&w=450&q=80&dpr=2"
        ]
        message = "Windy or cloudy weather ahead! Stay comfortable."
    return suggestion, message, image_urls


# Function to display weather GIFs in 3-hour intervals
def display_weather_gifs(weather_ids, timestamps):
    gif_mapping = {
        'clear': "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExdHl0czZ5aWJnbjFyN3YzanlkZmdmNXhtZGo5eDZha2swazJ6bDNmdCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/dW7we0bxfxssgKBjSD/giphy.gif",
        'rainy': "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExMnBwdzUxNG1lNjBhMDZxcHU0cWlzazhnZnVnZHI1ZHdpcTI2am15dSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Lsjt3tlPdUPppC1Q7n/giphy.gif",
        'snow': "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExbG5tanp2NG5uZ3NpdGRoN3diYm9vdXg4aGsxaXZ1ZGp3c2xsdjdnbCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/cgcysfCtVOdrqlUQoC/giphy.gif",
        'cloudy': "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNXdidmNwazVudDRyanNvNnhhdW80eTBoMTNnemkzZXduZGNmbzlnciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ibrhK7rIpilOkj4XUO/giphy.gif",
        'frosty': "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExMzA3aTJyejU0NWhiM3Nkcmk5aXFyanZhdHlza2p3bWNkNnNrbGw3diZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/24it69lSNV5ulAJMIh/giphy.gif",
        'stormy': "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExcmszYXAxc2syNGJ5Y2ZkZTd0aGRjaDhlZ2pleXA1b3ZodnkyZXpvYyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/tw3RWcuHEGX6GUaYGq/giphy.gif",
        'drizzle': "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExczV3NnU0ajh1OGt6ODl2bWRxc2J3N2RneTJiYmRyYzZ6MWpwdWxpOCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/aNVaFcPU2Sex69LWWa/giphy.gif"
    }

    def get_gif_by_weather_id(weather_id):
        if weather_id == 800:  # Clear sky
            return gif_mapping['clear']
        elif 200 <= weather_id < 300:  # stormy
            return gif_mapping['stormy']
        elif 300 <= weather_id < 500:  # drizzle
            return gif_mapping['drizzle']
        elif 500 <= weather_id < 600:  # rainy
            return gif_mapping['rainy']
        elif 600 <= weather_id < 700:  # Snow
            return gif_mapping['snow']
        elif 700 <= weather_id < 800:  # Frosty
            return gif_mapping['frosty']
        elif 800 < weather_id < 900:  # Cloudy
            return gif_mapping['cloudy']
   
    for i, weather_id in enumerate(weather_ids):
        gif_url = get_gif_by_weather_id(weather_id)
        if st.button(timestamps[i], key=f"time_{i}"):
            st.session_state.selected_time_index = i
        st.image(gif_url, width=240)

# Function to display clothing suggestions based on a specific timestamp
def display_clothing_suggestion(index, forecast_data, city_name):
    temp = round(convert_temperature(forecast_data['list'][index]['main']['temp'], unit))
    weather_id = forecast_data['list'][index]['weather'][0]['id']
    weather_condition = forecast_data['list'][index]['weather'][0]['description'].capitalize()

    suggestion, message, image_urls = clothing_suggestion(temp, weather_id)

    st.write(f"<h1 style='color:#0784b5; font-size:40px;'>{message}</h1>", unsafe_allow_html=True)
    st.write(f"<h3>Suggested clothing: {suggestion}</h3>", unsafe_allow_html=True)
    # Display clothing images
    if image_urls and len(image_urls) > 0:  # Ensure image_urls is not None or empty
        cols = st.columns(len(image_urls))
        # Instead of using nested columns, display images sequentially
        for i, image_url in enumerate(image_urls):
            with cols[i]:
                response = requests.get(image_url)
                img = Image.open(BytesIO(response.content))
                img = img.resize((400, 608))  # Set fixed width and height
                 #Display the resized image
                st.image(img, caption=f"Clothing item {i+1}")
          
    # Display weather info
    if unit =="Celsius":
        st.write(f"<h3>Temperature: {temp}°C</h3>", unsafe_allow_html=True)
    else:
        st.write(f"<h3>Temperature: {temp}°F</h3>", unsafe_allow_html=True)
    st.write(f"<h4 style='color:gray;'>Weather conditions: {weather_condition}</h4>", unsafe_allow_html=True)

# Sidebar for the title
st.sidebar.title("Weather2Day")

# Use st.form to capture city input and enter event
with st.sidebar.form(key='city_form'):
    city_name = st.text_input('Ready to head out? Tell me where you\'re going, and I\'ll hook you up with weather-proof advice!', '')
    submit_button = st.form_submit_button(label='Get Weather and Outfits')
   
    # Function to convert temperature
def convert_temperature(temp, unit):
    if unit == "Fahrenheit":
        return temp * 9/5 + 32
    return temp

#Sidebar displaying the farenheit and celcius
with st.sidebar:
    unit = st.radio("Select Temperature Unit", ("Celsius", "Fahrenheit"))
    
# Fetch weather data only when the form is submitted
if submit_button:
    forecast_data = get_weather_forecast(city_name)
    
    # Check if the API returned successful data
    if forecast_data.get('cod') == '200':
        st.session_state.forecast_data = forecast_data
        st.session_state.city_name = city_name
        st.session_state.selected_time_index = 0  # Reset time index on new city selection
    else:
        st.write("<h3 style='color:#627e75;'>City not found. Please try again.</h3>", unsafe_allow_html=True)

# Ensure forecast data is available in the session state before continuing
if 'forecast_data' in st.session_state:
    forecast_data = st.session_state.forecast_data
    city_name = st.session_state.city_name

    # Prepare weather IDs and timestamps for display
    weather_ids = [forecast_data['list'][i]['weather'][0]['id'] for i in range(0, 24, 3)]  # 3-hour intervals
    current_time = datetime.now()
    timestamps = ["Now" if i == 0 else (current_time + timedelta(hours=3 * i)).strftime("%I:%M %p") for i in range(8)]

    # Initialize selected_time_index if it doesn't exist
    if 'selected_time_index' not in st.session_state:
        st.session_state.selected_time_index = 0

    # Create a layout with 2 columns: Left for clothes and right for weather GIFs
    col1, col2 = st.columns([3, 1])  # Main column 3x wider than the right GIF column


    # Display GIFs for future timestamps in the right column
    with col2:
        display_weather_gifs(weather_ids, timestamps)

    # Display clothing suggestions in the left column
    with col1:
        display_clothing_suggestion(st.session_state.selected_time_index, forecast_data, city_name)

else:
    st.write("<h3 style='color:#627e75;'>City not found. Please try again.</h3>", unsafe_allow_html=True)