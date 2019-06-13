# DO NOT EDIT! This file is automatically generated

import datetime
import enum
import typing

from commercetools.types._abstract import _BaseType
from commercetools.types._common import (
    LoggedResource,
    PagedQueryResponse,
    Reference,
    ReferenceTypeId,
)

if typing.TYPE_CHECKING:
    from ._common import CreatedBy, LastModifiedBy, LocalizedString
__all__ = [
    "AttributeBooleanType",
    "AttributeConstraintEnum",
    "AttributeConstraintEnumDraft",
    "AttributeDateTimeType",
    "AttributeDateType",
    "AttributeDefinition",
    "AttributeDefinitionDraft",
    "AttributeEnumType",
    "AttributeLocalizableTextType",
    "AttributeLocalizedEnumType",
    "AttributeLocalizedEnumValue",
    "AttributeMoneyType",
    "AttributeNestedType",
    "AttributeNumberType",
    "AttributePlainEnumValue",
    "AttributeReferenceType",
    "AttributeSetType",
    "AttributeTextType",
    "AttributeTimeType",
    "AttributeType",
    "ProductType",
    "ProductTypeAddAttributeDefinitionAction",
    "ProductTypeAddLocalizedEnumValueAction",
    "ProductTypeAddPlainEnumValueAction",
    "ProductTypeChangeAttributeConstraintAction",
    "ProductTypeChangeAttributeNameAction",
    "ProductTypeChangeAttributeOrderAction",
    "ProductTypeChangeAttributeOrderByNameAction",
    "ProductTypeChangeDescriptionAction",
    "ProductTypeChangeEnumKeyAction",
    "ProductTypeChangeInputHintAction",
    "ProductTypeChangeIsSearchableAction",
    "ProductTypeChangeLabelAction",
    "ProductTypeChangeLocalizedEnumValueLabelAction",
    "ProductTypeChangeLocalizedEnumValueOrderAction",
    "ProductTypeChangeNameAction",
    "ProductTypeChangePlainEnumValueLabelAction",
    "ProductTypeChangePlainEnumValueOrderAction",
    "ProductTypeDraft",
    "ProductTypePagedQueryResponse",
    "ProductTypeReference",
    "ProductTypeRemoveAttributeDefinitionAction",
    "ProductTypeRemoveEnumValuesAction",
    "ProductTypeSetInputTipAction",
    "ProductTypeSetKeyAction",
    "ProductTypeUpdate",
    "ProductTypeUpdateAction",
    "TextInputHint",
]


class AttributeConstraintEnum(enum.Enum):
    NONE = "None"
    UNIQUE = "Unique"
    COMBINATION_UNIQUE = "CombinationUnique"
    SAME_FOR_ALL = "SameForAll"


class AttributeConstraintEnumDraft(enum.Enum):
    NONE = "None"


