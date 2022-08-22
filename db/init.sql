CREATE TABLE IF NOT EXISTS  "Users" (
	"Id" varchar(255) NOT NULL,
	"Username" varchar(63) NOT NULL UNIQUE,
	"Password" varchar(511) NOT NULL,
	"Email" varchar(63) NOT NULL UNIQUE,
	"Description" varchar(255),
	"Image" varchar(255),
	"CreatedAt" DATE NOT NULL,
	"UpdatedAt" DATE,
	"LastUpdatedBy" varchar(63),
	CONSTRAINT "Users_pk" PRIMARY KEY ("Id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE IF NOT EXISTS  "Wallets" (
	"Id" varchar(255) NOT NULL,
	"UserId" varchar(255) NOT NULL,
	"Name" varchar(63) NOT NULL,
	"State" json,
	"WrongTransaction" json,
	"LastCompilation" DATE,
	"CreatedAt" DATE NOT NULL,
	"UpdatedAt" DATE,
	"LastUpdatedBy" varchar(63),
	CONSTRAINT "Wallets_pk" PRIMARY KEY ("Id")
) WITH (
  OIDS=FALSE
);



--CREATE TABLE IF NOT EXISTS  "Settings" (
--	"Id" varchar(255) NOT NULL,
--	"UserId" varchar(255) NOT NULL UNIQUE,
--	"BaseCurrency" varchar(16) NOT NULL DEFAULT 'USD',
--	CONSTRAINT "Settings_pk" PRIMARY KEY ("Id")
--) WITH (
--  OIDS=FALSE
--);



CREATE TABLE IF NOT EXISTS  "Transactions" (
	"Id" varchar(255) NOT NULL,
	"WalletId" varchar(255) NOT NULL,
	"Type" varchar(31) NOT NULL DEFAULT 'Add',
	"BuyAmount" FLOAT,
	"BuyCur" varchar(15),
	"SellAmount" FLOAT,
	"SellCur" varchar(15),
	"CommissionAmount" FLOAT,
	"CommissionCur" varchar(15),
	"Description" varchar(255),
	"Date" DATE NOT NULL,
	"CreatedAt" DATE NOT NULL,
	"UpdatedAt" DATE,
	"LastUpdatedBy" varchar(63),
	CONSTRAINT "Transactions_pk" PRIMARY KEY ("Id")
) WITH (
  OIDS=FALSE
);


ALTER TABLE "Wallets" ADD CONSTRAINT "Wallets_fk0" FOREIGN KEY ("UserId") REFERENCES "Users"("Id");

ALTER TABLE "Transactions" ADD CONSTRAINT "Transactions_fk0" FOREIGN KEY ("WalletId") REFERENCES "Wallets"("Id");
