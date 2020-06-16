class vehicle:
  
  
  def __init__(self,engineSizeInput,vehicleColorInput,wheelSizeInput,frameTypeInput,isVehicle):
    self.engineSize=engineSizeInput
    self.vehicleColor=vehicleColorInput
    self.wheelSize=wheelSizeInput
    self.frameType=frameTypeInput
    self.vehicle=isVehicle
  

  def drive(self):
    print("Driving down the road.")
  def speedUp(self):
    print("Speeding up! vroom vroom")
  def crash(self):
    print("EXPLOSION! BOOM!")
  def openTrunk(self):
    print("Trunk opened")
  def turn(self,turnDirection):
    print("Turning" +turnDirection)

WontonVehicle=vehicle(200,"blue",50,"smooth",True)

print(WontonVehicle.engineSize)
WontonVehicle.speedUp()
WontonVehicle.crash()
WontonVehicle.openTrunk()
WontonVehicle.turn(" left")