# DO NOT EDIT! This file is automatically generated

import datetime
import enum
import typing

from commercetools.types._abstract import _BaseType
from commercetools.types._common import (
    LoggedResource,
    Reference,
    ReferenceTypeId,
    ResourceIdentifier,
)

if typing.TYPE_CHECKING:
    from ._common import CreatedBy, LastModifiedBy, LocalizedString, Money, TypedMoney
    from ._customer import CustomerReference, CustomerResourceIdentifier
    from ._state import StateReference, StateResourceIdentifier
    from ._type import (
        CustomFields,
        CustomFieldsDraft,
        FieldContainer,
        TypeResourceIdentifier,
    )
__all__ = [
    "Payment",
    "PaymentAddInterfaceInteractionAction",
    "PaymentAddTransactionAction",
    "PaymentChangeAmountPlannedAction",
    "PaymentChangeTransactionInteractionIdAction",
    "PaymentChangeTransactionStateAction",
    "PaymentChangeTransactionTimestampAction",
    "PaymentDraft",
    "PaymentMethodInfo",
    "PaymentPagedQueryResponse",
    "PaymentReference",
    "PaymentResourceIdentifier",
    "PaymentSetAmountPaidAction",
    "PaymentSetAmountRefundedAction",
    "PaymentSetAnonymousIdAction",
    "PaymentSetAuthorizationAction",
    "PaymentSetCustomFieldAction",
    "PaymentSetCustomTypeAction",
    "PaymentSetCustomerAction",
    "PaymentSetExternalIdAction",
    "PaymentSetInterfaceIdAction",
    "PaymentSetKeyAction",
    "PaymentSetMethodInfoInterfaceAction",
    "PaymentSetMethodInfoMethodAction",
    "PaymentSetMethodInfoNameAction",
    "PaymentSetStatusInterfaceCodeAction",
    "PaymentSetStatusInterfaceTextAction",
    "PaymentStatus",
    "PaymentStatusDraft",
    "PaymentTransitionStateAction",
    "PaymentUpdate",
    "PaymentUpdateAction",
    "Transaction",
    "TransactionDraft",
    "TransactionState",
    "TransactionType",
]


