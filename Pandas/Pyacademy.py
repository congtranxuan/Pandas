# Dependencies and Setup
import pandas as pd
import numpy as np

# File to Load (Remember to Change These)
school_data_to_load = "../../RICEHOU201906DATA1/HW/04-Pandas/Instructions/PyCitySchools/Resources/schools_complete.csv"
student_data_to_load = school_data_to_load = "../../RICEHOU201906DATA1/HW/04-Pandas/Instructions/PyCitySchools/Resources/students_complete.csv"


# Read School and Student Data File and store into Pandas Data Frames
school_data = pd.read_csv(school_data_to_load)
student_data = pd.read_csv(student_data_to_load)
#student_data.head()
#student_data.head()
# Combine the data into a single dataset
school_data_complete = pd.merge(student_data,school_data,on="school_name",how="outer")
school_data_complete