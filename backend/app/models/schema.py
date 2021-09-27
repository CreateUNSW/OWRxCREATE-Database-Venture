from typing import Optional

from pydantic import (
    BaseModel,
    constr,
    PositiveInt,
    NonNegativeInt,
    Json
)
from sqlalchemy.sql.sqltypes import JSON

from . import models

import datetime

#################################################################################
# Hide password
class Person(BaseModel):
    zid: constr(min_length=8, max_length=8)
    first_name: str
    last_name: str
    email: str
    phone: str
    picture: str

class RegisterRequest(BaseModel):
    zid: constr(min_length=8, max_length=8)
    password: str
    first_name: constr(min_length=1)
    last_name: str
    email: constr(regex=r'''(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])''')
    phone: constr(regex=r'[0-9]{10}')
    picture: Optional[str]
    role: Optional[models.RoleType]

class PersonCredentials(BaseModel):
    zid: constr(min_length=8, max_length=8)
    password: str

class LoginRequest(BaseModel):
    zid: constr(min_length=8, max_length=8)
    password: str

class LoginResponse(BaseModel):
    success: bool
    token: str

#################################################################################

class Location(BaseModel):
    id: PositiveInt
    name: constr(min_length=1)
    description: Optional[str]
    picutre: Optional[str]

class Item(BaseModel):
    sku: PositiveInt
    name: constr(min_length=1)
    image: Optional[str]
    description: Optional[str]

class ItemAt(BaseModel):
    sku: PositiveInt
    location_id: int
    qty: int

class Tag(BaseModel):
    id: PositiveInt
    name: constr(min_length=1)
    description: Optional[str]
    colour: Optional[str]

class ItemTags(BaseModel):
    sku: PositiveInt
    tag_id: PositiveInt

#################################################################################

class Approval(BaseModel):
    id: PositiveInt
    status: models.ApprovalStatus
    approved_on: datetime.datetime
    approved_by: constr(min_length=8, max_length=8) # zid
    notes: Optional[str]

class Checkout(BaseModel):
    id: PositiveInt
    type: models.CheckoutType
    requested_by: constr(min_length=8, max_length=8) # zid
    reason: Optional[str]
    status: models.CheckoutStatus
    lodged_on: datetime.datetime
    checkedout_on: datetime.datetime
    returned_on: Optional[datetime.datetime]

class CheckoutSummary(BaseModel):
    checkout_id: PositiveInt
    sku: PositiveInt
    qty: PositiveInt

class CheckoutApproval(BaseModel):
    checkout_id: PositiveInt
    approval_id: PositiveInt

#################################################################################

class Orders(BaseModel):
    id: PositiveInt
    lodged_by: constr(min_length=8, max_length=8) # zid
    lodged_on: datetime.datetime
    description: Optional[str]
    approved_on: datetime.datetime
    purchased_on: datetime.datetime

class OrderSummary(BaseModel):
    order_id: PositiveInt
    sku: PositiveInt
    qty: PositiveInt
    unit_price: NonNegativeInt
    documentation: Optional[str]

class OrderApproval(BaseModel):
    order_id: PositiveInt
    approval_id: PositiveInt

#################################################################################