class Payment(LoggedResource):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.PaymentSchema`."
    #: Optional :class:`commercetools.types.CustomerReference`
    customer: typing.Optional["CustomerReference"]
    #: Optional :class:`str` `(Named` ``anonymousId`` `in Commercetools)`
    anonymous_id: typing.Optional[str]
    #: Optional :class:`str` `(Named` ``externalId`` `in Commercetools)`
    external_id: typing.Optional[str]
    #: Optional :class:`str` `(Named` ``interfaceId`` `in Commercetools)`
    interface_id: typing.Optional[str]
    #: :class:`commercetools.types.TypedMoney` `(Named` ``amountPlanned`` `in Commercetools)`
    amount_planned: typing.Optional["TypedMoney"]
    #: Optional :class:`commercetools.types.TypedMoney` `(Named` ``amountAuthorized`` `in Commercetools)`
    amount_authorized: typing.Optional["TypedMoney"]
    #: Optional :class:`str` `(Named` ``authorizedUntil`` `in Commercetools)`
    authorized_until: typing.Optional[str]
    #: Optional :class:`commercetools.types.TypedMoney` `(Named` ``amountPaid`` `in Commercetools)`
    amount_paid: typing.Optional["TypedMoney"]
    #: Optional :class:`commercetools.types.TypedMoney` `(Named` ``amountRefunded`` `in Commercetools)`
    amount_refunded: typing.Optional["TypedMoney"]
    #: :class:`commercetools.types.PaymentMethodInfo` `(Named` ``paymentMethodInfo`` `in Commercetools)`
    payment_method_info: typing.Optional["PaymentMethodInfo"]
    #: :class:`commercetools.types.PaymentStatus` `(Named` ``paymentStatus`` `in Commercetools)`
    payment_status: typing.Optional["PaymentStatus"]
    #: List of :class:`commercetools.types.Transaction`
    transactions: typing.Optional[typing.List["Transaction"]]
    #: List of :class:`commercetools.types.CustomFields` `(Named` ``interfaceInteractions`` `in Commercetools)`
    interface_interactions: typing.Optional[typing.List["CustomFields"]]
    #: Optional :class:`commercetools.types.CustomFields`
    custom: typing.Optional["CustomFields"]
    #: Optional :class:`str`
    key: typing.Optional[str]

    def __init__(
        self,
        *,
        id: typing.Optional[str] = None,
        version: typing.Optional[int] = None,
        created_at: typing.Optional[datetime.datetime] = None,
        last_modified_at: typing.Optional[datetime.datetime] = None,
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        customer: typing.Optional["CustomerReference"] = None,
        anonymous_id: typing.Optional[str] = None,
        external_id: typing.Optional[str] = None,
        interface_id: typing.Optional[str] = None,
        amount_planned: typing.Optional["TypedMoney"] = None,
        amount_authorized: typing.Optional["TypedMoney"] = None,
        authorized_until: typing.Optional[str] = None,
        amount_paid: typing.Optional["TypedMoney"] = None,
        amount_refunded: typing.Optional["TypedMoney"] = None,
        payment_method_info: typing.Optional["PaymentMethodInfo"] = None,
        payment_status: typing.Optional["PaymentStatus"] = None,
        transactions: typing.Optional[typing.List["Transaction"]] = None,
        interface_interactions: typing.Optional[typing.List["CustomFields"]] = None,
        custom: typing.Optional["CustomFields"] = None,
        key: typing.Optional[str] = None
    ) -> None:
        self.customer = customer
        self.anonymous_id = anonymous_id
        self.external_id = external_id
        self.interface_id = interface_id
        self.amount_planned = amount_planned
        self.amount_authorized = amount_authorized
        self.authorized_until = authorized_until
        self.amount_paid = amount_paid
        self.amount_refunded = amount_refunded
        self.payment_method_info = payment_method_info
        self.payment_status = payment_status
        self.transactions = transactions
        self.interface_interactions = interface_interactions
        self.custom = custom
        self.key = key
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
        )

    def __repr__(self) -> str:
        return (
            "Payment(id=%r, version=%r, created_at=%r, last_modified_at=%r, last_modified_by=%r, created_by=%r, customer=%r, anonymous_id=%r, external_id=%r, interface_id=%r, amount_planned=%r, amount_authorized=%r, authorized_until=%r, amount_paid=%r, amount_refunded=%r, payment_method_info=%r, payment_status=%r, transactions=%r, interface_interactions=%r, custom=%r, key=%r)"
            % (
                self.id,
                self.version,
                self.created_at,
                self.last_modified_at,
                self.last_modified_by,
                self.created_by,
                self.customer,
                self.anonymous_id,
                self.external_id,
                self.interface_id,
                self.amount_planned,
                self.amount_authorized,
                self.authorized_until,
                self.amount_paid,
                self.amount_refunded,
                self.payment_method_info,
                self.payment_status,
                self.transactions,
                self.interface_interactions,
                self.custom,
                self.key,
            )
        )


class PaymentDraft(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.PaymentDraftSchema`."
    #: Optional :class:`commercetools.types.CustomerResourceIdentifier`
    customer: typing.Optional["CustomerResourceIdentifier"]
    #: Optional :class:`str` `(Named` ``anonymousId`` `in Commercetools)`
    anonymous_id: typing.Optional[str]
    #: Optional :class:`str` `(Named` ``externalId`` `in Commercetools)`
    external_id: typing.Optional[str]
    #: Optional :class:`str` `(Named` ``interfaceId`` `in Commercetools)`
    interface_id: typing.Optional[str]
    #: :class:`commercetools.types.Money` `(Named` ``amountPlanned`` `in Commercetools)`
    amount_planned: typing.Optional["Money"]
    #: Optional :class:`commercetools.types.Money` `(Named` ``amountAuthorized`` `in Commercetools)`
    amount_authorized: typing.Optional["Money"]
    #: Optional :class:`str` `(Named` ``authorizedUntil`` `in Commercetools)`
    authorized_until: typing.Optional[str]
    #: Optional :class:`commercetools.types.Money` `(Named` ``amountPaid`` `in Commercetools)`
    amount_paid: typing.Optional["Money"]
    #: Optional :class:`commercetools.types.Money` `(Named` ``amountRefunded`` `in Commercetools)`
    amount_refunded: typing.Optional["Money"]
    #: Optional :class:`commercetools.types.PaymentMethodInfo` `(Named` ``paymentMethodInfo`` `in Commercetools)`
    payment_method_info: typing.Optional["PaymentMethodInfo"]
    #: Optional :class:`commercetools.types.PaymentStatusDraft` `(Named` ``paymentStatus`` `in Commercetools)`
    payment_status: typing.Optional["PaymentStatusDraft"]
    #: Optional list of :class:`commercetools.types.TransactionDraft`
    transactions: typing.Optional[typing.List["TransactionDraft"]]
    #: Optional list of :class:`commercetools.types.CustomFieldsDraft` `(Named` ``interfaceInteractions`` `in Commercetools)`
    interface_interactions: typing.Optional[typing.List["CustomFieldsDraft"]]
    #: Optional :class:`commercetools.types.CustomFieldsDraft`
    custom: typing.Optional["CustomFieldsDraft"]
    #: Optional :class:`str`
    key: typing.Optional[str]

    def __init__(
        self,
        *,
        customer: typing.Optional["CustomerResourceIdentifier"] = None,
        anonymous_id: typing.Optional[str] = None,
        external_id: typing.Optional[str] = None,
        interface_id: typing.Optional[str] = None,
        amount_planned: typing.Optional["Money"] = None,
        amount_authorized: typing.Optional["Money"] = None,
        authorized_until: typing.Optional[str] = None,
        amount_paid: typing.Optional["Money"] = None,
        amount_refunded: typing.Optional["Money"] = None,
        payment_method_info: typing.Optional["PaymentMethodInfo"] = None,
        payment_status: typing.Optional["PaymentStatusDraft"] = None,
        transactions: typing.Optional[typing.List["TransactionDraft"]] = None,
        interface_interactions: typing.Optional[
            typing.List["CustomFieldsDraft"]
        ] = None,
        custom: typing.Optional["CustomFieldsDraft"] = None,
        key: typing.Optional[str] = None
    ) -> None:
        self.customer = customer
        self.anonymous_id = anonymous_id
        self.external_id = external_id
        self.interface_id = interface_id
        self.amount_planned = amount_planned
        self.amount_authorized = amount_authorized
        self.authorized_until = authorized_until
        self.amount_paid = amount_paid
        self.amount_refunded = amount_refunded
        self.payment_method_info = payment_method_info
        self.payment_status = payment_status
        self.transactions = transactions
        self.interface_interactions = interface_interactions
        self.custom = custom
        self.key = key
        super().__init__()

    def __repr__(self) -> str:
        return (
            "PaymentDraft(customer=%r, anonymous_id=%r, external_id=%r, interface_id=%r, amount_planned=%r, amount_authorized=%r, authorized_until=%r, amount_paid=%r, amount_refunded=%r, payment_method_info=%r, payment_status=%r, transactions=%r, interface_interactions=%r, custom=%r, key=%r)"
            % (
                self.customer,
                self.anonymous_id,
                self.external_id,
                self.interface_id,
                self.amount_planned,
                self.amount_authorized,
                self.authorized_until,
                self.amount_paid,
                self.amount_refunded,
                self.payment_method_info,
                self.payment_status,
                self.transactions,
                self.interface_interactions,
                self.custom,
                self.key,
            )
        )


