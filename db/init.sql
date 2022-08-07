CREATE TABLE IF NOT EXISTS  "public.Users" (
	"Id" serial NOT NULL,
	"Username" varchar(64) NOT NULL UNIQUE,
	"Email" varchar(64) NOT NULL UNIQUE,
	"Description" varchar(255),
	"JoiningDate" DATE NOT NULL,
	CONSTRAINT "Users_pk" PRIMARY KEY ("Id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE IF NOT EXISTS  "public.Wallets" (
	"Id" serial NOT NULL,
	"UserId" integer NOT NULL,
	"Name" varchar(64) NOT NULL,
	CONSTRAINT "Wallets_pk" PRIMARY KEY ("Id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE IF NOT EXISTS  "public.Settings" (
	"Id" serial NOT NULL,
	"UserId" integer NOT NULL UNIQUE,
	"BaseCurrency" varchar(16) NOT NULL DEFAULT 'USD',
	CONSTRAINT "Settings_pk" PRIMARY KEY ("Id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE IF NOT EXISTS  "public.Transactions" (
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




ALTER TABLE "Wallets" ADD CONSTRAINT "Wallets_fk0" FOREIGN KEY ("UserId") REFERENCES "Users"("Id");

ALTER TABLE "Settings" ADD CONSTRAINT "Settings_fk0" FOREIGN KEY ("UserId") REFERENCES "Users"("Id");

ALTER TABLE "Transactions" ADD CONSTRAINT "Transactions_fk0" FOREIGN KEY ("WalletId") REFERENCES "Wallets"("Id");