-- Creating tables for Migration-FlowDB

CREATE TABLE States(
	state_no int NOT NULL,
	region_no int NOT NULL,
	population_1YR_ago float NOT NULL,
	different_state_1YR_ago float NOT NULL,
	PRIMARY KEY(state_no),
	-- UNIQUE(region_no)
);
DROP TABLE State CASCADE;
SELECT * FROM States

CREATE TABLE Region(
	region_no int NOT NULL,
	region_name varchar(20) NOT NULL,
	PRIMARY KEY(region_no),
	FOREIGN KEY(region_no) REFERENCES State(region_no)
);

SELECT * FROM Region

CREATE TABLE Housing_and_Income(
	state_no int NOT NULL,
	median_income float NOT NULL,
	median_housing_cost float NOT Null,
	median_home_value float NOT NULL,
	median_RE_taxes float NOT NULL,
	PRIMARY KEY(state_no),
	--FOREIGN KEY(state_no) REFERENCES State(state_no)
);
SELECT * FROM Housing_and_Income

CREATE TABLE CA_Migration_2Other_States(
	state_no int NOT NULL,
	state_name varchar NOT NULL,
	total_from_CA float NOT NULL,
	PRIMARY KEY(state_no)
); 
SELECT * FROM CA_Migration_2Other_States