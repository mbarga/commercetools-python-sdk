# DO NOT EDIT! This file is automatically generated

import datetime
import typing

from commercetools.types._abstract import _BaseType
from commercetools.types._common import (
    LoggedResource,
    Reference,
    ReferenceTypeId,
    ResourceIdentifier,
)

if typing.TYPE_CHECKING:
    from ._common import (
        Asset,
        AssetDraft,
        AssetSource,
        CreatedBy,
        LastModifiedBy,
        LocalizedString,
    )
    from ._type import (
        CustomFields,
        CustomFieldsDraft,
        FieldContainer,
        TypeResourceIdentifier,
    )
__all__ = [
    "Category",
    "CategoryAddAssetAction",
    "CategoryChangeAssetNameAction",
    "CategoryChangeAssetOrderAction",
    "CategoryChangeNameAction",
    "CategoryChangeOrderHintAction",
    "CategoryChangeParentAction",
    "CategoryChangeSlugAction",
    "CategoryDraft",
    "CategoryPagedQueryResponse",
    "CategoryReference",
    "CategoryRemoveAssetAction",
    "CategoryResourceIdentifier",
    "CategorySetAssetCustomFieldAction",
    "CategorySetAssetCustomTypeAction",
    "CategorySetAssetDescriptionAction",
    "CategorySetAssetKeyAction",
    "CategorySetAssetSourcesAction",
    "CategorySetAssetTagsAction",
    "CategorySetCustomFieldAction",
    "CategorySetCustomTypeAction",
    "CategorySetDescriptionAction",
    "CategorySetExternalIdAction",
    "CategorySetKeyAction",
    "CategorySetMetaDescriptionAction",
    "CategorySetMetaKeywordsAction",
    "CategorySetMetaTitleAction",
    "CategoryUpdate",
    "CategoryUpdateAction",
]


