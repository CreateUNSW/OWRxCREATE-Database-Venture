from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    ForeignKey,
    TIMESTAMP,
    DATETIME,
    Float,
    Enum,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import CheckConstraint

import enum

Base = declarative_base

# Enum's
class RoleType(enum.Enum):
    admin = 1
    member = 2


class ColourType(enum.Enum):
    red = 1
    orange = 2
    yellow = 3
    blue = 4
    green = 5
    grey = 6
    brown = 7
    purple = 8
    pink = 9


class CheckoutType(enum.Enum):
    borrow = 1
    use = 2


class CheckoutStatus(enum.Enum):
    waiting = 1
    checkedOut = 2
    returned = 3


class ApprovalStatus(enum.Enum):
    pendingApproval = 1
    approved = 2
    notApproved = 3


class Person(Base):
    __tablename__ = "Person"
    zID = Column(
        String(7),
        CheckConstraint("zID ~ '^[1-9][0-9]{6}$'"),
        primary_key=True,
        unique=True,
    )
    password = Column(String(12), nullable=False)
    FirstName = Column(String(30), nullable=False)
    LastName = Column(String(30))
    Email = Column(String(50), nullable=False)
    Phone = Column(String(10), CheckConstraint("Phone ~ '[0-9]{10}'"))
    Picture = Column(Text)
    Role = Column(Enum(RoleType))


class Location(Base):
    __tablename__ = "Location"
    id = Column(Integer, primary_key=True)
    Name = Column(String(20), nullable=False)
    Description = Column(Text)
    Picture = Column(Text)


class Item(Base):
    __tablename__ = "Item"
    SKU = Column(Integer, primary_key=True)
    Name = Column(String(50), nullable=False)
    Image = Column(Text)
    Description = Column(Text)


class ItemAt(Base):
    __tablename__ = "ItemAt"
    SKU = Column(Integer, ForeignKey("Item.SKU"), primary_key=True)
    LocationID = Column(Integer, ForeignKey("Location.id"), primary_key=True)
    Qty = Column(Integer, CheckConstraint("Qty >= 1"))


class Tag(Base):
    __tablename__ = "Tag"
    id = Column(Integer, primary_key=True)
    Name = Column(String(20), nullable=False)
    Description = Column(Text)
    Colour = Column(Enum(ColourType))


class ItemTags(Base):
    __tablename__ = "ItemTags"
    SKU = Column(Integer, ForeignKey("Item.SKU"), primary_key=True)
    TagID = Column(Integer, ForeignKey("Tag.id"), primary_key=True)


class Approval(Base):
    __tablename__ = "Approval"
    id = Column(Integer, primary_key=True)
    Status = Column(Enum(ApprovalStatus))
    ApprovedOn = Column(TIMESTAMP, nullable=False)
    ApprovedBy = Column(Integer, ForeignKey("Person.zID"), nullable=False)
    Notes = Column(Text)


class Checkout(Base):
    __tablename__ = "Checkout"
    id = Column(Integer, primary_key=True)
    Type = Column(Enum(CheckoutType))
    RequestedBy = Column(Integer, ForeignKey("Person.zID"), nullable=False)
    Reason = Column(Text)
    Status = Column(Enum(CheckoutStatus))
    LodgedOn = Column(TIMESTAMP, nullable=False)


class BorrowPeriod(Base):
    __tablename__ = "BorrowPeriod"
    CheckoutID = Column(Integer, ForeignKey("Checkout.id"), primary_key=True)
    PeriodStart = Column(TIMESTAMP, nullable=False)
    PeriodEnd = Column(TIMESTAMP)


class CheckoutSummary(Base):
    __tablename__ = "CheckoutSummary"
    CheckoutID = Column(Integer, ForeignKey("Checkout.id"), primary_key=True)
    SKU = Column(Integer, ForeignKey("Item.SKU"), primary_key=True)
    Qty = Column(Integer, CheckConstraint("Qty >= 1"))


class CheckoutApprovals(Base):
    __tablename__ = "CheckoutApprovals"
    CheckoutID = Column(Integer, ForeignKey("Checkout.id"), primary_key=True)
    ApprovalID = Column(Integer, ForeignKey("Approval.id"), primary_key=True)


class Orders(Base):
    __tablename__ = "Orders"
    id = Column(Integer, primary_key=True)
    LodgedBy = Column(Integer, ForeignKey("Person.zID"), nullable=False)
    LodgedOn = Column(TIMESTAMP, nullable=False)
    Description = Column(Text)
    FinalApprovalOn = Column(DATETIME)
    PurchasedOn = Column(DATETIME)


class OrderSummary(Base):
    __tablename__ = "OrderSummary"
    OrderID = Column(Integer, ForeignKey("Orders.id"), primary_key=True)
    SKU = Column(Integer, ForeignKey("Item.SKU"), primary_key=True)
    Qty = Column(Integer, CheckConstraint("Qty >= 1"))
    UnitPrice = Column(Float, CheckConstraint("UnitPrice >= 0"))
    Documentation = Column(Text)


class OrderApprovals(Base):
    __tablename__ = "OrderApprovals"
    OrderID = Column(Integer, ForeignKey("Order.id"), primary_key=True)
    ApprovalID = Column(Integer, ForeignKey("Approval.id"), primary_key=True)
