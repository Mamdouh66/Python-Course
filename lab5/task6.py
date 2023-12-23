# In a particular jurisdiction, taxi fares consist of a base fare of $4.00, plus $0.25 for every 140 meters traveled.
# Write a function that takes the distance traveled (in kilometers) as its only parameter and returns the total
# fare as its only result. Write a main program that demonstrates the function.

if __name__ == "__main__":
    taxi = lambda km: 4 + (km * 1000) / 140 * 0.25
    print(taxi(0.14))
