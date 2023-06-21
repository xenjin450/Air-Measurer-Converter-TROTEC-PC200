
# Define the conversion functions
def micromolar_to_ppm(micromolar, temperature, pressure):
    # Convert micromolar to ppm
    ppm = micromolar * 24.45 * (temperature + 273.15) / (pressure * 100)
    return ppm

def ppm_to_ugm3(ppm, molecular_weight, temperature, pressure):
    # Convert ppm to ug/m3
    density = (molecular_weight * 1e-3) / 24.45
    ugm3 = ppm * density * (pressure * 100) / (8.314 * (temperature + 273.15))
    return ugm3

def ppm_to_mgm3(ppm, molecular_weight, temperature, pressure):
    # Convert ppm to mg/m3
    mgm3 = ppm_to_ugm3(ppm, molecular_weight, temperature, pressure) / 1000
    return mgm3

# Define the input parameters
temperature = float(input("Temperature AT: "))
dp = float(input("Dew Point DP: "))
rh = float(input("Relative Humidity RH: "))
wb = float(input("Wet Bulb Temperature WB: "))
micromolar_2_5 = float(input("Enter 2.5um micromolar with Decimal Point (Ex 2.31): "))

# Calculate the pressure using the Magnus formula
pressure = 6.112 * 10 ** ((7.5 * temperature) / (237.7 + temperature)) * (rh/100)

# Calculate the Dew Point and convert to ug/m3 and mg/m3
dp_ppm = micromolar_to_ppm(dp, temperature, pressure)
ugm3_dp = ppm_to_ugm3(dp_ppm, 18.01528, temperature, pressure)
mgm3_dp = ppm_to_mgm3(dp_ppm, 18.01528, temperature, pressure)

# Calculate the Wet Bulb Temperature and convert to ug/m3 and mg/m3
wb_ppm = micromolar_to_ppm(wb, temperature, pressure)
ugm3_wb = ppm_to_ugm3(wb_ppm, 18.01528, temperature, pressure)
mgm3_wb = ppm_to_mgm3(wb_ppm, 18.01528, temperature, pressure)

# Calculate the conversions to PPM
ppm_2_5 = micromolar_to_ppm(micromolar_2_5, temperature, pressure)

# Define molecular weights for common pollutants
molecular_weight_PM25 = 12.011 + 2 * 15.999 + 2 * 14.007


# Convert PPM to ug/m3 and mg/m3
ugm3_2_5 = ppm_to_ugm3(ppm_2_5, molecular_weight_PM25, temperature, pressure)
mgm3_2_5 = ppm_to_mgm3(ppm_2_5, molecular_weight_PM25, temperature, pressure)



def get_pollutant_level(aqi):
    if aqi >= 0 and aqi <= 50:
        return "Green"
    elif aqi > 50 and aqi <= 100:
        return "Moderate"
    elif aqi > 100 and aqi <= 150:
        return "Unhealthy for Sensitive Groups"
    elif aqi > 150 and aqi <= 200:
        return "Unhealthy"
    elif aqi > 200 and aqi <= 300:
        return "Very Unhealthy"
    elif aqi > 300 and aqi <= 500:
        return "Hazardous"
    else:
        return "Deadly"





def ugm3_to_aqi(ugm3):
    if ugm3 >= 0 and ugm3 <= 12:
        aqi = ((50-0)/(12-0)) * (ugm3-0) + 0
    elif ugm3 > 12 and ugm3 <= 35.4:
        aqi = ((100-51)/(35.4-12.1)) * (ugm3-12.1) + 51
    elif ugm3 > 35.4 and ugm3 <= 55.4:
        aqi = ((150-101)/(55.4-35.5)) * (ugm3-35.5) + 101
    elif ugm3 > 55.4 and ugm3 <= 150.4:
        aqi = ((200-151)/(150.4-55.5)) * (ugm3-55.5) + 151
    elif ugm3 > 150.4 and ugm3 <= 250.4:
        aqi = ((300-201)/(250.4-150.5)) * (ugm3-150.5) + 201
    elif ugm3 > 250.4 and ugm3 <= 350.4:
        aqi = ((400-301)/(350.4-250.5)) * (ugm3-250.5) + 301
    elif ugm3 > 350.4 and ugm3 <= 500.4:
        aqi = ((500-401)/(500.4-350.5)) * (ugm3-350.5) + 401
    else:
        aqi = "Out of range"
    return aqi

aqi_2_5 = ugm3_to_aqi(ugm3_2_5)

level_2_5 = get_pollutant_level(aqi_2_5)



# Output the WHO measurements
print("2.5um micromolar in PPM: {:.2f}".format(ppm_2_5))
print("2.5um PPM in ug/m3: {:.3f}".format(ugm3_2_5))
print("2.5um PPM in mg/m3: {:.6f}".format(mgm3_2_5))
print("2.5um AQI WHO: {:.3f}".format(aqi_2_5))



input()
