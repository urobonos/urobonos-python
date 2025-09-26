CREATE TABLE crawling_target (
	id INT UNSIGNED auto_increment NOT NULL,
	target_url VARCHAR(500) NULL,
	CONSTRAINT crawling_target_pk PRIMARY KEY (id)
);