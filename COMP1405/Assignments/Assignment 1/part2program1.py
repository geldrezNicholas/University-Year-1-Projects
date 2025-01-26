#   COMP 1405 Section C - Assignment 1 Program 1
#    Project Details
#       Name: Nicholas Geldrez
#       Date Created: September 27, 2024

standardRate = 120
maxKG = 20
overWeightFee = 0.015

print('Hello welcome to Geldrez airlines!')
weight = float(input('What is the weight of your bag:')) 
if(weight <= maxKG and weight >= 0): #is the weight equal or between 0 to 20
    print(f"Your flight is costs {standardRate}!")
elif(weight > maxKG): #weight is heavier than 20
    excessWeight = weight - maxKG 
    totalExtra = excessWeight * overWeightFee * standardRate #calculates extra paid
    totalCost = standardRate + totalExtra 
    print(f"Your flight is costs ${totalCost}, due to the added ${totalExtra} from your baggage!")
else: #negative number
    print('This is not a weight!')