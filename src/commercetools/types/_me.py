# DO NOT EDIT! This file is automatically generated

import datetime
import typing

from commercetools.types._abstract import _BaseType

if typing.TYPE_CHECKING:
    from ._cart import InventoryMode, ItemShippingDetailsDraft, TaxMode
    from ._channel import ChannelResourceIdentifier
    from ._common import Address
    from ._shipping_method import ShippingMethodResourceIdentifier
    from ._type import CustomFields, CustomFieldsDraft
__all__ = ["MyCartDraft", "MyCustomerDraft", "MyLineItemDraft", "MyOrderFromCartDraft"]


class MyCartDraft(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.MyCartDraftSchema`."
    #: :class:`str`
    currency: typing.Optional["str"]
    #: Optional :class:`str` `(Named` ``customerEmail`` `in Commercetools)`
    customer_email: typing.Optional[str]
    #: Optional :class:`str`
    country: typing.Optional[str]
    #: Optional :class:`commercetools.types.InventoryMode` `(Named` ``inventoryMode`` `in Commercetools)`
    inventory_mode: typing.Optional["InventoryMode"]
    #: Optional list of :class:`commercetools.types.MyLineItemDraft` `(Named` ``lineItems`` `in Commercetools)`
    line_items: typing.Optional[typing.List["MyLineItemDraft"]]
    #: Optional :class:`commercetools.types.Address` `(Named` ``shippingAddress`` `in Commercetools)`
    shipping_address: typing.Optional["Address"]
    #: Optional :class:`commercetools.types.Address` `(Named` ``billingAddress`` `in Commercetools)`
    billing_address: typing.Optional["Address"]
    #: Optional :class:`commercetools.types.ShippingMethodResourceIdentifier` `(Named` ``shippingMethod`` `in Commercetools)`
    shipping_method: typing.Optional["ShippingMethodResourceIdentifier"]
    #: Optional :class:`commercetools.types.CustomFieldsDraft`
    custom: typing.Optional["CustomFieldsDraft"]
    #: Optional :class:`str`
    locale: typing.Optional[str]
    #: Optional :class:`commercetools.types.TaxMode` `(Named` ``taxMode`` `in Commercetools)`
    tax_mode: typing.Optional["TaxMode"]
    #: Optional :class:`int` `(Named` ``deleteDaysAfterLastModification`` `in Commercetools)`
    delete_days_after_last_modification: typing.Optional[int]
    #: Optional list of :class:`commercetools.types.Address` `(Named` ``itemShippingAddresses`` `in Commercetools)`
    item_shipping_addresses: typing.Optional[typing.List["Address"]]

    def __init__(
        self,
        *,
        currency: typing.Optional["str"] = None,
        customer_email: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        inventory_mode: typing.Optional["InventoryMode"] = None,
        line_items: typing.Optional[typing.List["MyLineItemDraft"]] = None,
        shipping_address: typing.Optional["Address"] = None,
        billing_address: typing.Optional["Address"] = None,
        shipping_method: typing.Optional["ShippingMethodResourceIdentifier"] = None,
        custom: typing.Optional["CustomFieldsDraft"] = None,
        locale: typing.Optional[str] = None,
        tax_mode: typing.Optional["TaxMode"] = None,
        delete_days_after_last_modification: typing.Optional[int] = None,
        item_shipping_addresses: typing.Optional[typing.List["Address"]] = None
    ) -> None:
        self.currency = currency
        self.customer_email = customer_email
        self.country = country
        self.inventory_mode = inventory_mode
        self.line_items = line_items
        self.shipping_address = shipping_address
        self.billing_address = billing_address
        self.shipping_method = shipping_method
        self.custom = custom
        self.locale = locale
        self.tax_mode = tax_mode
        self.delete_days_after_last_modification = delete_days_after_last_modification
        self.item_shipping_addresses = item_shipping_addresses
        super().__init__()

    def __repr__(self) -> str:
        return (
            "MyCartDraft(currency=%r, customer_email=%r, country=%r, inventory_mode=%r, line_items=%r, shipping_address=%r, billing_address=%r, shipping_method=%r, custom=%r, locale=%r, tax_mode=%r, delete_days_after_last_modification=%r, item_shipping_addresses=%r)"
            % (
                self.currency,
                self.customer_email,
                self.country,
                self.inventory_mode,
                self.line_items,
                self.shipping_address,
                self.billing_address,
                self.shipping_method,
                self.custom,
                self.locale,
                self.tax_mode,
                self.delete_days_after_last_modification,
                self.item_shipping_addresses,
            )
        )


class MyCustomerDraft(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.MyCustomerDraftSchema`."
    #: :class:`str`
    email: typing.Optional[str]
    #: :class:`str`
    password: typing.Optional[str]
    #: Optional :class:`str` `(Named` ``firstName`` `in Commercetools)`
    first_name: typing.Optional[str]
    #: Optional :class:`str` `(Named` ``lastName`` `in Commercetools)`
    last_name: typing.Optional[str]
    #: Optional :class:`str` `(Named` ``middleName`` `in Commercetools)`
    middle_name: typing.Optional[str]
    #: Optional :class:`str`
    title: typing.Optional[str]
    #: Optional :class:`datetime.date` `(Named` ``dateOfBirth`` `in Commercetools)`
    date_of_birth: typing.Optional[datetime.date]
    #: Optional :class:`str` `(Named` ``companyName`` `in Commercetools)`
    company_name: typing.Optional[str]
    #: Optional :class:`str` `(Named` ``vatId`` `in Commercetools)`
    vat_id: typing.Optional[str]
    #: Optional list of :class:`commercetools.types.Address`
    addresses: typing.Optional[typing.List["Address"]]
    #: Optional :class:`int` `(Named` ``defaultShippingAddress`` `in Commercetools)`
    default_shipping_address: typing.Optional[int]
    #: Optional :class:`int` `(Named` ``defaultBillingAddress`` `in Commercetools)`
    default_billing_address: typing.Optional[int]
    #: Optional :class:`commercetools.types.CustomFields`
    custom: typing.Optional["CustomFields"]
    #: Optional :class:`str`
    locale: typing.Optional[str]

    def __init__(
        self,
        *,
        email: typing.Optional[str] = None,
        password: typing.Optional[str] = None,
        first_name: typing.Optional[str] = None,
        last_name: typing.Optional[str] = None,
        middle_name: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        date_of_birth: typing.Optional[datetime.date] = None,
        company_name: typing.Optional[str] = None,
        vat_id: typing.Optional[str] = None,
        addresses: typing.Optional[typing.List["Address"]] = None,
        default_shipping_address: typing.Optional[int] = None,
        default_billing_address: typing.Optional[int] = None,
        custom: typing.Optional["CustomFields"] = None,
        locale: typing.Optional[str] = None
    ) -> None:
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.title = title
        self.date_of_birth = date_of_birth
        self.company_name = company_name
        self.vat_id = vat_id
        self.addresses = addresses
        self.default_shipping_address = default_shipping_address
        self.default_billing_address = default_billing_address
        self.custom = custom
        self.locale = locale
        super().__init__()

    def __repr__(self) -> str:
        return (
            "MyCustomerDraft(email=%r, password=%r, first_name=%r, last_name=%r, middle_name=%r, title=%r, date_of_birth=%r, company_name=%r, vat_id=%r, addresses=%r, default_shipping_address=%r, default_billing_address=%r, custom=%r, locale=%r)"
            % (
                self.email,
                self.password,
                self.first_name,
                self.last_name,
                self.middle_name,
                self.title,
                self.date_of_birth,
                self.company_name,
                self.vat_id,
                self.addresses,
                self.default_shipping_address,
                self.default_billing_address,
                self.custom,
                self.locale,
            )
        )


class MyLineItemDraft(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.MyLineItemDraftSchema`."
    #: :class:`str` `(Named` ``productId`` `in Commercetools)`
    product_id: typing.Optional[str]
    #: :class:`int` `(Named` ``variantId`` `in Commercetools)`
    variant_id: typing.Optional[int]
    #: :class:`int`
    quantity: typing.Optional[int]
    #: Optional :class:`commercetools.types.ChannelResourceIdentifier` `(Named` ``supplyChannel`` `in Commercetools)`
    supply_channel: typing.Optional["ChannelResourceIdentifier"]
    #: Optional :class:`commercetools.types.ChannelResourceIdentifier` `(Named` ``distributionChannel`` `in Commercetools)`
    distribution_channel: typing.Optional["ChannelResourceIdentifier"]
    #: Optional :class:`commercetools.types.CustomFieldsDraft`
    custom: typing.Optional["CustomFieldsDraft"]
    #: Optional :class:`commercetools.types.ItemShippingDetailsDraft` `(Named` ``shippingDetails`` `in Commercetools)`
    shipping_details: typing.Optional["ItemShippingDetailsDraft"]

    def __init__(
        self,
        *,
        product_id: typing.Optional[str] = None,
        variant_id: typing.Optional[int] = None,
        quantity: typing.Optional[int] = None,
        supply_channel: typing.Optional["ChannelResourceIdentifier"] = None,
        distribution_channel: typing.Optional["ChannelResourceIdentifier"] = None,
        custom: typing.Optional["CustomFieldsDraft"] = None,
        shipping_details: typing.Optional["ItemShippingDetailsDraft"] = None
    ) -> None:
        self.product_id = product_id
        self.variant_id = variant_id
        self.quantity = quantity
        self.supply_channel = supply_channel
        self.distribution_channel = distribution_channel
        self.custom = custom
        self.shipping_details = shipping_details
        super().__init__()

    def __repr__(self) -> str:
        return (
            "MyLineItemDraft(product_id=%r, variant_id=%r, quantity=%r, supply_channel=%r, distribution_channel=%r, custom=%r, shipping_details=%r)"
            % (
                self.product_id,
                self.variant_id,
                self.quantity,
                self.supply_channel,
                self.distribution_channel,
                self.custom,
                self.shipping_details,
            )
        )


class MyOrderFromCartDraft(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.MyOrderFromCartDraftSchema`."
    #: :class:`str`
    id: typing.Optional[str]
    #: :class:`int`
    version: typing.Optional[int]

    def __init__(
        self, *, id: typing.Optional[str] = None, version: typing.Optional[int] = None
    ) -> None:
        self.id = id
        self.version = version
        super().__init__()

    def __repr__(self) -> str:
        return "MyOrderFromCartDraft(id=%r, version=%r)" % (self.id, self.version)
