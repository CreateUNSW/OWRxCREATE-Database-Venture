from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    ForeignKey,
    TIMESTAMP,
    Enum,
)
from sqlalchemy.sql.expression import false
from sqlalchemy.sql.schema import CheckConstraint

from sqlalchemy.dialects.postgresql import MONEY

import enum

from .database import Base

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
    checked_out = 2
    returned = 3


class ApprovalStatus(enum.Enum):
    pending_approval = 1
    approved = 2
    not_approved = 3


class Person(Base):
    __tablename__ = "person"
    zid = Column(
        String(7),
        CheckConstraint("zid ~* '^[1-9][0-9]{6}$'"),
        primary_key=True,
        unique=True,
    )
    password = Column(String(12), nullable=False)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30))
    email = Column(
        String(50),
        CheckConstraint("email ~* '^[A-Za-z0-9]+[\._]?[A-Za-z0-9]+[@]\w+[.]\w{2,3}$'"),
        nullable=False,
    )
    phone = Column(String(10), CheckConstraint("phone ~* '[0-9]{10}'"))
    picture = Column(Text)
    role = Column(Enum(RoleType), nullable=False)


class Location(Base):
    __tablename__ = "location"
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    description = Column(Text)
    picture = Column(Text)


class Item(Base):
    __tablename__ = "item"
    sku = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    image = Column(Text)
    description = Column(Text)


class ItemAt(Base):
    __tablename__ = "item_at"
    sku = Column(Integer, ForeignKey("item.sku"), primary_key=True)
    location_id = Column(Integer, ForeignKey("location.id"), primary_key=True)
    qty = Column(Integer, CheckConstraint("Qty >= 0"))


class Tag(Base):
    __tablename__ = "tag"
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    description = Column(Text)
    colour = Column(Enum(ColourType))


class ItemTags(Base):
    __tablename__ = "item_tags"
    sku = Column(Integer, ForeignKey("item.sku"), primary_key=True)
    tag_id = Column(Integer, ForeignKey("tag.id"), primary_key=True)


class Approval(Base):
    __tablename__ = "approval"
    id = Column(Integer, primary_key=True)
    status = Column(Enum(ApprovalStatus))
    approved_on = Column(TIMESTAMP, nullable=False)
    approved_by = Column(String(7), ForeignKey("person.zid"), nullable=False)
    notes = Column(Text)


class Checkout(Base):
    __tablename__ = "checkout"
    id = Column(Integer, primary_key=True)
    type = Column(Enum(CheckoutType))
    requested_by = Column(String(7), ForeignKey("person.zid"), nullable=False)
    reason = Column(Text)
    status = Column(Enum(CheckoutStatus))
    lodged_on = Column(TIMESTAMP, nullable=False)
    checkedout_on = Column(TIMESTAMP, nullable=False)
    returned_on = Column(TIMESTAMP)


class CheckoutSummary(Base):
    __tablename__ = "checkout_summary"
    checkout_id = Column(Integer, ForeignKey("checkout.id"), primary_key=True)
    sku = Column(Integer, ForeignKey("item.sku"), primary_key=True)
    qty = Column(Integer, CheckConstraint("qty >= 1"))


class checkout_approval(Base):
    __tablename__ = "checkout_approval"
    checkout_id = Column(Integer, ForeignKey("checkout.id"), primary_key=True)
    approval_id = Column(Integer, ForeignKey("approval.id"), primary_key=True)


class Orders(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    lodged_by = Column(String(7), ForeignKey("person.zid"), nullable=False)
    lodged_on = Column(TIMESTAMP, nullable=False)
    description = Column(Text)
    approved_on = Column(TIMESTAMP)
    purchased_on = Column(TIMESTAMP)


class OrderSummary(Base):
    __tablename__ = "order_summary"
    order_id = Column(Integer, ForeignKey("orders.id"), primary_key=True)
    sku = Column(Integer, ForeignKey("item.sku"), primary_key=True)
    qty = Column(Integer, CheckConstraint("qty >= 1"), nullable=False)
    unit_price = Column(MONEY, CheckConstraint("unit_price >= CAST('0' as MONEY)"))
    documentation = Column(Text)


class OrderApproval(Base):
    __tablename__ = "order_approval"
    order_id = Column(Integer, ForeignKey("orders.id"), primary_key=True)
    approval_id = Column(Integer, ForeignKey("approval.id"), primary_key=True)
