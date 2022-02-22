# ------------------------------------------ CONSIDERATIONS ------------------------------------------
# SoC changes at the rate of 1% per unit km
# ----------------------------------------------------------------------------------------------------

# Libraries
import collections
from tabnanny import check
from turtle import distance
from numpy import number
import pandas as pd
import matplotlib.pyplot as plt

# Constant parameters
num_of_bikes = 100                      # Total number of Bikes
total_distance_in_one_trip = 132        # distance in kms
SoC_logging_distance = 1                # distance in kms

# Which Data will I be using from Spreadsheet?
dataColumn = "Random1"
# dataColumn = "Normal1"

# Number of times Bike travels from A to B and viceversa
total_number_of_trips = range(2)
present_SoC = 0
# Distance travelled by that instant in the present trip
distance_travelled = 0
counter = 0
result = {}

checkpoint_1 = 44
checkpoint_2 = 88
checkpoint_3 = 132
# checkpoint_4 = 132

checkpoint_1_distances = {}
checkpoint_2_distances = {}
checkpoint_3_distances = {}
checkpoint_4_distances = {}

weighted_summation_for_checkpoint = 0
total_frequency_for_checkpoint = 1

weighted_summation_for_checkpoint1 = 0
total_frequency_for_checkpoint1 = 1

weighted_summation_for_checkpoint2 = 0
total_frequency_for_checkpoint2 = 1

weighted_summation_for_checkpoint3 = 0
total_frequency_for_checkpoint3 = 1

weighted_summation_for_checkpoint4 = 0
total_frequency_for_checkpoint4 = 1

strandedRiderCount = 0
total_strandedRiderCount = 0

leastSoC_before_getting_stranded = 5
checkpoint_charging_frequency = 0
checkpointOccupancy = {}
chargingSoC = {}
checkpointwise_Stranded_Count = {}

total_rider_count = 0

strandedRiderCount_checkpoint1 = 0
strandedRiderCount_checkpoint2 = 0
strandedRiderCount_checkpoint3 = 0
strandedRiderCount_checkpoint4 = 0

checkpoint1_charging_frequency = 0
checkpoint2_charging_frequency = 0
checkpoint3_charging_frequency = 0
checkpoint4_charging_frequency = 0

anxietyLevels = [1, 2, 3, 4, 5, 6, 7, 8, 9]
anxietyLevelFrequency = [0, 0, 0, 0, 0, 0, 0, 0, 0]

all_charging_SoC = []

# SoC data input for the system
df = pd.read_excel(r'data_collection.xlsx')
initial_values = []

print("Data Column Used:                            ", dataColumn)
for count in range(len(df[dataColumn])):
    initial_values.append(df[dataColumn][count])

# Output Variable define
points_of_recharge = []

# print(initial_values)

# Begin Logic
for initial_SoC in initial_values:
    # print("For this initial SoC: ")
    # print(initial_SoC)
    present_SoC = initial_SoC
    # print(present_SoC)
    distance_travelled = 0
    # for trip_number in total_number_of_trips:
    #     if(trip_number % 2 == 0):
    while (distance_travelled < total_distance_in_one_trip):
        if (present_SoC <= 50):
            points_of_recharge.append(distance_travelled)
            # print(present_SoC)
            # print(points_of_recharge)
            # print("--")
            present_SoC = 100                           # Bike recharged to full when reached to 50%
        else:
            # Bike SoC decreases with increase in travel displacement by 1km
            present_SoC -= 1
            # print("SoC is decreasing")

        # Increase distance travelled by 1km
        distance_travelled += 1
        # print(distance_travelled)

        # elif (trip_number % 2 == 1):

        #     while (distance_travelled <= total_distance_in_one_trip and distance_travelled > 0):
        #         if (present_SoC <= 50):
        #             points_of_recharge.append(distance_travelled)
        #             present_SoC = 100                           # Bike recharged to full when reached to 50%
        #         else:
        #             # Bike SoC decreases with increase in travel displacement by 1km
        #             present_SoC -= 1
        #         # Increase distance travelled by 1km
        #         distance_travelled -= 1

# Arrange Dictionary keys in ascending order


def ascendingKeys(frequency_of_occurence):
    for i in sorted(frequency_of_occurence):
        result.update({
            i: frequency_of_occurence[i]
        })
    # print("\n")
    print('---------------------- SORTED DICTIONARY : KEY as DISTANCE, VALUE as FREQUENCY -----------------------------')
    print(result)

# print("Points of Recharge:")
# print(points_of_recharge)
ctr = collections.Counter(points_of_recharge)
# print("Values for ctr:")
# print(ctr)
frequency = dict(ctr)
ascendingKeys(frequency)

Distance_x_axis = list(result.keys())
Frequency_y_axis = list(result.values())

print("\n")

plt.plot(Distance_x_axis, Frequency_y_axis)
plt.xlabel('Distance')
plt.ylabel('Frequency')
plt.show()


# ------------------------------------------- INSERT DATA FROM PYTHON TO EXCEL -------------------------------------


