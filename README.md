# csv2django_model
convert csv to a model

* creates a django model from csv

turning this:
"Dimensions.Height","Dimensions.Length","Dimensions.Width","Engine Information.Driveline","Engine Information.Engine Type","Engine Information.Hybrid","Engine Information.Number of Forward Gears","Engine Information.Transmission","Fuel Information.City mpg","Fuel Information.Fuel Type","Fuel Information.Highway mpg","Identification.Classification","Identification.ID","Identification.Make","Identification.Model Year","Identification.Year","Engine Information.Engine Statistics.Horsepower","Engine Information.Engine Statistics.Torque"
"140","143","202","All-wheel drive","Audi 3.2L 6 cylinder 250hp 236ft-lbs","True","","6 Speed Automatic Select Shift","18.1","Gasoline","25","Automatic transmission","2009 Audi A3 3.2","Audi","2009 Audi A3","2009","250","236"

into this:

dimensions_height = models.PositiveSmallIntegerField("Dimensions.Height")
dimensions_length = models.PositiveSmallIntegerField("Dimensions.Length")
dimensions_width = models.PositiveSmallIntegerField("Dimensions.Width")
engine_information_driveline = models.CharField("Engine Information.Driveline", max_length=20)
engine_information_engine_type = models.CharField("Engine Information.Engine Type", max_length=63)
engine_information_hybrid = models.BooleanField("Engine Information.Hybrid")
engine_information_number_of_forward_gears = models.FloatField("Engine Information.Number of Forward Gears")
engine_information_transmission = models.CharField("Engine Information.Transmission", max_length=33)
fuel_information_city_mpg = models.FloatField("Fuel Information.City mpg")
fuel_information_fuel_type = models.CharField("Fuel Information.Fuel Type", max_length=25)
fuel_information_highway_mpg = models.PositiveSmallIntegerField("Fuel Information.Highway mpg")
identification_classification = models.CharField("Identification.Classification", max_length=25)
identification_id = models.CharField("Identification.ID", max_length=70)
identification_make = models.CharField("Identification.Make", max_length=21)
identification_model_year = models.CharField("Identification.Model Year", max_length=51)
identification_year = models.PositiveSmallIntegerField("Identification.Year")
engine_information_engine_statistics_horsepower = models.PositiveSmallIntegerField("Engine Information.Engine Statistics.Horsepower")
engine_information_engine_statistics_torque = models.PositiveSmallIntegerField("Engine Information.Engine Statistics.Torque")
