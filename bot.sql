/*without Payment Card view*/
CREATE VIEW WithoutPaymentCard AS
SELECT * FROM EXCEPTIONS
WHERE WithoutPaymentCard LIKE '%Yes%'

/*Without Bank Account*/
CREATE VIEW WithoutBankAccount AS
SELECT * FROM EXCEPTIONS
WHERE WithoutBankAccount LIKE '%Yes%'

/*Primary Recipient IPRS Mismatch*/
CREATE VIEW PrimaryRecipientIPRSMismatch AS
SELECT * FROM EXCEPTIONS
WHERE PrimaryRecipientIPRSMismatch LIKE '%Yes%'

/*Primary Recipient Duplicated Within*/
CREATE VIEW PrimaryRecipientduplicatedWithin AS
SELECT * FROM EXCEPTIONS
WHERE PrimaryRecipientduplicatedWithin LIKE '%Yes%'

/*Primary Recipient Duplicated Across*/
CREATE VIEW PrimaryRecipientduplicatedacross AS
SELECT * FROM EXCEPTIONS
WHERE PrimaryRecipientDuplicatedAcross LIKE '%Yes%'

/*Primary Recipient Missing or Ineligible*/
CREATE VIEW PrimaryRecipientMissingOrIneligible AS
SELECT * FROM EXCEPTIONS
WHERE PrimaryRecipientMissingOrIneligible LIKE '%Yes%'

/*Secondary Recipient Duplicated Within*/
CREATE VIEW SecondaryRecipientduplicatedWithin AS
SELECT * FROM EXCEPTIONS
WHERE SecondaryRecipientduplicatedWithin LIKE '%Yes%'

/*Secondary Recipient IPRS Mismatch*/
CREATE VIEW SecondaryRecipientIPRSMismatch AS
SELECT * FROM EXCEPTIONS
WHERE SecondaryRecipientIPRSMismatch LIKE '%Yes%'

/*Secondary Recipient Duplicated Across*/
CREATE VIEW SecondaryRecipientDuplicatedacross AS
SELECT * FROM EXCEPTIONS
WHERE SecondaryRecipientDuplicatedAcross LIKE '%Yes%'

/*Secondary Recipient Missing*/
CREATE VIEW SecondaryRecipientMissing AS
SELECT * FROM EXCEPTIONS
WHERE SecondaryRecipientMissing LIKE '%Yes%'

/*Household suspended*/
CREATE VIEW Householdsuspended AS
SELECT * FROM EXCEPTIONS
WHERE HouseholdSuspended LIKE '%Yes%'

/*Dormant Account*/
CREATE VIEW DormantAccount AS
SELECT * FROM EXCEPTIONS
WHERE DormantAccount LIKE '%Yes%'

/*suspicious payment*/
CREATE VIEW SuspiciousPayment AS
SELECT * FROM EXCEPTIONS
WHERE SuspiciousPayment LIKE '%Yes%'