class Category(LoggedResource):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CategorySchema`."
    #: :class:`commercetools.types.LocalizedString`
    name: typing.Optional["LocalizedString"]
    #: :class:`commercetools.types.LocalizedString`
    slug: typing.Optional["LocalizedString"]
    #: Optional :class:`commercetools.types.LocalizedString`
    description: typing.Optional["LocalizedString"]
    #: List of :class:`commercetools.types.CategoryReference`
    ancestors: typing.Optional[typing.List["CategoryReference"]]
    #: Optional :class:`commercetools.types.CategoryReference`
    parent: typing.Optional["CategoryReference"]
    #: :class:`str` `(Named` ``orderHint`` `in Commercetools)`
    order_hint: typing.Optional[str]
    #: Optional :class:`str` `(Named` ``externalId`` `in Commercetools)`
    external_id: typing.Optional[str]
    #: Optional :class:`commercetools.types.LocalizedString` `(Named` ``metaTitle`` `in Commercetools)`
    meta_title: typing.Optional["LocalizedString"]
    #: Optional :class:`commercetools.types.LocalizedString` `(Named` ``metaDescription`` `in Commercetools)`
    meta_description: typing.Optional["LocalizedString"]
    #: Optional :class:`commercetools.types.LocalizedString` `(Named` ``metaKeywords`` `in Commercetools)`
    meta_keywords: typing.Optional["LocalizedString"]
    #: Optional :class:`commercetools.types.CustomFields`
    custom: typing.Optional["CustomFields"]
    #: Optional list of :class:`commercetools.types.Asset`
    assets: typing.Optional[typing.List["Asset"]]
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
        name: typing.Optional["LocalizedString"] = None,
        slug: typing.Optional["LocalizedString"] = None,
        description: typing.Optional["LocalizedString"] = None,
        ancestors: typing.Optional[typing.List["CategoryReference"]] = None,
        parent: typing.Optional["CategoryReference"] = None,
        order_hint: typing.Optional[str] = None,
        external_id: typing.Optional[str] = None,
        meta_title: typing.Optional["LocalizedString"] = None,
        meta_description: typing.Optional["LocalizedString"] = None,
        meta_keywords: typing.Optional["LocalizedString"] = None,
        custom: typing.Optional["CustomFields"] = None,
        assets: typing.Optional[typing.List["Asset"]] = None,
        key: typing.Optional[str] = None
    ) -> None:
        self.name = name
        self.slug = slug
        self.description = description
        self.ancestors = ancestors
        self.parent = parent
        self.order_hint = order_hint
        self.external_id = external_id
        self.meta_title = meta_title
        self.meta_description = meta_description
        self.meta_keywords = meta_keywords
        self.custom = custom
        self.assets = assets
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
            "Category(id=%r, version=%r, created_at=%r, last_modified_at=%r, last_modified_by=%r, created_by=%r, name=%r, slug=%r, description=%r, ancestors=%r, parent=%r, order_hint=%r, external_id=%r, meta_title=%r, meta_description=%r, meta_keywords=%r, custom=%r, assets=%r, key=%r)"
            % (
                self.id,
                self.version,
                self.created_at,
                self.last_modified_at,
                self.last_modified_by,
                self.created_by,
                self.name,
                self.slug,
                self.description,
                self.ancestors,
                self.parent,
                self.order_hint,
                self.external_id,
                self.meta_title,
                self.meta_description,
                self.meta_keywords,
                self.custom,
                self.assets,
                self.key,
            )
        )


class CategoryDraft(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CategoryDraftSchema`."
    #: :class:`commercetools.types.LocalizedString`
    name: typing.Optional["LocalizedString"]
    #: :class:`commercetools.types.LocalizedString`
    slug: typing.Optional["LocalizedString"]
    #: Optional :class:`commercetools.types.LocalizedString`
    description: typing.Optional["LocalizedString"]
    #: Optional :class:`commercetools.types.CategoryResourceIdentifier`
    parent: typing.Optional["CategoryResourceIdentifier"]
    #: Optional :class:`str` `(Named` ``orderHint`` `in Commercetools)`
    order_hint: typing.Optional[str]
    #: Optional :class:`str` `(Named` ``externalId`` `in Commercetools)`
    external_id: typing.Optional[str]
    #: Optional :class:`commercetools.types.LocalizedString` `(Named` ``metaTitle`` `in Commercetools)`
    meta_title: typing.Optional["LocalizedString"]
    #: Optional :class:`commercetools.types.LocalizedString` `(Named` ``metaDescription`` `in Commercetools)`
    meta_description: typing.Optional["LocalizedString"]
    #: Optional :class:`commercetools.types.LocalizedString` `(Named` ``metaKeywords`` `in Commercetools)`
    meta_keywords: typing.Optional["LocalizedString"]
    #: Optional :class:`commercetools.types.CustomFieldsDraft`
    custom: typing.Optional["CustomFieldsDraft"]
    #: Optional list of :class:`commercetools.types.AssetDraft`
    assets: typing.Optional[typing.List["AssetDraft"]]
    #: Optional :class:`str`
    key: typing.Optional[str]

    def __init__(
        self,
        *,
        name: typing.Optional["LocalizedString"] = None,
        slug: typing.Optional["LocalizedString"] = None,
        description: typing.Optional["LocalizedString"] = None,
        parent: typing.Optional["CategoryResourceIdentifier"] = None,
        order_hint: typing.Optional[str] = None,
        external_id: typing.Optional[str] = None,
        meta_title: typing.Optional["LocalizedString"] = None,
        meta_description: typing.Optional["LocalizedString"] = None,
        meta_keywords: typing.Optional["LocalizedString"] = None,
        custom: typing.Optional["CustomFieldsDraft"] = None,
        assets: typing.Optional[typing.List["AssetDraft"]] = None,
        key: typing.Optional[str] = None
    ) -> None:
        self.name = name
        self.slug = slug
        self.description = description
        self.parent = parent
        self.order_hint = order_hint
        self.external_id = external_id
        self.meta_title = meta_title
        self.meta_description = meta_description
        self.meta_keywords = meta_keywords
        self.custom = custom
        self.assets = assets
        self.key = key
        super().__init__()

    def __repr__(self) -> str:
        return (
            "CategoryDraft(name=%r, slug=%r, description=%r, parent=%r, order_hint=%r, external_id=%r, meta_title=%r, meta_description=%r, meta_keywords=%r, custom=%r, assets=%r, key=%r)"
            % (
                self.name,
                self.slug,
                self.description,
                self.parent,
                self.order_hint,
                self.external_id,
                self.meta_title,
                self.meta_description,
                self.meta_keywords,
                self.custom,
                self.assets,
                self.key,
            )
        )


