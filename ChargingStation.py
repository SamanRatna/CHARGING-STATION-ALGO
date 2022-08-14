# ------------------------------------------ CONSIDERATIONS ------------------------------------------
# SoC changes at the rate of 1% per unit km
# ----------------------------------------------------------------------------------------------------

# Libraries
import collections
from tabnanny import check
from turtle import distance
from unittest import case, findTestCases
from numpy import number
import pandas as pd
import matplotlib.pyplot as plt
import operator
import math
import itertools
import csv

# Constant parameters
num_of_bikes = 100                      # Total number of Bikes
total_distance_in_one_trip = 200        # distance in kms
SoC_logging_distance = 1                # distance in kms
full_charge_value = 100
number_of_charging_stations = 4
distance_where_charging_starts = 50

x_axis_distance_in_a_trip = []
y_axis_number_of_unstranded_riders = []
filtered_list = []
discarded_list_count = 0
discarded_number_of_sets = 0

least_number_of_charging_stations = math.floor(total_distance_in_one_trip/80)
most_number_of_charging_stations = math.ceil(total_distance_in_one_trip/25)

print("least_number_of_charging_stations : ", least_number_of_charging_stations)
print("Most_number_of_charging_stations : ", most_number_of_charging_stations)

# Which Data will I be using from Spreadsheet?
dataColumn = "Random1"
# dataColumn = "random data 1"
# dataColumn = "5% change C"

# Number of times Bike travels from A to B and viceversa
total_number_of_trips = range(2)
present_SoC = 0
# Distance travelled by that instant in the present trip
distance_travelled = 0
counter = 0
result = {}

strandedRiderCount = 0
# total_strandedRiderCount = 0

leastSoC_before_getting_stranded = 5
checkpoint_charging_frequency = 0
checkpointOccupancy = {}
chargingSoC = {}
checkpointwise_Stranded_Count = {}

total_rider_count = 0

anxietyLevels = [1, 2, 3, 4, 5, 6, 7, 8, 9]
anxietyLevelFrequency = [0, 0, 0, 0, 0, 0, 0, 0, 0]

all_charging_SoC = []

AnxietyLevelCollection_setOfTwo = []
AnxietyLevelCollection_setOfThree = []

# SoC data input for the system
df = pd.read_excel(r'data_collection2.xlsx')
initial_values = []

print("Data Column Used:                            ", dataColumn)
for count in range(len(df[dataColumn])):
    initial_values.append(df[dataColumn][count])

# Output Variable define
points_of_recharge = []

# -------------------------------------------------------------------------------------

# PRINT POINTS OF RECHARGE WHEN 100 RIDERS RIDE FROM A->B AND THEN B->A

# -------------------------------------------------------------------------------------

# Begin Logic
for initial_SoC in initial_values:

    distance_travelled = 0

    for trip_number in total_number_of_trips:

        if(trip_number % 2 == 0):

            present_SoC = initial_SoC

            while (distance_travelled < total_distance_in_one_trip):

                if (present_SoC <= distance_where_charging_starts):

                    points_of_recharge.append(distance_travelled)

                    # Bike recharged to full when reached to 50%
                    present_SoC = full_charge_value
                
                else:

                    # Bike SoC decreases with increase in travel displacement by 1km
                    present_SoC -= 1

                # Increase distance travelled by 1km
                distance_travelled += 1

        elif (trip_number % 2 == 1):

            present_SoC = initial_SoC

            while (distance_travelled <= total_distance_in_one_trip and distance_travelled > 0):

                if (present_SoC <= distance_where_charging_starts):

                    points_of_recharge.append(distance_travelled)

                    # Bike recharged to full when reached to 50%
                    present_SoC = full_charge_value                           
                
                else:
                    
                    # Bike SoC decreases with increase in travel displacement by 1km
                    present_SoC -= 1

                # Increase distance travelled by 1km
                distance_travelled -= 1

# Arrange Dictionary keys in ascending order
def ascendingKeys(frequency_of_occurence):
    for i in sorted(frequency_of_occurence):
        result.update({
            i: frequency_of_occurence[i]
        })
 

ctr = collections.Counter(points_of_recharge)
frequency = dict(ctr)
ascendingKeys(frequency)

Distance_x_axis = list(result.keys())
Frequency_y_axis = list(result.values())

print("\n")
print("Points of Recharge")
print(Distance_x_axis)
print("Total number of Points of Recharge : ", len(Distance_x_axis))

# # -------------------------------------------------------------------------------------

# # GENERIC LOGIC

