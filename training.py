import csv

with open('training.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["Weight", "Length", "Breadth", "Height"]
    
    writer.writerow(field)
    writer.writerow(["50 kg     220 cm	 1300 cm     132 cm "])
    writer.writerow(["12 kg  	200 cm 	 1200 cm 	 160 cm "])
    writer.writerow(["200 kg 	110 cm 	 110 cm  	 198 cm "])
    writer.writerow(["240 kg 	130 cm 	 1000 cm 	 122 cm "])
    writer.writerow(["200 kg 	110 cm 	 110 cm  	 198 cm "])
    writer.writerow(["45 kg	    234 cm	 1100 cm	 130 cm "])
    writer.writerow(["67 kg	    321 cm	 1250 cm	 234 cm "])
    writer.writerow(["32 kg	    456 cm	 1234 cm	 450 cm"])
    writer.writerow(["76 kg	    120 cm	 1100 cm	 980 cm "])
    writer.writerow(["23 kg	    450 cm	 1349 cm	 120 cm "])