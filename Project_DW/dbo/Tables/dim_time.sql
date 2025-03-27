CREATE TABLE [dbo].[dim_time] (

	[ORDERDATE] varchar(8000) NULL, 
	[YEAR_ID] varchar(8000) NULL, 
	[MONTH_ID] varchar(8000) NULL, 
	[QTR_ID] varchar(8000) NULL
);


GO
ALTER TABLE [dbo].[dim_time] ADD CONSTRAINT UQ_343406d5_6a91_4530_a37d_449591882dea unique NONCLUSTERED ([ORDERDATE]);