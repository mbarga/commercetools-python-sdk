# DO NOT EDIT! This file is automatically generated

import datetime
import enum
import typing

from commercetools.types._abstract import _BaseType
from commercetools.types._common import (
    BaseResource,
    Reference,
    ReferenceTypeId,
    ResourceIdentifier,
)

if typing.TYPE_CHECKING:
    from ._common import Money, TypedMoney
    from ._tax_category import TaxCategoryReference, TaxCategoryResourceIdentifier
    from ._zone import ZoneReference, ZoneResourceIdentifier
__all__ = [
    "CartClassificationTier",
    "CartScoreTier",
    "CartValueTier",
    "PriceFunction",
    "ShippingMethod",
    "ShippingMethodAddShippingRateAction",
    "ShippingMethodAddZoneAction",
    "ShippingMethodChangeIsDefaultAction",
    "ShippingMethodChangeNameAction",
    "ShippingMethodChangeTaxCategoryAction",
    "ShippingMethodDraft",
    "ShippingMethodPagedQueryResponse",
    "ShippingMethodReference",
    "ShippingMethodRemoveShippingRateAction",
    "ShippingMethodRemoveZoneAction",
    "ShippingMethodResourceIdentifier",
    "ShippingMethodSetDescriptionAction",
    "ShippingMethodSetKeyAction",
    "ShippingMethodSetPredicateAction",
    "ShippingMethodUpdate",
    "ShippingMethodUpdateAction",
    "ShippingRate",
    "ShippingRateDraft",
    "ShippingRatePriceTier",
    "ShippingRateTierType",
    "ZoneRate",
    "ZoneRateDraft",
]


class PriceFunction(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.PriceFunctionSchema`."
    #: :class:`str` `(Named` ``currencyCode`` `in Commercetools)`
    currency_code: typing.Optional["str"]
    #: :class:`str`
    function: typing.Optional[str]

    def __init__(
        self,
        *,
        currency_code: typing.Optional["str"] = None,
        function: typing.Optional[str] = None
    ) -> None:
        self.currency_code = currency_code
        self.function = function
        super().__init__()

    def __repr__(self) -> str:
        return "PriceFunction(currency_code=%r, function=%r)" % (
            self.currency_code,
            self.function,
        )


class ShippingMethod(BaseResource):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ShippingMethodSchema`."
    #: Optional :class:`str`
    key: typing.Optional[str]
    #: :class:`str`
    name: typing.Optional[str]
    #: Optional :class:`str`
    description: typing.Optional[str]
    #: :class:`commercetools.types.TaxCategoryReference` `(Named` ``taxCategory`` `in Commercetools)`
    tax_category: typing.Optional["TaxCategoryReference"]
    #: List of :class:`commercetools.types.ZoneRate` `(Named` ``zoneRates`` `in Commercetools)`
    zone_rates: typing.Optional[typing.List["ZoneRate"]]
    #: :class:`bool` `(Named` ``isDefault`` `in Commercetools)`
    is_default: typing.Optional[bool]
    #: Optional :class:`str`
    predicate: typing.Optional[str]

    def __init__(
        self,
        *,
        id: typing.Optional[str] = None,
        version: typing.Optional[int] = None,
        created_at: typing.Optional[datetime.datetime] = None,
        last_modified_at: typing.Optional[datetime.datetime] = None,
        key: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        tax_category: typing.Optional["TaxCategoryReference"] = None,
        zone_rates: typing.Optional[typing.List["ZoneRate"]] = None,
        is_default: typing.Optional[bool] = None,
        predicate: typing.Optional[str] = None
    ) -> None:
        self.key = key
        self.name = name
        self.description = description
        self.tax_category = tax_category
        self.zone_rates = zone_rates
        self.is_default = is_default
        self.predicate = predicate
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
        )

    def __repr__(self) -> str:
        return (
            "ShippingMethod(id=%r, version=%r, created_at=%r, last_modified_at=%r, key=%r, name=%r, description=%r, tax_category=%r, zone_rates=%r, is_default=%r, predicate=%r)"
            % (
                self.id,
                self.version,
                self.created_at,
                self.last_modified_at,
                self.key,
                self.name,
                self.description,
                self.tax_category,
                self.zone_rates,
                self.is_default,
                self.predicate,
            )
        )


