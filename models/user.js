CREATE TABLE [dbo].[USERS](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[created_at] [datetime] NOT NULL,
	[updated_at] [datetime] NOT NULL,
	[last_name] [varchar](100) NOT NULL,
	[middle_name] [varchar](100) NULL,
	[first_name] [varchar](100) NOT NULL,
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]