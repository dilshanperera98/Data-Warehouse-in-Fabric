CREATE TABLE [dbo].[fact_sales] (

	[CUSTOMERNAME] varchar(8000) NULL, 
	[ORDERNUMBER] varchar(8000) NULL, 
	[PRODUCTCODE] varchar(8000) NULL, 
	[ORDERDATE] varchar(8000) NULL, 
	[QUANTITYORDERED] varchar(8000) NULL, 
	[PRICEEACH] varchar(8000) NULL, 
	[SALES] varchar(8000) NULL, 
	[ORDERLINENUMBER] varchar(8000) NULL, 
	[STATUS] varchar(8000) NULL, 
	[DEALSIZE] varchar(8000) NULL, 
	[CUSTOMER_ID] varchar(8000) NULL, 
	[PHONE] varchar(8000) NULL, 
	[ADDRESSLINE1] varchar(8000) NULL, 
	[ADDRESSLINE2] varchar(8000) NULL, 
	[CITY] varchar(8000) NULL, 
	[STATE] varchar(8000) NULL, 
	[POSTALCODE] varchar(8000) NULL, 
	[COUNTRY] varchar(8000) NULL, 
	[TERRITORY] varchar(8000) NULL, 
	[CONTACTLASTNAME] varchar(8000) NULL, 
	[CONTACTFIRSTNAME] varchar(8000) NULL, 
	[STATUS_ID] varchar(8000) NULL
);


GO
ALTER TABLE [dbo].[fact_sales] ADD CONSTRAINT FK_5d968cbd_2ff3_4f0a_96a8_b06bfeb5a8de FOREIGN KEY ([STATUS_ID]) REFERENCES [dbo].[dim_status]([STATUS_ID]);
GO
ALTER TABLE [dbo].[fact_sales] ADD CONSTRAINT FK_7cbcd056_a08d_488b_964c_f8bf4a1d0e3f FOREIGN KEY ([ORDERDATE]) REFERENCES [dbo].[dim_time]([ORDERDATE]);
GO
ALTER TABLE [dbo].[fact_sales] ADD CONSTRAINT FK_94385605_6c31_4aaa_abb5_e0dca7b4af6e FOREIGN KEY ([PRODUCTCODE]) REFERENCES [dbo].[dim_product]([PRODUCTCODE]);
GO
ALTER TABLE [dbo].[fact_sales] ADD CONSTRAINT FK_b908c7bd_6a0c_4abd_affb_b8a4bf7d96b1 FOREIGN KEY ([CUSTOMER_ID]) REFERENCES [dbo].[dim_customers_new]([CUSTOMER_ID (String)]);