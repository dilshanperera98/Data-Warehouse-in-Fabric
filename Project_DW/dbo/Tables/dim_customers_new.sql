CREATE TABLE [dbo].[dim_customers_new] (

	[CUSTOMER_ID (String)] varchar(8000) NULL, 
	[CUSTOMERNAME] varchar(8000) NULL, 
	[PHONE] varchar(8000) NULL, 
	[ADDRESSLINE1] varchar(8000) NULL, 
	[ADDRESSLINE2] varchar(8000) NULL, 
	[CITY] varchar(8000) NULL, 
	[STATE] varchar(8000) NULL, 
	[POSTALCODE] varchar(8000) NULL, 
	[COUNTRY] varchar(8000) NULL, 
	[TERRITORY] varchar(8000) NULL, 
	[CONTACTLASTNAME] varchar(8000) NULL, 
	[CONTACTFIRSTNAME] varchar(8000) NULL
);


GO
ALTER TABLE [dbo].[dim_customers_new] ADD CONSTRAINT UQ_c656079f_5f5c_4442_ab4b_6c7333a7b835 unique NONCLUSTERED ([CUSTOMER_ID (String)]);