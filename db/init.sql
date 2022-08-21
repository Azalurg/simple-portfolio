CREATE TABLE IF NOT EXISTS  "Users" (
	"Id" serial NOT NULL,
	"PublicId" varchar(255) NOT NULL UNIQUE,
	"Username" varchar(64) NOT NULL UNIQUE,
	"Password" varchar(255) NOT NULL,
	"Email" varchar(64) NOT NULL UNIQUE,
	"Description" varchar(255),
	"CreatedAt" DATE NOT NULL,
	"UpdatedAt" DATE,
	"LastUpdatedBy" varchar(64),
	CONSTRAINT "Users_pk" PRIMARY KEY ("Id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE IF NOT EXISTS  "Wallets" (
	"Id" serial NOT NULL,
	"UserId" integer NOT NULL,
	"Name" varchar(64) NOT NULL,
	CONSTRAINT "Wallets_pk" PRIMARY KEY ("Id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE IF NOT EXISTS  "Settings" (
	"Id" serial NOT NULL,
	"UserId" integer NOT NULL UNIQUE,
	"BaseCurrency" varchar(16) NOT NULL DEFAULT 'USD',
	CONSTRAINT "Settings_pk" PRIMARY KEY ("Id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE IF NOT EXISTS  "Transactions" (
	"Id" serial NOT NULL,
	"WalletId" integer NOT NULL,
	"Type" varchar(32) NOT NULL DEFAULT 'Add',
	"BuyAmount" FLOAT,
	"BuyCur" varchar(16),
	"SellAmount" FLOAT,
	"SellCur" varchar(16),
	"CommissionAmount" FLOAT,
	"CommissionCur" varchar(16),
	"Description" varchar(255),
	"Date" DATE NOT NULL,
	CONSTRAINT "Transactions_pk" PRIMARY KEY ("Id")
) WITH (
  OIDS=FALSE
);

CREATE TABLE IF NOT EXISTS  "Summary" (
	"Id" serial NOT NULL,
	"WalletId" integer NOT NULL UNIQUE,
	"Summary" json NOT NULL,
	CONSTRAINT "Summary_pk" PRIMARY KEY ("Id")
) WITH (
  OIDS=FALSE
);

ALTER TABLE "Wallets" ADD CONSTRAINT "Wallets_fk0" FOREIGN KEY ("UserId") REFERENCES "Users"("Id");

ALTER TABLE "Settings" ADD CONSTRAINT "Settings_fk0" FOREIGN KEY ("UserId") REFERENCES "Users"("Id");

ALTER TABLE "Transactions" ADD CONSTRAINT "Transactions_fk0" FOREIGN KEY ("WalletId") REFERENCES "Wallets"("Id");

ALTER TABLE "Summary" ADD CONSTRAINT "Summary_fk0" FOREIGN KEY ("WalletId") REFERENCES "Wallets"("Id");