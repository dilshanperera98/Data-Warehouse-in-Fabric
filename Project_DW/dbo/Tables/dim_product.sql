CREATE TABLE [dbo].[dim_product] (

	[PRODUCTCODE] varchar(8000) NULL, 
	[PRODUCTLINE] varchar(8000) NULL, 
	[MSRP] varchar(8000) NULL
);


GO
ALTER TABLE [dbo].[dim_product] ADD CONSTRAINT UQ_dc58fb5c_3f8e_46c4_a3d1_cce4497f9d11 unique NONCLUSTERED ([PRODUCTCODE]);