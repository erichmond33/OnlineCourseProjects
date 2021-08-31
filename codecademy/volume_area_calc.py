print 'Volume/Area Calculator'

area_or_volume = raw_input ('For area type "A" For volume type "V" ')
if area_or_volume == 'V' or area_or_volume == "A":
  Unit = raw_input ('What unit of measurment is this? (cm, in, ft,  etc...) : ')
else:
  print'Error: No input/inncorrect input'
  quit()
#^This step determines unit and Area or Volume
if len(Unit) > 0 and Unit.isalpha():
 'we are good'
else:
  print 'Error: No input/inncorrect input'
  quit()
#^This ensures a unit was typed and it was letters
if area_or_volume == "V":
  Length = raw_input ('What is the length: ') 
  Width = raw_input ('What is the width: ') 
  Height = raw_input ('What is the Height: ')
if area_or_volume == "A":
  Length = raw_input ('What is the length: ') 
  Width = raw_input ('What is the width: ')
  Height = "1"
#^This gets the LWH needed for the formula
if area_or_volume == "V" or area_or_volume == "A":
  Volume = float(Length)*float(Width)*float(Height)
else:
  print 'Error: No Input/Input was not a number'
#^This makes sure it was a number
if area_or_volume == "V":
 print str(Volume) + str(Unit) + ' cubed'
if area_or_volume == "A":
  print str(Volume) + str(Unit) + ' squared'
#^This prints the final product

  
 