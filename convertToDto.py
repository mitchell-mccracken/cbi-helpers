def parse_kotlin_vals(input_text):
    # Define mappings from Kotlin DSL functions to Kotlin types
    type_mapping = {
        "integer": "Int",
        "varchar": "String",
        "char": "Char",
        "datetime": "LocalDateTime",
        "text": "String",
        "reference": "Int",  # Foreign key reference is typically Int
    }

    # Process each line and extract the relevant details
    output = []
    lines = input_text.strip().split("\n")
    for line in lines:
        line = line.strip()
        if line.startswith("val "):  # Process only lines that define values
            # Extract the field name and type
            parts = line.split("=", 1)
            field_name = parts[0].strip().split()[1]
            type_info = parts[1].strip()

            # Detect the base type
            base_type = type_info.split("(")[0]
            kotlin_type = type_mapping.get(base_type, "Any")

            # Check if the field is nullable
            is_nullable = ".nullable()" in type_info
            if is_nullable:
                kotlin_type += "?"

            # Generate the description
            output.append(f"val {field_name}: {kotlin_type},")

    return output


# Input: Paste your Kotlin values as plain text
kotlin_input = """
val className = varchar("CLASS_NAME", 200)
    val instanceId = reference("INSTANCE_ID", JpClassInstances)
    val nextStaggerId = reference("NEXT_STAGGER_ID", JpClassStaggers).nullable()
    val spotsLeftActual = integer("SPOTS_LEFT_ACTUAL")
    val spotsLeft = integer("SPOTS_LEFT")
    val waitlistCount = integer("WAITLIST_COUNT").nullable()
    val signupCount = integer("SIGNUP_COUNT")
    val signupMax = integer("SIGNUP_MAX")
    val noLimit = char("NO_LIMIT")
    val nextSpotsOpeningDatetime = datetime("NEXT_SPOTS_OPENING_DATETIME").nullable()
    val nextStaggerOccupancy = integer("NEXT_STAGGER_OCCUPANCY").nullable()
"""

# Generate output
parsed_fields = parse_kotlin_vals(kotlin_input)

# Print results
for field in parsed_fields:
    print(field)
