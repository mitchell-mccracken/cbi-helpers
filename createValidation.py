def create_validation(input_text, dto_name):
  output = []
  lines = input_text.strip().split("\n")
  for line in lines:
    line = line.strip()

    if line[:8] == "override":
      continue
    
    # if "varchar" in line:
    line = line.replace('val ', '')
    field = line.split("=")[0].strip()

    if 'varchar' in line:
      length = line.split("varchar(")[1].split(')')[0].split(',')[1].strip()
    elif 'char' in line:
      length = 1
      
    output_line = f'{dto_name}::{field} ifPresent {{ maxLength({length})}}'
    print(output_line)
    
    # print(f'field: {field} | length {length}')


input_text = """
val ethnicity = varchar("ETHNICITY", 100).nullable()
    val language = varchar("LANGUAGE", 100).nullable()
    val referralSource = varchar("REFERRAL_SOURCE", 200).nullable()
    val sailingExp = varchar("SAILING_EXP", 100).nullable()
    val organization = varchar("ORGANIZATION", 100).nullable()
    val orgContact = varchar("ORG_CONTACT", 200).nullable()
    val student = char("STUDENT").nullable()
"""

create_validation(input_text, "PersonUpdateDTO")