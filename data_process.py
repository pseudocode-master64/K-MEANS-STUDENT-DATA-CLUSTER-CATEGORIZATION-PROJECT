import csv
with open("data/original_data.csv", "r") as f:
    reader = csv.DictReader(f)
    records = list(reader)
    langs = ['Chinese A: Literature', 'English B', 'English A', 'Korean A','Chinese B','Chinese A']
    stems = ['Chemistry','Physics','Design Technology','Biology','Mathematics Applications & Interpretations','Mathematics Analysis & Approaches', "Mathematics"]
    hums = ['Geography', 'Economics', 'History', 'Business Management','Philosophy','Psychology']

    total_students = 48
    students = []

    for i in range (total_students): # Total
      
        lang_z_total = 0
        stem_z_total = 0
        hum_z_total = 0
        subjects = 0
        student = {}
        lang_counter = 0
        stem_counter = 0
        hum_counter = 0
        for record in records:
            if int(record['student']) == i+1: #Look at the data of a single student CSV data 默认是string
                subjects += 1
        
        if subjects == 8: #Ensure the student has 8 subjects
            for record in records:

                    if record['subject'] in langs and int(record['student']) == i+1:
                        lang_counter += 1
                        lang_z_total += float(record['z_score'])

                    if record['subject'] in stems and int(record['student']) == i+1:
                        stem_counter += 1
                        stem_z_total += float(record['z_score'])

                    if record['subject'] in hums and int(record['student']) == i+1:
                        hum_counter += 1
                        hum_z_total += float(record['z_score'])

            lang_z_mean = lang_z_total / lang_counter # Average zscore per student  
            stem_z_mean = stem_z_total / stem_counter  
            hum_z_mean = hum_z_total / hum_counter
        
            student = {'id': i+1, 'lang_z': lang_z_mean, 'stem_z': stem_z_mean, 'hum_z': hum_z_mean}
            students.append(student)

field_names = ['id', 'lang_z', 'stem_z', 'hum_z']

with open ("data/processed_data.csv", 'w') as w:
    writer = csv.DictWriter(w, fieldnames = field_names)
    writer.writeheader()
    writer.writerows(students)

print("\n The processed data is stored in data/processed_data.csv\n")