class ShippingMethodDraft(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ShippingMethodDraftSchema`."
    #: Optional :class:`str`
    key: typing.Optional[str]
    #: :class:`str`
    name: typing.Optional[str]
    #: Optional :class:`str`
    description: typing.Optional[str]
    #: :class:`commercetools.types.TaxCategoryResourceIdentifier` `(Named` ``taxCategory`` `in Commercetools)`
    tax_category: typing.Optional["TaxCategoryResourceIdentifier"]
    #: List of :class:`commercetools.types.ZoneRateDraft` `(Named` ``zoneRates`` `in Commercetools)`
    zone_rates: typing.Optional[typing.List["ZoneRateDraft"]]
    #: :class:`bool` `(Named` ``isDefault`` `in Commercetools)`
    is_default: typing.Optional[bool]
    #: Optional :class:`str`
    predicate: typing.Optional[str]

    def __init__(
        self,
        *,
        key: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        tax_category: typing.Optional["TaxCategoryResourceIdentifier"] = None,
        zone_rates: typing.Optional[typing.List["ZoneRateDraft"]] = None,
        is_default: typing.Optional[bool] = None,
        predicate: typing.Optional[str] = None
    ) -> None:
        self.key = key
        self.name = name
        self.description = description
        self.tax_category = tax_category
        self.zone_rates = zone_rates
        self.is_default = is_default
        self.predicate = predicate
        super().__init__()

    def __repr__(self) -> str:
        return (
            "ShippingMethodDraft(key=%r, name=%r, description=%r, tax_category=%r, zone_rates=%r, is_default=%r, predicate=%r)"
            % (
                self.key,
                self.name,
                self.description,
                self.tax_category,
                self.zone_rates,
                self.is_default,
                self.predicate,
            )
        )


class ShippingMethodPagedQueryResponse(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ShippingMethodPagedQueryResponseSchema`."
    #: :class:`int`
    count: typing.Optional[int]
    #: Optional :class:`int`
    total: typing.Optional[int]
    #: :class:`int`
    offset: typing.Optional[int]
    #: List of :class:`commercetools.types.ShippingMethod`
    results: typing.Optional[typing.Sequence["ShippingMethod"]]

    def __init__(
        self,
        *,
        count: typing.Optional[int] = None,
        total: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        results: typing.Optional[typing.Sequence["ShippingMethod"]] = None
    ) -> None:
        self.count = count
        self.total = total
        self.offset = offset
        self.results = results
        super().__init__()

    def __repr__(self) -> str:
        return (
            "ShippingMethodPagedQueryResponse(count=%r, total=%r, offset=%r, results=%r)"
            % (self.count, self.total, self.offset, self.results)
        )


class ShippingMethodReference(Reference):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ShippingMethodReferenceSchema`."
    #: Optional :class:`commercetools.types.ShippingMethod`
    obj: typing.Optional["ShippingMethod"]

    def __init__(
        self,
        *,
        type_id: typing.Optional["ReferenceTypeId"] = None,
        id: typing.Optional[str] = None,
        obj: typing.Optional["ShippingMethod"] = None
    ) -> None:
        self.obj = obj
        super().__init__(type_id=ReferenceTypeId.SHIPPING_METHOD, id=id)

    def __repr__(self) -> str:
        return "ShippingMethodReference(type_id=%r, id=%r, obj=%r)" % (
            self.type_id,
            self.id,
            self.obj,
        )


class ShippingMethodResourceIdentifier(ResourceIdentifier):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ShippingMethodResourceIdentifierSchema`."

    def __init__(
        self,
        *,
        type_id: typing.Optional["ReferenceTypeId"] = None,
        id: typing.Optional[str] = None,
        key: typing.Optional[str] = None
    ) -> None:
        super().__init__(type_id=ReferenceTypeId.SHIPPING_METHOD, id=id, key=key)

    def __repr__(self) -> str:
        return "ShippingMethodResourceIdentifier(type_id=%r, id=%r, key=%r)" % (
            self.type_id,
            self.id,
            self.key,
        )


class ShippingMethodUpdate(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ShippingMethodUpdateSchema`."
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
        return "ShippingMethodUpdate(version=%r, actions=%r)" % (
            self.version,
            self.actions,
        )


class ShippingMethodUpdateAction(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ShippingMethodUpdateActionSchema`."
    #: :class:`str`
    action: typing.Optional[str]

    def __init__(self, *, action: typing.Optional[str] = None) -> None:
        self.action = action
        super().__init__()

    def __repr__(self) -> str:
        return "ShippingMethodUpdateAction(action=%r)" % (self.action,)


class ShippingRate(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ShippingRateSchema`."
    #: :class:`commercetools.types.TypedMoney`
    price: typing.Optional["TypedMoney"]
    #: Optional :class:`commercetools.types.TypedMoney` `(Named` ``freeAbove`` `in Commercetools)`
    free_above: typing.Optional["TypedMoney"]
    #: Optional :class:`bool` `(Named` ``isMatching`` `in Commercetools)`
    is_matching: typing.Optional[bool]
    #: List of :class:`commercetools.types.ShippingRatePriceTier`
    tiers: typing.Optional[typing.List["ShippingRatePriceTier"]]

    def __init__(
        self,
        *,
        price: typing.Optional["TypedMoney"] = None,
        free_above: typing.Optional["TypedMoney"] = None,
        is_matching: typing.Optional[bool] = None,
        tiers: typing.Optional[typing.List["ShippingRatePriceTier"]] = None
    ) -> None:
        self.price = price
        self.free_above = free_above
        self.is_matching = is_matching
        self.tiers = tiers
        super().__init__()

    def __repr__(self) -> str:
        return "ShippingRate(price=%r, free_above=%r, is_matching=%r, tiers=%r)" % (
            self.price,
            self.free_above,
            self.is_matching,
            self.tiers,
        )


class ShippingRateDraft(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ShippingRateDraftSchema`."
    #: :class:`commercetools.types.Money`
    price: typing.Optional["Money"]
    #: Optional :class:`commercetools.types.Money` `(Named` ``freeAbove`` `in Commercetools)`
    free_above: typing.Optional["Money"]
    #: Optional list of :class:`commercetools.types.ShippingRatePriceTier`
    tiers: typing.Optional[typing.List["ShippingRatePriceTier"]]

    def __init__(
        self,
        *,
        price: typing.Optional["Money"] = None,
        free_above: typing.Optional["Money"] = None,
        tiers: typing.Optional[typing.List["ShippingRatePriceTier"]] = None
    ) -> None:
        self.price = price
        self.free_above = free_above
        self.tiers = tiers
        super().__init__()

    def __repr__(self) -> str:
        return "ShippingRateDraft(price=%r, free_above=%r, tiers=%r)" % (
            self.price,
            self.free_above,
            self.tiers,
        )


class ShippingRatePriceTier(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ShippingRatePriceTierSchema`."
    #: :class:`commercetools.types.ShippingRateTierType`
    type: typing.Optional["ShippingRateTierType"]

    def __init__(self, *, type: typing.Optional["ShippingRateTierType"] = None) -> None:
        self.type = type
        super().__init__()

    def __repr__(self) -> str:
        return "ShippingRatePriceTier(type=%r)" % (self.type,)


class ShippingRateTierType(enum.Enum):
    CART_VALUE = "CartValue"
    CART_CLASSIFICATION = "CartClassification"
    CART_SCORE = "CartScore"


class ZoneRate(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ZoneRateSchema`."
    #: :class:`commercetools.types.ZoneReference`
    zone: typing.Optional["ZoneReference"]
    #: List of :class:`commercetools.types.ShippingRate` `(Named` ``shippingRates`` `in Commercetools)`
    shipping_rates: typing.Optional[typing.List["ShippingRate"]]

    def __init__(
        self,
        *,
        zone: typing.Optional["ZoneReference"] = None,
        shipping_rates: typing.Optional[typing.List["ShippingRate"]] = None
    ) -> None:
        self.zone = zone
        self.shipping_rates = shipping_rates
        super().__init__()

    def __repr__(self) -> str:
        return "ZoneRate(zone=%r, shipping_rates=%r)" % (self.zone, self.shipping_rates)


class ZoneRateDraft(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ZoneRateDraftSchema`."
    #: :class:`commercetools.types.ZoneResourceIdentifier`
    zone: typing.Optional["ZoneResourceIdentifier"]
    #: List of :class:`commercetools.types.ShippingRateDraft` `(Named` ``shippingRates`` `in Commercetools)`
    shipping_rates: typing.Optional[typing.List["ShippingRateDraft"]]

    def __init__(
        self,
        *,
        zone: typing.Optional["ZoneResourceIdentifier"] = None,
        shipping_rates: typing.Optional[typing.List["ShippingRateDraft"]] = None
    ) -> None:
        self.zone = zone
        self.shipping_rates = shipping_rates
        super().__init__()

    def __repr__(self) -> str:
        return "ZoneRateDraft(zone=%r, shipping_rates=%r)" % (
            self.zone,
            self.shipping_rates,
        )


class CartClassificationTier(ShippingRatePriceTier):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CartClassificationTierSchema`."
    #: :class:`str`
    value: typing.Optional[str]
    #: :class:`commercetools.types.Money`
    price: typing.Optional["Money"]
    #: Optional :class:`bool` `(Named` ``isMatching`` `in Commercetools)`
    is_matching: typing.Optional[bool]

    def __init__(
        self,
        *,
        type: typing.Optional["ShippingRateTierType"] = None,
        value: typing.Optional[str] = None,
        price: typing.Optional["Money"] = None,
        is_matching: typing.Optional[bool] = None
    ) -> None:
        self.value = value
        self.price = price
        self.is_matching = is_matching
        super().__init__(type=ShippingRateTierType.CART_CLASSIFICATION)

    def __repr__(self) -> str:
        return "CartClassificationTier(type=%r, value=%r, price=%r, is_matching=%r)" % (
            self.type,
            self.value,
            self.price,
            self.is_matching,
        )


class CartScoreTier(ShippingRatePriceTier):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CartScoreTierSchema`."
    #: :class:`int`
    score: typing.Optional[int]
    #: Optional :class:`commercetools.types.Money`
    price: typing.Optional["Money"]
    #: Optional :class:`commercetools.types.PriceFunction` `(Named` ``priceFunction`` `in Commercetools)`
    price_function: typing.Optional["PriceFunction"]
    #: Optional :class:`bool` `(Named` ``isMatching`` `in Commercetools)`
    is_matching: typing.Optional[bool]

    def __init__(
        self,
        *,
        type: typing.Optional["ShippingRateTierType"] = None,
        score: typing.Optional[int] = None,
        price: typing.Optional["Money"] = None,
        price_function: typing.Optional["PriceFunction"] = None,
        is_matching: typing.Optional[bool] = None
    ) -> None:
        self.score = score
        self.price = price
        self.price_function = price_function
        self.is_matching = is_matching
        super().__init__(type=ShippingRateTierType.CART_SCORE)

    def __repr__(self) -> str:
        return (
            "CartScoreTier(type=%r, score=%r, price=%r, price_function=%r, is_matching=%r)"
            % (self.type, self.score, self.price, self.price_function, self.is_matching)
        )


class CartValueTier(ShippingRatePriceTier):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CartValueTierSchema`."
    #: :class:`int` `(Named` ``minimumCentAmount`` `in Commercetools)`
    minimum_cent_amount: typing.Optional[int]
    #: :class:`commercetools.types.Money`
    price: typing.Optional["Money"]
    #: Optional :class:`bool` `(Named` ``isMatching`` `in Commercetools)`
    is_matching: typing.Optional[bool]

    def __init__(
        self,
        *,
        type: typing.Optional["ShippingRateTierType"] = None,
        minimum_cent_amount: typing.Optional[int] = None,
        price: typing.Optional["Money"] = None,
        is_matching: typing.Optional[bool] = None
    ) -> None:
        self.minimum_cent_amount = minimum_cent_amount
        self.price = price
        self.is_matching = is_matching
        super().__init__(type=ShippingRateTierType.CART_VALUE)

    def __repr__(self) -> str:
        return (
            "CartValueTier(type=%r, minimum_cent_amount=%r, price=%r, is_matching=%r)"
            % (self.type, self.minimum_cent_amount, self.price, self.is_matching)
        )


class ShippingMethodAddShippingRateAction(ShippingMethodUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ShippingMethodAddShippingRateActionSchema`."
    #: :class:`commercetools.types.ZoneResourceIdentifier`
    zone: typing.Optional["ZoneResourceIdentifier"]
    #: :class:`commercetools.types.ShippingRateDraft` `(Named` ``shippingRate`` `in Commercetools)`
    shipping_rate: typing.Optional["ShippingRateDraft"]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        zone: typing.Optional["ZoneResourceIdentifier"] = None,
        shipping_rate: typing.Optional["ShippingRateDraft"] = None
    ) -> None:
        self.zone = zone
        self.shipping_rate = shipping_rate
        super().__init__(action="addShippingRate")

    def __repr__(self) -> str:
        return (
            "ShippingMethodAddShippingRateAction(action=%r, zone=%r, shipping_rate=%r)"
            % (self.action, self.zone, self.shipping_rate)
        )


class ShippingMethodAddZoneAction(ShippingMethodUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ShippingMethodAddZoneActionSchema`."
    #: :class:`commercetools.types.ZoneResourceIdentifier`
    zone: typing.Optional["ZoneResourceIdentifier"]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        zone: typing.Optional["ZoneResourceIdentifier"] = None
    ) -> None:
        self.zone = zone
        super().__init__(action="addZone")

    def __repr__(self) -> str:
        return "ShippingMethodAddZoneAction(action=%r, zone=%r)" % (
            self.action,
            self.zone,
        )


class ShippingMethodChangeIsDefaultAction(ShippingMethodUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ShippingMethodChangeIsDefaultActionSchema`."
    #: :class:`bool` `(Named` ``isDefault`` `in Commercetools)`
    is_default: typing.Optional[bool]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        is_default: typing.Optional[bool] = None
    ) -> None:
        self.is_default = is_default
        super().__init__(action="changeIsDefault")

    def __repr__(self) -> str:
        return "ShippingMethodChangeIsDefaultAction(action=%r, is_default=%r)" % (
            self.action,
            self.is_default,
        )


class ShippingMethodChangeNameAction(ShippingMethodUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ShippingMethodChangeNameActionSchema`."
    #: :class:`str`
    name: typing.Optional[str]

    def __init__(
        self, *, action: typing.Optional[str] = None, name: typing.Optional[str] = None
    ) -> None:
        self.name = name
        super().__init__(action="changeName")

    def __repr__(self) -> str:
        return "ShippingMethodChangeNameAction(action=%r, name=%r)" % (
            self.action,
            self.name,
        )


class ShippingMethodChangeTaxCategoryAction(ShippingMethodUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ShippingMethodChangeTaxCategoryActionSchema`."
    #: :class:`commercetools.types.TaxCategoryResourceIdentifier` `(Named` ``taxCategory`` `in Commercetools)`
    tax_category: typing.Optional["TaxCategoryResourceIdentifier"]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        tax_category: typing.Optional["TaxCategoryResourceIdentifier"] = None
    ) -> None:
        self.tax_category = tax_category
        super().__init__(action="changeTaxCategory")

    def __repr__(self) -> str:
        return "ShippingMethodChangeTaxCategoryAction(action=%r, tax_category=%r)" % (
            self.action,
            self.tax_category,
        )


class ShippingMethodRemoveShippingRateAction(ShippingMethodUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ShippingMethodRemoveShippingRateActionSchema`."
    #: :class:`commercetools.types.ZoneResourceIdentifier`
    zone: typing.Optional["ZoneResourceIdentifier"]
    #: :class:`commercetools.types.ShippingRateDraft` `(Named` ``shippingRate`` `in Commercetools)`
    shipping_rate: typing.Optional["ShippingRateDraft"]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        zone: typing.Optional["ZoneResourceIdentifier"] = None,
        shipping_rate: typing.Optional["ShippingRateDraft"] = None
    ) -> None:
        self.zone = zone
        self.shipping_rate = shipping_rate
        super().__init__(action="removeShippingRate")

    def __repr__(self) -> str:
        return (
            "ShippingMethodRemoveShippingRateAction(action=%r, zone=%r, shipping_rate=%r)"
            % (self.action, self.zone, self.shipping_rate)
        )


class ShippingMethodRemoveZoneAction(ShippingMethodUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ShippingMethodRemoveZoneActionSchema`."
    #: :class:`commercetools.types.ZoneResourceIdentifier`
    zone: typing.Optional["ZoneResourceIdentifier"]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        zone: typing.Optional["ZoneResourceIdentifier"] = None
    ) -> None:
        self.zone = zone
        super().__init__(action="removeZone")

    def __repr__(self) -> str:
        return "ShippingMethodRemoveZoneAction(action=%r, zone=%r)" % (
            self.action,
            self.zone,
        )


class ShippingMethodSetDescriptionAction(ShippingMethodUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ShippingMethodSetDescriptionActionSchema`."
    #: Optional :class:`str`
    description: typing.Optional[str]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        description: typing.Optional[str] = None
    ) -> None:
        self.description = description
        super().__init__(action="setDescription")

    def __repr__(self) -> str:
        return "ShippingMethodSetDescriptionAction(action=%r, description=%r)" % (
            self.action,
            self.description,
        )


class ShippingMethodSetKeyAction(ShippingMethodUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ShippingMethodSetKeyActionSchema`."
    #: Optional :class:`str`
    key: typing.Optional[str]

    def __init__(
        self, *, action: typing.Optional[str] = None, key: typing.Optional[str] = None
    ) -> None:
        self.key = key
        super().__init__(action="setKey")

    def __repr__(self) -> str:
        return "ShippingMethodSetKeyAction(action=%r, key=%r)" % (self.action, self.key)


class ShippingMethodSetPredicateAction(ShippingMethodUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ShippingMethodSetPredicateActionSchema`."
    #: Optional :class:`str`
    predicate: typing.Optional[str]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        predicate: typing.Optional[str] = None
    ) -> None:
        self.predicate = predicate
        super().__init__(action="setPredicate")

    def __repr__(self) -> str:
        return "ShippingMethodSetPredicateAction(action=%r, predicate=%r)" % (
            self.action,
            self.predicate,
        )
