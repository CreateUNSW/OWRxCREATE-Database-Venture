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
    id          serial,
    Name        varchar(20) NOT NULL,
    Description text,
    Picture     text,
    PRIMARY KEY (id)
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
    LocationID   integer,
    Qty          integer CHECK (Qty >= 0),
    PRIMARY KEY (SKU, LocationID),
    FOREIGN KEY SKU REFERENCES Item(SKU),
    FOREIGN KEY LocationID REFERENCES Location(id),
);

CREATE TABLE Tag (
    id          serial,
    Name        varchar(20) NOT NULL,
    Description text,
    Colour      ColourType,
    PRIMARY KEY (id)
);

CREATE TABLE ItemTags (
    SKU          integer,
    TagID        integer,
    PRIMARY KEY (SKU, Tag),
    FOREIGN KEY SKU REFERENCES Item(SKU),
    FOREIGN KEY Tag REFERENCES Tag(id),
);

CREATE TABLE Approval (
    id           serial,
    Status       ApprovalStatus NOT NULL,
    ApprovedOn   timestamp,
    ApprovedBy   integer,
    Notes        text,
    PRIMARY KEY (id),
    FOREIGN KEY (ApprovedBy) REFERENCES Person(zID) 
);

CREATE TABLE Checkout (
    id           serial,
    Type         CheckoutType NOT NULL,
    RequstedBy   integer NOT NULL,
    Reason       text,
    Status       CheckoutStatus NOT NULL,
    LodgedOn     timestamp NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (RequestedBy) REFERENCES Person(zID)
);

CREATE TABLE BorrowPeriod (
    CheckoutID   integer,
    PeriodStart  timestamp NOT NULL,
    PeriodEnd    timestamp,
    PRIMARY KEY (CheckoutID),
    FOREIGN KEY (CheckoutID) REFERENCES Checkout(id)
);

CREATE TABLE CheckoutSummary (
    CheckoutID   integer,
    SKU          integer,
    Qty          integer CHECK (Qty >= 1),
    PRIMARY KEY (CheckoutID, SKU),
    FOREIGN KEY (CheckoutID) REFERENCES Checkout(id),
    FOREIGN KEY (SKU) REFERENCES Item(SKU)
);

CREATE TABLE CheckoutApprovals (
    CheckoutID   integer,
    ApprovalID   integer,
    PRIMARY KEY (CheckoutID, ApprovalID),
    FOREIGN KEY (CheckoutID) REFERENCES Checkout(id),
    FOREIGN KEY (ApprovalID) REFERENCES Approval(id)
);

CREATE TABLE Orders (
    id           serial,
    LodgedBy     integer NOT NULL,
    LodgedOn     timestamp NOT NULL,
    Description  text,
    FinalApprovalOn datetime,
    PurchasedOn  datetime,
    PRIMARY KEY (id),
    FOREIGN KEY (LodgedBy) REFERENCES Person(zID)
);

CREATE TABLE OrderSummary (
    OrderID      integer,
    SKU          integer,
    Qty          integer CHECK (Qty >= 1),
    UnitPrice    float CHECK (UnitPrice >= 0),
    Documentation text,
    PRIMARY KEY (OrderID, SKU),
    FOREIGN KEY (OrderID) REFERENCES Orders(id),
    FOREIGN KEY (SKU) REFERENCES Item(SKU)
);

CREATE TABLE OrderApprovals (
    OrderID      integer,
    ApprovalID   integer,
    PRIMARY KEY (OrderID, ApprovalID),
    FOREIGN KEY (OrderID) REFERENCES Orders(id),
    FOREIGN KEY (ApprovalID) REFERENCES Approval(id)
);

