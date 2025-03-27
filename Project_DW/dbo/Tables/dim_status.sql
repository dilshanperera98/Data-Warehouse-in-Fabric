CREATE TABLE [dbo].[dim_status] (

	[STATUS_ID] varchar(8000) NULL, 
	[STATUS] varchar(8000) NULL
);


GO
ALTER TABLE [dbo].[dim_status] ADD CONSTRAINT UQ_9027bd64_a25a_41f6_b062_72b9a0a2ed41 unique NONCLUSTERED ([STATUS_ID]);