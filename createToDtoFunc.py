def create_to_dto_func(input_text, tableVal):
    output = []
    lines = input_text.strip().split("\n")
    for line in lines:
        line = line.replace('val ', '')
        line = line.strip()
        # print(line)
        valName = line.split(":")[0]

        newLine = f'{valName} = row[{tableVal}.{valName}],'
        output.append(newLine)
    return output



input_text = """
val cancelByOverride: LocalDateTime?,
    val formatId: Int?,
    val signupsStartOverride: LocalDateTime?,
    val cancelledDatetime: LocalDateTime?,
    val price: Int?,
    val signupMax: Int?,
    val signupMin: Int?,
    val doNotAutoCancel: String?,
    val hideOnline: String?,
    val locationString: String?,
    val instructorId: Int?,
"""

tableVal = 'apClassInstances'

output = create_to_dto_func(input_text, tableVal)

for line in output:
    print(line)