class CategoryPagedQueryResponse(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CategoryPagedQueryResponseSchema`."
    #: :class:`int`
    count: typing.Optional[int]
    #: Optional :class:`int`
    total: typing.Optional[int]
    #: :class:`int`
    offset: typing.Optional[int]
    #: List of :class:`commercetools.types.Category`
    results: typing.Optional[typing.Sequence["Category"]]

    def __init__(
        self,
        *,
        count: typing.Optional[int] = None,
        total: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        results: typing.Optional[typing.Sequence["Category"]] = None
    ) -> None:
        self.count = count
        self.total = total
        self.offset = offset
        self.results = results
        super().__init__()

    def __repr__(self) -> str:
        return (
            "CategoryPagedQueryResponse(count=%r, total=%r, offset=%r, results=%r)"
            % (self.count, self.total, self.offset, self.results)
        )


class CategoryReference(Reference):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CategoryReferenceSchema`."
    #: Optional :class:`commercetools.types.Category`
    obj: typing.Optional["Category"]

    def __init__(
        self,
        *,
        type_id: typing.Optional["ReferenceTypeId"] = None,
        id: typing.Optional[str] = None,
        obj: typing.Optional["Category"] = None
    ) -> None:
        self.obj = obj
        super().__init__(type_id=ReferenceTypeId.CATEGORY, id=id)

    def __repr__(self) -> str:
        return "CategoryReference(type_id=%r, id=%r, obj=%r)" % (
            self.type_id,
            self.id,
            self.obj,
        )


class CategoryResourceIdentifier(ResourceIdentifier):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CategoryResourceIdentifierSchema`."

    def __init__(
        self,
        *,
        type_id: typing.Optional["ReferenceTypeId"] = None,
        id: typing.Optional[str] = None,
        key: typing.Optional[str] = None
    ) -> None:
        super().__init__(type_id=ReferenceTypeId.CATEGORY, id=id, key=key)

    def __repr__(self) -> str:
        return "CategoryResourceIdentifier(type_id=%r, id=%r, key=%r)" % (
            self.type_id,
            self.id,
            self.key,
        )


class CategoryUpdate(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CategoryUpdateSchema`."
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
        return "CategoryUpdate(version=%r, actions=%r)" % (self.version, self.actions)


class CategoryUpdateAction(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CategoryUpdateActionSchema`."
    #: :class:`str`
    action: typing.Optional[str]

    def __init__(self, *, action: typing.Optional[str] = None) -> None:
        self.action = action
        super().__init__()

    def __repr__(self) -> str:
        return "CategoryUpdateAction(action=%r)" % (self.action,)


class CategoryAddAssetAction(CategoryUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CategoryAddAssetActionSchema`."
    #: :class:`commercetools.types.AssetDraft`
    asset: typing.Optional["AssetDraft"]
    #: Optional :class:`int`
    position: typing.Optional[int]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        asset: typing.Optional["AssetDraft"] = None,
        position: typing.Optional[int] = None
    ) -> None:
        self.asset = asset
        self.position = position
        super().__init__(action="addAsset")

    def __repr__(self) -> str:
        return "CategoryAddAssetAction(action=%r, asset=%r, position=%r)" % (
            self.action,
            self.asset,
            self.position,
        )


class CategoryChangeAssetNameAction(CategoryUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CategoryChangeAssetNameActionSchema`."
    #: Optional :class:`str` `(Named` ``assetId`` `in Commercetools)`
    asset_id: typing.Optional[str]
    #: Optional :class:`str` `(Named` ``assetKey`` `in Commercetools)`
    asset_key: typing.Optional[str]
    #: :class:`commercetools.types.LocalizedString`
    name: typing.Optional["LocalizedString"]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        asset_id: typing.Optional[str] = None,
        asset_key: typing.Optional[str] = None,
        name: typing.Optional["LocalizedString"] = None
    ) -> None:
        self.asset_id = asset_id
        self.asset_key = asset_key
        self.name = name
        super().__init__(action="changeAssetName")

    def __repr__(self) -> str:
        return (
            "CategoryChangeAssetNameAction(action=%r, asset_id=%r, asset_key=%r, name=%r)"
            % (self.action, self.asset_id, self.asset_key, self.name)
        )


class CategoryChangeAssetOrderAction(CategoryUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CategoryChangeAssetOrderActionSchema`."
    #: List of :class:`str` `(Named` ``assetOrder`` `in Commercetools)`
    asset_order: typing.Optional[typing.List[str]]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        asset_order: typing.Optional[typing.List[str]] = None
    ) -> None:
        self.asset_order = asset_order
        super().__init__(action="changeAssetOrder")

    def __repr__(self) -> str:
        return "CategoryChangeAssetOrderAction(action=%r, asset_order=%r)" % (
            self.action,
            self.asset_order,
        )


class CategoryChangeNameAction(CategoryUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CategoryChangeNameActionSchema`."
    #: :class:`commercetools.types.LocalizedString`
    name: typing.Optional["LocalizedString"]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        name: typing.Optional["LocalizedString"] = None
    ) -> None:
        self.name = name
        super().__init__(action="changeName")

    def __repr__(self) -> str:
        return "CategoryChangeNameAction(action=%r, name=%r)" % (self.action, self.name)


class CategoryChangeOrderHintAction(CategoryUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CategoryChangeOrderHintActionSchema`."
    #: :class:`str` `(Named` ``orderHint`` `in Commercetools)`
    order_hint: typing.Optional[str]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        order_hint: typing.Optional[str] = None
    ) -> None:
        self.order_hint = order_hint
        super().__init__(action="changeOrderHint")

    def __repr__(self) -> str:
        return "CategoryChangeOrderHintAction(action=%r, order_hint=%r)" % (
            self.action,
            self.order_hint,
        )


class CategoryChangeParentAction(CategoryUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CategoryChangeParentActionSchema`."
    #: :class:`commercetools.types.CategoryResourceIdentifier`
    parent: typing.Optional["CategoryResourceIdentifier"]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        parent: typing.Optional["CategoryResourceIdentifier"] = None
    ) -> None:
        self.parent = parent
        super().__init__(action="changeParent")

    def __repr__(self) -> str:
        return "CategoryChangeParentAction(action=%r, parent=%r)" % (
            self.action,
            self.parent,
        )


class CategoryChangeSlugAction(CategoryUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CategoryChangeSlugActionSchema`."
    #: :class:`commercetools.types.LocalizedString`
    slug: typing.Optional["LocalizedString"]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        slug: typing.Optional["LocalizedString"] = None
    ) -> None:
        self.slug = slug
        super().__init__(action="changeSlug")

    def __repr__(self) -> str:
        return "CategoryChangeSlugAction(action=%r, slug=%r)" % (self.action, self.slug)


class CategoryRemoveAssetAction(CategoryUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CategoryRemoveAssetActionSchema`."
    #: Optional :class:`str` `(Named` ``assetId`` `in Commercetools)`
    asset_id: typing.Optional[str]
    #: Optional :class:`str` `(Named` ``assetKey`` `in Commercetools)`
    asset_key: typing.Optional[str]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        asset_id: typing.Optional[str] = None,
        asset_key: typing.Optional[str] = None
    ) -> None:
        self.asset_id = asset_id
        self.asset_key = asset_key
        super().__init__(action="removeAsset")

    def __repr__(self) -> str:
        return "CategoryRemoveAssetAction(action=%r, asset_id=%r, asset_key=%r)" % (
            self.action,
            self.asset_id,
            self.asset_key,
        )


class CategorySetAssetCustomFieldAction(CategoryUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CategorySetAssetCustomFieldActionSchema`."
    #: Optional :class:`str` `(Named` ``assetId`` `in Commercetools)`
    asset_id: typing.Optional[str]
    #: Optional :class:`str` `(Named` ``assetKey`` `in Commercetools)`
    asset_key: typing.Optional[str]
    #: :class:`str`
    name: typing.Optional[str]
    #: Optional :class:`typing.Any`
    value: typing.Optional[typing.Any]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        asset_id: typing.Optional[str] = None,
        asset_key: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        value: typing.Optional[typing.Any] = None
    ) -> None:
        self.asset_id = asset_id
        self.asset_key = asset_key
        self.name = name
        self.value = value
        super().__init__(action="setAssetCustomField")

    def __repr__(self) -> str:
        return (
            "CategorySetAssetCustomFieldAction(action=%r, asset_id=%r, asset_key=%r, name=%r, value=%r)"
            % (self.action, self.asset_id, self.asset_key, self.name, self.value)
        )


class CategorySetAssetCustomTypeAction(CategoryUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CategorySetAssetCustomTypeActionSchema`."
    #: Optional :class:`str` `(Named` ``assetId`` `in Commercetools)`
    asset_id: typing.Optional[str]
    #: Optional :class:`str` `(Named` ``assetKey`` `in Commercetools)`
    asset_key: typing.Optional[str]
    #: Optional :class:`commercetools.types.TypeResourceIdentifier`
    type: typing.Optional["TypeResourceIdentifier"]
    #: Optional :class:`object`
    fields: typing.Optional[object]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        asset_id: typing.Optional[str] = None,
        asset_key: typing.Optional[str] = None,
        type: typing.Optional["TypeResourceIdentifier"] = None,
        fields: typing.Optional[object] = None
    ) -> None:
        self.asset_id = asset_id
        self.asset_key = asset_key
        self.type = type
        self.fields = fields
        super().__init__(action="setAssetCustomType")

    def __repr__(self) -> str:
        return (
            "CategorySetAssetCustomTypeAction(action=%r, asset_id=%r, asset_key=%r, type=%r, fields=%r)"
            % (self.action, self.asset_id, self.asset_key, self.type, self.fields)
        )


class CategorySetAssetDescriptionAction(CategoryUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CategorySetAssetDescriptionActionSchema`."
    #: Optional :class:`str` `(Named` ``assetId`` `in Commercetools)`
    asset_id: typing.Optional[str]
    #: Optional :class:`str` `(Named` ``assetKey`` `in Commercetools)`
    asset_key: typing.Optional[str]
    #: Optional :class:`commercetools.types.LocalizedString`
    description: typing.Optional["LocalizedString"]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        asset_id: typing.Optional[str] = None,
        asset_key: typing.Optional[str] = None,
        description: typing.Optional["LocalizedString"] = None
    ) -> None:
        self.asset_id = asset_id
        self.asset_key = asset_key
        self.description = description
        super().__init__(action="setAssetDescription")

    def __repr__(self) -> str:
        return (
            "CategorySetAssetDescriptionAction(action=%r, asset_id=%r, asset_key=%r, description=%r)"
            % (self.action, self.asset_id, self.asset_key, self.description)
        )


class CategorySetAssetKeyAction(CategoryUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CategorySetAssetKeyActionSchema`."
    #: :class:`str` `(Named` ``assetId`` `in Commercetools)`
    asset_id: typing.Optional[str]
    #: Optional :class:`str` `(Named` ``assetKey`` `in Commercetools)`
    asset_key: typing.Optional[str]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        asset_id: typing.Optional[str] = None,
        asset_key: typing.Optional[str] = None
    ) -> None:
        self.asset_id = asset_id
        self.asset_key = asset_key
        super().__init__(action="setAssetKey")

    def __repr__(self) -> str:
        return "CategorySetAssetKeyAction(action=%r, asset_id=%r, asset_key=%r)" % (
            self.action,
            self.asset_id,
            self.asset_key,
        )


class CategorySetAssetSourcesAction(CategoryUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CategorySetAssetSourcesActionSchema`."
    #: Optional :class:`str` `(Named` ``assetId`` `in Commercetools)`
    asset_id: typing.Optional[str]
    #: Optional :class:`str` `(Named` ``assetKey`` `in Commercetools)`
    asset_key: typing.Optional[str]
    #: List of :class:`commercetools.types.AssetSource`
    sources: typing.Optional[typing.List["AssetSource"]]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        asset_id: typing.Optional[str] = None,
        asset_key: typing.Optional[str] = None,
        sources: typing.Optional[typing.List["AssetSource"]] = None
    ) -> None:
        self.asset_id = asset_id
        self.asset_key = asset_key
        self.sources = sources
        super().__init__(action="setAssetSources")

    def __repr__(self) -> str:
        return (
            "CategorySetAssetSourcesAction(action=%r, asset_id=%r, asset_key=%r, sources=%r)"
            % (self.action, self.asset_id, self.asset_key, self.sources)
        )


class CategorySetAssetTagsAction(CategoryUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CategorySetAssetTagsActionSchema`."
    #: Optional :class:`str` `(Named` ``assetId`` `in Commercetools)`
    asset_id: typing.Optional[str]
    #: Optional :class:`str` `(Named` ``assetKey`` `in Commercetools)`
    asset_key: typing.Optional[str]
    #: Optional list of :class:`str`
    tags: typing.Optional[typing.List[str]]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        asset_id: typing.Optional[str] = None,
        asset_key: typing.Optional[str] = None,
        tags: typing.Optional[typing.List[str]] = None
    ) -> None:
        self.asset_id = asset_id
        self.asset_key = asset_key
        self.tags = tags
        super().__init__(action="setAssetTags")

    def __repr__(self) -> str:
        return (
            "CategorySetAssetTagsAction(action=%r, asset_id=%r, asset_key=%r, tags=%r)"
            % (self.action, self.asset_id, self.asset_key, self.tags)
        )


class CategorySetCustomFieldAction(CategoryUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CategorySetCustomFieldActionSchema`."
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
        return "CategorySetCustomFieldAction(action=%r, name=%r, value=%r)" % (
            self.action,
            self.name,
            self.value,
        )


class CategorySetCustomTypeAction(CategoryUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CategorySetCustomTypeActionSchema`."
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
        return "CategorySetCustomTypeAction(action=%r, type=%r, fields=%r)" % (
            self.action,
            self.type,
            self.fields,
        )


class CategorySetDescriptionAction(CategoryUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CategorySetDescriptionActionSchema`."
    #: Optional :class:`commercetools.types.LocalizedString`
    description: typing.Optional["LocalizedString"]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        description: typing.Optional["LocalizedString"] = None
    ) -> None:
        self.description = description
        super().__init__(action="setDescription")

    def __repr__(self) -> str:
        return "CategorySetDescriptionAction(action=%r, description=%r)" % (
            self.action,
            self.description,
        )


class CategorySetExternalIdAction(CategoryUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CategorySetExternalIdActionSchema`."
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
        return "CategorySetExternalIdAction(action=%r, external_id=%r)" % (
            self.action,
            self.external_id,
        )


class CategorySetKeyAction(CategoryUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CategorySetKeyActionSchema`."
    #: Optional :class:`str`
    key: typing.Optional[str]

    def __init__(
        self, *, action: typing.Optional[str] = None, key: typing.Optional[str] = None
    ) -> None:
        self.key = key
        super().__init__(action="setKey")

    def __repr__(self) -> str:
        return "CategorySetKeyAction(action=%r, key=%r)" % (self.action, self.key)


class CategorySetMetaDescriptionAction(CategoryUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CategorySetMetaDescriptionActionSchema`."
    #: Optional :class:`commercetools.types.LocalizedString` `(Named` ``metaDescription`` `in Commercetools)`
    meta_description: typing.Optional["LocalizedString"]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        meta_description: typing.Optional["LocalizedString"] = None
    ) -> None:
        self.meta_description = meta_description
        super().__init__(action="setMetaDescription")

    def __repr__(self) -> str:
        return "CategorySetMetaDescriptionAction(action=%r, meta_description=%r)" % (
            self.action,
            self.meta_description,
        )


class CategorySetMetaKeywordsAction(CategoryUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CategorySetMetaKeywordsActionSchema`."
    #: Optional :class:`commercetools.types.LocalizedString` `(Named` ``metaKeywords`` `in Commercetools)`
    meta_keywords: typing.Optional["LocalizedString"]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        meta_keywords: typing.Optional["LocalizedString"] = None
    ) -> None:
        self.meta_keywords = meta_keywords
        super().__init__(action="setMetaKeywords")

    def __repr__(self) -> str:
        return "CategorySetMetaKeywordsAction(action=%r, meta_keywords=%r)" % (
            self.action,
            self.meta_keywords,
        )


class CategorySetMetaTitleAction(CategoryUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CategorySetMetaTitleActionSchema`."
    #: Optional :class:`commercetools.types.LocalizedString` `(Named` ``metaTitle`` `in Commercetools)`
    meta_title: typing.Optional["LocalizedString"]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        meta_title: typing.Optional["LocalizedString"] = None
    ) -> None:
        self.meta_title = meta_title
        super().__init__(action="setMetaTitle")

    def __repr__(self) -> str:
        return "CategorySetMetaTitleAction(action=%r, meta_title=%r)" % (
            self.action,
            self.meta_title,
        )
