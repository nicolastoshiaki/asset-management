CREATE TABLE AM_USER (
	LOGIN_USER				VARCHAR(40)			NULL	,
	PASSWORD_USER			VARCHAR(20)			NULL	,
	USERNAME				VARCHAR(40)			NULL	,
	DT_LAST_lOG				DATETIME			NULL	,		
	ID_USER					INT					NOT NULL IDENTITY(1,1) PRIMARY KEY
)


CREATE TABLE AM_PROD_TYPE (
	DES_TYPE				VARCHAR(256)		NULL	,
	DES_TYPE_SHORT			CHAR(3)				NULL	,
	ID_TYPE					INT					NOT NULL IDENTITY(1,1) PRIMARY KEY
)


CREATE TABLE AM_PRODUCTS(
	PRODUCT_NAME			VARCHAR(256)		NULL	,
	ID_TYPE					INT					NULL	,
	ID_PRODUCT				INT					NOT NULL IDENTITY(1,1) PRIMARY KEY
    CONSTRAINT FK_PROD_TYPE_IDENT FOREIGN KEY (ID_TYPE) references AM_PROD_TYPE (ID_TYPE),
)


CREATE TABLE AM_INVEST_PORT (
	ID_USER					INT					NULL	,
	ID_PRODUCT				INT					NULL	,
	PRODUCT_QUANTITY		INT					NULL	,
	ID_INVEST_PORT			INT					NOT NULL IDENTITY(1,1) PRIMARY KEY,
    CONSTRAINT FK_USER_IDENT foreign key (ID_USER) references AM_USER (ID_USER),
    CONSTRAINT FK_PROD_IDENT foreign key (ID_PRODUCT) references AM_PRODUCTS (ID_PRODUCT)
)