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
    //Instance Fields
    val instanceId : Int,
    val limitOverride : Int?,
    val nameOverride : String?,
    val instanceMaxAge : Int?,
    val createdOn : LocalDateTime?,
    val createdBy : String?,
    val updatedOn : LocalDateTime?,
    val updatedBy : String?,
    val instanceMinAge : Int?,
    val price : Int?,
    val regCodeRowId : Int?,
    val confirmTemplate : String?,
    val adminHold : Char?,
    val instructorId : Int?,
    val locationId : Int?,
    val reservedForGroup : Char?,
    val overrideNoLimit : Char?,
    //Type Fields
    val typeId: Int,
    val typeName: String?,
    val signupMax: Int?,
    val allowMultiple: Char?,
    val ratingPrereq: Int?,
    val sessionLength: Int?,
    val sessionCt: Int?,
    val ratingOverkill: Int?,
    val typeMinAge: Int?,
    val typeMaxAge: Int?,
    val minSessionsForAttended: Int?,
    val active: Char?,
    val displayOrder: Int?,
    val noLimit: Char?,

    // Person Fields
    val instructorNameFirst: String?,
    val instructorNameMiddleInitial: String?,
    val instructorNameLast: String?,

    // Rating Fields
    val ratingName: String?,

    //Session Fields
    val sessionsList : List<JpClassSessionDTO>,
    // Staggers
    val staggersList: List<JpClassStaggerExtendedDTO>,

    // counts
    var enrolledCount: Int? = null,
    var waitlistCount: Int? = null,

    // availability
    val classAvailability: JpClassAvailabilityViewDTO
"""

# print(convert_kotlin_dto_to_typescript(kotlin_dto))
convert_kotlin_dto_to_typescript(kotlin_dto)