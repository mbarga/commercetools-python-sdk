# DO NOT EDIT! This file is automatically generated

import re

import marshmallow
import marshmallow_enum

from commercetools import helpers, types
from commercetools.schemas._base import (
    PagedQueryResponseSchema,
    UpdateActionSchema,
    UpdateSchema,
)
from commercetools.schemas._common import (
    LocalizedStringField,
    ReferenceSchema,
    ResourceSchema,
)
from commercetools.schemas._type import FieldContainerField

__all__ = [
    "ChannelAddRolesActionSchema",
    "ChannelChangeDescriptionActionSchema",
    "ChannelChangeKeyActionSchema",
    "ChannelChangeNameActionSchema",
    "ChannelDraftSchema",
    "ChannelPagedQueryResponseSchema",
    "ChannelReferenceSchema",
    "ChannelRemoveRolesActionSchema",
    "ChannelSchema",
    "ChannelSetAddressActionSchema",
    "ChannelSetCustomFieldActionSchema",
    "ChannelSetCustomTypeActionSchema",
    "ChannelSetGeoLocationActionSchema",
    "ChannelSetRolesActionSchema",
    "ChannelUpdateActionSchema",
    "ChannelUpdateSchema",
]


class ChannelDraftSchema(marshmallow.Schema):
    "Marshmallow schema for :class:`commercetools.types.ChannelDraft`."
    key = marshmallow.fields.String(allow_none=True)
    roles = marshmallow.fields.List(
        marshmallow_enum.EnumField(types.ChannelRoleEnum, by_value=True), missing=None
    )
    name = LocalizedStringField(allow_none=True, missing=None)
    description = LocalizedStringField(allow_none=True, missing=None)
    address = marshmallow.fields.Nested(
        nested="commercetools.schemas._common.AddressSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )
    custom = marshmallow.fields.Nested(
        nested="commercetools.schemas._type.CustomFieldsDraftSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )
    geo_location = marshmallow.fields.Nested(
        nested="commercetools.schemas._common.GeoJsonPointSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
        data_key="geoLocation",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        return types.ChannelDraft(**data)


class ChannelPagedQueryResponseSchema(PagedQueryResponseSchema):
    "Marshmallow schema for :class:`commercetools.types.ChannelPagedQueryResponse`."
    results = marshmallow.fields.Nested(
        nested="commercetools.schemas._channel.ChannelSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        return types.ChannelPagedQueryResponse(**data)


class ChannelReferenceSchema(ReferenceSchema):
    "Marshmallow schema for :class:`commercetools.types.ChannelReference`."
    obj = marshmallow.fields.Nested(
        nested="commercetools.schemas._channel.ChannelSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["type_id"]
        return types.ChannelReference(**data)


class ChannelSchema(ResourceSchema):
    "Marshmallow schema for :class:`commercetools.types.Channel`."
    key = marshmallow.fields.String(allow_none=True)
    roles = marshmallow.fields.List(
        marshmallow_enum.EnumField(types.ChannelRoleEnum, by_value=True)
    )
    name = LocalizedStringField(allow_none=True, missing=None)
    description = LocalizedStringField(allow_none=True, missing=None)
    address = marshmallow.fields.Nested(
        nested="commercetools.schemas._common.AddressSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )
    review_rating_statistics = marshmallow.fields.Nested(
        nested="commercetools.schemas._review.ReviewRatingStatisticsSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
        data_key="reviewRatingStatistics",
    )
    custom = marshmallow.fields.Nested(
        nested="commercetools.schemas._type.CustomFieldsSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )
    geo_location = marshmallow.fields.Nested(
        nested="commercetools.schemas._common.GeoJsonPointSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
        data_key="geoLocation",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        return types.Channel(**data)


class ChannelUpdateActionSchema(UpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.ChannelUpdateAction`."

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.ChannelUpdateAction(**data)


class ChannelUpdateSchema(UpdateSchema):
    "Marshmallow schema for :class:`commercetools.types.ChannelUpdate`."
    actions = marshmallow.fields.List(
        helpers.Discriminator(
            discriminator_field=("action", "action"),
            discriminator_schemas={
                "addRoles": "commercetools.schemas._channel.ChannelAddRolesActionSchema",
                "changeDescription": "commercetools.schemas._channel.ChannelChangeDescriptionActionSchema",
                "changeKey": "commercetools.schemas._channel.ChannelChangeKeyActionSchema",
                "changeName": "commercetools.schemas._channel.ChannelChangeNameActionSchema",
                "removeRoles": "commercetools.schemas._channel.ChannelRemoveRolesActionSchema",
                "setAddress": "commercetools.schemas._channel.ChannelSetAddressActionSchema",
                "setCustomField": "commercetools.schemas._channel.ChannelSetCustomFieldActionSchema",
                "setCustomType": "commercetools.schemas._channel.ChannelSetCustomTypeActionSchema",
                "setGeoLocation": "commercetools.schemas._channel.ChannelSetGeoLocationActionSchema",
                "setRoles": "commercetools.schemas._channel.ChannelSetRolesActionSchema",
            },
            unknown=marshmallow.EXCLUDE,
            allow_none=True,
        ),
        allow_none=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        return types.ChannelUpdate(**data)


class ChannelAddRolesActionSchema(ChannelUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.ChannelAddRolesAction`."
    roles = marshmallow.fields.List(
        marshmallow_enum.EnumField(types.ChannelRoleEnum, by_value=True)
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.ChannelAddRolesAction(**data)


class ChannelChangeDescriptionActionSchema(ChannelUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.ChannelChangeDescriptionAction`."
    description = LocalizedStringField(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.ChannelChangeDescriptionAction(**data)


class ChannelChangeKeyActionSchema(ChannelUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.ChannelChangeKeyAction`."
    key = marshmallow.fields.String(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.ChannelChangeKeyAction(**data)


class ChannelChangeNameActionSchema(ChannelUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.ChannelChangeNameAction`."
    name = LocalizedStringField(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.ChannelChangeNameAction(**data)


class ChannelRemoveRolesActionSchema(ChannelUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.ChannelRemoveRolesAction`."
    roles = marshmallow.fields.List(
        marshmallow_enum.EnumField(types.ChannelRoleEnum, by_value=True)
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.ChannelRemoveRolesAction(**data)


class ChannelSetAddressActionSchema(ChannelUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.ChannelSetAddressAction`."
    address = marshmallow.fields.Nested(
        nested="commercetools.schemas._common.AddressSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.ChannelSetAddressAction(**data)


class ChannelSetCustomFieldActionSchema(ChannelUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.ChannelSetCustomFieldAction`."
    name = marshmallow.fields.String(allow_none=True)
    value = marshmallow.fields.Raw(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.ChannelSetCustomFieldAction(**data)


class ChannelSetCustomTypeActionSchema(ChannelUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.ChannelSetCustomTypeAction`."
    type = marshmallow.fields.Nested(
        nested="commercetools.schemas._type.TypeReferenceSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )
    fields = FieldContainerField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.ChannelSetCustomTypeAction(**data)


class ChannelSetGeoLocationActionSchema(ChannelUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.ChannelSetGeoLocationAction`."
    geo_location = marshmallow.fields.Nested(
        nested="commercetools.schemas._common.GeoJsonPointSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
        data_key="geoLocation",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.ChannelSetGeoLocationAction(**data)


class ChannelSetRolesActionSchema(ChannelUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.ChannelSetRolesAction`."
    roles = marshmallow.fields.List(
        marshmallow_enum.EnumField(types.ChannelRoleEnum, by_value=True)
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.ChannelSetRolesAction(**data)
