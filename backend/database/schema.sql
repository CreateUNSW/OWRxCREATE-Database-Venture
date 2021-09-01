create type RoleType as enum ('Admin', 'Member');
create type ColourType as enum ('Red', 'Orange', 'Yellow', 'Blue', 'Green', 'Grey', 'Brown', 'Purple', 'Pink');
create type CheckoutType as enum ('Borrow', 'Use');
create type CheckoutStatus as enum ('Waiting', 'CheckedOut', 'Returned');
create type ApprovalStatus as enum ('PendingApproval', 'Approved', 'NotApproved');


CREATE TABLE Person (
    zID         integer check (zID ~ '^[1-9][0-9]{6}$'),
    password    varchar(12) NOT NULL,
    FirstName   varchar(30) NOT NULL,
    LastName    varchar(30),
    Email       varchar(50) check (Email ~ '^[A-Za-z0-9]+[\._]?[A-Za-z0-9]+[@]\w+[.]\w{2,3}$') NOT NULL,
    Phone       varchar(10) check (Phone ~ '[0-9]{10}'),
    Picture     text,
    Role        RoleType NOT NULL,
    PRIMARY KEY (zID)
);

CREATE TABLE Location (
    LocationID  serial,
    Name        varchar(20) NOT NULL,
    Description text,
    Picture     text,
    PRIMARY KEY (LocationID)
);

CREATE TABLE Tag (
    TagID       serial,
    Name        varchar(20) NOT NULL,
    Description text,
    Colour      ColourType,
    PRIMARY KEY (TagID)
);

CREATE TABLE Item (
    SKU          serial,
    name         varchar(50) NOT NULL,
    Image        text,
    Description  text,
    PRIMARY KEY (SKU)
);

CREATE TABLE Location (
    LocationID   serial,
    Name         varchar(20) NOT NULL,
    Description  text,
    Picture      text,
    PRIMARY KEY (LocationID),
);

CREATE TABLE ItemAt (
    Item         integer NOT NULL,
    Qty          integer NOT NULL,
    Location     integer NOT NULL,
    FOREIGN KEY Item REFERENCES Item(SKU),
    FOREIGN KEY Location REFERENCES Location(Location),
);

CREATE TABLE ItemTags (
    Item         integer NOT NULL,
    Tag          integer NOT NULL,
    FOREIGN KEY Item REFERENCES Item(SKU),
    FOREIGN KEY Tag REFERENCES Tag(TagID),
);

CREATE TABLE Approval (
    ApprovalID   serial,
    ApproveBy    integer NOT NULL,
    ApprovedOn   timestamp,
    Status       ApprovalStatus NOT NULL,
    Notes        text,
    PRIMARY KEY (ApprovalID),
    FOREIGN KEY (ApproveBy) REFERENCES Person(zID)
);

CREATE TABLE Checkout (
    CheckoutID   serial,
    Type         CheckoutType NOT NULL,
    SKU          integer[] NOT NULL,
    Qty          integer[] NOT NULL,
    RequstedBy   integer NOT NULL,
    Reason       text,
    Status       CheckoutStatus NOT NULL
);