# df = pd.DataFrame(data=result, index=[0])
# df = (df.T)
# print (df)
# df.to_excel('Random1_data.xlsx')

# print(list(result))
# print(result.values())


# result_distances = list(result)
# result_frequencies = result.values()

# print(type(result_distances))
# print(type(result_frequencies))

# for weighted_average_distance in result_distances:
#     if (weighted_average_distance <= checkpoint_1):
#         new_pair = {weighted_average_distance: }
#         weighted_distance_dictionary_for_checkpoint_1.update()


# for result_distance, frequency in result.items():

#     weighted_summation_for_checkpoint += (result_distance * frequency)
#     total_frequency_for_checkpoint += frequency

#     if (result_distance <= checkpoint_1):
#         checkpoint_1_distances.update({result_distance: frequency})
#     elif (result_distance <= checkpoint_2):
#         checkpoint_2_distances.update({result_distance: frequency})
#     elif (result_distance <= checkpoint_3):
#         checkpoint_3_distances.update({result_distance: frequency})
#     # elif (result_distance <= checkpoint_4):
#     #     checkpoint_4_distances.update({result_distance: frequency})

# weighted_average_for_checkpoint = weighted_summation_for_checkpoint / \
# total_frequency_for_checkpoint
# print("CHECKPOINT   :                               ", weighted_average_for_checkpoint)

# print("\n--- CALCULATING WEIGHTED AVERAGES TO DETERMINE CHARGING STATION CHECKPOINTS")

# for _distance, _frequency in checkpoint_1_distances.items():
#     weighted_summation_for_checkpoint1 += (_distance * _frequency)
#     total_frequency_for_checkpoint1 += _frequency

# weighted_average_for_checkpoint1 = weighted_summation_for_checkpoint1 / \
#     total_frequency_for_checkpoint1
# print("CHECKPOINT 1 :                               ",
#       weighted_average_for_checkpoint1)


# for _distance, _frequency in checkpoint_2_distances.items():
#     weighted_summation_for_checkpoint2 += (_distance * _frequency)
#     total_frequency_for_checkpoint2 += _frequency

# weighted_average_for_checkpoint2 = weighted_summation_for_checkpoint2 / \
#     total_frequency_for_checkpoint2
# print("CHECKPOINT 2 :                               ",
#       weighted_average_for_checkpoint2)


# for _distance, _frequency in checkpoint_3_distances.items():
#     weighted_summation_for_checkpoint3 += (_distance * _frequency)
#     total_frequency_for_checkpoint3 += _frequency

# weighted_average_for_checkpoint3 = weighted_summation_for_checkpoint3 / \
#     total_frequency_for_checkpoint3
# print("CHECKPOINT 3 :                               ",
#       weighted_average_for_checkpoint3)

# # for _distance, _frequency in checkpoint_4_distances.items():
# #     weighted_summation_for_checkpoint4 += (_distance * _frequency)
# #     total_frequency_for_checkpoint4 += _frequency

# # weighted_average_for_checkpoint4 = weighted_summation_for_checkpoint4 / \
# #     total_frequency_for_checkpoint4
# # print("CHECKPOINT 4 :                               ",
# #       weighted_average_for_checkpoint4)


# # Record initial_SoC for stranded ones.
# # Frequency of the charging station checkpoints that are being used the most

# # Take the 100 bikes to the trip of 132 km keeping Charging Stations at the 3 checkpoints, then let the bikes look for
# # nearest charging station.
# #
# # Output should be:
# #   - How many were stranded during the commute
# #   - The unstranded ones charged at what SoC %
# #   - Frequency of the Charging Stations

# chargingStationCheckpoints = [int(weighted_average_for_checkpoint1), int(weighted_average_for_checkpoint2),
#                               int(weighted_average_for_checkpoint3)]

# # chargingStationCheckpoints = [int(weighted_average_for_checkpoint1), int(weighted_average_for_checkpoint2)]

# # chargingStationCheckpoints = [int(weighted_average_for_checkpoint1), int(weighted_average_for_checkpoint2),
# #                               int(weighted_average_for_checkpoint3), int(weighted_average_for_checkpoint4)]

# # chargingStationCheckpoints = [int(weighted_average_for_checkpoint1), int(weighted_average_for_checkpoint2)]

# distance_travelled = 0
# distanceFromCheckpoint = []

# for initial_SoC in initial_values:
#     present_SoC = initial_SoC
#     chargingSoC_list = []

#     # Total number of trips for each bike
#     for trip_number in total_number_of_trips:

#         # Moving from A -> B
#         if(trip_number % 2 == 0):

#             # When the rider hasn't reached the destination
#             while (distance_travelled < total_distance_in_one_trip):

#                 if (distance_travelled in chargingStationCheckpoints):
#                     checkpointIndex = chargingStationCheckpoints.index(
#                         distance_travelled)

#                     if (present_SoC <= leastSoC_before_getting_stranded):

#                         total_strandedRiderCount += 1