class PaymentMethodInfo(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.PaymentMethodInfoSchema`."
    #: Optional :class:`str` `(Named` ``paymentInterface`` `in Commercetools)`
    payment_interface: typing.Optional[str]
    #: Optional :class:`str`
    method: typing.Optional[str]
    #: Optional :class:`commercetools.types.LocalizedString`
    name: typing.Optional["LocalizedString"]

    def __init__(
        self,
        *,
        payment_interface: typing.Optional[str] = None,
        method: typing.Optional[str] = None,
        name: typing.Optional["LocalizedString"] = None
    ) -> None:
        self.payment_interface = payment_interface
        self.method = method
        self.name = name
        super().__init__()

    def __repr__(self) -> str:
        return "PaymentMethodInfo(payment_interface=%r, method=%r, name=%r)" % (
            self.payment_interface,
            self.method,
            self.name,
        )


class PaymentPagedQueryResponse(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.PaymentPagedQueryResponseSchema`."
    #: :class:`int`
    count: typing.Optional[int]
    #: Optional :class:`int`
    total: typing.Optional[int]
    #: :class:`int`
    offset: typing.Optional[int]
    #: List of :class:`commercetools.types.Payment`
    results: typing.Optional[typing.Sequence["Payment"]]

    def __init__(
        self,
        *,
        count: typing.Optional[int] = None,
        total: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        results: typing.Optional[typing.Sequence["Payment"]] = None
    ) -> None:
        self.count = count
        self.total = total
        self.offset = offset
        self.results = results
        super().__init__()

    def __repr__(self) -> str:
        return (
            "PaymentPagedQueryResponse(count=%r, total=%r, offset=%r, results=%r)"
            % (self.count, self.total, self.offset, self.results)
        )


class PaymentReference(Reference):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.PaymentReferenceSchema`."
    #: Optional :class:`commercetools.types.Payment`
    obj: typing.Optional["Payment"]

    def __init__(
        self,
        *,
        type_id: typing.Optional["ReferenceTypeId"] = None,
        id: typing.Optional[str] = None,
        obj: typing.Optional["Payment"] = None
    ) -> None:
        self.obj = obj
        super().__init__(type_id=ReferenceTypeId.PAYMENT, id=id)

    def __repr__(self) -> str:
        return "PaymentReference(type_id=%r, id=%r, obj=%r)" % (
            self.type_id,
            self.id,
            self.obj,
        )


class PaymentResourceIdentifier(ResourceIdentifier):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.PaymentResourceIdentifierSchema`."

    def __init__(
        self,
        *,
        type_id: typing.Optional["ReferenceTypeId"] = None,
        id: typing.Optional[str] = None,
        key: typing.Optional[str] = None
    ) -> None:
        super().__init__(type_id=ReferenceTypeId.PAYMENT, id=id, key=key)

    def __repr__(self) -> str:
        return "PaymentResourceIdentifier(type_id=%r, id=%r, key=%r)" % (
            self.type_id,
            self.id,
            self.key,
        )


class PaymentStatus(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.PaymentStatusSchema`."
    #: Optional :class:`str` `(Named` ``interfaceCode`` `in Commercetools)`
    interface_code: typing.Optional[str]
    #: Optional :class:`str` `(Named` ``interfaceText`` `in Commercetools)`
    interface_text: typing.Optional[str]
    #: Optional :class:`commercetools.types.StateReference`
    state: typing.Optional["StateReference"]

    def __init__(
        self,
        *,
        interface_code: typing.Optional[str] = None,
        interface_text: typing.Optional[str] = None,
        state: typing.Optional["StateReference"] = None
    ) -> None:
        self.interface_code = interface_code
        self.interface_text = interface_text
        self.state = state
        super().__init__()

    def __repr__(self) -> str:
        return "PaymentStatus(interface_code=%r, interface_text=%r, state=%r)" % (
            self.interface_code,
            self.interface_text,
            self.state,
        )


class PaymentStatusDraft(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.PaymentStatusDraftSchema`."
    #: Optional :class:`str` `(Named` ``interfaceCode`` `in Commercetools)`
    interface_code: typing.Optional[str]
    #: Optional :class:`str` `(Named` ``interfaceText`` `in Commercetools)`
    interface_text: typing.Optional[str]
    #: Optional :class:`commercetools.types.StateResourceIdentifier`
    state: typing.Optional["StateResourceIdentifier"]

    def __init__(
        self,
        *,
        interface_code: typing.Optional[str] = None,
        interface_text: typing.Optional[str] = None,
        state: typing.Optional["StateResourceIdentifier"] = None
    ) -> None:
        self.interface_code = interface_code
        self.interface_text = interface_text
        self.state = state
        super().__init__()

    def __repr__(self) -> str:
        return "PaymentStatusDraft(interface_code=%r, interface_text=%r, state=%r)" % (
            self.interface_code,
            self.interface_text,
            self.state,
        )


class PaymentUpdate(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.PaymentUpdateSchema`."
    #: :class:`int`
    version: typing.Optional[int]
    #: :class:`list`
    actions: typing.Optional[list]

    def __init__(
        self,
        *,
        version: typing.Optional[int] = None,
        actions: typing.Optional[list] = None
    ) -> None:
        self.version = version
        self.actions = actions
        super().__init__()

    def __repr__(self) -> str:
        return "PaymentUpdate(version=%r, actions=%r)" % (self.version, self.actions)


class PaymentUpdateAction(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.PaymentUpdateActionSchema`."
    #: :class:`str`
    action: typing.Optional[str]

    def __init__(self, *, action: typing.Optional[str] = None) -> None:
        self.action = action
        super().__init__()

    def __repr__(self) -> str:
        return "PaymentUpdateAction(action=%r)" % (self.action,)


class Transaction(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.TransactionSchema`."
    #: :class:`str`
    id: typing.Optional[str]
    #: Optional :class:`datetime.datetime`
    timestamp: typing.Optional[datetime.datetime]
    #: :class:`commercetools.types.TransactionType`
    type: typing.Optional["TransactionType"]
    #: :class:`commercetools.types.TypedMoney`
    amount: typing.Optional["TypedMoney"]
    #: Optional :class:`str` `(Named` ``interactionId`` `in Commercetools)`
    interaction_id: typing.Optional[str]
    #: Optional :class:`commercetools.types.TransactionState`
    state: typing.Optional["TransactionState"]

    def __init__(
        self,
        *,
        id: typing.Optional[str] = None,
        timestamp: typing.Optional[datetime.datetime] = None,
        type: typing.Optional["TransactionType"] = None,
        amount: typing.Optional["TypedMoney"] = None,
        interaction_id: typing.Optional[str] = None,
        state: typing.Optional["TransactionState"] = None
    ) -> None:
        self.id = id
        self.timestamp = timestamp
        self.type = type
        self.amount = amount
        self.interaction_id = interaction_id
        self.state = state
        super().__init__()

    def __repr__(self) -> str:
        return (
            "Transaction(id=%r, timestamp=%r, type=%r, amount=%r, interaction_id=%r, state=%r)"
            % (
                self.id,
                self.timestamp,
                self.type,
                self.amount,
                self.interaction_id,
                self.state,
            )
        )


class TransactionDraft(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.TransactionDraftSchema`."
    #: Optional :class:`datetime.datetime`
    timestamp: typing.Optional[datetime.datetime]
    #: :class:`commercetools.types.TransactionType`
    type: typing.Optional["TransactionType"]
    #: :class:`commercetools.types.Money`
    amount: typing.Optional["Money"]
    #: Optional :class:`str` `(Named` ``interactionId`` `in Commercetools)`
    interaction_id: typing.Optional[str]
    #: Optional :class:`commercetools.types.TransactionState`
    state: typing.Optional["TransactionState"]

    def __init__(
        self,
        *,
        timestamp: typing.Optional[datetime.datetime] = None,
        type: typing.Optional["TransactionType"] = None,
        amount: typing.Optional["Money"] = None,
        interaction_id: typing.Optional[str] = None,
        state: typing.Optional["TransactionState"] = None
    ) -> None:
        self.timestamp = timestamp
        self.type = type
        self.amount = amount
        self.interaction_id = interaction_id
        self.state = state
        super().__init__()

    def __repr__(self) -> str:
        return (
            "TransactionDraft(timestamp=%r, type=%r, amount=%r, interaction_id=%r, state=%r)"
            % (self.timestamp, self.type, self.amount, self.interaction_id, self.state)
        )


class TransactionState(enum.Enum):
    INITIAL = "Initial"
    PENDING = "Pending"
    SUCCESS = "Success"
    FAILURE = "Failure"


class TransactionType(enum.Enum):
    AUTHORIZATION = "Authorization"
    CANCEL_AUTHORIZATION = "CancelAuthorization"
    CHARGE = "Charge"
    REFUND = "Refund"
    CHARGEBACK = "Chargeback"


class PaymentAddInterfaceInteractionAction(PaymentUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.PaymentAddInterfaceInteractionActionSchema`."
    #: :class:`commercetools.types.TypeResourceIdentifier`
    type: typing.Optional["TypeResourceIdentifier"]
    #: Optional :class:`commercetools.types.FieldContainer`
    fields: typing.Optional["FieldContainer"]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        type: typing.Optional["TypeResourceIdentifier"] = None,
        fields: typing.Optional["FieldContainer"] = None
    ) -> None:
        self.type = type
        self.fields = fields
        super().__init__(action="addInterfaceInteraction")

    def __repr__(self) -> str:
        return "PaymentAddInterfaceInteractionAction(action=%r, type=%r, fields=%r)" % (
            self.action,
            self.type,
            self.fields,
        )


class PaymentAddTransactionAction(PaymentUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.PaymentAddTransactionActionSchema`."
    #: :class:`commercetools.types.TransactionDraft`
    transaction: typing.Optional["TransactionDraft"]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        transaction: typing.Optional["TransactionDraft"] = None
    ) -> None:
        self.transaction = transaction
        super().__init__(action="addTransaction")

    def __repr__(self) -> str:
        return "PaymentAddTransactionAction(action=%r, transaction=%r)" % (
            self.action,
            self.transaction,
        )


class PaymentChangeAmountPlannedAction(PaymentUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.PaymentChangeAmountPlannedActionSchema`."
    #: :class:`commercetools.types.Money`
    amount: typing.Optional["Money"]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        amount: typing.Optional["Money"] = None
    ) -> None:
        self.amount = amount
        super().__init__(action="changeAmountPlanned")

    def __repr__(self) -> str:
        return "PaymentChangeAmountPlannedAction(action=%r, amount=%r)" % (
            self.action,
            self.amount,
        )


class PaymentChangeTransactionInteractionIdAction(PaymentUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.PaymentChangeTransactionInteractionIdActionSchema`."
    #: :class:`str` `(Named` ``transactionId`` `in Commercetools)`
    transaction_id: typing.Optional[str]
    #: :class:`str` `(Named` ``interactionId`` `in Commercetools)`
    interaction_id: typing.Optional[str]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        transaction_id: typing.Optional[str] = None,
        interaction_id: typing.Optional[str] = None
    ) -> None:
        self.transaction_id = transaction_id
        self.interaction_id = interaction_id
        super().__init__(action="changeTransactionInteractionId")

    def __repr__(self) -> str:
        return (
            "PaymentChangeTransactionInteractionIdAction(action=%r, transaction_id=%r, interaction_id=%r)"
            % (self.action, self.transaction_id, self.interaction_id)
        )


class PaymentChangeTransactionStateAction(PaymentUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.PaymentChangeTransactionStateActionSchema`."
    #: :class:`str` `(Named` ``transactionId`` `in Commercetools)`
    transaction_id: typing.Optional[str]
    #: :class:`commercetools.types.TransactionState`
    state: typing.Optional["TransactionState"]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        transaction_id: typing.Optional[str] = None,
        state: typing.Optional["TransactionState"] = None
    ) -> None:
        self.transaction_id = transaction_id
        self.state = state
        super().__init__(action="changeTransactionState")

    def __repr__(self) -> str:
        return (
            "PaymentChangeTransactionStateAction(action=%r, transaction_id=%r, state=%r)"
            % (self.action, self.transaction_id, self.state)
        )


class PaymentChangeTransactionTimestampAction(PaymentUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.PaymentChangeTransactionTimestampActionSchema`."
    #: :class:`str` `(Named` ``transactionId`` `in Commercetools)`
    transaction_id: typing.Optional[str]
    #: :class:`datetime.datetime`
    timestamp: typing.Optional[datetime.datetime]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        transaction_id: typing.Optional[str] = None,
        timestamp: typing.Optional[datetime.datetime] = None
    ) -> None:
        self.transaction_id = transaction_id
        self.timestamp = timestamp
        super().__init__(action="changeTransactionTimestamp")

    def __repr__(self) -> str:
        return (
            "PaymentChangeTransactionTimestampAction(action=%r, transaction_id=%r, timestamp=%r)"
            % (self.action, self.transaction_id, self.timestamp)
        )


class PaymentSetAmountPaidAction(PaymentUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.PaymentSetAmountPaidActionSchema`."
    #: Optional :class:`commercetools.types.Money`
    amount: typing.Optional["Money"]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        amount: typing.Optional["Money"] = None
    ) -> None:
        self.amount = amount
        super().__init__(action="setAmountPaid")

    def __repr__(self) -> str:
        return "PaymentSetAmountPaidAction(action=%r, amount=%r)" % (
            self.action,
            self.amount,
        )


class PaymentSetAmountRefundedAction(PaymentUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.PaymentSetAmountRefundedActionSchema`."
    #: Optional :class:`commercetools.types.Money`
    amount: typing.Optional["Money"]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        amount: typing.Optional["Money"] = None
    ) -> None:
        self.amount = amount
        super().__init__(action="setAmountRefunded")

    def __repr__(self) -> str:
        return "PaymentSetAmountRefundedAction(action=%r, amount=%r)" % (
            self.action,
            self.amount,
        )


class PaymentSetAnonymousIdAction(PaymentUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.PaymentSetAnonymousIdActionSchema`."
    #: Optional :class:`str` `(Named` ``anonymousId`` `in Commercetools)`
    anonymous_id: typing.Optional[str]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        anonymous_id: typing.Optional[str] = None
    ) -> None:
        self.anonymous_id = anonymous_id
        super().__init__(action="setAnonymousId")

    def __repr__(self) -> str:
        return "PaymentSetAnonymousIdAction(action=%r, anonymous_id=%r)" % (
            self.action,
            self.anonymous_id,
        )


class PaymentSetAuthorizationAction(PaymentUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.PaymentSetAuthorizationActionSchema`."
    #: Optional :class:`commercetools.types.Money`
    amount: typing.Optional["Money"]
    #: Optional :class:`datetime.datetime`
    until: typing.Optional[datetime.datetime]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        amount: typing.Optional["Money"] = None,
        until: typing.Optional[datetime.datetime] = None
    ) -> None:
        self.amount = amount
        self.until = until
        super().__init__(action="setAuthorization")

    def __repr__(self) -> str:
        return "PaymentSetAuthorizationAction(action=%r, amount=%r, until=%r)" % (
            self.action,
            self.amount,
            self.until,
        )


class PaymentSetCustomFieldAction(PaymentUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.PaymentSetCustomFieldActionSchema`."
    #: :class:`str`
    name: typing.Optional[str]
    #: Optional :class:`typing.Any`
    value: typing.Optional[typing.Any]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        value: typing.Optional[typing.Any] = None
    ) -> None:
        self.name = name
        self.value = value
        super().__init__(action="setCustomField")

    def __repr__(self) -> str:
        return "PaymentSetCustomFieldAction(action=%r, name=%r, value=%r)" % (
            self.action,
            self.name,
            self.value,
        )


class PaymentSetCustomTypeAction(PaymentUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.PaymentSetCustomTypeActionSchema`."
    #: Optional :class:`commercetools.types.TypeResourceIdentifier`
    type: typing.Optional["TypeResourceIdentifier"]
    #: Optional :class:`commercetools.types.FieldContainer`
    fields: typing.Optional["FieldContainer"]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        type: typing.Optional["TypeResourceIdentifier"] = None,
        fields: typing.Optional["FieldContainer"] = None
    ) -> None:
        self.type = type
        self.fields = fields
        super().__init__(action="setCustomType")

    def __repr__(self) -> str:
        return "PaymentSetCustomTypeAction(action=%r, type=%r, fields=%r)" % (
            self.action,
            self.type,
            self.fields,
        )


class PaymentSetCustomerAction(PaymentUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.PaymentSetCustomerActionSchema`."
    #: Optional :class:`commercetools.types.CustomerResourceIdentifier`
    customer: typing.Optional["CustomerResourceIdentifier"]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        customer: typing.Optional["CustomerResourceIdentifier"] = None
    ) -> None:
        self.customer = customer
        super().__init__(action="setCustomer")

    def __repr__(self) -> str:
        return "PaymentSetCustomerAction(action=%r, customer=%r)" % (
            self.action,
            self.customer,
        )


class PaymentSetExternalIdAction(PaymentUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.PaymentSetExternalIdActionSchema`."
    #: Optional :class:`str` `(Named` ``externalId`` `in Commercetools)`
    external_id: typing.Optional[str]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        external_id: typing.Optional[str] = None
    ) -> None:
        self.external_id = external_id
        super().__init__(action="setExternalId")

    def __repr__(self) -> str:
        return "PaymentSetExternalIdAction(action=%r, external_id=%r)" % (
            self.action,
            self.external_id,
        )


class PaymentSetInterfaceIdAction(PaymentUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.PaymentSetInterfaceIdActionSchema`."
    #: :class:`str` `(Named` ``interfaceId`` `in Commercetools)`
    interface_id: typing.Optional[str]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        interface_id: typing.Optional[str] = None
    ) -> None:
        self.interface_id = interface_id
        super().__init__(action="setInterfaceId")

    def __repr__(self) -> str:
        return "PaymentSetInterfaceIdAction(action=%r, interface_id=%r)" % (
            self.action,
            self.interface_id,
        )


class PaymentSetKeyAction(PaymentUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.PaymentSetKeyActionSchema`."
    #: Optional :class:`str`
    key: typing.Optional[str]

    def __init__(
        self, *, action: typing.Optional[str] = None, key: typing.Optional[str] = None
    ) -> None:
        self.key = key
        super().__init__(action="setKey")

    def __repr__(self) -> str:
        return "PaymentSetKeyAction(action=%r, key=%r)" % (self.action, self.key)


class PaymentSetMethodInfoInterfaceAction(PaymentUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.PaymentSetMethodInfoInterfaceActionSchema`."
    #: :class:`str`
    interface: typing.Optional[str]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        interface: typing.Optional[str] = None
    ) -> None:
        self.interface = interface
        super().__init__(action="setMethodInfoInterface")

    def __repr__(self) -> str:
        return "PaymentSetMethodInfoInterfaceAction(action=%r, interface=%r)" % (
            self.action,
            self.interface,
        )


class PaymentSetMethodInfoMethodAction(PaymentUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.PaymentSetMethodInfoMethodActionSchema`."
    #: Optional :class:`str`
    method: typing.Optional[str]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        method: typing.Optional[str] = None
    ) -> None:
        self.method = method
        super().__init__(action="setMethodInfoMethod")

    def __repr__(self) -> str:
        return "PaymentSetMethodInfoMethodAction(action=%r, method=%r)" % (
            self.action,
            self.method,
        )


class PaymentSetMethodInfoNameAction(PaymentUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.PaymentSetMethodInfoNameActionSchema`."
    #: Optional :class:`commercetools.types.LocalizedString`
    name: typing.Optional["LocalizedString"]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        name: typing.Optional["LocalizedString"] = None
    ) -> None:
        self.name = name
        super().__init__(action="setMethodInfoName")

    def __repr__(self) -> str:
        return "PaymentSetMethodInfoNameAction(action=%r, name=%r)" % (
            self.action,
            self.name,
        )


class PaymentSetStatusInterfaceCodeAction(PaymentUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.PaymentSetStatusInterfaceCodeActionSchema`."
    #: Optional :class:`str` `(Named` ``interfaceCode`` `in Commercetools)`
    interface_code: typing.Optional[str]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        interface_code: typing.Optional[str] = None
    ) -> None:
        self.interface_code = interface_code
        super().__init__(action="setStatusInterfaceCode")

    def __repr__(self) -> str:
        return "PaymentSetStatusInterfaceCodeAction(action=%r, interface_code=%r)" % (
            self.action,
            self.interface_code,
        )


class PaymentSetStatusInterfaceTextAction(PaymentUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.PaymentSetStatusInterfaceTextActionSchema`."
    #: :class:`str` `(Named` ``interfaceText`` `in Commercetools)`
    interface_text: typing.Optional[str]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        interface_text: typing.Optional[str] = None
    ) -> None:
        self.interface_text = interface_text
        super().__init__(action="setStatusInterfaceText")

    def __repr__(self) -> str:
        return "PaymentSetStatusInterfaceTextAction(action=%r, interface_text=%r)" % (
            self.action,
            self.interface_text,
        )


class PaymentTransitionStateAction(PaymentUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.PaymentTransitionStateActionSchema`."
    #: :class:`commercetools.types.StateResourceIdentifier`
    state: typing.Optional["StateResourceIdentifier"]
    #: Optional :class:`bool`
    force: typing.Optional[bool]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        state: typing.Optional["StateResourceIdentifier"] = None,
        force: typing.Optional[bool] = None
    ) -> None:
        self.state = state
        self.force = force
        super().__init__(action="transitionState")

    def __repr__(self) -> str:
        return "PaymentTransitionStateAction(action=%r, state=%r, force=%r)" % (
            self.action,
            self.state,
            self.force,
        )
