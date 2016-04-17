CREATE TABLE field (
    id_field	INTEGER			PRIMARY KEY		ASC AUTOINCREMENT	NOT NULL,
    field_name	VARCHAR(30)		UNIQUE          NOT NULL
 );

CREATE TABLE event_register (
    id_event_reg	INTEGER		PRIMARY KEY		ASC AUTOINCREMENT	NOT NULL,
    date_created	DATETIME	NOT NULL
);

CREATE TABLE event (
    id_event 		INTEGER		PRIMARY KEY		ASC AUTOINCREMENT	NOT NULL,
    id_event_reg	INTEGER		NOT NULL,
    id_field		INTEGER		NOT NULL,
    value_field		INTEGER		NULL,
    FOREIGN KEY (id_event_reg)	REFERENCES event_register (id_event_reg),
    FOREIGN KEY (id_field)		REFERENCES field (id_field)
);