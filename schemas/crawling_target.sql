CREATE TABLE IF NOT EXISTS crawling_target (
	id INT UNSIGNED auto_increment NOT NULL,
	target_url VARCHAR(500) NULL,
	CONSTRAINT crawling_target_pk PRIMARY KEY (id)
);

ALTER TABLE crawled_links ADD CONSTRAINT crawled_links_unique UNIQUE KEY (url);