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
    Email       varchar(50) CHECK (Email ~ '^[A-Za-z0-9]+[\._]?[A-Za-z0-9]+[@]\w+[.]\w{2,3}$') NOT NULL,
    Phone       varchar(10) CHECK (Phone ~ '[0-9]{10}'),
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

CREATE TABLE ItemAt (
    SKU          integer,
    Qty          integer CHECK (Qty >= 0),
    LocationID       integer,
    PRIMARY KEY (SKU, LocationID),
    FOREIGN KEY SKU REFERENCES Item(SKU),
    FOREIGN KEY LocationID REFERENCES Location(LocationID),
);

CREATE TABLE ItemTags (
    SKU          integer,
    Tag          integer,
    PRIMARY KEY (SKU, Tag),
    FOREIGN KEY SKU REFERENCES Item(SKU),
    FOREIGN KEY Tag REFERENCES Tag(TagID),
);

CREATE TABLE Approval (
    ApprovalID   serial,
    Status       ApprovalStatus NOT NULL,
    Notes        text,
    PRIMARY KEY (ApprovalID),
);

CREATE TABLE ApprovedBy (
    ApprovalID   integer,
    PersonID     integer, 
    ApprovedOn   timestamp,
    PRIMARY KEY (ApprovalID, PersonID),
    FOREIGN KEY (ApprovalID) REFERENCES Approval(ApprovalID),
    FOREIGN KEY (PersonID) REFERENCES Person(zID) 
);

CREATE TABLE Checkout (
    CheckoutID   serial,
    Type         CheckoutType NOT NULL,
    RequstedBy   integer NOT NULL,
    Reason       text,
    Status       CheckoutStatus NOT NULL,
    LodgedOn     timestamp NOT NULL,
    PRIMARY KEY (CheckoutID),
    FOREIGN KEY (RequestedBy) REFERENCES Person(zID)
);

CREATE TABLE BorrowPeriod (
    CheckoutID   integer,
    BorrowPeriodStart timestamp NOT NULL,
    BorrowPeriodEnd timestamp,
    PRIMARY KEY (CheckoutID),
    FOREIGN KEY (CheckoutID) REFERENCES Checkout(CheckoutID)
);

CREATE TABLE CheckoutSummary (
    CheckoutID   integer,
    SKU          integer,
    Qty          integer CHECK (Qty >= 1),
    PRIMARY KEY (CheckoutID, SKU),
    FOREIGN KEY (CheckoutID) REFERENCES Checkout(CheckoutID),
    FOREIGN KEY (SKU) REFERENCES Item(SKU)
);

CREATE TABLE CheckoutApprovals (
    CheckoutID   integer,
    ApprovalID   integer,
    PRIMARY KEY (CheckoutID, ApprovalID),
    FOREIGN KEY (CheckoutID) REFERENCES Checkout(CheckoutID),
    FOREIGN KEY (ApprovalID) REFERENCES Approval(ApprovalID)
);



