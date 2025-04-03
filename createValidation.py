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

    length = None
    if 'varchar' in line:
      length = line.split("varchar(")[1].split(')')[0].split(',')[1].strip()
    elif 'char' in line:
      length = 1
    else:
      continue
      
    output_line = f'{dto_name}::{field} ifPresent {{ maxLength({length}) }}'
    print(output_line)
    
    # print(f'field: {field} | length {length}')


input_text = """
    val assignId = integer("ASSIGN_ID").autoIncrement("PERSONS_MEMBERSHIPS_SEQ")
    override val id = assignId.entityId()
    override val primaryKey = PrimaryKey(id, name = "PERSONS_MEMBERSHIPS_PK")
    val personId = reference("PERSON_ID", Persons)
    val membershipTypeId = reference("MEMBERSHIP_TYPE_ID", MembershipTypes)
    val purchaseDate = datetime("PURCHASE_DATE").nullable()
    val startDate = datetime("START_DATE").nullable()
    val expirationDate = datetime("EXPIRATION_DATE").nullable()
    val schoolId = reference("SCHOOL_ID", HighSchools).nullable()
    val orderId = reference("ORDER_ID", OrderNumbers).nullable()
    val price = integer("PRICE")
    val createdOn = datetime("CREATED_ON")
    val createdBy = varchar("CREATED_BY", 500).nullable()
    val updatedOn = datetime("UPDATED_ON")
    val updatedBy = varchar("UPDATED_BY", 500).nullable()
    val temp = char("TEMP", 1)
    val paymentLocation = varchar("PAYMENT_LOCATION", 50).nullable()
    val paymentMedium = varchar("PAYMENT_MEDIUM", 50).nullable()
    val discountId = integer("DISCOUNT_ID").nullable()
    val oldCardNum = varchar("OLD_CARD_NUM", 100).nullable()
    val oldCompReason = varchar("OLD_COMP_REASON", 500).nullable()
    val oldDmgWaiver = char("OLD_DMG_WAIVER", 1).nullable()
    val closeId = reference("CLOSE_ID", FoCloses).nullable()
    val ccTransNum = integer("CC_TRANS_NUM").nullable()
    val groupId = reference("GROUP_ID", JpGroups).nullable()
    val discountInstanceId = reference("DISCOUNT_INSTANCE_ID", DiscountInstances).nullable()
    val notes = varchar("NOTES", 4000).nullable()
    val voidCloseId = reference("VOID_CLOSE_ID", FoCloses).nullable()
    val discountAmt = integer("DISCOUNT_AMT").nullable()
    val pretaxPrice = integer("PRETAX_PRICE").nullable()
    val taxRate = integer("TAX_RATE").nullable()
    val ignoreDiscountFrozen = char("IGNORE_DISCOUNT_FROZEN", 1).nullable()
    val originalExpirationDate = datetime("ORIGINAL_EXPIRATION_DATE").nullable()
    val covidEmailSent = char("COVID_EMAIL_SENT", 1).nullable()
    val covidDays = integer("COVID_DAYS").nullable()
    val compassOrderID = reference("COMPASS_ORDER_ID", CompassOrders).nullable()
"""

create_validation(input_text, "MembershipCreateDTO")