create type role_type as enum ('Admin', 'Member');
create type colour_type as enum ('Red', 'Orange', 'Yellow', 'Blue', 'Green', 'Grey', 'Brown', 'Purple', 'Pink');
create type checkout_type as enum ('Borrow', 'Use');
create type checkout_status as enum ('Waiting', 'CheckedOut', 'Returned');
create type approval_status as enum ('PendingApproval', 'Approved', 'NotApproved');

-- Need to cast zid as text so regex match can work
CREATE TABLE Person (
    zid             integer PRIMARY KEY,
    password        varchar(12) NOT NULL,
    first_name      varchar(30) NOT NULL,
    last_name       varchar(30),
    email           varchar(50) NOT NULL,
    phone_no        varchar(10),
    picture         text,
    role            role_type NOT NULL,
    CONSTRAINT CK_zid CHECK (CAST(zid as text) ~* '^[1-9][0-9]{6}$'),
    CONSTRAINT CK_email CHECK (email ~* '^[A-Za-z0-9]+[\._]?[A-Za-z0-9]+[@]\w+[.]\w{2,3}$'),
    CONSTRAINT CK_phone CHECK (phone_no ~* '[0-9]{10}')
);

CREATE TABLE Location (
    id              serial PRIMARY KEY,
    name            varchar(20) NOT NULL,
    description     text,
    picture         text
);

CREATE TABLE Item (
    sku             serial PRIMARY KEY,
    name            varchar(50) NOT NULL,
    image           text,
    description     text
);

CREATE TABLE item_at (
    sku             integer REFERENCES Item(sku),
    location_id     integer REFERENCES Location(id),
    qty             integer CHECK (qty >= 0),
    PRIMARY KEY (sku, location_id)
);

CREATE TABLE Tag (
    id              serial PRIMARY KEY,
    name            varchar(20) NOT NULL,
    description     text,
    colour          colour_type
);

CREATE TABLE item_tags (
    sku             integer REFERENCES Item(sku),
    tag_id          integer REFERENCES Tag(id),
    PRIMARY KEY (sku, tag_id)
);

CREATE TABLE Approval (
    id              serial PRIMARY KEY,
    Status          approval_status NOT NULL,
    approved_on     timestamp,
    approved_by     integer REFERENCES Person(zid) NOT NULL,
    Notes           text
);

CREATE TABLE Checkout (
    id              serial PRIMARY KEY, 
    type            checkout_type NOT NULL,
    requested_by    integer REFERENCES Person(zid) NOT NULL,
    reason          text,
    status          checkout_status NOT NULL,
    lodged_on       timestamp NOT NULL,
    checkedout_on   timestamp NOT NULL,
    returned_on     timestamp     
);

CREATE TABLE checkout_summary (
    checkout_id     integer REFERENCES Checkout(id),
    sku             integer REFERENCES Item(sku),
    qty             integer CHECK (qty >= 1),
    PRIMARY KEY (checkout_id, sku)
);

CREATE TABLE checkout_approvals (
    checkout_id     integer REFERENCES Checkout(id),
    ApprovalId      integer REFERENCES Approval(id),
    PRIMARY KEY (checkout_id, ApprovalId)
);

CREATE TABLE orders (
    id              serial PRIMARY KEY,
    lodged_by       integer REFERENCES Person(zid) NOT NULL,
    lodged_on       timestamp NOT NULL,
    description     text,
    approvaled_on   timestamp,
    purchased_on    timestamp
);

CREATE TABLE order_summary (
    order_id        integer REFERENCES orders(id),
    sku             integer REFERENCES Item(sku),
    qty             integer CHECK (qty >= 1) NOT NULL,
    unit_price      money NOT NULL,
    documentation   text,
    PRIMARY KEY (order_id, sku)
);

CREATE TABLE order_approvals (
    order_id        integer REFERENCES orders(id),
    ApprovalId      integer REFERENCES Approval(id),
    PRIMARY KEY (order_id, ApprovalId)
);

