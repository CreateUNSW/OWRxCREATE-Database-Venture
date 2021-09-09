create type role_type as enum ('admin', 'member');
create type colour_type as enum ('red', 'orange', 'yellow', 'blue', 'green', 'grey', 'brown', 'purple', 'pink');
create type checkout_type as enum ('borrow', 'use');
create type checkout_status as enum ('waiting', 'checked_out', 'returned');
create type approval_status as enum ('pending_approval', 'approved', 'not_approved');

CREATE TABLE person (
    zid             varchar(7) PRIMARY KEY,
    password        varchar(12) NOT NULL,
    first_name      varchar(30) NOT NULL,
    last_name       varchar(30),
    email           varchar(50) NOT NULL,
    phone           varchar(10),
    picture         text,
    role            role_type NOT NULL,
    CONSTRAINT CK_zid CHECK (zid ~* '^[1-9][0-9]{6}$'),
    CONSTRAINT CK_email CHECK (email ~* '^[A-Za-z0-9]+[\._]?[A-Za-z0-9]+[@]\w+[.]\w{2,3}$'),
    CONSTRAINT CK_phone CHECK (phone ~* '[0-9]{10}')
);

CREATE TABLE location (
    id              serial PRIMARY KEY,
    name            varchar(20) NOT NULL,
    description     text,
    picture         text
);

CREATE TABLE item (
    sku             serial PRIMARY KEY,
    name            varchar(50) NOT NULL,
    image           text,
    description     text
);

CREATE TABLE item_at (
    sku             integer REFERENCES item(sku),
    location_id     integer REFERENCES location(id),
    qty             integer CHECK (qty >= 0),
    PRIMARY KEY (sku, location_id)
);

CREATE TABLE tag (
    id              serial PRIMARY KEY,
    name            varchar(20) NOT NULL,
    description     text,
    colour          colour_type
);

CREATE TABLE item_tags (
    sku             integer REFERENCES item(sku),
    tag_id          integer REFERENCES tag(id),
    PRIMARY KEY (sku, tag_id)
);

CREATE TABLE approval (
    id              serial PRIMARY KEY,
    status          approval_status NOT NULL,
    approved_on     timestamp,
    approved_by     varchar(7) REFERENCES person(zid) NOT NULL,
    notes           text
);

CREATE TABLE checkout (
    id              serial PRIMARY KEY, 
    type            checkout_type NOT NULL,
    requested_by    varchar(7) REFERENCES person(zid) NOT NULL,
    reason          text,
    status          checkout_status NOT NULL,
    lodged_on       timestamp NOT NULL,
    checkedout_on   timestamp NOT NULL,
    returned_on     timestamp     
);

CREATE TABLE checkout_summary (
    checkout_id     integer REFERENCES checkout(id),
    sku             integer REFERENCES item(sku),
    qty             integer CHECK (qty >= 1),
    PRIMARY KEY (checkout_id, sku)
);

CREATE TABLE checkout_approval (
    checkout_id     integer REFERENCES checkout(id),
    approval_id     integer REFERENCES approval(id),
    PRIMARY KEY (checkout_id, approval_id)
);

CREATE TABLE order (
    id              serial PRIMARY KEY,
    lodged_by       varchar(7) REFERENCES person(zid) NOT NULL,
    lodged_on       timestamp NOT NULL,
    description     text,
    approvaled_on   timestamp,
    purchased_on    timestamp
);

CREATE TABLE order_summary (
    order_id        integer REFERENCES order(id),
    sku             integer REFERENCES item(sku),
    qty             integer CHECK (qty >= 1) NOT NULL,
    unit_price      money NOT NULL,
    documentation   text,
    PRIMARY KEY (order_id, sku)
);

CREATE TABLE order_approval (
    order_id        integer REFERENCES order(id),
    approval_id     integer REFERENCES approval(id),
    PRIMARY KEY (order_id, approval_id)
);