#                         if (checkpointIndex == 0):
#                             strandedRiderCount_checkpoint1 += 1
#                         elif (checkpointIndex == 1):
#                             strandedRiderCount_checkpoint2 += 1
#                         elif (checkpointIndex == 2):
#                             strandedRiderCount_checkpoint3 += 1
#                         # elif (checkpointIndex == 3):
#                         #     strandedRiderCount_checkpoint4 += 1

#                         break

#                     elif (present_SoC > leastSoC_before_getting_stranded and present_SoC <= 50):

#                         # The rider charged to the nearest charging Station that was in the direction towards his destination

#                         # Update frequency of the particular Checkpoint being used
#                         if (checkpointIndex == 0):
#                             checkpoint1_charging_frequency += 1
#                         elif (checkpointIndex == 1):
#                             checkpoint2_charging_frequency += 1
#                         elif (checkpointIndex == 2):
#                             checkpoint3_charging_frequency += 1
#                         # elif (checkpointIndex == 3):
#                         #     checkpoint4_charging_frequency += 1

#                         # At what SoC values are each riders charging?
#                         chargingSoC_list.append(present_SoC)

#                         all_charging_SoC.append(present_SoC)

#                         if (present_SoC > 45 and present_SoC <= 50):
#                             anxietyLevelFrequency[0] += 1

#                         elif (present_SoC > 40 and present_SoC <= 45):
#                             anxietyLevelFrequency[1] += 1

#                         elif (present_SoC > 35 and present_SoC <= 40):
#                             anxietyLevelFrequency[2] += 1

#                         elif (present_SoC > 30 and present_SoC <= 35):
#                             anxietyLevelFrequency[3] += 1

#                         elif (present_SoC > 25 and present_SoC <= 30):
#                             anxietyLevelFrequency[4] += 1

#                         elif (present_SoC > 20 and present_SoC <= 25):
#                             anxietyLevelFrequency[5] += 1

#                         elif (present_SoC > 15 and present_SoC <= 20):
#                             anxietyLevelFrequency[6] += 1

#                         elif (present_SoC > 10 and present_SoC <= 15):
#                             anxietyLevelFrequency[7] += 1

#                         elif (present_SoC > 5 and present_SoC <= 10):
#                             anxietyLevelFrequency[8] += 1

#                         present_SoC = 100

#                     strandedRiderCount = 0
#                     checkpoint_charging_frequency = 0

#                 # Rider just travelled 1 km
#                 # Increase distance travelled by 1km
#                 distance_travelled += 1

#                 # Rider's SoC decreases by 1 %
#                 present_SoC -= 1

#             distance_travelled = 0

#     chargingSoC.update({initial_SoC: chargingSoC_list})
#     total_rider_count += 1

# # Average Charging SoC
# avgChargingSoC = sum(all_charging_SoC) / len(all_charging_SoC)

# # Stranded Rider count that each checkpoint had
# checkpointwise_Stranded_Count = {
#     chargingStationCheckpoints[0]: strandedRiderCount_checkpoint1,
#     chargingStationCheckpoints[1]: strandedRiderCount_checkpoint2,
#     chargingStationCheckpoints[2]: strandedRiderCount_checkpoint3,
#     # chargingStationCheckpoints[3]: strandedRiderCount_checkpoint4
# }

# # Checkpointwise busy Charging Stations
# checkpointOccupancy = {
#     chargingStationCheckpoints[0]: checkpoint1_charging_frequency,
#     chargingStationCheckpoints[1]: checkpoint2_charging_frequency,
#     chargingStationCheckpoints[2]: checkpoint3_charging_frequency,
#     # chargingStationCheckpoints[3]: checkpoint4_charging_frequency
# }

# # Anxiety Level Measurement
# AnxietyLevel = {
#     anxietyLevels[0]: anxietyLevelFrequency[0],
#     anxietyLevels[1]: anxietyLevelFrequency[1],
#     anxietyLevels[2]: anxietyLevelFrequency[2],
#     anxietyLevels[3]: anxietyLevelFrequency[3],
#     anxietyLevels[4]: anxietyLevelFrequency[4],
#     anxietyLevels[5]: anxietyLevelFrequency[5],
#     anxietyLevels[6]: anxietyLevelFrequency[6],
#     anxietyLevels[7]: anxietyLevelFrequency[7],
#     anxietyLevels[8]: anxietyLevelFrequency[8]
# }

# print("Charging Station Locations:                  ", chargingStationCheckpoints)

# print("\n--- RIDERS CHARGING PROFILE")
# print("How many bikes did each checkpoint charge?   ", checkpointOccupancy)
# print("RiderCount stranded before each checkpoint?  ",
#       checkpointwise_Stranded_Count)
# print("At what SoCs did each bike charge?           ", chargingSoC)
# print("Total number of stranded riders:             ", total_strandedRiderCount)
# print("Total riders on account:                     ", total_rider_count)
# print("Anxiety Levels:                              ", AnxietyLevel)
# print("Average Charging SoC:                        ", avgChargingSoC)


# # plt.plot(list(AnxietyLevel.keys()), list(AnxietyLevel.values()))
# # plt.xlabel('Anxiety Levels from low to high')
# # plt.ylabel('Frequency')
# # plt.show()
