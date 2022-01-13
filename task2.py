def extract_reading(x): # Function to extract only reading(or numbers) from the data
    return float(x[1:])

def convert_km_to_miles(x): # Function to convert km to miles
    return x/1.60934

print("Speed Analysis 1.0")
reading_kph_in_list = [] # List to store the readings

while True:
    reading = input("Enter the reading : ")

    if reading == "": # checking if the input is empty
        break

    if reading[0].upper() not in ["E", "U"] or  any(char.isalpha() for char in reading[1:]): # Validating the Format of the reading
        print("Invalid Format!")
        continue
    print("Reading is saved")

    if reading[0].upper() == "E":
        reading_kph_in_list.append(extract_reading(reading))

    else :
        reading_kph_in_list.append(extract_reading(reading)*1.60934) # Converting mph to kph reading and storing

if reading_kph_in_list == []:
    print("No Readings Found. Nothing to do.")
else:
    print("Results Summary\n")
    print(f"{len(reading_kph_in_list)} readings analyzed.")

    max_speed_in_km = max(reading_kph_in_list)
    max_speed_in_miles = convert_km_to_miles(max_speed_in_km)

    min_speed_in_km = min(reading_kph_in_list)
    min_speed_in_miles = convert_km_to_miles(min_speed_in_km)

    avg_speed_in_km = sum(reading_kph_in_list)/len(reading_kph_in_list)
    avg_speed_in_miles = convert_km_to_miles(avg_speed_in_km)

    print("Max speed: %.1f MPH %.1f KPH."%(max_speed_in_km,max_speed_in_miles))
    print("Min speed: %.1f MPH %.1f KPH."%(min_speed_in_km,min_speed_in_miles))
    print("Avg speed: %.1f MPH %.1f KPH."%(avg_speed_in_km,avg_speed_in_miles))






