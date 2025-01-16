def parse_kotlin_vals(input_text):
    # Define mappings from Kotlin DSL functions to Kotlin types
    type_mapping = {
        "integer": "Int",
        "varchar": "String",
        "char": "String",
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
    val instanceId = integer("INSTANCE_ID").autoIncrement("AP_CLASS_INSTANCES_SEQ")
    override val id = instanceId.entityId()
    override val primaryKey = PrimaryKey(id, name = "AP_CLASS_INSTANCES_PK")
    val createdOn = datetime("CREATED_ON").nullable()
    val createdBy = varchar("CREATED_BY", 500).nullable()
    val updatedOn = datetime("UPDATED_ON").nullable()
    val updatedBy = varchar("UPDATED_BY", 500).nullable()
    val cancelByOverride = datetime("CANCEL_BY_OVERRIDE").nullable()
    val formatId = reference("FORMAT_ID", ApClassFormats).nullable()
    val signupsStartOverride = datetime("SIGNUPS_START_OVERRIDE").nullable()
    val cancelledDatetime = datetime("CANCELLED_DATETIME").nullable()
    val price = integer("PRICE").nullable()
    val signupMax = integer("SIGNUP_MAX").nullable()
    val signupMin = integer("SIGNUP_MIN").nullable()
    val doNotAutoCancel = char("DO_NOT_AUTO_CANCEL").nullable()
    val hideOnline = char("HIDE_ONLINE").nullable()
    val locationString = varchar("LOCATION_STRING", 100).nullable()
    val instructorId = reference("INSTRUCTOR_ID", Persons).nullable()
"""

# Generate output
parsed_fields = parse_kotlin_vals(kotlin_input)

# Print results
for field in parsed_fields:
    print(field)
