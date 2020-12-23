def ground_shipping(weight):
  flat = 20.00
  if weight <= 2:
    total_ground = weight * 1.50 + flat
  elif 6 >= weight >= 2:
    total_ground = weight * 3.00 + flat
  elif 10 >= weight >= 6:
    total_ground = weight * 4.00 + flat
  elif weight >= 10:
    total_ground = weight * 4.75 + flat
  return total_ground

print(ground_shipping(8.4))

premium_ground = 125.00

def drone_shipping(weight):
  flat = 00.00
  if weight <= 2:
    total_drone = weight * 4.50
  elif 6 >= weight >= 2:
    total_drone = weight * 9.00
  elif 10 >= weight >= 6:
    total_drone = weight * 12.00
  elif weight >= 10:
    total_drone = weight * 14.25
  return total_drone

print(drone_shipping(1.5))

def best_shipping(weight):
  ground = ground_shipping(weight)
  drone = drone_shipping(weight)
  premium = premium_ground
  if ground < premium and drone:
    return "Ground shipping is the cheapest and it costs " + str(ground)
  elif premium < ground and drone:
    return "Premium ground shipping is the cheapest and it costs " + str(premium)
  else: 
    return "Drone shipping is the cheapest and it costs " + str(drone)

print(best_shipping(4.8))
print(best_shipping(41.5))

