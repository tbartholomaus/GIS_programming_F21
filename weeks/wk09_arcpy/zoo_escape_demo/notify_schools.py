fcList = ["FieldSightings_Lola", "FieldSightings_Jimmy"]
print(fcList)
buffList = []

type(buffList)





for fc in fcList:
    buff = arcpy.analysis.Buffer(fc,fc+"_Buffer","1 kilometer")
    buffList.append(buff)

buffList



for buff in buffList:
    arcpy.SelectLayerByLocation_management('Redlands_Schools', 'WITHIN',buff,0, 'ADD_TO_SELECTION')


schools_in_buffer = redlands_schools.within(buff) # boolean of those schools within the buffers
redlands_schools_close = redlands_schools[schools_in_buffer]
import numpy as np
aa = np.array([4, 7, 3.4, 2])

selecting_boolean = np.array([False, False, True, False])
aa[ selecting_boolean ]

at_risk_schools = 'Redlands_Schools_close'

arcpy.CopyFeatures_management('Redlands_Schools', at_risk_schools)

fields = arcpy.ListFields(at_risk_schools)
fields

fields[3].name

fields[3].precision

# List comprehension
field_names = [f.name for f in fields]


# For loop 1
field_names = []
for f in fields:
    field_names.append(f.name)

# For Loop 2
field_names = []
for i in range(len(fields)):
    field_names.append(fields[i].name)

field_names

field_names[3]

arcpy.da.TableToNumPyArray(at_risk_schools, field_names[3])


