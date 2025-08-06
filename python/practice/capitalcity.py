#store the capital city and countries in as key value pairs in a dictionary where country is the key and capital city is the value
import random
capitals = {
  "Algeria": "Algiers",
  "Angola": "Luanda",
  "Benin": "Porto-Novo",
  "Botswana": "Gaborone",
  "Burkina Faso": "Ouagadougou",
  "Burundi": "Gitega",
  "Cape Verde": "Praia",
  "Cameroon": "Yaoundé",
  "Central African Republic": "Bangui",
  "Chad": "N'Djamena",
  "Comoros": "Moroni",
  "DRC Congo": "Kinshasa",
  "Republic of the Congo": "Brazzaville",
  "Djibouti": "Djibouti",
  "Egypt": "Cairo",
  "Equatorial Guinea": "Malabo",
  "Eritrea": "Asmara",
  "Eswatini": "Mbabane",
  "Ethiopia": "Addis Ababa",
  "Gabon": "Libreville",
  "Gambia": "Banjul",
  "Ghana": "Accra",
  "Guinea": "Conakry",
  "Guinea-Bissau": "Bissau",
  "Ivory Coast": "Yamoussoukro",
  "Kenya": "Nairobi",
  "Lesotho": "Maseru",
  "Liberia": "Monrovia",
  "Libya": "Tripoli",
  "Madagascar": "Antananarivo",
  "Malawi": "Lilongwe",
  "Mali": "Bamako",
  "Mauritania": "Nouakchott",
  "Mauritius": "Port Louis",
  "Morocco": "Rabat",
  "Mozambique": "Maputo",
  "Namibia": "Windhoek",
  "Niger": "Niamey",
  "Nigeria": "Abuja",
  "Rwanda": "Kigali",
  "Sao Tome and Principe": "São Tomé",
  "Senegal": "Dakar",
  "Seychelles": "Victoria",
  "Sierra Leone": "Freetown",
  "Somalia": "Mogadishu",
  "South Africa": "Pretoria",
  "South Sudan": "Juba",
  "Sudan": "Khartoum",
  "Tanzania": "Dodoma",
  "Togo": "Lomé",
  "Tunisia": "Tunis",
  "Uganda": "Kampala",
  "Zambia": "Lusaka",
  "Zimbabwe": "Harare"
}

while True:
  print("Lets Play a Guessing Game!")
  # Randomly select a country and its capital city
  # capitals.items() returns a list of tuples (country, capital)
  # list() converts the tuples to a list
  country, capital = random. choice(list(capitals.items()))
  print(f"What is the capital city of {country}?")
  # Allow user to input their answer
  input_capital = input("Enter your answer: ").strip().title()
  # Check if the user's answer matches the capital city
  if capital == input_capital:
    print(f"Well Done! You Got It Right") 

  else:
    if capital != input_capital:
      print(f"Incorrect! The capital city of {country} is {capital}.")      

  # Ask the user if they want to play again
  play_again = input("Would you like to play again? (yes/no): ").strip().lower()
  if play_again != "yes":
    print("It was nice playing with you. GoodBye!")
    break
