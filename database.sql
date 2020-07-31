CREATE TABLE IF NOT EXISTS accounts (
	id integer PRIMARY KEY AUTOINCREMENT,
	website_name text NOT NULL,
    user_account text,
	user_password text,
	pass_key text
);