# # -------------------------------------------------------------------------------------
least_number_of_charging_stations = math.floor(total_distance_in_one_trip/80)
most_number_of_charging_stations = math.ceil(total_distance_in_one_trip/25)


all_possible_combinations = itertools.combinations(Distance_x_axis, number_of_charging_stations)
list_with_verified_distances = []
counter_exception = 0

for every_combination in all_possible_combinations:
    count += 1

    last_checkpoint = 0
    validity_counter = 0

    for station_position in range(number_of_charging_stations+1):

        if (station_position == number_of_charging_stations):

            # When accounting for distance between last charging station and total distance in a trip
            if ((total_distance_in_one_trip - every_combination[station_position - 1] >= 25) and (total_distance_in_one_trip - every_combination[station_position - 1] <= 50)):

                validity_counter += 1
                last_checkpoint = total_distance_in_one_trip
            
            else:
                last_checkpoint = 0
                break
            
        elif ((every_combination[station_position] - last_checkpoint >= 25) and (every_combination[station_position] - last_checkpoint <= 50)):

            validity_counter += 1
            last_checkpoint = every_combination[station_position]
        
        else:
            last_checkpoint = 0
            counter_exception += 1
            break

    if (validity_counter == number_of_charging_stations + 1):
        list_with_verified_distances.append(every_combination)



# -------------------------------------------------------------------------------------

# FILTER OUT STRANDED RIDERS FROM THE VERIFIED SET

# -------------------------------------------------------------------------------------

result_setofThree = {}
Anxiety_Avg_dict = {}
counter = 0
# list_with_verified_distances = [[25, 6, 114, 158]]
# 25	64	114	158
for _set_of_three in list_with_verified_distances:

    anxietyLevelFrequency = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    total_strandedRiderCount = 0
    ending_SoC_list = []
    total_number_of_charges = 0
    discard_set = 0
    checkpointBased_Charging_Number_Count = []

    for i in range(number_of_charging_stations):
        checkpointBased_Charging_Number_Count.append(0)

    checkpointBased_strandedRiderCount = []

    for i in range(number_of_charging_stations):
        checkpointBased_strandedRiderCount.append(0)

    chargingStationCheckpoints = _set_of_three

    counter = 0

    for initial_SoC in initial_values:

        distance_travelled = 0
        counter += 1

        for trip_number in total_number_of_trips:

            if(trip_number % 2 == 0):

                present_SoC = initial_SoC

                # When the rider hasn't reached the destination
                while (distance_travelled < total_distance_in_one_trip):

                    if (distance_travelled in chargingStationCheckpoints):

                        checkpointIndex = chargingStationCheckpoints.index(distance_travelled)

                        if (present_SoC > leastSoC_before_getting_stranded and present_SoC <= distance_where_charging_starts):
                            
                            for i in range(number_of_charging_stations):
                                if (checkpointIndex == i):
                                    checkpointBased_Charging_Number_Count[i] += 1

                            if (present_SoC > 45 and present_SoC <= 50):
                                anxietyLevelFrequency[0] += 1

                            elif (present_SoC > 40 and present_SoC <= 45):
                                anxietyLevelFrequency[1] += 1

                            elif (present_SoC > 35 and present_SoC <= 40):
                                anxietyLevelFrequency[2] += 1

                            elif (present_SoC > 30 and present_SoC <= 35):
                                anxietyLevelFrequency[3] += 1

                            elif (present_SoC > 25 and present_SoC <= 30):
                                anxietyLevelFrequency[4] += 1

                            elif (present_SoC > 20 and present_SoC <= 25):
                                anxietyLevelFrequency[5] += 1

                            elif (present_SoC > 15 and present_SoC <= 20):
                                anxietyLevelFrequency[6] += 1

                            elif (present_SoC > 10 and present_SoC <= 15):
                                anxietyLevelFrequency[7] += 1

                            elif (present_SoC > 5 and present_SoC <= 10):
                                anxietyLevelFrequency[8] += 1

                            present_SoC = full_charge_value

                        elif (present_SoC <= leastSoC_before_getting_stranded):                        

                            total_strandedRiderCount += 1

                            for i in range(number_of_charging_stations):

                                if (checkpointIndex == i):
                                    checkpointBased_strandedRiderCount[i] += 1

                            discard_set = 1
                            break
                    
                    distance_travelled += 1
                    present_SoC -= 1 

                if (discard_set == 1):
                    break
                ending_SoC_list.append(present_SoC)

            elif(trip_number % 2 == 1):

                present_SoC = initial_SoC
                distance_travelled = total_distance_in_one_trip

                # When the rider hasn't reached the destination
                while (distance_travelled <= total_distance_in_one_trip and distance_travelled > 0):

                    if (distance_travelled in chargingStationCheckpoints):

                        checkpointIndex = chargingStationCheckpoints.index(distance_travelled)

                        if (present_SoC > leastSoC_before_getting_stranded and present_SoC <= 50):

                            for i in range(number_of_charging_stations):
                                if (checkpointIndex == i):
                                    checkpointBased_Charging_Number_Count[i] += 1

                            if (present_SoC > 45 and present_SoC <= 50):
                                anxietyLevelFrequency[0] += 1

                            elif (present_SoC > 40 and present_SoC <= 45):
                                anxietyLevelFrequency[1] += 1

                            elif (present_SoC > 35 and present_SoC <= 40):
                                anxietyLevelFrequency[2] += 1

                            elif (present_SoC > 30 and present_SoC <= 35):
                                anxietyLevelFrequency[3] += 1

                            elif (present_SoC > 25 and present_SoC <= 30):
                                anxietyLevelFrequency[4] += 1

                            elif (present_SoC > 20 and present_SoC <= 25):
                                anxietyLevelFrequency[5] += 1

                            elif (present_SoC > 15 and present_SoC <= 20):
                                anxietyLevelFrequency[6] += 1

                            elif (present_SoC > 10 and present_SoC <= 15):
                                anxietyLevelFrequency[7] += 1

                            elif (present_SoC > 5 and present_SoC <= 10):
                                anxietyLevelFrequency[8] += 1

                            present_SoC = full_charge_value

                        elif (present_SoC <= leastSoC_before_getting_stranded):                        

                            total_strandedRiderCount += 1

                            for i in range(number_of_charging_stations):
                                if (checkpointIndex == i):
                                    checkpointBased_strandedRiderCount[i] += 1

                            break
                    
                    distance_travelled -= 1
                    present_SoC -= 1
                
                ending_SoC_list.append(present_SoC)


        if (discard_set == 1):
            break

    for i in range(number_of_charging_stations):
        total_number_of_charges = total_number_of_charges + checkpointBased_Charging_Number_Count[i]
    
    for i in range(number_of_charging_stations):
        if (checkpointBased_Charging_Number_Count[i] == 0):
            discarded_list_count += 1
           
    # if (total_strandedRiderCount == 0 and discarded_list_count == 0):
    if (discarded_list_count == 0):

        averageEndingSoC = sum(ending_SoC_list) / len(ending_SoC_list)

        i = 1
        summ = 0
        for _value in anxietyLevelFrequency:
            summ = summ + _value*i
            i += 1

            # Anxiety Average dictionary:
            Anxiety_Avg_dict.update({
                tuple(_set_of_three) : [(summ / total_number_of_charges), averageEndingSoC]
            })

