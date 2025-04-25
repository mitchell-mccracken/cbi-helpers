import re

def convert_kotlin_dto_to_typescript(kotlin_dto: str) -> str:
    kotlin_to_ts_types = {
        "Int": "number",
        "Double": "number",
        "String": "string",
        "Boolean": "boolean",
        "LocalDateTime": "string"
    }


    lines = kotlin_dto.strip().split("\n")

    for line in lines:
        line = line.strip()
        if len(line) == 0 or line[:2] == "//":
           print(line)
           continue

        line = line.replace("var ", "")
        line = line.replace("val ", "")
        line = line.replace(",", "")
        

        parts = line.split(":")
        key = parts[0]
        isNullable =  "?" in parts[1]
        value = parts[1].replace("?", "").strip()
        
        ret = key
        # if isNullable:
        #   ret += "?"
        

        # TODO: strip out content if value has default values (ie = null)
        _value = None
        try:
           _value = kotlin_to_ts_types[value]
        except:
          if "dto" in value.lower():
            _value = value
          else:
            _value = "string"

        ret += f": {_value}"

        if isNullable:
           ret += " | null"

        ret += ";"

        print(ret)

# Example usage
kotlin_dto = """
val ratingId: Int,
    val skillId: Int?,
    val ratingName: String,
    val ratingSeq: Int,
    val createdOn: LocalDateTime?,
    val createdBy: String?,
    val updatedOn: LocalDateTime?,
    val updatedBy: String?,
"""

# print(convert_kotlin_dto_to_typescript(kotlin_dto))
convert_kotlin_dto_to_typescript(kotlin_dto)