class AttributeDefinition(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.AttributeDefinitionSchema`."
    #: :class:`commercetools.types.AttributeType`
    type: typing.Optional["AttributeType"]
    #: :class:`str`
    name: typing.Optional[str]
    #: :class:`commercetools.types.LocalizedString`
    label: typing.Optional["LocalizedString"]
    #: :class:`bool` `(Named` ``isRequired`` `in Commercetools)`
    is_required: typing.Optional[bool]
    #: :class:`commercetools.types.AttributeConstraintEnum` `(Named` ``attributeConstraint`` `in Commercetools)`
    attribute_constraint: typing.Optional["AttributeConstraintEnum"]
    #: Optional :class:`commercetools.types.LocalizedString` `(Named` ``inputTip`` `in Commercetools)`
    input_tip: typing.Optional["LocalizedString"]
    #: :class:`commercetools.types.TextInputHint` `(Named` ``inputHint`` `in Commercetools)`
    input_hint: typing.Optional["TextInputHint"]
    #: :class:`bool` `(Named` ``isSearchable`` `in Commercetools)`
    is_searchable: typing.Optional[bool]

    def __init__(
        self,
        *,
        type: typing.Optional["AttributeType"] = None,
        name: typing.Optional[str] = None,
        label: typing.Optional["LocalizedString"] = None,
        is_required: typing.Optional[bool] = None,
        attribute_constraint: typing.Optional["AttributeConstraintEnum"] = None,
        input_tip: typing.Optional["LocalizedString"] = None,
        input_hint: typing.Optional["TextInputHint"] = None,
        is_searchable: typing.Optional[bool] = None
    ) -> None:
        self.type = type
        self.name = name
        self.label = label
        self.is_required = is_required
        self.attribute_constraint = attribute_constraint
        self.input_tip = input_tip
        self.input_hint = input_hint
        self.is_searchable = is_searchable
        super().__init__()

    def __repr__(self) -> str:
        return (
            "AttributeDefinition(type=%r, name=%r, label=%r, is_required=%r, attribute_constraint=%r, input_tip=%r, input_hint=%r, is_searchable=%r)"
            % (
                self.type,
                self.name,
                self.label,
                self.is_required,
                self.attribute_constraint,
                self.input_tip,
                self.input_hint,
                self.is_searchable,
            )
        )


class AttributeDefinitionDraft(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.AttributeDefinitionDraftSchema`."
    #: :class:`commercetools.types.AttributeType`
    type: typing.Optional["AttributeType"]
    #: :class:`str`
    name: typing.Optional[str]
    #: :class:`commercetools.types.LocalizedString`
    label: typing.Optional["LocalizedString"]
    #: :class:`bool` `(Named` ``isRequired`` `in Commercetools)`
    is_required: typing.Optional[bool]
    #: Optional :class:`commercetools.types.AttributeConstraintEnum` `(Named` ``attributeConstraint`` `in Commercetools)`
    attribute_constraint: typing.Optional["AttributeConstraintEnum"]
    #: Optional :class:`commercetools.types.LocalizedString` `(Named` ``inputTip`` `in Commercetools)`
    input_tip: typing.Optional["LocalizedString"]
    #: Optional :class:`commercetools.types.TextInputHint` `(Named` ``inputHint`` `in Commercetools)`
    input_hint: typing.Optional["TextInputHint"]
    #: Optional :class:`bool` `(Named` ``isSearchable`` `in Commercetools)`
    is_searchable: typing.Optional[bool]

    def __init__(
        self,
        *,
        type: typing.Optional["AttributeType"] = None,
        name: typing.Optional[str] = None,
        label: typing.Optional["LocalizedString"] = None,
        is_required: typing.Optional[bool] = None,
        attribute_constraint: typing.Optional["AttributeConstraintEnum"] = None,
        input_tip: typing.Optional["LocalizedString"] = None,
        input_hint: typing.Optional["TextInputHint"] = None,
        is_searchable: typing.Optional[bool] = None
    ) -> None:
        self.type = type
        self.name = name
        self.label = label
        self.is_required = is_required
        self.attribute_constraint = attribute_constraint
        self.input_tip = input_tip
        self.input_hint = input_hint
        self.is_searchable = is_searchable
        super().__init__()

    def __repr__(self) -> str:
        return (
            "AttributeDefinitionDraft(type=%r, name=%r, label=%r, is_required=%r, attribute_constraint=%r, input_tip=%r, input_hint=%r, is_searchable=%r)"
            % (
                self.type,
                self.name,
                self.label,
                self.is_required,
                self.attribute_constraint,
                self.input_tip,
                self.input_hint,
                self.is_searchable,
            )
        )


class AttributeLocalizedEnumValue(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.AttributeLocalizedEnumValueSchema`."
    #: :class:`str`
    key: typing.Optional[str]
    #: :class:`commercetools.types.LocalizedString`
    label: typing.Optional["LocalizedString"]

    def __init__(
        self,
        *,
        key: typing.Optional[str] = None,
        label: typing.Optional["LocalizedString"] = None
    ) -> None:
        self.key = key
        self.label = label
        super().__init__()

    def __repr__(self) -> str:
        return "AttributeLocalizedEnumValue(key=%r, label=%r)" % (self.key, self.label)


class AttributePlainEnumValue(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.AttributePlainEnumValueSchema`."
    #: :class:`str`
    key: typing.Optional[str]
    #: :class:`str`
    label: typing.Optional[str]

    def __init__(
        self, *, key: typing.Optional[str] = None, label: typing.Optional[str] = None
    ) -> None:
        self.key = key
        self.label = label
        super().__init__()

    def __repr__(self) -> str:
        return "AttributePlainEnumValue(key=%r, label=%r)" % (self.key, self.label)


class AttributeType(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.AttributeTypeSchema`."
    #: :class:`str`
    name: typing.Optional[str]

    def __init__(self, *, name: typing.Optional[str] = None) -> None:
        self.name = name
        super().__init__()

    def __repr__(self) -> str:
        return "AttributeType(name=%r)" % (self.name,)


class ProductType(LoggedResource):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ProductTypeSchema`."
    #: Optional :class:`str`
    key: typing.Optional[str]
    #: :class:`str`
    name: typing.Optional[str]
    #: :class:`str`
    description: typing.Optional[str]
    #: Optional list of :class:`commercetools.types.AttributeDefinition`
    attributes: typing.Optional[typing.List["AttributeDefinition"]]

    def __init__(
        self,
        *,
        id: typing.Optional[str] = None,
        version: typing.Optional[int] = None,
        created_at: typing.Optional[datetime.datetime] = None,
        last_modified_at: typing.Optional[datetime.datetime] = None,
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        key: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        attributes: typing.Optional[typing.List["AttributeDefinition"]] = None
    ) -> None:
        self.key = key
        self.name = name
        self.description = description
        self.attributes = attributes
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
            "ProductType(id=%r, version=%r, created_at=%r, last_modified_at=%r, last_modified_by=%r, created_by=%r, key=%r, name=%r, description=%r, attributes=%r)"
            % (
                self.id,
                self.version,
                self.created_at,
                self.last_modified_at,
                self.last_modified_by,
                self.created_by,
                self.key,
                self.name,
                self.description,
                self.attributes,
            )
        )


class ProductTypeDraft(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ProductTypeDraftSchema`."
    #: Optional :class:`str`
    key: typing.Optional[str]
    #: :class:`str`
    name: typing.Optional[str]
    #: :class:`str`
    description: typing.Optional[str]
    #: Optional list of :class:`commercetools.types.AttributeDefinitionDraft`
    attributes: typing.Optional[typing.List["AttributeDefinitionDraft"]]

    def __init__(
        self,
        *,
        key: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        attributes: typing.Optional[typing.List["AttributeDefinitionDraft"]] = None
    ) -> None:
        self.key = key
        self.name = name
        self.description = description
        self.attributes = attributes
        super().__init__()

    def __repr__(self) -> str:
        return "ProductTypeDraft(key=%r, name=%r, description=%r, attributes=%r)" % (
            self.key,
            self.name,
            self.description,
            self.attributes,
        )


class ProductTypePagedQueryResponse(PagedQueryResponse):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ProductTypePagedQueryResponseSchema`."
    #: List of :class:`commercetools.types.ProductType`
    results: typing.Optional[typing.Sequence["ProductType"]]

    def __init__(
        self,
        *,
        count: typing.Optional[int] = None,
        total: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        results: typing.Optional[typing.Sequence["ProductType"]] = None
    ) -> None:
        self.results = results
        super().__init__(count=count, total=total, offset=offset, results=results)

    def __repr__(self) -> str:
        return (
            "ProductTypePagedQueryResponse(count=%r, total=%r, offset=%r, results=%r)"
            % (self.count, self.total, self.offset, self.results)
        )


class ProductTypeReference(Reference):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ProductTypeReferenceSchema`."
    #: Optional :class:`commercetools.types.ProductType`
    obj: typing.Optional["ProductType"]

    def __init__(
        self,
        *,
        type_id: typing.Optional["ReferenceTypeId"] = None,
        id: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        obj: typing.Optional["ProductType"] = None
    ) -> None:
        self.obj = obj
        super().__init__(type_id=ReferenceTypeId.PRODUCT_TYPE, id=id, key=key)

    def __repr__(self) -> str:
        return "ProductTypeReference(type_id=%r, id=%r, key=%r, obj=%r)" % (
            self.type_id,
            self.id,
            self.key,
            self.obj,
        )


class ProductTypeUpdate(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ProductTypeUpdateSchema`."
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
        return "ProductTypeUpdate(version=%r, actions=%r)" % (
            self.version,
            self.actions,
        )


class ProductTypeUpdateAction(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ProductTypeUpdateActionSchema`."
    #: :class:`str`
    action: typing.Optional[str]

    def __init__(self, *, action: typing.Optional[str] = None) -> None:
        self.action = action
        super().__init__()

    def __repr__(self) -> str:
        return "ProductTypeUpdateAction(action=%r)" % (self.action,)


class TextInputHint(enum.Enum):
    SINGLE_LINE = "SingleLine"
    MULTI_LINE = "MultiLine"


class AttributeBooleanType(AttributeType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.AttributeBooleanTypeSchema`."

    def __init__(self, *, name: typing.Optional[str] = None) -> None:
        super().__init__(name="boolean")

    def __repr__(self) -> str:
        return "AttributeBooleanType(name=%r)" % (self.name,)


class AttributeDateTimeType(AttributeType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.AttributeDateTimeTypeSchema`."

    def __init__(self, *, name: typing.Optional[str] = None) -> None:
        super().__init__(name="datetime")

    def __repr__(self) -> str:
        return "AttributeDateTimeType(name=%r)" % (self.name,)


class AttributeDateType(AttributeType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.AttributeDateTypeSchema`."

    def __init__(self, *, name: typing.Optional[str] = None) -> None:
        super().__init__(name="date")

    def __repr__(self) -> str:
        return "AttributeDateType(name=%r)" % (self.name,)


class AttributeEnumType(AttributeType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.AttributeEnumTypeSchema`."
    #: List of :class:`commercetools.types.AttributePlainEnumValue`
    values: typing.Optional[typing.List["AttributePlainEnumValue"]]

    def __init__(
        self,
        *,
        name: typing.Optional[str] = None,
        values: typing.Optional[typing.List["AttributePlainEnumValue"]] = None
    ) -> None:
        self.values = values
        super().__init__(name="enum")

    def __repr__(self) -> str:
        return "AttributeEnumType(name=%r, values=%r)" % (self.name, self.values)


class AttributeLocalizableTextType(AttributeType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.AttributeLocalizableTextTypeSchema`."

    def __init__(self, *, name: typing.Optional[str] = None) -> None:
        super().__init__(name="ltext")

    def __repr__(self) -> str:
        return "AttributeLocalizableTextType(name=%r)" % (self.name,)


class AttributeLocalizedEnumType(AttributeType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.AttributeLocalizedEnumTypeSchema`."
    #: List of :class:`commercetools.types.AttributeLocalizedEnumValue`
    values: typing.Optional[typing.List["AttributeLocalizedEnumValue"]]

    def __init__(
        self,
        *,
        name: typing.Optional[str] = None,
        values: typing.Optional[typing.List["AttributeLocalizedEnumValue"]] = None
    ) -> None:
        self.values = values
        super().__init__(name="lenum")

    def __repr__(self) -> str:
        return "AttributeLocalizedEnumType(name=%r, values=%r)" % (
            self.name,
            self.values,
        )


class AttributeMoneyType(AttributeType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.AttributeMoneyTypeSchema`."

    def __init__(self, *, name: typing.Optional[str] = None) -> None:
        super().__init__(name="money")

    def __repr__(self) -> str:
        return "AttributeMoneyType(name=%r)" % (self.name,)


class AttributeNestedType(AttributeType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.AttributeNestedTypeSchema`."
    #: :class:`commercetools.types.ProductTypeReference` `(Named` ``typeReference`` `in Commercetools)`
    type_reference: typing.Optional["ProductTypeReference"]

    def __init__(
        self,
        *,
        name: typing.Optional[str] = None,
        type_reference: typing.Optional["ProductTypeReference"] = None
    ) -> None:
        self.type_reference = type_reference
        super().__init__(name="nested")

    def __repr__(self) -> str:
        return "AttributeNestedType(name=%r, type_reference=%r)" % (
            self.name,
            self.type_reference,
        )


class AttributeNumberType(AttributeType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.AttributeNumberTypeSchema`."

    def __init__(self, *, name: typing.Optional[str] = None) -> None:
        super().__init__(name="number")

    def __repr__(self) -> str:
        return "AttributeNumberType(name=%r)" % (self.name,)


class AttributeReferenceType(AttributeType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.AttributeReferenceTypeSchema`."
    #: :class:`commercetools.types.ReferenceTypeId` `(Named` ``referenceTypeId`` `in Commercetools)`
    reference_type_id: typing.Optional["ReferenceTypeId"]

    def __init__(
        self,
        *,
        name: typing.Optional[str] = None,
        reference_type_id: typing.Optional["ReferenceTypeId"] = None
    ) -> None:
        self.reference_type_id = reference_type_id
        super().__init__(name="reference")

    def __repr__(self) -> str:
        return "AttributeReferenceType(name=%r, reference_type_id=%r)" % (
            self.name,
            self.reference_type_id,
        )


class AttributeSetType(AttributeType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.AttributeSetTypeSchema`."
    #: :class:`commercetools.types.AttributeType` `(Named` ``elementType`` `in Commercetools)`
    element_type: typing.Optional["AttributeType"]

    def __init__(
        self,
        *,
        name: typing.Optional[str] = None,
        element_type: typing.Optional["AttributeType"] = None
    ) -> None:
        self.element_type = element_type
        super().__init__(name="set")

    def __repr__(self) -> str:
        return "AttributeSetType(name=%r, element_type=%r)" % (
            self.name,
            self.element_type,
        )


class AttributeTextType(AttributeType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.AttributeTextTypeSchema`."

    def __init__(self, *, name: typing.Optional[str] = None) -> None:
        super().__init__(name="text")

    def __repr__(self) -> str:
        return "AttributeTextType(name=%r)" % (self.name,)


class AttributeTimeType(AttributeType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.AttributeTimeTypeSchema`."

    def __init__(self, *, name: typing.Optional[str] = None) -> None:
        super().__init__(name="time")

    def __repr__(self) -> str:
        return "AttributeTimeType(name=%r)" % (self.name,)


class ProductTypeAddAttributeDefinitionAction(ProductTypeUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ProductTypeAddAttributeDefinitionActionSchema`."
    #: :class:`commercetools.types.AttributeDefinitionDraft`
    attribute: typing.Optional["AttributeDefinitionDraft"]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        attribute: typing.Optional["AttributeDefinitionDraft"] = None
    ) -> None:
        self.attribute = attribute
        super().__init__(action="addAttributeDefinition")

    def __repr__(self) -> str:
        return "ProductTypeAddAttributeDefinitionAction(action=%r, attribute=%r)" % (
            self.action,
            self.attribute,
        )


class ProductTypeAddLocalizedEnumValueAction(ProductTypeUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ProductTypeAddLocalizedEnumValueActionSchema`."
    #: :class:`str` `(Named` ``attributeName`` `in Commercetools)`
    attribute_name: typing.Optional[str]
    #: :class:`commercetools.types.AttributeLocalizedEnumValue`
    value: typing.Optional["AttributeLocalizedEnumValue"]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        attribute_name: typing.Optional[str] = None,
        value: typing.Optional["AttributeLocalizedEnumValue"] = None
    ) -> None:
        self.attribute_name = attribute_name
        self.value = value
        super().__init__(action="addLocalizedEnumValue")

    def __repr__(self) -> str:
        return (
            "ProductTypeAddLocalizedEnumValueAction(action=%r, attribute_name=%r, value=%r)"
            % (self.action, self.attribute_name, self.value)
        )


class ProductTypeAddPlainEnumValueAction(ProductTypeUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ProductTypeAddPlainEnumValueActionSchema`."
    #: :class:`str` `(Named` ``attributeName`` `in Commercetools)`
    attribute_name: typing.Optional[str]
    #: :class:`commercetools.types.AttributePlainEnumValue`
    value: typing.Optional["AttributePlainEnumValue"]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        attribute_name: typing.Optional[str] = None,
        value: typing.Optional["AttributePlainEnumValue"] = None
    ) -> None:
        self.attribute_name = attribute_name
        self.value = value
        super().__init__(action="addPlainEnumValue")

    def __repr__(self) -> str:
        return (
            "ProductTypeAddPlainEnumValueAction(action=%r, attribute_name=%r, value=%r)"
            % (self.action, self.attribute_name, self.value)
        )


class ProductTypeChangeAttributeConstraintAction(ProductTypeUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ProductTypeChangeAttributeConstraintActionSchema`."
    #: :class:`str` `(Named` ``attributeName`` `in Commercetools)`
    attribute_name: typing.Optional[str]
    #: :class:`commercetools.types.AttributeConstraintEnumDraft` `(Named` ``newValue`` `in Commercetools)`
    new_value: typing.Optional["AttributeConstraintEnumDraft"]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        attribute_name: typing.Optional[str] = None,
        new_value: typing.Optional["AttributeConstraintEnumDraft"] = None
    ) -> None:
        self.attribute_name = attribute_name
        self.new_value = new_value
        super().__init__(action="changeAttributeConstraint")

    def __repr__(self) -> str:
        return (
            "ProductTypeChangeAttributeConstraintAction(action=%r, attribute_name=%r, new_value=%r)"
            % (self.action, self.attribute_name, self.new_value)
        )


class ProductTypeChangeAttributeNameAction(ProductTypeUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ProductTypeChangeAttributeNameActionSchema`."
    #: :class:`str` `(Named` ``attributeName`` `in Commercetools)`
    attribute_name: typing.Optional[str]
    #: :class:`str` `(Named` ``newAttributeName`` `in Commercetools)`
    new_attribute_name: typing.Optional[str]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        attribute_name: typing.Optional[str] = None,
        new_attribute_name: typing.Optional[str] = None
    ) -> None:
        self.attribute_name = attribute_name
        self.new_attribute_name = new_attribute_name
        super().__init__(action="changeAttributeName")

    def __repr__(self) -> str:
        return (
            "ProductTypeChangeAttributeNameAction(action=%r, attribute_name=%r, new_attribute_name=%r)"
            % (self.action, self.attribute_name, self.new_attribute_name)
        )


class ProductTypeChangeAttributeOrderAction(ProductTypeUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ProductTypeChangeAttributeOrderActionSchema`."
    #: List of :class:`commercetools.types.AttributeDefinition`
    attributes: typing.Optional[typing.List["AttributeDefinition"]]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        attributes: typing.Optional[typing.List["AttributeDefinition"]] = None
    ) -> None:
        self.attributes = attributes
        super().__init__(action="changeAttributeOrder")

    def __repr__(self) -> str:
        return "ProductTypeChangeAttributeOrderAction(action=%r, attributes=%r)" % (
            self.action,
            self.attributes,
        )


class ProductTypeChangeAttributeOrderByNameAction(ProductTypeUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ProductTypeChangeAttributeOrderByNameActionSchema`."
    #: List of :class:`str` `(Named` ``attributeNames`` `in Commercetools)`
    attribute_names: typing.Optional[typing.List[str]]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        attribute_names: typing.Optional[typing.List[str]] = None
    ) -> None:
        self.attribute_names = attribute_names
        super().__init__(action="changeAttributeOrderByName")

    def __repr__(self) -> str:
        return (
            "ProductTypeChangeAttributeOrderByNameAction(action=%r, attribute_names=%r)"
            % (self.action, self.attribute_names)
        )


class ProductTypeChangeDescriptionAction(ProductTypeUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ProductTypeChangeDescriptionActionSchema`."
    #: :class:`str`
    description: typing.Optional[str]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        description: typing.Optional[str] = None
    ) -> None:
        self.description = description
        super().__init__(action="changeDescription")

    def __repr__(self) -> str:
        return "ProductTypeChangeDescriptionAction(action=%r, description=%r)" % (
            self.action,
            self.description,
        )


class ProductTypeChangeEnumKeyAction(ProductTypeUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ProductTypeChangeEnumKeyActionSchema`."
    #: :class:`str` `(Named` ``attributeName`` `in Commercetools)`
    attribute_name: typing.Optional[str]
    #: :class:`str`
    key: typing.Optional[str]
    #: :class:`str` `(Named` ``newKey`` `in Commercetools)`
    new_key: typing.Optional[str]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        attribute_name: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        new_key: typing.Optional[str] = None
    ) -> None:
        self.attribute_name = attribute_name
        self.key = key
        self.new_key = new_key
        super().__init__(action="changeEnumKey")

    def __repr__(self) -> str:
        return (
            "ProductTypeChangeEnumKeyAction(action=%r, attribute_name=%r, key=%r, new_key=%r)"
            % (self.action, self.attribute_name, self.key, self.new_key)
        )


class ProductTypeChangeInputHintAction(ProductTypeUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ProductTypeChangeInputHintActionSchema`."
    #: :class:`str` `(Named` ``attributeName`` `in Commercetools)`
    attribute_name: typing.Optional[str]
    #: :class:`commercetools.types.TextInputHint` `(Named` ``newValue`` `in Commercetools)`
    new_value: typing.Optional["TextInputHint"]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        attribute_name: typing.Optional[str] = None,
        new_value: typing.Optional["TextInputHint"] = None
    ) -> None:
        self.attribute_name = attribute_name
        self.new_value = new_value
        super().__init__(action="changeInputHint")

    def __repr__(self) -> str:
        return (
            "ProductTypeChangeInputHintAction(action=%r, attribute_name=%r, new_value=%r)"
            % (self.action, self.attribute_name, self.new_value)
        )


class ProductTypeChangeIsSearchableAction(ProductTypeUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ProductTypeChangeIsSearchableActionSchema`."
    #: :class:`str` `(Named` ``attributeName`` `in Commercetools)`
    attribute_name: typing.Optional[str]
    #: :class:`bool` `(Named` ``isSearchable`` `in Commercetools)`
    is_searchable: typing.Optional[bool]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        attribute_name: typing.Optional[str] = None,
        is_searchable: typing.Optional[bool] = None
    ) -> None:
        self.attribute_name = attribute_name
        self.is_searchable = is_searchable
        super().__init__(action="changeIsSearchable")

    def __repr__(self) -> str:
        return (
            "ProductTypeChangeIsSearchableAction(action=%r, attribute_name=%r, is_searchable=%r)"
            % (self.action, self.attribute_name, self.is_searchable)
        )


class ProductTypeChangeLabelAction(ProductTypeUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ProductTypeChangeLabelActionSchema`."
    #: :class:`str` `(Named` ``attributeName`` `in Commercetools)`
    attribute_name: typing.Optional[str]
    #: :class:`commercetools.types.LocalizedString`
    label: typing.Optional["LocalizedString"]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        attribute_name: typing.Optional[str] = None,
        label: typing.Optional["LocalizedString"] = None
    ) -> None:
        self.attribute_name = attribute_name
        self.label = label
        super().__init__(action="changeLabel")

    def __repr__(self) -> str:
        return (
            "ProductTypeChangeLabelAction(action=%r, attribute_name=%r, label=%r)"
            % (self.action, self.attribute_name, self.label)
        )


class ProductTypeChangeLocalizedEnumValueLabelAction(ProductTypeUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ProductTypeChangeLocalizedEnumValueLabelActionSchema`."
    #: :class:`str` `(Named` ``attributeName`` `in Commercetools)`
    attribute_name: typing.Optional[str]
    #: :class:`commercetools.types.AttributeLocalizedEnumValue` `(Named` ``newValue`` `in Commercetools)`
    new_value: typing.Optional["AttributeLocalizedEnumValue"]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        attribute_name: typing.Optional[str] = None,
        new_value: typing.Optional["AttributeLocalizedEnumValue"] = None
    ) -> None:
        self.attribute_name = attribute_name
        self.new_value = new_value
        super().__init__(action="changeLocalizedEnumValueLabel")

    def __repr__(self) -> str:
        return (
            "ProductTypeChangeLocalizedEnumValueLabelAction(action=%r, attribute_name=%r, new_value=%r)"
            % (self.action, self.attribute_name, self.new_value)
        )


class ProductTypeChangeLocalizedEnumValueOrderAction(ProductTypeUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ProductTypeChangeLocalizedEnumValueOrderActionSchema`."
    #: :class:`str` `(Named` ``attributeName`` `in Commercetools)`
    attribute_name: typing.Optional[str]
    #: List of :class:`commercetools.types.AttributeLocalizedEnumValue`
    values: typing.Optional[typing.List["AttributeLocalizedEnumValue"]]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        attribute_name: typing.Optional[str] = None,
        values: typing.Optional[typing.List["AttributeLocalizedEnumValue"]] = None
    ) -> None:
        self.attribute_name = attribute_name
        self.values = values
        super().__init__(action="changeLocalizedEnumValueOrder")

    def __repr__(self) -> str:
        return (
            "ProductTypeChangeLocalizedEnumValueOrderAction(action=%r, attribute_name=%r, values=%r)"
            % (self.action, self.attribute_name, self.values)
        )


class ProductTypeChangeNameAction(ProductTypeUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ProductTypeChangeNameActionSchema`."
    #: :class:`str`
    name: typing.Optional[str]

    def __init__(
        self, *, action: typing.Optional[str] = None, name: typing.Optional[str] = None
    ) -> None:
        self.name = name
        super().__init__(action="changeName")

    def __repr__(self) -> str:
        return "ProductTypeChangeNameAction(action=%r, name=%r)" % (
            self.action,
            self.name,
        )


class ProductTypeChangePlainEnumValueLabelAction(ProductTypeUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ProductTypeChangePlainEnumValueLabelActionSchema`."
    #: :class:`str` `(Named` ``attributeName`` `in Commercetools)`
    attribute_name: typing.Optional[str]
    #: :class:`commercetools.types.AttributePlainEnumValue` `(Named` ``newValue`` `in Commercetools)`
    new_value: typing.Optional["AttributePlainEnumValue"]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        attribute_name: typing.Optional[str] = None,
        new_value: typing.Optional["AttributePlainEnumValue"] = None
    ) -> None:
        self.attribute_name = attribute_name
        self.new_value = new_value
        super().__init__(action="changePlainEnumValueLabel")

    def __repr__(self) -> str:
        return (
            "ProductTypeChangePlainEnumValueLabelAction(action=%r, attribute_name=%r, new_value=%r)"
            % (self.action, self.attribute_name, self.new_value)
        )


class ProductTypeChangePlainEnumValueOrderAction(ProductTypeUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ProductTypeChangePlainEnumValueOrderActionSchema`."
    #: :class:`str` `(Named` ``attributeName`` `in Commercetools)`
    attribute_name: typing.Optional[str]
    #: List of :class:`commercetools.types.AttributePlainEnumValue`
    values: typing.Optional[typing.List["AttributePlainEnumValue"]]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        attribute_name: typing.Optional[str] = None,
        values: typing.Optional[typing.List["AttributePlainEnumValue"]] = None
    ) -> None:
        self.attribute_name = attribute_name
        self.values = values
        super().__init__(action="changePlainEnumValueOrder")

    def __repr__(self) -> str:
        return (
            "ProductTypeChangePlainEnumValueOrderAction(action=%r, attribute_name=%r, values=%r)"
            % (self.action, self.attribute_name, self.values)
        )


class ProductTypeRemoveAttributeDefinitionAction(ProductTypeUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ProductTypeRemoveAttributeDefinitionActionSchema`."
    #: :class:`str`
    name: typing.Optional[str]

    def __init__(
        self, *, action: typing.Optional[str] = None, name: typing.Optional[str] = None
    ) -> None:
        self.name = name
        super().__init__(action="removeAttributeDefinition")

    def __repr__(self) -> str:
        return "ProductTypeRemoveAttributeDefinitionAction(action=%r, name=%r)" % (
            self.action,
            self.name,
        )


class ProductTypeRemoveEnumValuesAction(ProductTypeUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ProductTypeRemoveEnumValuesActionSchema`."
    #: :class:`str` `(Named` ``attributeName`` `in Commercetools)`
    attribute_name: typing.Optional[str]
    #: List of :class:`str`
    keys: typing.Optional[typing.List[str]]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        attribute_name: typing.Optional[str] = None,
        keys: typing.Optional[typing.List[str]] = None
    ) -> None:
        self.attribute_name = attribute_name
        self.keys = keys
        super().__init__(action="removeEnumValues")

    def __repr__(self) -> str:
        return (
            "ProductTypeRemoveEnumValuesAction(action=%r, attribute_name=%r, keys=%r)"
            % (self.action, self.attribute_name, self.keys)
        )


class ProductTypeSetInputTipAction(ProductTypeUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ProductTypeSetInputTipActionSchema`."
    #: :class:`str` `(Named` ``attributeName`` `in Commercetools)`
    attribute_name: typing.Optional[str]
    #: Optional :class:`commercetools.types.LocalizedString` `(Named` ``inputTip`` `in Commercetools)`
    input_tip: typing.Optional["LocalizedString"]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        attribute_name: typing.Optional[str] = None,
        input_tip: typing.Optional["LocalizedString"] = None
    ) -> None:
        self.attribute_name = attribute_name
        self.input_tip = input_tip
        super().__init__(action="setInputTip")

    def __repr__(self) -> str:
        return (
            "ProductTypeSetInputTipAction(action=%r, attribute_name=%r, input_tip=%r)"
            % (self.action, self.attribute_name, self.input_tip)
        )


class ProductTypeSetKeyAction(ProductTypeUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ProductTypeSetKeyActionSchema`."
    #: Optional :class:`str`
    key: typing.Optional[str]

    def __init__(
        self, *, action: typing.Optional[str] = None, key: typing.Optional[str] = None
    ) -> None:
        self.key = key
        super().__init__(action="setKey")

    def __repr__(self) -> str:
        return "ProductTypeSetKeyAction(action=%r, key=%r)" % (self.action, self.key)