print("List before filtration : ", len(list_with_verified_distances))
print("List after filtration : ", len(Anxiety_Avg_dict))
# print("List after filtration : ", (Anxiety_Avg_dict))
print("Discarded count : ", discarded_number_of_sets)


# # -------------------------------------------------------------------------------------

# # TOP 10 SETS OF THREE WITH LEAST AVERAGE ANXIETY LEVELS

# # -------------------------------------------------------------------------------------
print("anxietyLevelFrequency ", anxietyLevelFrequency)

data = Anxiety_Avg_dict

anxLevelList = []
sortedDict = {}
minKey = 0

for i in range(10):
    minAnxTemp = 200
    for key, val in data.items():
        # print(key,val)
        if val[0] < minAnxTemp:
            minAnxTemp = val[0]
            minKey = key
            minVal = val
    del data[(minKey)]
    minVal[0] = round(minVal[0], 2)
    minVal[1] = round(minVal[1], 2)
    sortedDict.update({minKey: minVal})

print("Sorted Top 10: ")
print(sortedDict)



overall_data = []

for value1, value2 in sortedDict.items():

    current_temp_list = []

    for i in range(len(value1)):
        print(value1[i])
        current_temp_list.append(value1[i])
    
    current_temp_list.append(value2[0])
    current_temp_list.append(value2[1])

    overall_data.append(current_temp_list)

print(overall_data)


# open the file in the write mode
f = open('ChargingStation_csv/soc100_200_4CS.csv', 'w')

# create the csv writer
writer = csv.writer(f)

# write a row to the csv file
writer.writerows(overall_data)

# close the file
f.close()

print("\n")    

print(overall_data)



